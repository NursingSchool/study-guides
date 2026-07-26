#!/usr/bin/env python3
"""Randomize option order and balance where the correct answer lands.

Item authors overwhelmingly write the key first. Measured across the eight
quizzes built before this tool existed, the key sat at option A for 55-100% of
radio items (one quiz was 100%, another 86%), and option D was the answer
0-6% of the time. "Always pick A" beat most of them.

WHY NOT PURE RANDOM: random placement clumps at the sizes these quizzes use.
A genuinely random shuffle of a 14-item quiz produced 57% on B and 0% on C.
So radio keys are DEALT round-robin across the available positions -- uniform
by construction at any n -- while the assignment of items to slots and the
order of the distractors stay random. Random where it should be unpredictable,
balanced where it should be even.

Every permutation remaps its own keys and the keyed answer TEXT is asserted
unchanged, so option order changes and nothing about correctness moves.

Deterministic by default: the seed derives from the quiz content, so rebuilding
an unchanged quiz is stable and produces no diff. Pass --seed N to reshuffle
(e.g. to hand a study group a differently-ordered copy).

Usage:
    python balance_answers.py <quiz.json> [more.json ...] [--seed N] [--quiet]
"""
import argparse
import hashlib
import json
import random
import re
import sys
from collections import defaultdict


def keyed_text(q):
    """Every correct answer AS TEXT - the invariant we verify across shuffling."""
    t = q.get("type")
    try:
        if t == "radio":
            return [q["opts"][q["ans"]]]
        if t == "multi":
            return sorted(q["opts"][i] for i in q["ans"])
        if t == "cloze":
            return [b["opts"][b["a"]] for b in q.get("blanks", [])]
        if t == "bowtie":
            out = [q["problem"]["opts"][q["problem"]["a"]]]
            for g in ("actions", "params"):
                out += sorted(q[g]["opts"][i] for i in q[g]["ans"])
            return out
    except (KeyError, IndexError, TypeError):
        return None
    return []


_LEAD_NUM = re.compile(r"^\s*(?:level|stage|grade|step|phase|type|class)?\s*(\d+(?:\.\d+)?)", re.I)


def natural_order(opts):
    """Return the sorted order if these options are an intrinsic quantity series.

    NBME's Item-Writing Guide lists out-of-order numeric options under "Flaws
    Related to Irrelevant Difficulty" -- shuffling "4 months / 6 months / 9 months"
    into "6 / 4 / 9" is a defect, not added unpredictability. Same for ranked
    labels (Level 1-4, Stage I-IV).

    The distinction that matters: an option that IS a quantity must stay ordered;
    a clinical vignette that merely CONTAINS a number ("The 6-month-old with RSV
    whose breathing has become labored...") is prose and shuffles freely. Ordering
    vignettes by an incidental age would itself become a cue.
    """
    if len(opts) < 3:
        return None
    vals = []
    for o in opts:
        s = (o or "").strip()
        if len(s) > 28 or len(s.split()) > 4:   # prose, not a bare quantity
            return None
        m = _LEAD_NUM.match(s)
        if not m:
            return None
        vals.append(float(m.group(1)))
    if len(set(vals)) != len(vals):
        return None
    return sorted(range(len(opts)), key=lambda i: vals[i])


def _apply_natural(obj, field, key="ans"):
    """Sort an intrinsic quantity series into ascending order and remap its key."""
    opts = obj[field]
    order = natural_order(opts)
    if not order or order == list(range(len(opts))):
        return False
    remap = {old: new for new, old in enumerate(order)}
    obj[field] = [opts[i] for i in order]
    a = obj.get(key)
    obj[key] = sorted(remap[i] for i in a) if isinstance(a, list) else remap[a]
    return True


def _permute(rng, opts):
    """Canonicalize, then permute -- so the operation is IDEMPOTENT.

    Shuffling the incoming order makes each run depend on the previous one's
    output, so repeated runs keep producing different files even with a fixed
    seed. Sorting to a canonical order first means any input maps to the same
    output for a given seed, and re-running is a no-op.
    """
    order = sorted(range(len(opts)), key=lambda i: opts[i])
    canon = [opts[i] for i in order]
    to_canon = {old: new for new, old in enumerate(order)}
    idx = list(range(len(canon)))
    rng.shuffle(idx)
    final = [canon[i] for i in idx]
    canon_to_final = {old: new for new, old in enumerate(idx)}
    return final, {old: canon_to_final[to_canon[old]] for old in range(len(opts))}


def _row_order_bad(seq):
    """match/matrix answer orders that give the item away without reading it."""
    n = len(seq)
    if n < 3:
        return False
    if seq == list(range(n)):                              # identity: pick top-to-bottom
        return True
    if seq == sorted(seq) or seq == sorted(seq, reverse=True):   # pre-sorted grouping
        return True
    longest = run = 1
    for i in range(1, n):
        run = run + 1 if seq[i] == seq[i - 1] else 1
        longest = max(longest, run)
    return longest >= max(3, (n + 1) // 2)                  # one answer in a long block


def fix_rows(q, rng):
    """Reorder match/matrix ROWS so the answer sequence isn't guessable.

    Rows carry their own answer, so reordering them changes presentation only.
    Never touch the keys.
    """
    if q.get("type") not in ("match", "matrix"):
        return False
    rows = q.get("rows") or []
    seq = [r.get("a") for r in rows]
    if len(seq) < 3 or any(not isinstance(a, int) for a in seq) or not _row_order_bad(seq):
        return False
    canon = sorted(rows, key=lambda r: (r.get("a"), str(r.get("t"))))  # idempotent base
    for _ in range(400):
        cand = canon[:]
        rng.shuffle(cand)
        if not _row_order_bad([r.get("a") for r in cand]):
            q["rows"] = cand
            return True
    return False


def shuffle_non_radio(q, rng):
    """multi / cloze / bowtie: no single 'position', so plain randomization."""
    t = q.get("type")
    if t == "multi" and len(q.get("opts", [])) >= 2:
        if natural_order(q["opts"]):
            return _apply_natural(q, "opts")
        q["opts"], m = _permute(rng, q["opts"])
        q["ans"] = sorted(m[i] for i in q["ans"])
        return True
    if t == "cloze":
        did = False
        for b in q.get("blanks", []):
            if len(b.get("opts", [])) >= 2:
                if natural_order(b["opts"]):
                    did |= _apply_natural(b, "opts", key="a")
                    continue
                b["opts"], m = _permute(rng, b["opts"])
                b["a"] = m[b["a"]]
                did = True
        return did
    if t == "bowtie":
        p = q.get("problem", {})
        if len(p.get("opts", [])) >= 2:
            p["opts"], m = _permute(rng, p["opts"])
            p["a"] = m[p["a"]]
        for g in ("actions", "params"):
            grp = q.get(g, {})
            if len(grp.get("opts", [])) >= 2:
                grp["opts"], m = _permute(rng, grp["opts"])
                grp["ans"] = sorted(m[i] for i in grp["ans"])
        return True
    return False


def balance(path, seed=None, quiet=False):
    d = json.load(open(path, encoding="utf-8"))
    qs = d.get("questions", [])
    if not qs:
        print(f"  {path}: no questions", file=sys.stderr)
        return 1

    if seed is None:
        # Content-derived so rebuilds are stable and produce no diff.
        # hashlib, NOT hash(): built-in hash() is salted per process
        # (PYTHONHASHSEED), which would reshuffle on every single run.
        digest = hashlib.sha256(
            "".join(q.get("stem", "") for q in qs).encode("utf-8")
        ).hexdigest()
        seed = int(digest[:8], 16)
    rng = random.Random(seed)

    before = {id(q): keyed_text(q) for q in qs}
    touched = 0

    # radio: deal target positions round-robin, grouped by option count so a
    # 3-option item is never asked to put its key at index 3.
    groups = defaultdict(list)
    for q in qs:
        if q.get("type") == "radio" and isinstance(q.get("ans"), int) and len(q.get("opts", [])) >= 2:
            groups[len(q["opts"])].append(q)
    # Quantity series (4/6/9 months, Level 1-4) must stay in natural order --
    # NBME names out-of-order numeric options as an irrelevant-difficulty flaw.
    # Pull them out of position balancing entirely.
    for k in list(groups):
        keep = []
        for q in groups[k]:
            if natural_order(q["opts"]):
                if _apply_natural(q, "opts"):
                    touched += 1
            else:
                keep.append(q)
        groups[k] = keep

    for k, items in groups.items():
        # Balanced counts alone still let runs form -- a uniform 25/25/25/25 quiz
        # had four consecutive A's, which is what a student actually notices.
        # Deal greedily in quiz order instead: keep the counts balanced, but never
        # take a position that would make a third consecutive repeat.
        remaining = {p: 0 for p in range(k)}
        for i in range(len(items)):
            remaining[i % k] += 1
        targets, prev1, prev2 = [], None, None
        for _ in items:
            avail = [p for p, c in remaining.items() if c > 0]
            ok = [p for p in avail if not (p == prev1 and p == prev2)]
            pool = ok or avail
            best = max(remaining[p] for p in pool)          # drain the fullest first
            pick = rng.choice([p for p in pool if remaining[p] == best])
            remaining[pick] -= 1
            targets.append(pick)
            prev2, prev1 = prev1, pick
        for q, tgt in zip(items, targets):
            opts = q["opts"][:]
            key = opts.pop(q["ans"])
            opts.sort()          # canonical base -> idempotent across re-runs
            rng.shuffle(opts)
            opts.insert(tgt, key)
            q["opts"], q["ans"] = opts, tgt
            touched += 1

    for q in qs:
        if shuffle_non_radio(q, rng):
            touched += 1
    rows_fixed = sum(1 for q in qs if fix_rows(q, rng))

    for q in qs:
        if before[id(q)] is not None and keyed_text(q) != before[id(q)]:
            print(f"ABORT {path}: keyed answer text changed on '{q.get('topic')}' "
                  "- file NOT written", file=sys.stderr)
            return 1

    json.dump(d, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

    if not quiet:
        dist, tot = defaultdict(int), 0
        for q in qs:
            if q.get("type") == "radio" and isinstance(q.get("ans"), int):
                dist[q["ans"]] += 1
                tot += 1
        spread = " / ".join(f"{round(100*dist[i]/tot)}%" for i in range(4)) if tot else "-"
        name = path.replace("\\", "/").split("/")[-1]
        rows_note = f"  rows fixed: {rows_fixed}" if rows_fixed else ""
        print(f"  {name:<40} {touched:>3} items   radio A/B/C/D = {spread}{rows_note}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help="one or more <name>.quiz.json")
    ap.add_argument("--seed", type=int, default=None,
                    help="explicit seed; omit for a stable content-derived one")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    rc = 0
    for f in a.files:
        rc |= balance(f, a.seed, a.quiet)
    sys.exit(rc)


if __name__ == "__main__":
    main()
