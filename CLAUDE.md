# School — Edapt Module Extraction

This project extracts Edapt homework modules into verbatim Markdown study guides. Each class has its own subfolder (e.g., `maternal_child/`).

## What to Capture

**Capture:**
- Introduction section (always section 1)
- All Explore sections — including every tab, carousel slide, and accordion

Since the 2026-07 Edapt platform change (`edapt.covista.com`), **do not click through tabs/slides/accordions one at a time.** Collapsed panels stay in the DOM, so a single `browser_evaluate` pass returns all of them. See the `edapt-extract` skill for the extractor and the widget selectors.

**Skip entirely:**
- Prepare sections (pre-test / "test your knowledge" questions before the lesson)
- Self-Check sections (mid-module knowledge checks)
- Reflect sections (final reflection prompts)

## File Output Rules

- One `.md` file per module, named descriptively (e.g., `Week6_Newborn_Nutrition.md`)
- Append each section to the file immediately after capturing it — do not batch
- Use `Add-Content` with PowerShell single-quoted here-strings (`@'...'@`) for all file writes
- Closing `'@` must be at column 0 (no leading whitespace)

## Section Formatting

```
## Section N: <Section Title>

<content>

---
```

- Tabs → `### Tab: <Tab Name>`
- Carousel slides → `### Slide N: <Slide Title>`
- End each section with `---`
- Inline practice questions in Explore sections: note the question and computed answer inline; do not click through the interactive widget

## Navigation Rules

- Module sidebar buttons use outer-page `f1e`-prefixed refs; iframe content uses `f<N>e` refs. The iframe's `<N>` changes each time a different module is opened.
- Outer-page refs are reissued after every module open/close — re-snapshot and re-find the ref rather than reusing an old one
- Two Material dialogs block clicks and are **invisible to `browser_snapshot`**; a click failing with `cdk-overlay-backdrop ... intercepts pointer events` is the only signal:
  - "Welcome back" on the course page → click `app-student-course-landing-dialog button`
  - "Review mode" on opening a mastered module → click `app-confirm-dialog button:has-text("OK")`

## Session Start Checklist

1. Call `ToolSearch` with `query: "select:mcp__playwright__browser_click"` to load the browser_click schema before any clicks
2. Take an initial `browser_snapshot` to confirm current state
3. Note the current iframe body ref (e.g. `f2e1`) — it's the `target` for every extractor call

## Module Completion Audit

Append at the end of each module file. (Older guides use `## Module N Completion`; new work uses the heading below, which is now the most common in the corpus.)

```
## Module Completion Audit

**Sections captured (N):** Introduction: X (1), Explore: Y (3), ...

**Sections skipped (N):** Prepare: X (2), Self Check: Y (4), Reflect: Z (12), ...

**Interactive content expanded:** which hotspots / tab panels / carousel slides / image transcripts, so coverage is auditable

**[NEEDS MANUAL REVIEW]:** videos or media with no transcript (title + URL), or "None"

**Source-text anomalies:** verbatim typos and garbled sentences, with the intended meaning noted
```

Note the platform writes **`Self Check`** without a hyphen; match both spellings when applying skip rules.
