#!/usr/bin/env python3
"""Publish the captured Edapt study guides to the study hub, one page per class-week.

Usage:
    python build_guides.py <class-folder> --slug nr449-evidence-based-practice \
        --code NR449 --name "Evidence-Based Practice" --hub index.html

Writes `<hub-dir>/guides/<slug>/week-N.html` for every WeekN_*.md in the class folder, then
inserts (or updates) a "Study Guides" block on that class's page. Idempotent — re-run after a
new extraction and it refreshes in place.

Each week page renders the modules with the hub's styling, and embeds the raw markdown so a
reader can copy a module (or the whole week) and paste it into an AI to build their own quiz.

Markdown support is deliberately scoped to what our own extractor emits: ATX headings, bold,
italic, inline code, links, bullet/numbered lists (one nesting level), pipe tables,
blockquotes, and horizontal rules. No third-party dependencies.
"""
import argparse
import html as htmllib
import json
import pathlib
import re
import sys

ASSETS = pathlib.Path(__file__).resolve().parent.parent / "assets"
DEFAULT_REPO = "https://github.com/NursingSchool/study-guides/tree/main"


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")


# --- markdown -> html (scoped subset) ----------------------------------------
def _inline(s):
    s = htmllib.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    return s


_RULE = re.compile(r"(-{3,}|\*{3,}|_{3,})")
_HEAD = re.compile(r"^(#{1,6})\s+(.*)$")
_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
_SEP = re.compile(r"\|[\s:|-]+\|?")


def md_to_html(md):
    lines = md.split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        if _RULE.fullmatch(s):
            out.append("<hr>")
            i += 1
            continue
        m = _HEAD.match(s)
        if m:                                    # module headings sit under our own <h3>
            lvl = 4 if len(m.group(1)) <= 2 else 5
            out.append(f"<h{lvl}>{_inline(m.group(2))}</h{lvl}>")
            i += 1
            continue
        if s.startswith("|") and i + 1 < n and _SEP.fullmatch(lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join(f"<th>{_inline(c)}</th>" for c in header)
            trs = "".join("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>"
                          for r in rows)
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
            continue
        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote>{_inline(' '.join(buf))}</blockquote>")
            continue
        if _ITEM.match(lines[i]):
            ordered = bool(re.match(r"^\s*\d+[.)]\s+", lines[i]))
            items = []
            while i < n:
                mi = _ITEM.match(lines[i])
                if not mi:
                    if not lines[i].strip() and i + 1 < n and _ITEM.match(lines[i + 1]):
                        i += 1
                        continue
                    break
                items.append((len(mi.group(1)), mi.group(3)))
                i += 1
            tag = "ol" if ordered else "ul"
            base = items[0][0]
            html_out, sub = [f"<{tag}>"], False
            for indent, text in items:
                if indent > base:
                    if not sub:
                        html_out.append("<ul>")
                        sub = True
                else:
                    if sub:
                        html_out.append("</ul>")
                        sub = False
                html_out.append(f"<li>{_inline(text)}</li>")
            if sub:
                html_out.append("</ul>")
            html_out.append(f"</{tag}>")
            out.append("".join(html_out))
            continue
        buf = []
        while i < n:
            cur = lines[i].strip()
            if (not cur or _HEAD.match(cur) or cur.startswith(("|", ">"))
                    or _ITEM.match(lines[i]) or _RULE.fullmatch(cur)):
                break
            buf.append(cur)
            i += 1
        if buf:
            out.append(f"<p>{_inline(' '.join(buf))}</p>")
        else:
            i += 1
    return "\n".join(out)


# --- page + class-page assembly ----------------------------------------------
def module_title(path):
    """Week2_The_PICOT_Question.md -> 'The PICOT Question'."""
    stem = re.sub(r"^Week\d+_", "", path.stem)
    return stem.replace("_", " ").strip()


def build_week_page(*, code, name, slug, week, files, out_dir, github_url):
    tmpl = (ASSETS / "guide-page-template.html").read_text(encoding="utf-8")
    toc, content, md_map = [], [], {}
    for f in files:
        raw = f.read_text(encoding="utf-8")
        title = module_title(f)
        mid = slugify(f.stem)
        md_map[mid] = raw
        toc.append(f'<li><a href="#{mid}">{htmllib.escape(title)}</a></li>')
        content.append(
            f'  <div class="mod" id="{mid}">\n'
            f'    <div class="modhead"><h3>{htmllib.escape(title)}</h3>'
            f'<button class="btn" onclick="copyOne(\'{mid}\', this)">Copy markdown</button></div>\n'
            f'{md_to_html(raw)}\n'
            f'  </div>')
    page = (tmpl
            .replace("__CLASS_CODE__", htmllib.escape(code))
            .replace("__CLASS_NAME__", htmllib.escape(name))
            .replace("__WEEK_LABEL__", f"Week {week}")
            .replace("__MODULE_COUNT__", str(len(files)))
            .replace("__CLASS_HREF__", f"../../{slug}.html")
            .replace("__FILE_BASE__", f"{slug}-week-{week}")
            .replace("__GITHUB_URL__", github_url)
            .replace("__TOC__", "\n".join(toc))
            .replace("__CONTENT__", "\n".join(content))
            .replace("__MD_JSON__", json.dumps(md_map, ensure_ascii=False)))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"week-{week}.html"
    dest.write_text(page, encoding="utf-8")
    return dest


def build_week_card(slug, week, count):
    href = f"guides/{slug}/week-{week}.html"
    return (
        f'    <div class="card">\n'
        f'      <div class="row">\n'
        f'        <div><h3>Week {week}</h3>\n'
        f'        <div class="meta">{count} module{"" if count == 1 else "s"} · captured from Edapt</div></div>\n'
        f'        <a class="btn" href="{href}">Read ▸</a>\n'
        f'      </div>\n'
        f'    </div>')


def register_guides(class_path, slug, weeks, github_url):
    """Insert/replace the Study Guides block on the class page. Idempotent."""
    cards = "\n".join(build_week_card(slug, w, c) for w, c in weeks)
    block = (
        "  <!-- guides-block -->\n"
        "  <h2>Study Guides</h2>\n"
        f'  <div class="note">The verbatim Edapt modules behind these quizzes. Open a week to read it, '
        f'copy any module (or the whole week), and build your own practice — or grab the raw files '
        f'<a href="{github_url}" target="_blank" rel="noopener">on GitHub</a>.</div>\n'
        '  <div class="grid" style="margin-top:14px">\n'
        f"{cards}\n"
        "  </div>\n"
        "  <!-- /guides-block -->"
    )
    txt = class_path.read_text(encoding="utf-8")
    o, c = "<!-- guides-block -->", "<!-- /guides-block -->"
    if o in txt and c in txt:
        pre, post = txt[:txt.index(o)], txt[txt.index(c) + len(c):]
        txt = pre + block.lstrip() + post
        action = "updated"
    else:
        anchor = "  <footer>"
        if anchor not in txt:
            return f"could not find footer in {class_path.name}; guides block NOT added"
        idx = txt.index(anchor)
        txt = txt[:idx] + block + "\n\n" + txt[idx:]
        action = "added"
    # the note/grid styles live in the class-page template already, except .note
    if ".note{" not in txt:
        txt = txt.replace(
            "  footer{",
            "  .note{background:#22323f;border:1px dashed var(--line);border-radius:12px;"
            "padding:14px;color:var(--muted);font-size:13px;margin-top:14px}\n  footer{", 1)
    class_path.write_text(txt, encoding="utf-8")
    return f"{action} Study Guides block in {class_path.name}"


def main():
    ap = argparse.ArgumentParser(description="Publish captured Edapt guides to the study hub.")
    ap.add_argument("class_folder", help="folder holding the WeekN_*.md guides")
    ap.add_argument("--slug", required=True, help="classSlug (matches <slug>.html)")
    ap.add_argument("--code", required=True, help='course code, e.g. "NR449"')
    ap.add_argument("--name", required=True, help='course name, e.g. "Evidence-Based Practice"')
    ap.add_argument("--hub", default="index.html", help="path to the hub index.html")
    ap.add_argument("--repo-url", default=DEFAULT_REPO, help="base GitHub tree URL")
    args = ap.parse_args()

    folder = pathlib.Path(args.class_folder)
    hub = pathlib.Path(args.hub)
    class_path = hub.parent / f"{args.slug}.html"
    if not class_path.exists():
        print(f"ERROR: class page {class_path} not found - build a quiz with --hub first",
              file=sys.stderr)
        return 2

    by_week = {}
    for f in sorted(folder.glob("Week*_*.md")):
        m = re.match(r"^Week(\d+)_", f.name)
        if m:
            by_week.setdefault(int(m.group(1)), []).append(f)
    if not by_week:
        print(f"ERROR: no WeekN_*.md files in {folder}", file=sys.stderr)
        return 2

    github_url = f"{args.repo_url.rstrip('/')}/{folder.name}"
    out_dir = hub.parent / "guides" / args.slug
    weeks = []
    for week in sorted(by_week):
        files = by_week[week]
        dest = build_week_page(code=args.code, name=args.name, slug=args.slug, week=week,
                               files=files, out_dir=out_dir, github_url=github_url)
        weeks.append((week, len(files)))
        print(f"  week {week}: {len(files)} modules -> {dest}")
    print(register_guides(class_path, args.slug, weeks, github_url))
    return 0


if __name__ == "__main__":
    sys.exit(main())
