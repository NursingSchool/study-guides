# School — Edapt Module Extraction

This project extracts Edapt homework modules into verbatim Markdown study guides. Each class has its own subfolder (e.g., `maternal_child/`).

## What to Capture

**Capture:**
- Introduction section (always section 1)
- All Explore sections — click every tab, carousel slide, and accordion before writing

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

- Module sidebar buttons use outer-page `e`-prefixed refs
- Content inside the module iframe uses `f<N>e`-prefixed refs (e.g., `f56e27` for Next)
- Always take a fresh `browser_snapshot` after navigating before assuming content state
- If a module sidebar is open and clicking another module button fails, close the current sidebar first (iframe overlay intercepts clicks)
- When opening a mastered module, a "Review mode" dialog appears — dismiss it immediately with OK before proceeding

## Session Start Checklist

1. Call `ToolSearch` with `query: "select:mcp__playwright__browser_click"` to load the browser_click schema before any clicks
2. Take an initial `browser_snapshot` to confirm current state
3. Note the active module's iframe prefix (visible in snapshot refs, e.g., `f56e`)

## Module Completion Manifest

Append at the end of each module file:

```
## Module N Completion

**Sections captured:** Introduction (1), Explore: X (3), Explore: Y (5), ...

**Sections skipped (Prepare/Self-Check/Reflect):** Prepare (2), Self-Check: X (4), ...
```
