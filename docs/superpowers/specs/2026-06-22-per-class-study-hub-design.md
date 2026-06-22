# Per-Class Study Hub — Design Spec

**Date:** 2026-06-22
**Status:** Approved (design); pending implementation plan
**Component:** GitHub Pages study hub + `nclex-quiz-builder` skill (`assemble_quiz.py`)

## Context & problem

The study hub (`index.html`) is a single flat page with one "Practice Quizzes" grid
plus a "Downloads & Printables" section. Quizzes are now produced regularly by the
`nclex-quiz-builder` skill, and the hub is intended to **accumulate into a program-wide
NCLEX study archive** (potentially 30–60+ reviews across many classes). A flat page
does not scale to that, and hand-maintaining cards per quiz is toil.

Chris's content model: normally **one comprehensive review per exam**, occasionally a
smaller **week/topic practice** quiz between exams.

## Goals

- Navigation: **hub → class pages.** The landing page lists classes; each class has its
  own page listing that class's reviews, grouped by exam.
- Scales cleanly as a static archive on GitHub Pages (no framework, no build server).
- **Zero hand-maintenance:** building a quiz with the skill auto-registers it into the
  correct class page and the hub, idempotently.
- Reuse the existing dark theme / card / chip / button styles.
- Don't break existing URLs.

## Non-goals (YAGNI)

- Cross-class search / NCLEX-topic filtering (the A→B upgrade; see "Future").
- Authentication, analytics, comments.
- Renaming or moving the existing live quiz file.

## Decision

**Approach A — static per-class pages, auto-maintained by the assembler.** Chosen over
a JSON-manifest SPA (more complexity than needed now) and a single labeled page (does
not scale). A→B remains reachable because the same per-quiz metadata can later emit a
manifest.

## Metadata model

Add to each quiz's `*.quiz.json` `meta` (author supplies; script derives the rest):

| field | example | notes |
|---|---|---|
| `classCode` | `"NR327"` | required for hub registration |
| `className` | `"Maternal-Child Nursing"` | required |
| `classSlug` | `"nr327-maternal-child"` | optional; default = slugify(`classCode` + " " + `className`); overridable for clean filenames |
| `exam` | `"Exam 2"` | grouping bucket label; topic quizzes use the exam they prep for, else `"General practice"` |
| `examOrder` | `2` | integer; sorts exam sections on the class page |
| `kind` | `"exam-review"` | `exam-review` \| `topic-practice` → drives the card badge |
| `download` | `"files/nr327-exam2.zip"` | optional; renders a Download link on the card |

Existing fields (`title`/`cardTitle`, `header`, `subtitle`, `footnote`, `chips`) carry
over. Item count and case-study count are derived from `questions` as today.

If a quiz is built **without** the class fields, the assembler behaves as it does now
(no hub registration) — the fields are only required when `--hub` is used.

## Naming conventions

- **Class page file:** `<classSlug>.html` (e.g. `nr327-maternal-child.html`), in repo root beside `index.html`.
- **New quiz files:** `<classSlug>-<examOrTopic>.html` (e.g. `nr327-maternal-child-exam3.html`).
  The existing `maternal-child-weeks4-7.html` keeps its URL (it is NR327 Exam 2).
- **Card titles:** exam reviews → `"Exam 2 Review — Weeks 4-7 · Intrapartum → High-Risk Newborn"`;
  topic practice → `"Fetal Monitoring — practice"` with a *Topic Practice* badge.

## Page structures

Both reuse the existing CSS design tokens, `.card`, `.chip`, `.btn`, dark theme.

**Hub — `index.html`:** header (study-hub title), then a **"Classes"** grid: one card per
class showing `classCode · className`, a `"N reviews"` line, and exam chips, linking to
`<classSlug>.html`. The previous global quiz-list and downloads sections are removed
(downloads move onto class-page cards).

**Class page — `<classSlug>.html`:** header with class name + a "← Study Hub" back link,
then one **section per exam** ordered by `examOrder` (heading "Exam 1", "Exam 2", …).
Within a section: `exam-review` card(s) first, then `topic-practice` cards. Each card:
title, badge (Exam Review / Topic Practice), meta line (`N questions · NGN-style · K case
studies · rationale after each answer`), a **Start ▸** button → the quiz, and an optional
**Download** link when `download` is set.

## Generator changes (`assemble_quiz.py`)

Extends the existing idempotent single-card logic (`register_in_index`,
`<!-- quiz-card:href -->` markers) to two levels.

- **New flag `--hub <path>`** (`--index` is deprecated; for the transition it maps to
  `--hub`). Class page path = `dirname(hub)/<classSlug>.html`. If `--hub` is passed but
  the quiz's meta lacks `classCode`/`className`, the script prints a warning and **skips
  registration** while still building the quiz HTML (so a quiz can never silently fail to
  build over missing hub metadata).
- On build with `--hub`:
  1. **Class page:** if `<classSlug>.html` is missing, create it from a bundled
     `assets/class-page-template.html` (placeholders for class name + back link + an
     empty reviews container). Ensure an exam section for this quiz's `examOrder` exists
     (create + insert in sorted order if not), then insert/update this quiz's card under
     it — **idempotent by href** using the existing `<!-- quiz-card:href -->` markers;
     within a section, order exam-review before topic-practice.
  2. **Hub:** if the hub file is missing, scaffold it from a bundled
     `assets/hub-template.html`; otherwise insert/update the class's card — **idempotent
     by `classSlug`** (`<!-- class-card:<classSlug> -->`), recomputing the `"N reviews"`
     count from the class page's quiz-card markers and refreshing exam chips.
- All static string-surgery (same approach as the current implementation); UTF-8 output;
  ASCII hyphens in any console messages.
- The card-meta/`derive_chips` helpers are reused; add a small `slugify()` and the
  class-card / exam-section helpers.

## Migration (one-time, included in the work)

1. Convert `index.html` into the class-grid hub (preserve the title/footer/theme).
2. Add `classCode`/`className`/`classSlug`/`exam`/`examOrder`/`kind` to the existing
   `maternal-child-weeks4-7.quiz.json` (NR327, Maternal-Child Nursing, Exam 2,
   examOrder 2, kind exam-review).
3. Rebuild it with `--hub index.html`, generating `nr327-maternal-child.html` and the
   hub class card. The existing `maternal-child-weeks4-7.html` file/URL is unchanged.
4. Update the skill's `SKILL.md` + `build-process.md` to document the class metadata and
   the `--hub` step (replacing the old single-card `--index` guidance).

## Validation / testing

A scripted test (in the skill workspace):
- Build two quizzes in two different classes + one topic-practice quiz in one of them.
- Assert: hub has exactly two class cards with correct review counts; each class page has
  the right exam sections; the exam with two items lists the exam-review before the topic
  card; the `download` link renders only when set.
- Re-run all builds and assert **nothing duplicates** (idempotency) and counts are stable.

## Future (not built now)

The per-quiz metadata is sufficient to later emit a `quizzes.json` manifest and add a
cross-class **NCLEX-topic search/filter** view (the A→B upgrade) without changing how
quizzes are authored.
