# Comprehensive Exam Build — Plan → Map → Reduce

A comprehensive exam review (the default) is too large and too coverage-sensitive for one
agent to write in a single pass — that produces formulaic distractors, uneven coverage, and
difficulty drift. It is exactly what made the first test-run quiz guessable (73% length tells,
emergencies omitted, Management of Care / Psychosocial near zero). Build it in three phases.

## 1. PLAN (you, the main agent)

- **Inventory** every module (`WeekN_*.md`) in the exam block; skim each to gauge its weight.
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
- **List the must-test high-yield per module before writing:** emergencies, priority actions,
  "must report," meds + antidotes + contraindications first; nice-to-knows fill the rest. The
  per-module gap analyses in this folder's history are a model for what "high-yield" means.

## 2. MAP (one subagent per module, in parallel)

Dispatch one subagent per module with the briefing below. Each returns its module's items as a
JSON array (no file writes). Run them concurrently, then collect.

### Subagent briefing template (fill the <slots>)
```
Write NCLEX-RN exam items for ONE module. Return ONLY a JSON array of item objects —
no prose, no file writes.

Source (read in full): <abs path to WeekN_Topic.md>
Write exactly <N> items, distributed as <e.g. "7 radio, 3 SATA, 1 matrix; mostly Analysis">.
<If this module owns a case study:> Include a 6-item unfolding case study on <scenario>,
one item per NCJMM step, each stem labeled "CASE (n/6) <step>."

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
Return: a JSON array of items using the exact field names from the schema.
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
- **Report** the final coverage table + per-module allocation to Chris, and link the `.html`.

This is *why* fan-out works: every module is independently and deeply authored (a dedicated
agent finds the high-yield and writes tougher distractors), the floor guarantees even coverage,
parallelism makes 120–150 items feasible without one agent fatiguing, and the reduce step is a
single place to dedupe, rebalance, and hold the difficulty bar.
