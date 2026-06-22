#!/usr/bin/env python3
"""Assemble a self-contained NCLEX practice quiz (single HTML file) from a JSON
data file, and lint the items against NGN structural rules + the 2026 blueprint.

Usage:
    python assemble_quiz.py data.quiz.json [-o out.html] [--template path]

The data file is the ONLY thing a quiz author writes. The HTML engine
(rendering + scoring) lives in assets/quiz-template.html and is injected
verbatim, so the proven engine never has to be re-typed.

Exit code is non-zero if any ERROR is found, so this doubles as the test/eval
check. WARNINGS are advisory and do not fail the build (use --strict to make
warnings fatal).

Data file shape:
{
  "meta": {
    "title":    "<browser tab title>",
    "header":   "<H1 shown at top>",
    "subtitle": "<one-line description under the H1>",
    "footnote": "<small text on the results screen>"
  },
  "questions": [ <item objects>, ... ]
}

See references/ngn-item-writing.md for the per-type item schema.
"""

import argparse
import html as htmllib
import json
import os
import re
import sys
from pathlib import Path

# --- 2026 NCLEX-RN Client Needs blueprint (effective April 1, 2026) ----------
# Strings must match EXACTLY what the engine groups on (q.cat).
BLUEPRINT = {
    "Management of Care": (15, 21),
    "Safety & Infection Prevention and Control": (10, 16),
    "Health Promotion & Maintenance": (6, 12),
    "Psychosocial Integrity": (6, 12),
    "Basic Care & Comfort": (6, 12),
    "Pharmacological & Parenteral Therapies": (13, 19),
    "Reduction of Risk Potential": (9, 15),
    "Physiological Adaptation": (11, 17),
}
VALID_CATS = set(BLUEPRINT)
VALID_LVLS = {"Application", "Analysis", "Evaluation"}
VALID_TYPES = {"radio", "multi", "cloze", "matrix", "match", "bowtie", "calc"}
BANNED_PHRASES = ("all of the above", "none of the above")

# heuristic "too-easy" tells (advisory warnings, not errors)
THROWAWAY_RE = re.compile(r"document|no further action|\bno action\b|take no|continue routine|"
    r"routine monitoring|expected finding|normal finding|reassure|do nothing|as a normal", re.I)
EXTREME_RE = re.compile(r"\b(always|never|all of|only if|immediately|permanent(ly)?|vigorous(ly)?|"
    r"abruptly|completely|restrict (all )?fluid)\b|stop (breast)?feeding", re.I)
STARVED_CATS = ("Management of Care", "Psychosocial Integrity")

errors, warnings = [], []


def err(qn, msg):
    errors.append(f"  [item {qn}] {msg}")


def warn(qn, msg):
    warnings.append(f"  [item {qn}] {msg}")


def _idx_ok(v, n):
    return isinstance(v, int) and 0 <= v < n


def _check_options(qn, opts, where):
    """Shared distractor hygiene for any option list."""
    if not isinstance(opts, list) or len(opts) < 2:
        err(qn, f"{where}: needs at least 2 options")
        return
    for o in opts:
        if not isinstance(o, str) or not o.strip():
            err(qn, f"{where}: every option must be non-empty text")
        elif any(b in o.lower() for b in BANNED_PHRASES):
            err(qn, f'{where}: remove "all/none of the above" - banned on NCLEX')


def validate_item(q):
    qn = q.get("n", "?")
    # common fields
    for f in ("type", "cat", "lvl", "stem", "rat", "strat"):
        if not q.get(f) or not str(q.get(f)).strip():
            err(qn, f"missing required field: {f}")
    t = q.get("type")
    if t not in VALID_TYPES:
        err(qn, f'unsupported type "{t}" (the engine renders only {sorted(VALID_TYPES)})')
        return
    if q.get("cat") not in VALID_CATS:
        err(qn, f'cat "{q.get("cat")}" is not a 2026 Client Needs category')
    if q.get("lvl") not in VALID_LVLS:
        warn(qn, f'lvl "{q.get("lvl")}" not in {sorted(VALID_LVLS)} (items should be Application+)')

    if t in ("radio", "multi"):
        opts = q.get("opts", [])
        _check_options(qn, opts, "opts")
        n = len(opts) if isinstance(opts, list) else 0
        if n and n != 4 and t == "radio":
            warn(qn, f"radio has {n} options; NCLEX single-answer items are almost always 4")
        if t == "radio":
            if not _idx_ok(q.get("ans"), n):
                err(qn, "radio: ans must be a valid option index")
        else:  # multi
            ans = q.get("ans")
            if not isinstance(ans, list) or not ans:
                err(qn, "multi: ans must be a non-empty list of indices")
            elif len(set(ans)) != len(ans):
                err(qn, "multi: ans has duplicate indices")
            elif any(not _idx_ok(a, n) for a in ans):
                err(qn, "multi: ans contains an out-of-range index")
            elif n and len(ans) == n:
                warn(qn, "multi: every option is keyed correct - vary the count so it isn't a giveaway")
            if n and n < 5:
                warn(qn, f"multi has {n} options; SATA items usually offer 5-6")

    elif t == "cloze":
        blanks = q.get("blanks", [])
        if not isinstance(blanks, list) or not blanks:
            err(qn, "cloze: needs a non-empty blanks list")
        else:
            for bi, b in enumerate(blanks):
                if not b.get("label"):
                    warn(qn, f"cloze blank {bi}: missing label")
                _check_options(qn, b.get("opts", []), f"cloze blank {bi} opts")
                if not _idx_ok(b.get("a"), len(b.get("opts", []) or [])):
                    err(qn, f"cloze blank {bi}: a must be a valid option index")

    elif t in ("matrix", "match"):
        pool_key = "cols" if t == "matrix" else "shared"
        pool = q.get(pool_key, [])
        if not isinstance(pool, list) or len(pool) < 2:
            err(qn, f"{t}: {pool_key} needs at least 2 entries")
        rows = q.get("rows", [])
        if not isinstance(rows, list) or not rows:
            err(qn, f"{t}: needs a non-empty rows list")
        else:
            for ri, r in enumerate(rows):
                if not r.get("t"):
                    err(qn, f"{t} row {ri}: missing row text 't'")
                if not _idx_ok(r.get("a"), len(pool) if isinstance(pool, list) else 0):
                    err(qn, f"{t} row {ri}: a must index into {pool_key}")

    elif t == "bowtie":
        prob = q.get("problem", {})
        _check_options(qn, prob.get("opts", []), "bowtie problem opts")
        if not _idx_ok(prob.get("a"), len(prob.get("opts", []) or [])):
            err(qn, "bowtie: problem.a must be a valid index")
        for grp in ("actions", "params"):
            g = q.get(grp, {})
            opts = g.get("opts", [])
            _check_options(qn, opts, f"bowtie {grp} opts")
            ans = g.get("ans")
            if not isinstance(ans, list) or len(ans) != 2:
                err(qn, f"bowtie: {grp}.ans must key EXACTLY 2 (standard bowtie shape)")
            elif any(not _idx_ok(a, len(opts) if isinstance(opts, list) else 0) for a in ans):
                err(qn, f"bowtie: {grp}.ans has an out-of-range index")
            elif len(set(ans)) != 2:
                err(qn, f"bowtie: {grp}.ans has duplicate indices")

    elif t == "calc":
        lo, hi = q.get("acceptLo"), q.get("acceptHi")
        if not isinstance(lo, (int, float)) or not isinstance(hi, (int, float)):
            err(qn, "calc: acceptLo and acceptHi must be numbers")
        elif lo > hi:
            err(qn, "calc: acceptLo must be <= acceptHi")
        if not q.get("answer"):
            err(qn, "calc: needs an 'answer' string for the feedback")


def check_case_studies(questions):
    """Unfolding case studies must be 6 linked items, one per NCJMM step."""
    pat = re.compile(r"CASE[^\(]*\(\s*(\d+)\s*/\s*6\s*\)", re.IGNORECASE)
    groups = {}
    for q in questions:
        m = pat.search(q.get("stem", ""))
        if m:
            key = q.get("topic", "?")
            groups.setdefault(key, []).append(int(m.group(1)))
    for key, steps in groups.items():
        if len(steps) != 6 or sorted(steps) != [1, 2, 3, 4, 5, 6]:
            warnings.append(
                f"  [case '{key}'] found steps {sorted(steps)}; an unfolding case "
                f"study must be exactly 6 linked items numbered (1/6)..(6/6)"
            )


def coverage_report(questions):
    total = len(questions)
    by_cat, by_lvl = {}, {}
    for q in questions:
        by_cat[q.get("cat")] = by_cat.get(q.get("cat"), 0) + 1
        by_lvl[q.get("lvl")] = by_lvl.get(q.get("lvl"), 0) + 1
    lines = [f"\nCoverage ({total} items) vs. 2026 NCLEX-RN blueprint:"]
    lines.append(f"  {'Client Needs category':<44} {'n':>3} {'%':>5}   target")
    for cat, (lo, hi) in BLUEPRINT.items():
        n = by_cat.get(cat, 0)
        pct = round(n / total * 100) if total else 0
        flag = "" if lo <= pct <= hi or n == 0 else "  <-- off-blueprint"
        lines.append(f"  {cat:<44} {n:>3} {pct:>4}%   {lo}-{hi}%{flag}")
    extra = set(by_cat) - VALID_CATS - {None}
    for cat in extra:
        lines.append(f"  {str(cat):<44} {by_cat[cat]:>3}        (UNKNOWN category)")
    lines.append("\n  Cognitive level:")
    appplus = 0
    for lvl, n in sorted(by_lvl.items(), key=lambda x: -x[1]):
        lines.append(f"    {str(lvl):<20} {n:>3} ({round(n/total*100) if total else 0}%)")
        if lvl in VALID_LVLS:
            appplus += n
    if total and appplus / total < 0.8:
        lines.append("    NOTE: under 80% at Application+; raise the cognitive level of recall items.")
    if total < 25:
        lines.append(
            "\n  (Small/topic-focused set: the per-category band flags above are expected and\n"
            "   advisory - the blueprint % bands assume a full-length comprehensive exam. Do not\n"
            "   pad the item count just to land inside every band.)"
        )
    return "\n".join(lines)


def count_case_studies(questions):
    pat = re.compile(r"CASE[^\(]*\(\s*(\d+)\s*/\s*6\s*\)", re.IGNORECASE)
    groups = {}
    for q in questions:
        if pat.search(q.get("stem", "")):
            groups.setdefault(q.get("topic", "?"), True)
    return len(groups)


def derive_chips(questions, limit=12):
    """High-level topic chips for the hub card (dedup, drop 'Case:' prefixes)."""
    seen, chips = set(), []
    for q in questions:
        t = re.sub(r"^Case:\s*", "", q.get("topic", "")).strip()
        if t and t.lower() not in seen:
            seen.add(t.lower())
            chips.append(t)
    return chips[:limit]


def build_card(href, title, meta_line, chips):
    chip_html = "\n        ".join(
        f'<span class="chip">{htmllib.escape(c)}</span>' for c in chips
    )
    return (
        f'    <!-- quiz-card:{href} -->\n'
        f'    <div class="card" data-quiz="{href}">\n'
        f'      <div class="row">\n'
        f'        <div>\n'
        f'          <h3>{htmllib.escape(title)}</h3>\n'
        f'          <div class="meta">{htmllib.escape(meta_line)}</div>\n'
        f'        </div>\n'
        f'        <a class="btn" href="{href}">Start ▸</a>\n'
        f'      </div>\n'
        f'      <div class="chips">\n'
        f'        {chip_html}\n'
        f'      </div>\n'
        f'    </div>\n'
        f'    <!-- /quiz-card:{href} -->'
    )


def register_in_index(index_path, out_path, meta, questions):
    """Insert (or update, by href) a quiz card in the study-hub index. Idempotent."""
    index_path = Path(index_path)
    if not index_path.exists():
        return f"index not found, skipped: {index_path}"
    href = os.path.relpath(out_path, index_path.parent).replace(os.sep, "/")
    n = len(questions)
    cases = count_case_studies(questions)
    case_str = f" · {cases} unfolding case stud{'y' if cases == 1 else 'ies'}" if cases else ""
    meta_line = meta.get("cardMeta", f"{n} questions · NGN-style{case_str} · rationale after each answer")
    title = meta.get("cardTitle") or meta.get("header", "NCLEX Practice Quiz")
    chips = meta.get("chips") or derive_chips(questions)
    card = build_card(href, title, meta_line, chips)

    txt = index_path.read_text(encoding="utf-8")
    open_c, close_c = f"<!-- quiz-card:{href} -->", f"<!-- /quiz-card:{href} -->"
    if open_c in txt and close_c in txt:  # update existing card in place
        pre = txt[: txt.index(open_c)]
        post = txt[txt.index(close_c) + len(close_c):]
        txt = pre + card.lstrip() + post
        action = "updated card in"
    else:  # insert newest-first right after the grid opens
        anchor = '<div class="grid" id="quizzes">'
        if anchor not in txt:
            return f"could not find '{anchor}' in {index_path}; card NOT added"
        idx = txt.index(anchor) + len(anchor)
        txt = txt[:idx] + "\n\n" + card + "\n" + txt[idx:]
        action = "added card to"
    index_path.write_text(txt, encoding="utf-8")
    return f"{action} {index_path} (href={href})"


# --- per-class study hub (hub -> class pages -> exam-grouped review cards) ------
ASSETS = Path(__file__).resolve().parent.parent / "assets"


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")


def build_review_card(href, title, kind, meta_line, chips, download=None):
    badge = "Exam Review" if kind == "exam-review" else "Topic Practice"
    bcls = "badge-exam" if kind == "exam-review" else "badge-topic"
    chip_html = "".join(f'<span class="chip">{htmllib.escape(c)}</span>' for c in chips)
    dl = f'\n        <a class="dl" href="{download}">↓ Offline ZIP</a>' if download else ""
    return (
        f'      <!-- quiz-card:{href} -->\n'
        f'      <div class="card" data-quiz="{href}" data-kind="{kind}">\n'
        f'        <div class="row">\n'
        f'          <div><h3>{htmllib.escape(title)} <span class="badge {bcls}">{badge}</span></h3>\n'
        f'          <div class="meta">{htmllib.escape(meta_line)}</div></div>\n'
        f'          <a class="btn" href="{href}">Start ▸</a>\n'
        f'        </div>\n'
        f'        <div class="chips">{chip_html}</div>{dl}\n'
        f'      </div>\n'
        f'      <!-- /quiz-card:{href} -->'
    )


def ensure_class_page(class_path, class_code, class_name):
    """Create the class page from the template if it doesn't exist yet."""
    class_path = Path(class_path)
    if class_path.exists():
        return
    tmpl = (ASSETS / "class-page-template.html").read_text(encoding="utf-8")
    tmpl = (tmpl.replace("__CLASS_CODE__", htmllib.escape(class_code))
                .replace("__CLASS_NAME__", htmllib.escape(class_name)))
    class_path.write_text(tmpl, encoding="utf-8")


def register_on_class_page(class_path, *, href, exam, exam_order, kind,
                           title, meta_line, chips, download=None):
    """Insert/update a review card under its exam section. Idempotent by href.
    exam-review cards sit at the top of a section; topic-practice at the end."""
    class_path = Path(class_path)
    txt = class_path.read_text(encoding="utf-8")
    card = build_review_card(href, title, kind, meta_line, chips, download)
    qopen, qclose = f"<!-- quiz-card:{href} -->", f"<!-- /quiz-card:{href} -->"
    if qopen in txt and qclose in txt:                       # update in place
        pre = txt[:txt.index(qopen)]
        post = txt[txt.index(qclose) + len(qclose):]
        class_path.write_text(pre + card.lstrip() + post, encoding="utf-8")
        return

    sopen, sclose = f"<!-- exam:{exam_order} -->", f"<!-- /exam:{exam_order} -->"
    if sopen not in txt:                                     # create the exam section, in order
        section = (
            f'    <section data-exam-order="{exam_order}">\n'
            f'      {sopen}\n'
            f'      <h2>{htmllib.escape(exam)}</h2>\n'
            f'      <div class="grid">\n'
            f'      </div>\n'
            f'      {sclose}\n'
            f'    </section>\n'
        )
        higher = sorted(o for o in (int(m) for m in re.findall(r"<!-- exam:(\d+) -->", txt))
                        if o > exam_order)
        if higher:
            sec_tag = txt.rfind("<section", 0, txt.index(f"<!-- exam:{higher[0]} -->"))
            ins = txt.rfind("\n", 0, sec_tag) + 1
        else:
            ins = txt.rfind("\n", 0, txt.index("<!-- reviews-end -->")) + 1
        txt = txt[:ins] + section + txt[ins:]

    sstart, send = txt.index(sopen), txt.index(sclose)       # insert card into the section grid
    inner = txt[sstart:send]
    gpos = inner.index('<div class="grid">') + len('<div class="grid">')
    if kind == "exam-review":
        nl = inner.index("\n", gpos) + 1
        inner = inner[:nl] + card + "\n" + inner[nl:]
    else:
        gclose = inner.rfind("</div>")
        line_start = inner.rfind("\n", 0, gclose) + 1
        inner = inner[:line_start] + card + "\n" + inner[line_start:]
    class_path.write_text(txt[:sstart] + inner + txt[send:], encoding="utf-8")


def build_class_card(slug, code, name, href, review_count, exam_chips=None):
    chips = "".join(f'<span class="chip">{htmllib.escape(c)}</span>' for c in (exam_chips or []))
    rc = f"{review_count} review" + ("" if review_count == 1 else "s")
    return (
        f'    <!-- class-card:{slug} -->\n'
        f'    <div class="card" data-class="{slug}">\n'
        f'      <div class="row">\n'
        f'        <div><h3>{htmllib.escape(code)} · {htmllib.escape(name)}</h3>\n'
        f'        <div class="meta">{rc}</div></div>\n'
        f'        <a class="btn" href="{href}">View ▸</a>\n'
        f'      </div>\n'
        f'      <div class="chips">{chips}</div>\n'
        f'    </div>\n'
        f'    <!-- /class-card:{slug} -->'
    )


def register_class_on_hub(hub_path, *, class_slug, class_code, class_name,
                          class_page_href, review_count, exam_chips=None):
    """Insert/update a class card on the hub. Idempotent by class_slug."""
    hub_path = Path(hub_path)
    if not hub_path.exists():
        hub_path.write_text((ASSETS / "hub-template.html").read_text(encoding="utf-8"), encoding="utf-8")
    txt = hub_path.read_text(encoding="utf-8")
    card = build_class_card(class_slug, class_code, class_name, class_page_href, review_count, exam_chips)
    copen, cclose = f"<!-- class-card:{class_slug} -->", f"<!-- /class-card:{class_slug} -->"
    if copen in txt and cclose in txt:
        pre = txt[:txt.index(copen)]
        post = txt[txt.index(cclose) + len(cclose):]
        txt = pre + card.lstrip() + post
        action = "updated class card in"
    else:
        anchor = '<div class="grid" id="classes">'
        if anchor not in txt:
            return f"could not find '{anchor}' in {hub_path}; class card NOT added"
        idx = txt.index(anchor) + len(anchor)
        txt = txt[:idx] + "\n\n" + card + "\n" + txt[idx:]
        action = "added class card to"
    hub_path.write_text(txt, encoding="utf-8")
    return f"{action} {hub_path.name} (class={class_slug})"


def register_in_hub(hub_path, out_path, meta, questions):
    """Two-level registration: this quiz onto its class page, and the class onto the hub."""
    code, name = meta.get("classCode"), meta.get("className")
    if not code or not name:
        return "  [hub] skipped: meta lacks classCode/className (quiz built, not registered)"
    slug = meta.get("classSlug") or slugify(f"{code} {name}")
    hub_path = Path(hub_path)
    class_path = hub_path.parent / f"{slug}.html"
    href = os.path.relpath(out_path, hub_path.parent).replace(os.sep, "/")
    n, cases = len(questions), count_case_studies(questions)
    case_str = f" · {cases} case stud{'y' if cases == 1 else 'ies'}" if cases else ""
    meta_line = meta.get("cardMeta", f"{n} questions · NGN-style{case_str} · rationale after each answer")
    title = meta.get("cardTitle") or meta.get("header", "Review")
    chips = meta.get("chips") or derive_chips(questions)
    ensure_class_page(class_path, code, name)
    register_on_class_page(
        class_path, href=href, exam=meta.get("exam", "General practice"),
        exam_order=int(meta.get("examOrder", 0)), kind=meta.get("kind", "exam-review"),
        title=title, meta_line=meta_line, chips=chips, download=meta.get("download"))
    ctxt = class_path.read_text(encoding="utf-8")
    review_count = ctxt.count("<!-- quiz-card:")
    exam_labels = re.findall(r"<h2>(.*?)</h2>", ctxt)
    msg = register_class_on_hub(
        hub_path, class_slug=slug, class_code=code, class_name=name,
        class_page_href=f"{slug}.html", review_count=review_count, exam_chips=exam_labels)
    return f"  [hub] {class_path.name} now lists {review_count} review(s); {msg}"


def quality_audit(questions, total):
    """Heuristic difficulty/distractor guardrails. Advisory WARNINGS, not errors -
    they flag the tells that made the test-run quiz guessable so the builder can revise."""
    sata_counts = []
    for q in questions:
        t = q.get("type")
        if t == "radio":
            opts = q.get("opts") or []
            a = q.get("ans")
            if isinstance(a, int) and 0 <= a < len(opts) and len(opts) >= 2:
                correct = opts[a]
                if len(correct) == max(len(o) for o in opts) and \
                        sum(len(o) == len(correct) for o in opts) == 1:
                    warn(q["n"], "correct option is the LONGEST - a length tell; match option lengths")
                wrong = [o for i, o in enumerate(opts) if i != a]
                if any(THROWAWAY_RE.search(o) for o in wrong):
                    warn(q["n"], "throwaway distractor (document/no-action/normal) - every distractor should be a real, tempting error")
                if any(EXTREME_RE.search(o) for o in wrong):
                    warn(q["n"], "extreme/absolute distractor - too easy to eliminate; use plausible misconceptions")
        elif t == "multi" and isinstance(q.get("ans"), list):
            sata_counts.append(len(q["ans"]))
    if len(sata_counts) >= 3:
        if len(set(sata_counts)) == 1:
            warnings.append(f"  [SATA] all {len(sata_counts)} select-all items key {sata_counts[0]} correct - vary it (include 2- and 3-answer items)")
        elif min(sata_counts) >= 4:
            warnings.append("  [SATA] every select-all item keys 4+ correct - add some 2- and 3-answer items so 'pick most' doesn't win")
    if total >= 40:  # blueprint starvation only meaningful on a comprehensive set
        by_cat = {}
        for q in questions:
            by_cat[q.get("cat")] = by_cat.get(q.get("cat"), 0) + 1
        for cat in STARVED_CATS:
            pct = round(by_cat.get(cat, 0) / total * 100)
            if pct < BLUEPRINT[cat][0]:
                warnings.append(f"  [blueprint] {cat} is {pct}% (target >={BLUEPRINT[cat][0]}%) - chronically under-tested; add prioritization/delegation/psychosocial items")


def main():
    ap = argparse.ArgumentParser(description="Assemble + lint an NCLEX practice quiz.")
    ap.add_argument("data", help="path to the .quiz.json data file")
    ap.add_argument("-o", "--out", help="output HTML path (default: alongside data)")
    ap.add_argument("--template", help="path to quiz-template.html")
    ap.add_argument("--hub", help="study-hub index.html: register this quiz on its class page + the hub (needs class/exam/kind meta)")
    ap.add_argument("--index", help="DEPRECATED alias for --hub")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = ap.parse_args()

    data_path = Path(args.data)
    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERROR: could not read/parse {data_path}: {e}", file=sys.stderr)
        return 2

    meta = data.get("meta", {})
    questions = data.get("questions", [])
    if not questions:
        print("ERROR: no questions found", file=sys.stderr)
        return 2

    # renumber sequentially so the engine's display + "missed items" are clean
    for idx, q in enumerate(questions, 1):
        if q.get("n") not in (None, idx):
            warn(q.get("n"), f"renumbered to {idx} (items are numbered by array order)")
        q["n"] = idx

    for q in questions:
        validate_item(q)
    check_case_studies(questions)
    quality_audit(questions, len(questions))

    report = coverage_report(questions)
    print(report)
    if warnings:
        print("\nWARNINGS:")
        print("\n".join(warnings))
    if errors:
        print("\nERRORS:")
        print("\n".join(errors))
        print(f"\n{len(errors)} error(s) - not building. Fix and re-run.", file=sys.stderr)
        return 1
    if args.strict and warnings:
        print(f"\n--strict: {len(warnings)} warning(s) treated as errors.", file=sys.stderr)
        return 1

    tmpl_path = Path(args.template) if args.template else (
        Path(__file__).resolve().parent.parent / "assets" / "quiz-template.html"
    )
    tmpl = tmpl_path.read_text(encoding="utf-8")
    out = (tmpl
           .replace("__TITLE__", meta.get("title", "NCLEX Practice Quiz"))
           .replace("__HEADER__", meta.get("header", "NCLEX Practice"))
           .replace("__SUBTITLE__", meta.get("subtitle", ""))
           .replace("__FOOTNOTE__", meta.get("footnote", "NGN-style practice"))
           .replace("__QUESTIONS__", json.dumps(questions, ensure_ascii=False, indent=1)))

    out_path = Path(args.out) if args.out else data_path.with_suffix(".html")
    if out_path.suffix == ".json":  # data file was data.quiz.json -> data.quiz.html
        out_path = out_path.with_suffix(".html")
    out_path.write_text(out, encoding="utf-8")
    print(f"\nBuilt {out_path}  ({len(questions)} items, {out_path.stat().st_size} bytes)")

    hub = args.hub or args.index
    if hub:
        print(register_in_hub(hub, out_path, meta, questions))
    return 0


if __name__ == "__main__":
    sys.exit(main())
