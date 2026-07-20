# NGN Item Writing — Rules and the `Q[]` Item Schema

How to write items that read like operational NCLEX questions, and the exact JSON
shape each item must take so the engine renders it. The assembler (`scripts/assemble_quiz.py`)
checks all of this; this file explains the *why* so the items are actually good, not just valid.

## Quality rules (the part that makes items feel real)

These come from real NCLEX item-writing practice. Valid-but-shallow items are the
main failure mode — guard against it.

1. **Cognitive level.** Write the majority at Application or higher. The stem should
   force the candidate to interpret data and decide, not recognize a definition.
   Recall items are the exception, not the rule.
2. **The stem carries the data to reason with.** Give a realistic clinical picture:
   age, diagnosis, setting, relevant vitals, labs, meds, and findings — only data
   drawn from or consistent with the source material. A reader should be able to
   solve it from the stem alone.
3. **Distractors are plausible and diagnostic.** Every wrong option should reflect a
   *specific common error or misconception* a real student makes — not filler. Keep
   all options grammatically parallel and similar in length. No "all/none of the
   above." The keyed answer should avoid absolutes (always, never, all, none).
4. **Priority items need a defensible framework.** If the stem asks for the first /
   priority / most important action, the key must win by an explicit rule (ABCs,
   Maslow, safety, acute-over-chronic, unstable-over-stable, assess-before-intervene)
   — and the `rat` should name that framework.
5. **SATA = independent true/false judgments.** Each option is judged on its own, not
   compared to the others. **Vary the number correct** across your SATA items (some 2,
   some 3, some 4) so the count is never a giveaway. Offer 5–6 options.
6. **Patient-centered, unbiased language.** "Substance misuse," not "substance abuse";
   affirming, inclusive phrasing (see [blueprint-2026.md](blueprint-2026.md)).
7. **The `rat` field is one compact paragraph.** State why the key is right AND why the
   notable distractors are wrong, in 1–3 sentences. (This matches the existing quizzes
   and renders cleanly in the feedback box — it intentionally replaces the original
   "separate paragraph per distractor" format.)
8. **The `strat` field is one line** — a transferable test-taking heuristic or memory
   hook ("Variable + Cord both squeeze the cord — link them.").

## Distractor discipline & difficulty (why the first test-run quiz was too easy)

An audit of the naive test-run quiz found it guessable — **73% of single-answer items made
the correct option the longest**, ~1 in 5 could be solved with zero nursing knowledge, and
many "Analysis" items were really recall. A non-nursing person reasoned to many right answers.
That happens when the distractors do the work for the test-taker. Avoid these failure modes:

- **The layperson test (the core check).** Cover the rationale and try to pick the answer
  using only test-taking logic — length, tone, the one "measured" option, eliminating extremes.
  If you can, the distractors have failed. Each distractor must be a *specific clinical error a
  real student would actually make*: a plausible-but-wrong action, a confused mechanism, the
  right action at the wrong time, a look-alike value.
- **Match option lengths.** Don't make the key a long "comprehensive combo" while distractors
  are three words — that's the single biggest tell. Keep options in a similar length band and
  parallel grammar. (The linter warns when the key is the longest.)
- **No throwaway distractors** — "document and take no action," "continue routine monitoring,"
  "reassure, this is normal," "do nothing" — *unless* recognizing a normal finding is genuinely
  the point. Otherwise everyone eliminates them.
- **No absolute/extreme filler** — "never," "always," "vigorously massage," "restrict all
  fluids," "stop breastfeeding permanently," "immediately." An option flagged by an extreme word
  teaches test-wiseness, not nursing.
- **Don't telegraph case-study outcomes by valence.** On "which finding shows it worked?"
  items, wrong options must be plausible partial-successes or realistic-but-wrong endpoints —
  not obviously-bad outcomes ("high-pitched cry and arching") any reader rejects.
- **Write to the right altitude — and tag it honestly.** Application = apply a principle to
  this client. Analysis = discriminate among *competing plausible* explanations within a
  realistic cue set (atony vs. laceration vs. retained fragments, given the cues). Evaluation =
  judge whether the intervention worked / which evidence is strongest. Recall of a definition or
  a number is **not** Analysis — don't label it so. Aim for mostly Application/Analysis with some
  genuine Evaluation.
- **Cover the dangerous content first.** The audit's biggest gap was *omitted emergencies and
  safety/med facts* (uterine rupture, methylergonovine contraindicated in HTN, exchange
  transfusion, newborn security, skull-fracture ↑ICP). For each module, test its emergencies,
  priority actions, "must report," and meds/antidotes/contraindications **before** nice-to-knows.
- **No redundancy.** Don't spend two items on the same lookup table or single fact.
- **Test the procedure, not the worked example.** When a module builds an exercise around a
  specific named study, patient, or scenario ("Review this study by Gallegos & Sortedahl…",
  a PICOT walkthrough of one clinical question, a phenomenology example), the exam does **not**
  test that scenario — it presents a *different* one and asks the same question-types. Treat the
  named example as a demonstration of a *move* (appraise a framework, build a PICOT, classify a
  design) and write the item to run that move on a **fresh** stem. Never key an item to facts
  that live only in an assigned-but-unreachable source, and never flag a missing article as a
  content gap — the article is disposable; the skill it teaches is the testable content. (This
  is why EBP-24's unreachable Gallegos study is a non-issue: the Week 3 theory items exercise the
  six appraisal questions on new studies instead.)

## Supported item types

The engine renders **only** these seven. Do not invent others (no highlight/hot-spot,
no free drag-and-drop) — there is no renderer and the quiz will silently break.

Every item shares these fields:
`n` (int, auto-renumbered), `topic` (string, shown as a chip), `type`, `cat`
(Client Needs — verbatim from blueprint), `lvl` (Application/Analysis/Evaluation),
`stem` (use `\n` for line breaks), `rat`, `strat`.

### radio — single best answer (also: trend)
```json
{ "n":1, "topic":"Fetal Monitoring", "type":"radio",
  "cat":"Reduction of Risk Potential", "lvl":"Analysis",
  "stem":"The monitor shows a gradual FHR decrease beginning after the peak of the contraction... Priority action?",
  "opts":["Document as normal","Reposition to left lateral and notify the provider","Prepare for immediate delivery","Increase the oxytocin"],
  "ans":1,
  "rat":"A gradual decel starting after the peak is a LATE deceleration (uteroplacental insufficiency): reposition, fluids, O2, notify. Not early (head compression).",
  "strat":"Timing names the deceleration; 'late' = placenta = act." }
```
Usually 4 options. **Trend items** are just `radio` (or `multi`) with serial data over
≥3 timepoints written into the stem, e.g. `"...temps: 36.6°C at birth, 36.2°C at 30 min, 35.9°C at 60 min..."`.

### multi — select all that apply (SATA)
`opts` = 5–6 options; `ans` = array of correct indices (vary the length).
```json
{ "type":"multi", "opts":["...","...","...","...","..."], "ans":[0,1,3,4], ... }
```

### cloze — drop-down blanks
Stem references `[1] [2] ...`; each blank is its own dropdown.
```json
{ "type":"cloze",
  "stem":"The normal FHR baseline is [1]. Minimal variability may be caused by [2].",
  "blanks":[
    {"label":"[1] Normal baseline","opts":["90-110 bpm","110-160 bpm","120-180 bpm"],"a":1},
    {"label":"[2] Minimal variability","opts":["maternal fever","fetal sleep or opioids","cocaine use"],"a":1}],
  ... }
```

### matrix — grid (rows scored across columns)
e.g. Expected/Reportable, Indicated/Contraindicated/Non-essential, Expected/Unexpected.
```json
{ "type":"matrix", "cols":["Expected","Reportable"],
  "rows":[{"t":"Clear, odorless amniotic fluid","a":0},
          {"t":"Maternal temperature 38.4°C","a":1}],
  ... }
```

### match — match each row to one item from a shared pool
```json
{ "type":"match",
  "shared":["Stroke the cheek","A sudden noise","Stroke the heel upward","Turn the head to one side"],
  "rows":[{"t":"Rooting","a":0},{"t":"Moro","a":1},{"t":"Babinski","a":2},{"t":"Tonic neck","a":3}],
  ... }
```

### bowtie — central problem + 2 actions + 2 parameters
Key **exactly** one problem, two actions, two parameters (standard 5-token shape).
```json
{ "type":"bowtie",
  "stem":"CASE (4/6) Generate solutions (bowtie). Choose the central problem, two actions, and two parameters to monitor.",
  "problem":{"opts":["Uterine atony with hemorrhage","Puerperal infection","Postpartum depression"],"a":0},
  "actions":{"opts":["Massage the fundus","Empty the bladder","Apply ice to the perineum","Restrict fluids"],"ans":[0,1]},
  "params":{"opts":["Fundal tone and position","Lochia amount","Deep tendon reflexes","Bowel sounds"],"ans":[0,1]},
  ... }
```

### calc — numeric entry (dosage / weight loss / I&O)
`acceptLo`/`acceptHi` define a tolerance band; `answer` is the feedback string.
```json
{ "type":"calc", "stem":"Birth weight 3,400 g; day-3 weight 3,100 g. Enter % weight loss.",
  "acceptLo":8.5, "acceptHi":9.4, "answer":"9% (8.8%)",
  "rat":"300 ÷ 3,400 × 100 = 8.8% ≈ 9%. A loss over 7% early needs evaluation.",
  "strat":"Weight lost ÷ birth weight × 100; flag if it crosses 7% early." }
```

## Formatting gotchas (these break the build or the page)

- The data file is **JSON**: keys and strings use double quotes; escape inner double
  quotes as `\"`; apostrophes are fine as-is; line breaks in a stem are `\n`.
- `ans` indices are **0-based** and must point at real options.
- Keep Unicode (°, ×, ÷, em dash, ·) — the file is written UTF-8.
- Don't hand-number items; the assembler renumbers by array order.
