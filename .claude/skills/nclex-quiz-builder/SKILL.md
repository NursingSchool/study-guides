---
name: nclex-quiz-builder
description: >-
  Generate an interactive, self-contained NCLEX-RN practice quiz (single HTML
  file) from study material, matching the 2026 NCLEX-RN test plan and the NCSBN
  Clinical Judgment Measurement Model. Use whenever Chris wants to build an
  NCLEX-style EXAM REVIEW for an upcoming test (typically spanning a block of
  weeks / all modules on that exam), NCLEX/NGN practice questions, a quiz for his
  study group, to "quiz me on" exam material, or to turn his course study guides
  into questions for his GitHub study hub — even if he doesn't say the word
  "quiz." Produces the
  same dark-themed HTML format as his existing maternal-child quiz, with NGN item
  types (SATA, matrix, cloze, bowtie, trend, unfolding case studies), rationales,
  and a Client Needs coverage breakdown. Do NOT use for non-nursing quizzes or
  for the verbatim Edapt module extraction (that's the edapt-extract skill).
---

# NCLEX Quiz Builder

Turns nursing study material into an interactive, self-contained NCLEX-RN practice
quiz: one HTML file that renders questions, scores answers, shows per-item rationales,
and reports Client Needs coverage. Chris hosts these on his GitHub study-group page.

**These are usually comprehensive EXAM REVIEWS** — one quiz covering everything on an
upcoming exam (a block of weeks / all tested modules), like the live Weeks 4-7
maternal-child quiz (100 items, 2 unfolding case studies). A single-topic quiz is just
a smaller version of the same thing. Default to the exam-review scope unless Chris
narrows it.

You are an expert NCLEX-RN item writer. Write items indistinguishable in style,
difficulty, and structure from operational NCLEX questions, aligned to the **2026
NCLEX-RN Test Plan** (effective April 1, 2026) and the **NCSBN Clinical Judgment
Measurement Model**.

## How it works (architecture)

The HTML engine — rendering, scoring, results screen, coverage table — is fixed and
bundled. **Your job is to write the questions as a JSON data file; a script injects
them into the engine.** Never hand-write the HTML/JS engine; it's proven and the
script keeps it correct.

- `assets/quiz-template.html` — the engine (don't edit per-quiz).
- `scripts/assemble_quiz.py` — builds the final HTML from your JSON **and lints it**
  (structural rules + 2026 blueprint coverage). Non-zero exit = there are errors to fix.
- `references/blueprint-2026.md` — Client Needs categories + exact `cat` strings,
  NCJMM steps, terminology, prioritization frameworks. **Read this before classifying.**
- `references/ngn-item-writing.md` — quality rules, **distractor discipline & difficulty**,
  and the per-type item schema with examples. **Read this before writing items.**
- `references/build-process.md` — the multi-agent **Plan → Map → Reduce** build for
  comprehensive exams (the default). **Read this for any multi-module exam review.**

## Workflow

**Two modes.** A **comprehensive exam review** (the default) is built with the multi-agent
**Plan → Map → Reduce** process in [build-process.md](references/build-process.md) — read and
follow it, because a single agent writing 100+ items in one pass is what produced the
guessable, unevenly-covered test-run quiz. A single small/topic quiz can be written in one pass
using the steps below, which are also the shared mechanics (source resolution, data-file shape,
build/lint, hub) that the comprehensive build reuses in its Reduce phase.

1. **Get the source + settings.** The authoritative source is the repo's course
   material — see "Source material" below. Resolve what Chris means to actual files;
   only ask if you genuinely can't tell which week/topic he means.

   Settings (ask only if unclear; otherwise use these defaults):
   - **Scope & number of questions** — default to a **comprehensive exam review**:
     cover every module tested on the exam (the full block of weeks), sized like the
     live example (~50–100 items, scaled to how much material the exam spans). Go
     smaller only when Chris asks for a single topic or a quick set.
   - **Item-type mix** — default a realistic NGN blend: mostly single-best, several
     SATA, and a few clinical-judgment items (matrix, cloze, bowtie, a trend item,
     and at least one 6-item unfolding case study) when the content supports them.
   - **Difficulty** — default Application/Analysis; raise to Analysis/Evaluation on request.
   - **Topic focus** — default: follow the source material as given.

2. **Read the two reference files**, then write items per `references/ngn-item-writing.md`.
   Use only data drawn from or consistent with the source. If the source conflicts with
   current evidence-based practice, flag it instead of writing a wrong item.

3. **Write the data file** `<name>.quiz.json` next to where the quiz should live
   (the repo root for study-hub quizzes, so it sits beside `index.html`). Name it for
   the exam block, matching the live convention — e.g. `maternal-child-weeks4-7`. Shape:
   ```json
   { "meta": {
       "title":"<browser tab>", "header":"<H1 in the quiz>",
       "subtitle":"<line under the H1>", "footnote":"<results-screen note>",
       "cardTitle":"<optional: hub card title; defaults to header>",
       "chips":["optional","hub","card","tags"]
     },
     "questions": [ ... ] }
   ```
   Keep ≥80% at Application+. On blueprint coverage: a **comprehensive exam review**
   (the default) should spread `cat` values to roughly match the 2026 blueprint bands
   — with the whole exam block as source you have the breadth to do this, so aim for
   it. A **single-topic or small set** is the exception: follow the topic, and the
   per-category band flags are then expected and purely informational (the bands
   assume a full-length exam). Either way, **don't pad the item count just to land in
   a band** — size to the material and Chris's request.

4. **Build + lint (and register in the hub):**
   ```
   python .claude/skills/nclex-quiz-builder/scripts/assemble_quiz.py <name>.quiz.json --index index.html
   ```
   Read the coverage report. **Fix every ERROR** and re-run. Address WARNINGS unless
   there's a good reason not to (e.g., a deliberately small option set). Output is the
   standalone `<name>.html`, and `--index` adds/updates a card linking to it in the hub.

5. **Report** the coverage table to Chris and link the generated `.html`.

## Source material (repo layout)

The questions are grounded in material Chris has already captured — you are
*transforming verified content into NGN items*, not inventing clinical facts.

- Each class is a folder named after it (e.g. `maternal_child/`, `nutrition_nr228/`).
  Inside are verbatim **Edapt study guides**, one per module, named `WeekN_<Topic>.md`.
- Each guide has frontmatter (Course/Unit/Module), a Module Manifest, then
  `## Section N: <title>` blocks (often with `### Tab:` sub-content) — every Explore
  section/tab is a discrete, testable concept and good question fodder. They cite
  sources (e.g. Murray et al.) and **deliberately omit** the Edapt Prepare/Self-Check/
  Reflect questions, so you are writing fresh items, not copying.
- **Default to the whole exam block.** When Chris names an exam or a week range
  (e.g., "Weeks 4–7"), pull **every** `WeekN_*.md` across that range and read them in
  full — a comprehensive review draws on all of them. The guides' frontmatter
  (`Unit:` / `Week`) tells you which exam block a module belongs to. Narrow to
  specific files only when Chris asks for a single topic.
- Ground every item, value, and rationale in the guide. If a guide conflicts with
  current evidence-based practice, **flag it** to Chris rather than writing a wrong item.
- A folder may already hold a markdown quiz (`NCLEX_Quiz_*.md`) and/or a built `.html`.
  Reuse good items, but avoid producing a near-duplicate of an existing quiz unless asked.

## The study hub (`index.html`)

`index.html` is a **lean landing page** — a grid of cards, each linking to a standalone
quiz file. It never contains quiz content, so it stays small no matter how many quizzes
exist. The assembler's `--index` flag inserts a card (title, meta line, topic chips,
`Start ▸` link) for the new quiz, newest-first, and is **idempotent** — re-running
updates that quiz's card by its `href` instead of duplicating it. Always pass `--index`
for study-hub quizzes so the hub stays current automatically.

## Hard constraints (the engine + NCLEX both depend on these)

- Only the **7 supported types**: `radio`, `multi`, `cloze`, `matrix`, `match`,
  `bowtie`, `calc`. No highlight/hot-spot or free drag-and-drop — no renderer exists.
- **Unfolding case study = exactly 6 linked items**, one per NCJMM step, stems labeled
  `CASE (n/6) <step>.`, evolving one patient.
- **Bowtie = 1 problem + 2 actions + 2 parameters**, keyed exactly.
- **SATA**: judge each option independently; **vary the number correct** across items.
- **No "all/none of the above"**; keyed answers avoid absolutes; options parallel in
  grammar and length.
- `cat`/`lvl` strings **verbatim** from `references/blueprint-2026.md` (the results
  screen groups on them).
- Every clinical fact and rationale must be correct and current.
