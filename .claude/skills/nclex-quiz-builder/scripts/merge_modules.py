#!/usr/bin/env python3
"""REDUCE helper: merge per-module question files into one quiz data file.

Usage:
    python merge_modules.py <modules-dir> --meta <meta.json> -o <out.quiz.json>

Modules are merged in sorted filename order (so name them w4_01_*, w4_02_*, ... to
control teaching order). Each module file is a normal quiz data file; only its
`questions` array is used.

In any string value of the meta file, `{n}` is replaced with the total item count and
`{cases}` with the number of unfolding case studies found — so you can write
"subtitle": "... {n} items ..." and have it fill itself in.

Prints a per-module count table so you can see coverage at a glance.
"""
import argparse
import json
import pathlib
import re
import sys

CASE_RE = re.compile(r"CASE[^\(]*\(\s*\d+\s*/\s*6\s*\)", re.IGNORECASE)


def main():
    ap = argparse.ArgumentParser(description="Merge per-module quiz files into one quiz.")
    ap.add_argument("modules_dir", help="directory holding the per-module *.quiz.json files")
    ap.add_argument("--meta", required=True, help="JSON file containing the quiz `meta` object")
    ap.add_argument("-o", "--out", required=True, help="output .quiz.json path")
    args = ap.parse_args()

    mod_dir = pathlib.Path(args.modules_dir)
    files = sorted(mod_dir.glob("*.quiz.json"))
    if not files:
        print(f"ERROR: no *.quiz.json files in {mod_dir}", file=sys.stderr)
        return 2

    questions, per_module = [], []
    for f in files:
        try:
            qs = json.loads(f.read_text(encoding="utf-8")).get("questions", [])
        except Exception as e:
            print(f"ERROR: could not parse {f.name}: {e}", file=sys.stderr)
            return 2
        per_module.append((f.stem, len(qs)))
        questions.extend(qs)

    n = len(questions)
    cases = len({q.get("topic") for q in questions if CASE_RE.search(q.get("stem", ""))})

    meta = json.loads(pathlib.Path(args.meta).read_text(encoding="utf-8"))
    for k, v in meta.items():
        if isinstance(v, str):
            meta[k] = v.replace("{n}", str(n)).replace("{cases}", str(cases))

    out = pathlib.Path(args.out)
    out.write_text(json.dumps({"meta": meta, "questions": questions}, ensure_ascii=False, indent=1),
                   encoding="utf-8")

    width = max(len(s) for s, _ in per_module)
    for stem, c in per_module:
        print(f"  {stem:<{width}}  {c:>3}")
    print(f"\nmerged {len(files)} modules -> {n} items, {cases} case stud{'y' if cases == 1 else 'ies'}")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
