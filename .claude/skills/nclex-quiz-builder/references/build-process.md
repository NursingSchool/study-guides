# Comprehensive Exam Build — Plan → Map → Reduce

A comprehensive exam review (the default) is too large and too coverage-sensitive for one
agent to write in a single pass — that produces formulaic distractors, uneven coverage, and
difficulty drift. It is exactly what made the first test-run quiz guessable (73% length tells,
emergencies omitted, Management of Care / Psychosocial near zero). Build it in three phases.

## 1. PLAN (you, the main agent)

- **Read every `WeekN_Prepare_and_Plan.md` in the block FIRST — before inventorying modules.**
  This is the course's own statement of what the week tests, and it turns the plan from "cover the
  material" into "cover what they said they'd test."
  - Extract the **Weekly Objectives** across all weeks into one flat checklist. This is your
    scope. A ~3-week block typically yields ~19 objectives. **Every objective must be claimed by
    at least one module** in the allocation below; an unclaimed objective is a hole in the exam
    review, and you should say so rather than quietly ship it.
  - Note the **`(CO n)` tags** on the Weekly Outcomes. Carry them through so the final report can
    show course-outcome coverage next to Client Needs coverage.
  - Cross-check **Concepts with Exemplars** against the `WeekN_*.md` files present. A listed
    exemplar with no guide file is a **missing capture** — flag it to Chris; don't silently drop
    the topic.
  - Mine **Are You Ready to Apply?** for high-yield seeds; those are the course's own framing of
    what a student should be able to answer.
- **Inventory** every module (`WeekN_*.md`) in the exam block; skim each to gauge its weight.
  Include any `WeekN_Supplement_*.md` — those exist precisely because an objective outran the
  Edapt content, so they are high-yield by construction. Give a supplement its own MAP agent when
  it carries real volume (a full schedule, a drug class table); fold a thin one into the related
  content module.
- **Map objectives → modules.** Before allocating counts, write the objective-to-module mapping
  out. Objectives that no module covers are the gap list; objectives covered by several modules
  tell you where the exam's weight actually sits.
- **One module = one guide file.** Treat every `WeekN_*.md` as its own module and give it its
  own MAP agent — *including* the "overview" and "Nursing Application" companion guides. Never
  fold several files into one agent: it silently under-covers a module, and the student counts
  files as modules. Tell each overview/application agent to focus on its distinct angle
  (overview = integrative/classification/comparison; application = assessment/teaching/
  prioritization) so it complements rather than duplicates the content modules — the Reduce
  dedup pass catches any remaining overlap.
- **Allocate items per module, scaled to material volume, with a floor.** Denser guides earn
  more items; every module gets at least ~3–4 so nothing is a token mention. Size by material,
  not a round number — a ~20-module block (e.g. Weeks 4–7) supports ~120–150 quality items.
  Empirically that block wants roughly: Week 4 ~28, Week 5 ~32, Week 6 ~20, Week 7 ~50. Never
  cap coverage to hit a round number; if forced to, `log()`/note what you dropped.
- **Set difficulty + blueprint targets.** Mostly Application/Analysis with some Evaluation;
  ≥80% at Application+. Deliberately fund **Management of Care** (prioritization, delegation,
  referral) and **Psychosocial Integrity** — they're starved by default, but the guides hold the
  content (newborn security/abduction, family grief, postpartum mental health).
- **Assign and spread the NGN formats.** Decide which module owns each 6-item unfolding case
  study, bowtie, trend, and matrix — and spread them across the block. The richest emergency
  material (e.g. intrapartum: cord prolapse, tachysystole, dystocia) deserves a case study; don't
  cluster all case studies in one topic.
- **Budget the format mix at the block level, then hand each agent its exact quota.** Left to
  choose, agents over-produce multi-select — measured drift is ~50% against a 40% ceiling. Compute
  the block totals first (55–70% `radio`+`calc`, 10–20% `multi`, 15–25% `matrix`/`cloze`/`match`/
  `bowtie`), divide into per-module quotas, and state each as an explicit count in the briefing
  (e.g. "7 radio, 2 SATA, 1 matrix"). A module with only 4 items should usually be **all radio** —
  NGN formats belong in the modules rich enough to support them.
- **List the must-test high-yield per module before writing:** emergencies, priority actions,
  "must report," meds + antidotes + contraindications first; nice-to-knows fill the rest. The
  per-module gap analyses in this folder's history are a model for what "high-yield" means.

## 2. MAP (one subagent per module, in parallel)

Dispatch one subagent per module with the briefing below. Each returns its module's items as a
JSON array (no file writes). Run them concurrently, then collect.

### Subagent briefing template (fill the <slots>)
```
Write NCLEX-RN exam items for ONE module.

Source (read in full): <abs path to WeekN_Topic.md>
Write to exactly this absolute path: <abs path>/modules/<wN_NN_topic>.quiz.json
Shape: {"meta": {"title": "draft"}, "questions": [ ...items... ]}. The `meta` block is a
throwaway placeholder — `merge_modules.py` supplies the real one. Do NOT emit a bare array;
both scripts call .get("questions") and crash on a list.
Write exactly <N> items, distributed as <e.g. "7 radio, 3 SATA, 1 matrix; mostly Analysis">.
<If this module owns a case study:> Include a 6-item unfolding case study on <scenario>,
one item per NCJMM step, each stem labeled "CASE (n/6) <step>."

WEEKLY OBJECTIVES this module is responsible for (from the course's Prepare and Plan page —
these are the course's own statement of what is testable; each needs at least one item):
<the objectives mapped to this module in the PLAN, verbatim>

MUST-TEST high-yield (cover these first, they cannot be omitted):
<bulleted list from the PLAN — emergencies / priority / meds / contraindications>

Follow these exactly (read them first):
- Item schema + the 7 supported types: <skill>/references/ngn-item-writing.md
- Distractor discipline & difficulty (SAME file): every distractor must be a plausible error a
  real student makes; match option lengths; no throwaway/absolute filler; tag difficulty
  honestly; write to Application/Analysis, not recall. Apply the "layperson test" to each item.
- Client Needs `cat` strings (verbatim) + NCJMM steps: <skill>/references/blueprint-2026.md

Ground every value in the source and KEY THE GUIDE'S VERSION — ~90% of this student's exam
questions come straight from these Edapt modules, so the guide is the tested content. Do not
substitute current evidence-based practice and do not skip a topic because the guide lags
current standards. Only blatantly wrong/unsafe content or an obviously bad capture is an
exception; flag those in your summary instead of silently changing them.

Then self-lint until clean — 0 errors, 0 warnings:
  python <skill>/scripts/assemble_quiz.py <your output file>
Ignore the advisory per-category blueprint-band percentages; they assume a full-length exam
and do NOT apply to a single-module set. Never pad items to chase a band.

Report back briefly: (1) item count with type + cognitive level each, (2) whether you built a
case study and how many steps, (3) linter status, (4) which of your assigned weekly objectives
each item covers, and any you could NOT cover from this guide — say so explicitly rather than
stretching an item to claim one, (5) any internal contradiction, garbled text, or uncaptured
media you found in the guide — quote it. Points (4) and (5) feed the objective-coverage report
and a defect report back to the material's authors, so be specific.
```

## 3. REDUCE (you, the main agent)

- **Merge** all modules into one `questions` list with the bundled helper — don't hand-roll it:
  ```
  python <skill>/scripts/merge_modules.py <modules-dir> --meta meta.json -o <name>.quiz.json
  ```
  Modules merge in sorted filename order (name them `w4_01_*`, `w4_02_*`, … to set teaching
  order). `meta.json` holds the quiz `meta` object; `{n}` and `{cases}` in any meta string are
  filled in automatically. It prints a per-module count table so coverage is visible at a glance.
- **Dedupe** near-identical items (same fact/lookup table twice) — keep the stronger one.
- **Verify case studies**: each is exactly 6 linked items, one evolving patient, steps 1–6.
- **Build + lint**: write `<name>.quiz.json` (include the `classCode`/`className`/`exam`/
  `examOrder`/`kind` hub metadata — see SKILL.md), run `assemble_quiz.py … -o <name>.html
  --hub index.html` to build, lint, and register it on its class page + the hub.
  Read every WARNING.
- **Rebalance until clean**: rewrite items the linter flags for length-tell / throwaway /
  absolute / SATA-variation; if Management of Care or Psychosocial are under band, swap in
  prioritization/psychosocial items; re-run until the linter is quiet (or each remaining warning
  has a logged reason). This central pass is where even coverage and difficulty are enforced.
- **Run `balance_answers.py` — a required step, not an optional one.** Guessability tells are structurally invisible to per-module agents: each lints only its own handful of items, so a whole-quiz skew toward option A never shows up until merge.
  ```
  python <skill>/scripts/balance_answers.py <name>.quiz.json
  ```
  It rewrites the `.quiz.json` in place — run it **after** `merge_modules.py` and **before** `assemble_quiz.py`. What it does:
  - **Balances correct-answer position** for `radio`. Authors overwhelmingly write the key first: across the eight quizzes built before this tool existed, the key sat at option A for 55–100% of items (one was 100%, another 86%) and option D was correct 0–6% of the time. Targets are *dealt round-robin* per option-count, so the spread is uniform **by construction** — genuinely random shuffling still clumps at these sizes (a 14-item quiz landed 57% on B, 0% on C).
  - **Randomizes option order** for `multi`, `cloze`, and `bowtie`, where there's no single "position" to balance.
  - **Reorders match/matrix ROWS** out of identity (`[0,1,2,3]`, answerable top-to-bottom) and clustered (`[0,0,0,1,1,1]`, grouping visible without reading) orders. Rows carry their own answers, so keys are never touched.
  - **Asserts the keyed answer TEXT is unchanged** and refuses to write if it isn't.
  - **Idempotent and deterministic** — it canonicalizes before permuting and seeds from quiz content, so re-running is a no-op and rebuilds produce no spurious diff. `--seed N` gives a differently-ordered copy (e.g. a separate version for a study group).

  `assemble_quiz.py` then reports the position distribution and warns if any option exceeds 40%, and hard-ERRORs on an identity-mapped match. Those are the safety net; this tool is the fix.
- **Length tells.** The keyed option being longest — per-module agents usually catch this, but re-check the merged set.
- **Fix the format mix here.** Read the linter's `Item format mix` block. If multi-select is over
  the 40% ceiling or `radio` is under 55%, convert the weakest multi-select items to single-best
  — the usual candidates are SATA items whose options aren't truly independent, and `match`/`cloze`
  items that are really one fact split into blanks. Converting is better than deleting: keep the
  content, change the format. Re-run until the bands are met.
- **Check objective coverage before reporting.** Assemble the MAP agents' objective claims into
  one table: every weekly objective from the block, and which items cover it. **Any objective with
  zero items is a defect** — either write items for it, or, if the source genuinely doesn't
  support it, tell Chris the objective is untestable from current material and what's missing.
  Do not ship silently under-covered.
- **Report** to Chris: the Client Needs coverage table, the **objective-coverage table** (with any
  uncovered objectives called out), per-module allocation, any missing captures found via Concepts
  with Exemplars, and the link to the `.html`.

This is *why* fan-out works: every module is independently and deeply authored (a dedicated
agent finds the high-yield and writes tougher distractors), the floor guarantees even coverage,
parallelism makes 120–150 items feasible without one agent fatiguing, and the reduce step is a
single place to dedupe, rebalance, and hold the difficulty bar.
