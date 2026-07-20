# Study Guide Issues — NR328 Pediatrics & NR449 Evidence-Based Practice

> ## ✅ VERIFIED AGAINST LIVE MODULES — 2026-07-20
>
> All 12 **[CAPTURE-SUSPECT]** items plus 8 **[SOURCE-SUSPECT]** items were re-opened in Edapt review mode and checked against the live DOM.
>
> **Result: not one item was a capture failure.** 20 of 20 checks came back faithful to the source.
>
> Method: rather than re-reading the accessibility tree (which is what missed things the first time), each section was dumped via `textContent` — which includes collapsed tab panels and hidden nodes — plus a full inventory of `<img>` alt text, `<table>` rows, `.ednx-transcript-div` blocks, and `<iframe>`/`<track>` media. This surfaces anything a snapshot-based capture could have skipped.
>
> **The list below is therefore an author report, not a capture worklist.** Individual verdicts and evidence are inline under each item. Two genuine capture nits were found and already fixed (see "Capture fixes applied"). Three new author-side defects were discovered that were not on the original list (see "New findings").
>
> Remaining unverified (low priority, pure source-suspect): EBP-10, EBP-11, EBP-12 and the three "Minor, low priority" EBP notes.

## Capture fixes applied (2026-07-20)

1. `Week2_Pediatric_Respiratory_Alterations.md` §8 — table rows 3–5 were ordered *Viral Pneumonia, Influenza, Bacterial Pneumonia*; source order is *Influenza, Bacterial Pneumonia, Viral Pneumonia*. All 13 rows were present and content-correct; only the order was wrong. **Fixed.**
2. `Week2_Communicable_Diseases_and_Immunizations.md` §15 — added a study note recording that the linked CDC page carries birth–6 on-page and links onward to "Ages 7 to 18 years", since PEDS-01 assumed that schedule was missing entirely. **Added.**

## New findings (not on the original list)

- **Pertussis §9 has two contradictory summary cards in the source.** The reachable transcript says *"Isolation precautions: droplet and standard"*; a second `.ednx-transcript-div` immediately after the Kaltura audio says *"Isolation Precautions: droplet"*. The second has **no trigger element at all** (`prevSibling: null`, `display:none`) — no student can ever open it. This is both an author contradiction and an accessibility defect (orphaned content). Explains the PEDS-13 "and standard" asymmetry.
- **EBP-03's lost synonym happens inside §9 itself, not at §13.** §9 renders the same template table three times in a progressive build; version 2 has Terms `["older women", "HRT", "cancer"]` and version 3 has `["", "HRT", "cancer"]`. The source drops its own cell mid-section.
- **The asthma peak-flow error is a misquotation of a named source.** §15 attributes the zones to "the American Lung Association (2020)"; ALA publishes Yellow as 50–79%, the module says 50–80%. Worth citing in the report — it is not merely an internal inconsistency.

**Date:** 2026-06-22 (verified 2026-07-20)
**Courses covered:** NR328 Pediatric Nursing (Week 2; Week 3 where noted) · NR449 Evidence-Based Practice (Week 2)
**Not covered:** NR327 Maternal-Child and NR228 Nutrition were reviewed separately and are out of scope here.

> **Round 2 has been appended below** (2026-07-20) covering NR328 Weeks 1 & 3 and NR449 Weeks 1 & 3 — 20 more Pediatrics items and 7 more EBP items, IDs PEDS-16+ and EBP-13+. **Round 2 has NOT been verified against the live modules, and its capture-suspect/source-suspect labels are provisional guesses, not findings** — see the warning box at the head of that section before acting on any of them. Highest-priority item is **PEDS-31** (the Week 1 immunization schedule contradicts itself three ways).

## Purpose — read this first

This list is for the **Edapt extraction agent**. Every item below is a place where our captured study guide either contradicts itself, is missing promised content, or reads as garbled. For each one the question to answer is:

1. **Did we capture it wrong?** → fix the guide (re-extract the section, recover the dropped row/tab/table).
2. **Did we capture it right, but lose context?** → add the missing context (a tab we skipped, a figure caption, a table column).
3. **Did we capture it faithfully and the source itself is wrong?** → leave the guide alone and flag it for the authors.

Each entry gives the file, section, verbatim quote(s) of what our capture currently says, and a **Re-check** line naming exactly what to look for in the live module.

**Priority labels**
- **[CAPTURE-SUSPECT]** — the defect looks like extraction (dropped row, truncation, lost indentation, content promised but absent, tab/heading mismatch). Check these first; they're the ones we can actually fix.
- **[SOURCE-SUSPECT]** — probably faithful to Edapt. Confirm the capture matches, then it becomes an author report.

**Out of scope:** content that is merely behind current evidence-based practice. Nothing here is a "your source is outdated" complaint — those were deliberately excluded.

**Summary:** 15 Pediatrics items (7 capture-suspect) · 12 EBP items (5 capture-suspect).

---

# NR328 Pediatric Nursing

## Capture-suspect — check these first

### PEDS-01 · Immunization section promises content it does not contain
`Week2_Communicable_Diseases_and_Immunizations.md` §15 "Explore: Immunization Schedules"
> *"The Centers for Disease Control and Prevention provides the full immunization schedule. **Below are the recommended vaccines for birth to 6 years and 7 years and older.**"*

What follows is only:
> *"Download and review the [2025 Recommended Immunizations for Children From Birth Through 6 Years Old](https://www.cdc.gov/vaccines/imz-schedules/child-easyread.html) (CDC, 2025b)."*

No ages, doses, or intervals appear anywhere, and the one link covers only birth–6, so the 7-and-older schedule is entirely absent. §16 then proceeds as if the reader knows the schedule.

**Re-check:** "Below are the recommended vaccines" strongly implies embedded content followed — most likely one or two schedule **images or tables** that weren't captured. Re-open §15 and look for embedded charts/graphics, a second link for 7-and-older, or an expandable panel. This is the highest-value recapture on the list: the schedule is testable material and currently exists nowhere in our notes.

> **✅ VERDICT: capture faithful — premise of this item was wrong.** §15 contains exactly **one** image: a 2700×1800 JPEG with `alt=""` that is a **decorative stock photo of a child receiving a vaccine**, not a schedule. Its transcript div is empty (`&nbsp;`). Full link inventory for the section is exactly three content links (ACIP, AAP, and the birth–6 download) — there is no dropped second link and no expandable panel. Critically, the linked CDC page **does** satisfy the promise: it carries "Recommended Immunizations for Birth Through 6 Years Old, United States, 2025" on the page and links "Ages 7 to 18 years" under "For Other Groups". So "below" means "behind this link." No schedule was ever embedded to capture. Study note added to the guide pointing at the 7–18 schedule.

### PEDS-02 · Five-stage disease model established, then never applied — no incubation periods
`Week2_Communicable_Diseases_and_Immunizations.md`
- §3 defines five stages: *"**Incubation period:** the initial stage after exposure before symptoms are apparent"* … *"**Decline stage:** symptoms gradually improve"* … *"**Convalescence:** symptoms resolve"*
- §§5–9 (chickenpox, measles, mumps, German measles, whooping cough) present only *"Prodromal phase:"* and *"Acute phase:"* — pertussis alone adds a convalescent stage.

No incubation period is given for any disease, though that's the number needed for exposure and isolation decisions.

**Re-check:** each disease almost certainly had an incubation/communicability row or tab that wasn't captured. Re-open each disease section and check for additional tabs, a summary card row, or a table column we dropped.

> **✅ VERDICT: source defect — nothing was dropped.** Full `textContent` dumps (including hidden/collapsed nodes) of all five disease sections were searched for the string "incubat": **zero matches in any of them.** Every summary card has exactly four fields — Type, Transmission Source, Isolation Precautions, Complications — with no incubation or communicability row in the markup. The five-stage model in §3 is genuinely never applied. Report to authors: incubation periods are the numbers needed for exposure/isolation decisions and are absent module-wide.

### PEDS-03 · "Airborne Precautions" tab whose only signage says "Airborne Contact"
`Week2_Communicable_Diseases_and_Immunizations.md` §4 "Explore: Infection Control"
- *"### Tab: Airborne Precautions"* / *"- For illnesses transmitted by airborne particles."*
- Signage transcript in that same tab: *"**Transcript (isolation signage):** Airborne Contact Precautions (in addition to standard precautions)"*

The module never actually presents standalone airborne precautions, yet later sections cite "airborne contact" as if it were a defined category.

**Re-check:** likely a signage image attached to the wrong tab, or a separate airborne-only sign that wasn't captured. Confirm which signage images exist in §4 and which tab each belongs to.

> **✅ VERDICT: source defect — image is on the correct tab.** §4 holds five signage images, all `alt=""`. The one on the Airborne tab is `NR224_C108_Airborne_Precautions_Image.png` — correctly an airborne sign on the Airborne tab, **not** misattached. Its transcript genuinely reads "Airborne **Contact** Precautions (in addition to standard precautions)" and lists both gown+gloves *and* N95 + negative-pressure room, i.e. a genuine combined sign under a tab labelled airborne-only. Our §4 matches the live DOM word-for-word across all five tabs and all four transcripts (Respiratory Hygiene genuinely has none).

### PEDS-04 · RSV summary card bullet nesting garbled
`Week2_Pediatric_Respiratory_Alterations.md` §13 "Explore: Respiratory Syncytial Virus"
> *"- Contagious 3-8 days:"*
> *"  - Up to 4 weeks in infants and immunocompromised"*
> *"  - Resolves on own 1-2 weeks"*

"Resolves on own 1–2 weeks" is illness duration, not contagious period, but it's captured as a child of "Contagious 3-8 days" — so 3–8 days, 1–2 weeks, and 4 weeks read as competing values for the same attribute.

**Re-check:** indentation/nesting lost on capture. Re-open the summary card and confirm the real hierarchy. Also note the card's statistics (*"2.1 million outpatient visits," "57,527 hospitalizations"*) carry no year or source — check whether a citation line was dropped.

> **✅ VERDICT: source defect — nesting is authored that way.** Raw transcript HTML:
> ```html
> <li>Contagious 3-8 days:
>   <ul><li>up to 4 weeks in infants and immunocompromised</li>
>       <li>resolves on own 1-2 weeks</li></ul>
> </li>
> ```
> "resolves on own 1-2 weeks" is genuinely a child `<li>` of "Contagious 3-8 days". Our indentation reproduced the source exactly. The statistics sit nested under "In children under five:" and there is **no citation element anywhere in the transcript** — none was dropped.

### PEDS-05 · Peak flow zone thresholds overlap
`Week2_Pediatric_Respiratory_Alterations.md` §15 "Explore: Asthma" → Tab Therapeutic Management, peak-flow transcript
> *"- Green Zone: 80-100% of normal peak flow indicates good control"*
> *"- Yellow Zone: 50-80% of normal peak flow indicates caution and worsening symptoms"*

80% sits in both Green and Yellow (and 50% in both Yellow and Red), so a boundary reading has two contradictory actions.

**Re-check:** the American Lung Association source this is drawn from states Yellow as **50–79%**. A one-character capture slip (79 → 80) would explain it exactly. Verify the transcript against the on-screen figure before assuming the source is wrong.

> **✅ VERDICT: source defect — no transcription slip occurred.** The live DOM reads `Yellow Zone: 50-80% of normal peak flow`. Every percentage in the whole section is exactly `80-100%`, `50-80%`, `50%` — **the digits "79" appear nowhere in §15.** Escalate this one: the module explicitly credits "the American Lung Association (2020)", and ALA publishes Yellow as 50–79%, so the module **misquotes its own named source**, producing overlapping boundaries at 80% and 50%.

### PEDS-06 · CDC citation garbled, in-text suffix unmatched
`Week2_Communicable_Diseases_and_Immunizations.md` §15
- In-text: *"(CDC, 2025b)"*
- Reference list: *"- Centers for Disease and Control (2025). *Recommended vaccines for young children*."*

The agency name is garbled ("Centers for Disease **and** Control"), and `2025b` has no matching lettered entry — the list has two unlettered 2025 CDC entries plus one n.d.

**Re-check:** confirm the reference block was captured completely; a lettered entry (2025a/2025b) may have been dropped or merged.

> **✅ VERDICT: source defect — reference block captured completely.** The live §15 reference block contains exactly three entries, in this order and wording: CDC (n.d.) *Vaccines by age*; "Centers for Disease **and** Control (2025)" *Recommended vaccines for young children*; CDC (2025) *2025 recommended immunizations…*. The garbled agency name and the orphaned in-text `2025b` (no lettered entry exists) are both verbatim. Nothing dropped or merged.

### PEDS-07 · Media referenced with no transcript
| File · § | Missing asset | Why it matters |
|---|---|---|
| `Week2_Cystic_Fibrosis.md` §4 (Respiratory tab) | audio *"16_Cystic_Fibrosis"* | that tab is the module's **only** coverage of CF respiratory findings |
| `Week2_Communicable_Diseases_and_Immunizations.md` §9 | audio *"Pertussis_Symptoms_Sound"* | the pathognomonic whoop exists only as sound |
| `Week2_Croup_and_Bacterial_Epiglottitis.md` §4 | audio *"03_..._Croup"* and *"04_..._Epiglottitis"* | the two comparison exemplars for a module whose whole purpose is telling them apart |
| `Week2_Pediatric_Respiratory_Alterations.md` §3 | video *"respiratory assessment of pediatric clients"* | — |

**Re-check:** audio transcription isn't currently available, so these may stay gaps. But confirm whether any of them ship with **captions, a transcript panel, or alt text** that we could capture as text instead. If not, note them as known gaps and move on — this is also worth raising with the authors as an accessibility issue, since findings taught only as sound are unavailable to deaf and hard-of-hearing students.

> **✅ VERDICT: genuine gaps confirmed — no text alternative exists for any of them.** Every one is a Kaltura `<iframe>` embed; each was checked for `<track>` elements and **all returned `tracks: 0`** (CF §4, pertussis §9, croup/epiglottitis §4 — two embeds, respiratory assessment §3). No captions, no alt text, no transcript panel. These stay gaps.
>
> **Escalate the accessibility angle.** Pertussis §9 is the sharpest case: the module says "Listen to a child with whooping cough" and the pathognomonic whoop exists only as sound, with no captions — *and* the section contains an orphaned, permanently hidden transcript div (see "New findings"). Content taught only as audio, with the text alternative present but unreachable, is a concrete WCAG problem.

## Source-suspect — verify our capture is faithful, then report upstream

### PEDS-08 · Croup peak age differs across two Week 2 modules
- `Week2_Croup_and_Bacterial_Epiglottitis.md` §4: *"Acute laryngotracheobronchitis is the most common type of croup and primarily affects infants and children **less than 5 years old**."*
- `Week2_Pediatric_Respiratory_Alterations.md` §8 table: *"| Acute Laryngotracheobronchitis | Upper | **Children 6 months to 3 years** |"*

Epiglottitis is stated as 2–5 years in both, so the inconsistency is specific to LTB.
**Re-check:** confirm both were captured verbatim; if so, report.

### PEDS-09 · Laryngotracheobronchitis classified "Upper" against the section's own definition
`Week2_Pediatric_Respiratory_Alterations.md` §8
- Definition: *"upper airway (affecting the oronasopharynx, pharynx, larynx, and upper part of the trachea) or lower airway (affecting the lower trachea, **bronchi**, bronchioles, and alveoli)"*
- Table: *"| Acute Laryngotracheobronchitis | Upper | ... |"*

Laryngotracheo**bronch**itis is tabled Upper while the definition assigns bronchi to the lower airway. (Pertussis and bacterial tracheitis are also tabled "Upper" — lower confidence on those.)
**Re-check:** verify the table's classification column captured correctly, then report.

### PEDS-10 · CFTR expanded two different ways
`Week2_Cystic_Fibrosis.md`
- §3 and §5: *"a mutation in the cystic fibrosis transmembrane regulator (CFTR) gene"*
- §9: *"cystic fibrosis transmembrane **conductance** regulator (CFTR) modulators"*

§9 is correct; §3 and §5 drop "conductance."
**Re-check:** verify both spellings are in the source, then report.

### PEDS-11 · *Haemophilus influenzae* misspelled within one paragraph
`Week2_Croup_and_Bacterial_Epiglottitis.md` §4, consecutive sentences
> *"is often caused by haemophilus influenzae. The haemophilus influenza type B vaccine has dramatically reduced cases"*

"influenzae" then "influenza"; neither capitalized or italicized; the vaccine is *Haemophilus influenzae* type **b** (Hib), not "type B."
**Re-check:** confirm capture is verbatim (including the lost italics/capitalization — if the source italicizes the binomial and we flattened it, that's ours), then report the spelling.

### PEDS-12 · Adult respiratory rate presented as normal in a pediatric module
`Week3_Kawasaki_Disease_and_Multisystem_Inflammatory_Syndrome.md`, COVID-19 3D-model transcript, three separate places
> *"A normal respiratory rate is between 12 and 20 breaths per minute."*

12–20 is the adult range (infants ~30–60, toddlers ~24–40). Internally consistent, so this is an adult 3D-model asset reused in a pediatric course without a pediatric qualifier.
**Re-check:** confirm the transcript is complete and no pediatric qualifier was dropped, then report to authors — this one is worth escalating.

### PEDS-13 – PEDS-15 · Lower confidence, verify context wasn't lost
- **Transmission vs. precautions mismatches** (`Week2_Communicable_Diseases_and_Immunizations.md`): German measles narrative says *"spread through direct contact with nasopharyngeal secretions"* but its card lists droplet only, while mumps (saliva) gets *"droplet and contact"*; chickenpox narrative says *"transmitted through the air, direct contact, and through contaminated objects"* but its card lists *"respiratory secretions"* only; whooping cough's card alone appends *"and standard"*. **Re-check whether the summary cards were captured in full** — a dropped line would explain the asymmetry.
- **Stridor list omits croup** (`Week2_Pediatric_Respiratory_Alterations.md` §3): *"associated with epiglottitis, foreign body, and tracheitis"* — croup omitted, though the next bullet ties barking cough to croup, and that bullet locates it at *"the trachea and bronchi"* while the croup module locates croup at *"the larynx."* **Re-check the full bullet list.**
- **CF symptom lead-in vs tab count** (`Week2_Cystic_Fibrosis.md` §4): *"The most common symptoms are respiratory, gastrointestinal, growth failure, and diabetes symptoms"* — but the section has five tabs including Reproductive and Integumentary. **Re-check whether the lead-in sentence was truncated.**

---

# NR449 Evidence-Based Practice

## Capture-suspect — check these first

### EBP-01 · Research-process table missing the step the prose calls final
`Week2_The_Research_Process.md` §6 "Explore: Research Process Compared to Nursing Process"
- Body: *"Once the process is complete, we must communicate our findings. … **communication is the final step in both the nursing and research process**."*
- The transcript table immediately below ends at: *"| Evaluation | Analyze data |"*

No communication row exists — while §4 of the same file lists "Communicate Findings" as phase 7 of 8.

**Re-check:** a table row was almost certainly dropped on capture. Re-open §6 and confirm the table's full row set. (Separate author-side note: communication is not the final step of the ANA five-step nursing process, where evaluation is — but fix the capture first.)

> **✅ VERDICT: source defect — no row was dropped.** The §6 transcript is a **single-row, two-cell** table: cell 1 = "Nursing Process / Assessment Diagnosis Planning Implementation Evaluation", cell 2 = "Research Process / Ask questions Identify problem Determine design Collect data Analyze data". Five steps per column, ending at Evaluation ↔ Analyze data. **No communication row exists in the markup.** The prose immediately above it calls communication "the final step in both" — so the section contradicts its own adjacent image. Both author-side notes now stand: the missing step *and* the ANA-process error.

### EBP-02 · "Complete" search template uses AND where the guide teaches OR
`Week2_Literature_Review.md`
- §13 "Ready to Search" → Complete Literature Search Strategy Template: *"Parentheses: (post-menopausal women) AND (\"hormone replacement therapy\" **AND** HRT) AND (breast cancer)"*
- §11 Tab Parentheses: *"grouping (hormone replacement therapy **OR** HRT) tells the database to look for either term."*
- §11 worked example: *"| Parentheses | (\"hormone replacement therapy\" **OR** HRT) |"*

§9 defines AND as requiring both terms (*"AND will reduce your results and only show sources that contain both keywords it connects"*), so the final template reverses the rule taught two sections earlier and contradicts the earlier worked example in the same file. Run as written, the search returns almost nothing.

**Re-check:** the template is likely an image or formatted block — a single OR→AND transcription slip would explain it entirely. Verify against the on-screen template before reporting.

> **✅ VERDICT: source defect — transcription slip was impossible here.** §13's template is a real HTML `<table>`, **not** an image (`imgs: []` for the whole section), so there was nothing to transcribe by eye. The Parentheses row reads verbatim: `Parentheses: ( post-menopausal women) AND (“hormone replacement therapy” AND HRT) AND (breast cancer)`. The inner `AND` is the author's. Report stands: run as written the search returns almost nothing, and it contradicts §11's own worked example and §9's definition of AND.

### EBP-03 · Search-terms row silently loses a synonym
`Week2_Literature_Review.md`
- §9: *"Terms: post-menopausal women / **older women** | hormone replacement therapy / HRT | breast cancer / cancer"*
- §13 final template: *"Terms: post-menopausal women / **—** | hormone replacement therapy / HRT | breast cancer / cancer"*

"older women" is replaced by an em dash with no explanation while the other two pairs carry through unchanged. Quoting is also inconsistent between the two templates (§13 quotes only "hormone replacement therapy" and leaves post-menopausal women unquoted).

**Re-check:** an em dash in one cell of an otherwise-complete table is a classic empty-cell capture artifact. Confirm what that cell actually contains.

> **✅ VERDICT: source defect — and the loss happens earlier than this item assumed.** The cell is **genuinely empty in the source** (`["", "HRT", "cancer"]`), so our em dash was a rendering choice for a blank cell, not a lost synonym. More telling: **§9 itself renders the template three times in a progressive build**, and the drop happens *within §9* — version 2 has Terms `["older women", "HRT", "cancer"]`, version 3 has `["", "HRT", "cancer"]`. So the source loses its own cell mid-section, before §13 exists. Minor guide improvement: render the blank as "(blank in source)" rather than an em dash, which reads like redaction.

### EBP-04 · PICOT worked answer supplies a comparison absent from the source quote
`Week2_The_PICOT_Question.md` §8 "Explore: PICOT and Purpose Statements"
- Quoted purpose statement: *"The aim of the present study was to evaluate the effects of an oral hygiene protocol (consisting of 2% chlorhexidine and manual brushing) in a heterogeneous population of ICU patients on the VAP incidence…"*
- Provided answer: *"…compared to **placebo gel** with toothbrushing (comparison)…"*

Students are told to build the PICOT from the quoted statement, but "placebo gel" appears nowhere in it — so the answer can't be derived from the material given.

**Re-check:** the quoted purpose statement may have been truncated mid-capture (the ellipsis is suspicious). Verify whether the full on-screen quote includes the comparison arm.

> **✅ VERDICT: source defect (pedagogical) — the quote is NOT truncated.** The live statement ends properly with its citation: *"…lengths of the patients' ICU and hospital stays" (de Avila Meinberg et al., 2012, para. 4).* The word "placebo" appears **nowhere** in §8's document text. It lives inside the drag-drop widget, as **"Grabbable 3 of 4: placebo gel with toothbrushing"** / "Dropzone 3 of 4". So the comparison arm *is* module content and our capture recorded it correctly — but it genuinely cannot be derived from the quoted statement students are told to build the PICOT from. Report stands.

### EBP-05 · Truncated DOI and wrong journal name
`Week2_The_PICOT_Question.md` §8, reference block
> *"de Avila Meinberg, M. C., … & Lobo, S. M. (2012). The use of 2% chlorhexidine gel and toothbrushing for oral hygiene of patients receiving mechanical ventilation: Effects on ventilator-associated pneumonia. *Clinical Research, 24*(4). https://doi.org/10.1590/S"*

The DOI terminates at `10.1590/S` — a bare prefix plus one character, not resolvable. The italicized journal title reads "Clinical Research," which is a section label rather than a periodical; that 2012;24(4) citation belongs to *Revista Brasileira de Terapia Intensiva*. No page or article number is given.

**Re-check:** the truncated DOI is almost certainly ours — verify and recapture the full reference string.

> **✅ VERDICT: source defect — the DOI is truncated in the module itself.** The live reference block ends at `https://doi.org/10.1590/S`, and it is **plain text, not a hyperlink** (`doiLinks: []`), so there was no href for us to truncate. "Clinical Research, 24(4)" is likewise verbatim. Nothing to recapture. Report all three to authors: unresolvable DOI, wrong journal title (should be *Revista Brasileira de Terapia Intensiva*), and missing page/article number.

## Source-suspect — verify our capture is faithful, then report upstream

### EBP-06 · Evidence hierarchy: narrative ranking vs levels table
`Week2_Sources_and_Levels_of_Evidence.md`
- §8 "Grading Evidence" transcript: *"1. Clinical practice guidelines 2. Meta-analyses 3. Systematic reviews 4. Randomized clinical trials 5. Cohort studies 6. Outcome research 7. Case-controlled studies 8. Expert opinion"*
- §15 "Levels of Evidence" table: *"| Level 1 | Multiple randomized controlled trials that are part of a systematic review, meta-analysis, or practice guidelines |"* … *"| Level 3 | Case-controlled or cohort studies; Observational studies including retroactive chart reviews |"*

§8 ranks guidelines > meta-analyses > systematic reviews and puts cohort above case-control; §15 places all three aggregated forms at Level 1 and cohort and case-control together at Level 3. A student grading the same study gets two different answers. §10 reinforces §8: *"[Clinical practice guidelines are] the most comprehensive quality and highest strength evidence."*

**Re-check:** §8 is a transcript — confirm it's complete and that no framing sentence was lost (e.g. wording that scopes the ranking to a different purpose than the level table). If both are faithful, this is the headline author report; it's also the item most likely to cost a student points.

### EBP-07 · Hard-coded date range contradicts the stated five-year rule
`Week2_Literature_Review.md`
- §11 worked example and §13 template: *"| Date range | 2016-2021 |"*
- §11 Tab Search Filters: *"…typically within the last five years."* · §§7 and 14 criteria tables: *"| Year of publication | Within the last five years | None |"*

2016–2021 inclusive is a **six**-year span, so it never satisfied the guide's own rule even at authoring time — and it's stale besides.
**Re-check:** verify the dates were captured correctly, then report.

### EBP-08 · Worked example exceeds the stated limiter maximum
`Week2_Literature_Review.md` §11
- *"It is best to apply no more than one to two limiters initially."*
- Worked example immediately following: *"| Date range | 2016-2021 | Language | English | Peer reviewed | Yes, or checked |"*

Three filters, plus quotation marks and parentheses, on the first pass.
**Re-check:** confirm the limits table was captured whole, then report.

### EBP-09 · Mislabeled Boolean "common mistake"
`Week2_Literature_Review.md` §9 Tab Connectors
> *"**Placing the Connecting Word in the Wrong Place:** Correct: post-menopausal women **AND** hormone replacement therapy **AND** breast cancer / Incorrect: post-menopausal women **OR** hormone replacement therapy **AND** breast cancer"*

The heading describes a *placement* error; the example demonstrates a *substitution* error — the connector is in the same position in both lines, only AND→OR changed.
**Re-check:** confirm the heading and its example were captured as a pair and not spliced from adjacent items, then report.

### EBP-10 · Social media: conditional acceptance vs categorical rejection
`Week2_Sources_and_Levels_of_Evidence.md` §15
> *"Most researchers will not accept popular media or social media as evidence **except under specific conditions**."* … *"nothing should be accepted as an appropriate source through social media **unless** it is linked to an appropriate website and is verifiable."* … *"**Social media have a high risk of disinformation; therefore, they are not a credible source.**"*

Two conditional carve-outs (plus a Twitter example offered as a possible level-5 primary source) followed by a bolded unconditional rejection.
**Re-check:** verify no qualifying sentence was dropped between them — this reads like it could be missing a transition.

### EBP-11 · Hypothesis criteria conflict with nondirectional hypotheses
`Week2_The_PICOT_Question.md` §15 Tab Elements of a Good Hypothesis
- *"- Identified direction of interest"* listed as a required element
- Same tab: *"A **nondirectional** hypothesis is one in which the researcher is interested in a change in any direction."*

The section's own primary worked example is a null hypothesis, which has no direction.
**Re-check:** confirm the elements list is complete (a qualifier such as "for directional hypotheses" may have been dropped), then report.

### EBP-12 · Journal title error, repeated in two sections
`Week2_Identifying_Practice_Problems.md` §§8 and 9 (identical reference blocks)
> *"Alexander, G. K., Rollins, K., Walker, D., Wong, L., & Pennings, J. (2015). Yoga for self-care and burnout prevention among nurses. *Workplace Health & Safety Journal, 63*(10)."*

The journal is *Workplace Health & Safety*; "Journal" is appended in error. Both instances also omit page/article numbers, so a fix applies twice.
**Re-check:** verify against the on-screen reference, then report.

### Minor, low priority
- `Week2_Identifying_Practice_Problems.md` §4 is headed "Nurse-Sensitive Concepts" but the body alternates "nursing-sensitive indicators," "nurse-sensitive concept," and "medically-sensitive concept" without distinguishing indicators from concepts.
- `Week2_Literature_Review.md` §6: *"Limiting the number of databases searched can result in publication bias resulting in loss of findings."* — the described effect is retrieval/selection bias; publication bias concerns what gets published.
- `Week2_The_Research_Process.md` §11 uses *"Correlation research"* where the standard term is correlational research.
- `Week2_The_PICOT_Question.md` §12 FINER: *"**Interesting:** Is the question interesting?"* is circular and carries no criterion, unlike the other four entries — **possible truncation at capture, worth a look.**

---

## Source-suspect items verified faithful (2026-07-20)

Each was re-read in the live module and matched our capture. All are cleared to report upstream as author issues.

| Item | Live-DOM evidence |
|---|---|
| PEDS-08 croup peak age | Croup module §4 verbatim: *"primarily affects infants and children less than 5 years old."* Respiratory §8 table verbatim: `Acute Laryngotracheobronchitis \| upper \| children 6 months to 3 years`. Both faithful; the two modules genuinely disagree. |
| PEDS-09 LTB classified "Upper" | Table classification column captured correctly; all 13 data rows present. Definition verbatim, including "bronchi" assigned to lower airway. Pertussis and bacterial tracheitis are likewise genuinely tabled "upper". |
| PEDS-10 CFTR expansion | §3 reads *"cystic fibrosis transmembrane regulator (CFTR)"* with **no** "conductance" — verbatim match to our capture. |
| PEDS-11 *Haemophilus* | Verbatim: *"often caused by haemophilus influenzae. The haemophilus influenza type B vaccine…"* Decisive detail: `italicElements: []` — **the source never italicizes the binomial**, so the lost italics were not ours. Lowercase, mis-spelling, and "type B" are all the author's. |
| PEDS-12 adult respiratory rate | 3D-model transcript captured complete; no pediatric qualifier exists anywhere in it. Worth escalating — an adult asset reused in a pediatric course. |
| PEDS-13 transmission vs precautions | Chickenpox narrative ("air, direct contact, contaminated objects") vs card ("respiratory secretions"), German measles narrative ("direct contact with nasopharyngeal secretions") vs card ("droplet"), mumps card ("droplet and contact") — all verbatim, all cards exactly 4 fields. No dropped lines. Pertussis "and standard" now explained by the two-card bug in "New findings". |
| PEDS-14 stridor omits croup | Full 5-item list captured; stridor bullet verbatim *"associated with epiglottitis, foreign body, and tracheitis"*, barking-cough bullet verbatim *"trachea and bronchi"*. Nothing truncated. |
| PEDS-15 CF lead-in vs tab count | Lead-in is a complete, untruncated sentence naming 4 categories; the section genuinely has 5 tabs (Respiratory, Gastrointestinal, Reproductive, Integumentary, Endocrine). Author mismatch. |
| EBP-06 evidence hierarchy | **Headline report confirmed.** §8's transcript is complete *including* its framing sentence — *"Listed in order of evidence strength, from strongest to weakest:"* — which our capture preserved as the transcript heading. No scoping sentence was lost, so the ranking is unqualified and genuinely conflicts with §15's Levels table. |
| EBP-09 mislabeled Boolean mistake | Heading and example are genuinely paired in the source (and followed by a second mistake, "Using Lower Case"). Not spliced from adjacent items. |
| EBP FINER "Interesting" (minor) | Verbatim and complete: *"Interesting: Is the question interesting?"* sits between fully-specified Feasibility and Novel entries. **Not** a capture truncation — the circularity is the author's. Note: source says "Feasibility", not "Feasible". |

## Examined and NOT confirmed — do not chase these

| Candidate | Finding |
|---|---|
| NR449 "replication is essential" vs FINER "Novel" | Reconcilable, not a contradiction — the guide's own Novel criterion admits studies that *"confirm or refute previous findings."* The only residual issue is that *"Replication of previous studies is essential"* sits under a slide headed "Review the literature" and reads as a non sequitur. Editorial clarity at most. |

## Verified consistent — do not re-report

- **NR328:** epiglottitis age (2–5 years in both modules); epiglottitis 24-hour antibiotic timeline (§8 and §9 agree); pertussis stage durations (prodromal 1–2 wks, acute 4–6 wks, convalescent 1–2 wks); RSV precautions (droplet and contact); chickenpox precautions (airborne contact, narrative and card agree); **no section-numbering gaps** in any Week 2 module — captured plus skipped sections account for every number.
- **NR449:** all five module manifests account for every section number with no gaps.

## Low-severity formatting notes

Bundle rather than filing individually: `Week2_Croup_and_Bacterial_Epiglottitis.md`'s manifest lists *"Explore: Types of Croup (3)"* against an actual heading of *"Explore: Types of Croup Syndromes"*; `Week2_Cystic_Fibrosis.md` §6 places the *"Transcript (figure: 'Huff Coughing')"* several items below the huff-coughing bullet it belongs to.

---

# Round 2 — NR328 Weeks 1 & 3 · NR449 Week 1

**Date:** 2026-07-20
**Scope:** the modules not covered by the Week 2 audit above. IDs continue from Round 1.
**Summary:** 20 Pediatrics items · 7 EBP items. One capture bug was found and **already fixed** (see below).

> ### ⚠️ The CAPTURE-SUSPECT / SOURCE-SUSPECT labels in Round 2 are provisional — do not trust them
>
> In Round 1 those labels were assigned from evidence and then tested against the live modules. **In Round 2 they were assigned by analogy to Round 1's result** — "the source turned out to be sloppy last time, so it probably is again." That is not evidence, and it is the wrong inference to carry forward, because Round 1 earned its verdict through a verification pass Round 2 has never had.
>
> **Treat every Round 2 item as unclassified until the DOM pass is run.** What we actually know:
>
> | Evidence | Cuts which way |
> |---|---|
> | Round 1 tested 20 items that "looked like capture failures." **20 of 20 were faithful.** Including **PEDS-01**, the immunization item — the closest analogue to PEDS-31 — which was called the highest-value recapture on the list and turned out to be a decorative stock photo and a link. | Toward source |
> | Week 1 and Week 2 guides have **no Section Manifest**, so completeness cannot be checked from the file alone. (Week 2 was verified externally anyway; Week 1 never has been.) | Neutral — unverifiable, not bad |
> | Week 1 has a **demonstrated capture defect** the other weeks don't — 15 doubled apostrophes from here-string escaping. A pipeline that broke once may have broken elsewhere. | Toward capture, Week 1 only |
> | Section-gap analysis: `Week1_Nursing_Care_Pediatric_Populations.md` skips §§10–12 consecutively. **This is not a signal.** Two Week 2 modules show the same triple gaps and were verified faithful — runs of three Self-Checks are normal. | Inconclusive — discarded |
>
> Net: the Week 1 items carry a genuinely higher capture prior than the Week 3 items, because of the apostrophe bug and because Week 3's manifests reconcile 16/16. But **no Round 2 item has been adjudicated**, and the Round 1 base rate argues against assuming capture failure. The resolution is not more armchair analysis — it is the same `textContent` DOM pass Round 1 used, which is cheap and decisive.
>
> **One caveat on Week 3's manifests:** they track *sections*, not tabs, slides, or accordions *within* a section. So a reconciling manifest rules out a skipped section — it does not rule out a lost tab, which is exactly the shape of PEDS-21, PEDS-24 and PEDS-27 (adjacent statements that contradict, as if a qualifying header between them went missing).

## Capture fixes applied (round 2)

1. `Week1_Introduction_to_Pediatric_Nursing.md` — 15 doubled apostrophes (`Piaget''s`, `Erikson''s`, `parents''`, `child''s`, `Boys''`, `Girls''`, `other''s`, `others''`) leaked into the guide. Cause: PowerShell single-quoted here-strings escape an apostrophe as `''`, and the escape was written through instead of resolved. **Fixed** — all 15 collapsed to `'`. No other class folder is affected; this file was the only one.
   **Prevention:** the extractor never needs `''` inside a `@'...'@` here-string, because the delimiter is `'@`, not `'`. Worth a lint check on future captures.

---

# NR328 Pediatric Nursing — Weeks 1 & 3

## Capture-suspect — check these first

### PEDS-16 · Guide filename does not match the module it contains

`Week1_Nursing_Care_Pediatric_Populations.md`

The file is named for a "Nursing Care of Pediatric Populations" module, but its contents are Edapt **Module 3, "Pediatric Pain, Loss, and Grief."** There is no age-group population overview, no safety/injury-risk-by-age table, and no play-by-age content beyond play therapy under atraumatic care.

**Re-check:** determine which is wrong — was the file named from the sidebar/unit label while the content came from a different module, or does Edapt itself title this unit "Nursing Care of Pediatric Populations" with pain and grief content inside? If a *separate* populations module exists in Week 1, it was never captured and is missing from our notes entirely. This is the highest-value re-check in round 2.

### PEDS-17 · Vocabulary count garbled

`Week1_Introduction_to_Pediatric_Nursing.md` — preschool Cognitive row

> *"By age 6, children have a vocabulary of 8,000 to 140,000."*

Two problems: the range is implausible (140,000 exceeds adult vocabulary; the standard figure is 8,000–14,000), and the unit noun is missing — "of 8,000 to 140,000" *what*.

**Re-check:** almost certainly a stray `0`. Confirm the source reads "8,000 to 14,000 words."

### PEDS-18 · Wong-Baker FACES numbering garbled

`Week1_Nursing_Care_Pediatric_Populations.md` — pain assessment tools

> *"1 or 2 = Hurts little bit, 2 or 4 = Hurts little more … 5 or 10 = Hurts worst"*

The pairs are internally inconsistent — the first is not a doubling, the rest are. This reads like a two-column table (a 0–5 scale beside a 0–10 scale) flattened into one line, with the first row's left value dropped.

**Re-check:** re-open as a table. The intended content is near-certainly `0/0, 1/2, 2/4, 3/6, 4/8, 5/10`. No quiz item currently keys a FACES number because of this.

### PEDS-19 · Uncaptured video in the anemia module

`Week3_Pediatric_Hematologic_or_Immunologic_Alterations.md` §3 slide 4 carries our own `[NEEDS MANUAL REVIEW]` marker for an embedded "AnemiaVideo."

**Re-check:** look for a transcript track or caption file. Testable content may be sitting behind it.

### PEDS-20 · Fetal circulation lost to untranscribed video, in two modules

`Week3_Congenital_Heart_Disease_and_Cardiac_Anomalies.md` and `Week3_Pediatric_Circulatory_System_Alterations.md`

Both modules gesture at the fetal-to-newborn circulatory transition via video without a captured transcript. Fetal circulation underpins every shunt lesion in the week, and it currently exists nowhere in our notes.

**Re-check:** same as PEDS-19 — look for `<track>` elements or a `.ednx-transcript-div`.

## Source-suspect — verify our capture is faithful, then report upstream

### PEDS-21 · Pulmonary stenosis filed as obstructive, described as cyanotic

`Week3_Congenital_Heart_Disease_and_Cardiac_Anomalies.md`

The "obstruction to blood flow" section lists Pulmonary Stenosis alongside aortic stenosis and coarctation, and closes:

> *"These children have clinical manifestations of heart failure."*

The interactive transcript for the same defect says:

> *"Deoxygenated blood is forced through the foramen ovale, bypassing the right ventricle to the left side of the heart where it is pumped through systemic circulation. As a result, these infants will be cyanotic."*

So the module's own classification scheme (obstructive → heart failure) is contradicted by its own description (right-to-left shunt → cyanosis) for the same lesion. Both statements are defensible in isolation — severe PS with a patent foramen ovale genuinely does shunt — but the guide never reconciles them, and a student sorting defects into "cyanotic vs. acyanotic" gets opposite answers depending on which section they read.

**Report to authors:** one sentence noting that severe PS can present with cyanosis via a PFO despite being an obstructive lesion would resolve it.

### PEDS-22 · "Same as adults" immediately contradicted

`Week3_Pediatric_Circulatory_System_Alterations.md`

> *"Pulse locations and expected findings in children and adolescents are the same as those in the adult population."*

The next four bullets then list pediatric-specific findings: the radial pulse is unreliable under age 2, heart rate elevates from fear so listen before counting, and the apical pulse is at the **4th** intercostal space — the adult landmark is the 5th.

**Report to authors:** the lead sentence should say pulse *sites* are the same, not "locations and expected findings."

### PEDS-23 · IV ferrous sulfate

`Week3_Pediatric_Hematologic_or_Immunologic_Alterations.md`

> *"IV ferrous sulfate administration is very painful and requires close monitoring of the client during administration"*

Ferrous sulfate is an oral preparation; there is no IV form. The painful parenteral iron is iron dextran (IM Z-track or IV). Not keyed in any quiz item.

**Report to authors:** likely a substitution error for iron dextran.

### PEDS-24 · Hemophilia NSAID guidance contradicts itself in adjacent bullets

Same file, therapeutic management:

> *"Aspirin and nonsteroidal anti-inflammatory agents (NSAIDs) — avoid as they inhibit platelet function"*
>
> *"Ibuprofen and other non-steroidal anti-inflammatory drugs are used occasionally to treat inflammatory musculoskeletal and join pain, under close supervision by the primary care provider."*

A blanket avoid followed immediately by a use-case, with no framing to reconcile them. (Also: *"join pain"* → *"joint pain"*.) Quiz items key aspirin as contraindicated — the module's unambiguous half.

### PEDS-25 · Module title promises immunologic content that is absent

`Week3_Pediatric_Hematologic_or_Immunologic_Alterations.md` is titled "Hematologic **or Immunologic** Alterations" but contains no immunologic disorder at all — no immunodeficiency, no HIV, no allergy or hypersensitivity. The only immune-adjacent lines are that anemic children are infection-prone via tissue hypoxia, and corticosteroid infection precautions.

**Re-check:** confirm no immunologic sections were skipped. If the module genuinely has none, the title is the defect.

### PEDS-26 · Section titled for sickle cell, contains general anemia care

Same file, §4 — heading *"Nursing Care - Sickle Cell Anemia"*, but the slides are general anemia nursing care with no sickle-specific content. Sickle cell has its own dedicated module in the same week.

### PEDS-27 · Kawasaki skin care reverses between sections

`Week3_Kawasaki_Disease_and_Multisystem_Inflammatory_Syndrome.md` — §8 (KD nursing care) says to avoid soap because it dries the skin; §15 (MIS-C nursing care) says to apply skin lotions and omits the soap caution entirely. Same desquamation problem, opposite instruction. The quiz keys the §8 version as the module's dominant statement.

### PEDS-28 · Kawasaki introduced as a "Hematologic Alteration"

Same file — the Introduction files KD under hematologic alterations; the body correctly describes it as a vasculitis. Not keyed either way.

### PEDS-29 · Adult content in a pediatric course — now a pattern, not a typo

Three instances outside Week 2:

- `Week3_Kawasaki_Disease_and_Multisystem_Inflammatory_Syndrome.md` — the COVID-19 3D-model transcript gives *"normal respiratory rate 12-20 breaths/min"*, an adult range.
- `Week3_Pediatric_Circulatory_System_Alterations.md` — see PEDS-22.
- `Week1_Nursing_Care_Pediatric_Populations.md` — §3's two case studies are **adults aged 34 and 54**, in a pediatric pain module.

Together with **PEDS-12** from Week 2, this is four instances across three weeks. Worth reporting as a single systemic finding — adult assets appear to be reused into the pediatric course without adaptation — rather than as four isolated typos.

### PEDS-30 · Piaget: no stage for 3–5 year olds, then a stage for 3–5 year olds

`Week1_Introduction_to_Pediatric_Nursing.md` — preschool Cognitive row

> *"Piaget's cognitive theory does not include a period specifically for children 3 to 5 years old. The preoperational is divided into two stages: the preconceptual (2 to 4 years), and intuitive thought (4 to 7 years)."*

The disclaimer is contradicted by the rest of its own sentence, and by the toddler row, which places preoperational at 2–7 years. The intended point is presumably that Piaget draws no stage boundary *at* 3–5 — but as written it reads as a denial that the age band is covered. Quiz items key the preoperational version.

### PEDS-31 · Immunization schedule is internally inconsistent — highest priority

`Week1_Introduction_to_Pediatric_Nursing.md` — the Health Promotion rows across infant / toddler / preschool / school-age

| Stated as | Then given |
|---|---|
| *"Inactivated poliovirus (IPV): 3-dose series at 2, 4, and 6-15 months"* | *"Inactivated poliovirus: 3rd dose at 18 months"* (toddler), *"4th dose (4-6 years)"* (preschool) |
| *"Diphtheria, tetanus, and acellular pertussis (DTap): 4-dose series at 2, 4, 6, 15 months"* | *"DTap: 4th dose at 15 months"* (toddler — consistent), then *"Tetanus, diphtheria & acellular pertussis (Ddap): 5th dose (4-6 years)"* (preschool) |

Three distinct problems:

1. **IPV** is called a 3-dose series but four doses are listed, and the 3rd dose is placed at both *"6-15 months"* and *"18 months."*
2. **DTaP** is called a 4-dose series but a 5th dose is listed.
3. ***"Ddap"*** appears twice — at 4–6 years and at 11–12 years — and is not a vaccine. The 4–6 year dose is **DTaP #5**; the 11–12 year dose is **Tdap**. The guide uses one misspelling for two different products. (`DTap` is also the wrong casing for DTaP throughout.)

This is the second immunization defect on this report after **PEDS-01** — but unlike PEDS-01, the content *is* present here. It is just wrong. Chris has confirmed immunization schedules are tested material. **No quiz item keys any of it.**

**Re-check:** confirm our capture is faithful — these are table cells and could have lost a row. If faithful, this is the single most important item to send the authors, and the schedule should be reconciled against the CDC chart handed out in class before anyone studies from this guide.

### PEDS-32 · Developmental age ranges disagree between sections

`Week1_Introduction_to_Pediatric_Nursing.md` — adolescence is given as 13–20 years in one section and split as early 11–14 / middle 15–17 / late 18–22 in the next. Toddler and preschool also overlap at 36 months.

### PEDS-33 – PEDS-35 · Gaps rather than errors — confirm nothing was skipped

- **PEDS-33 · Child maltreatment** (`Week1_Child_Abuse.md`): states mandatory reporting exists in all 50 states with civil and criminal penalties, but gives **no reporting timeframe, no agency, and no bruise-dating criteria**. The quiz deliberately makes "estimate the age of each bruise in days" a distractor rather than invent a standard. Also inconsistent terminology: §§8 and 12 say *"Substance abuse"*, §17 says *"substance misuse."*
- **PEDS-34 · Sickle cell** (`Week3_Sickle_Cell_Anemia.md`): gives **no pediatric vital-sign norms** anywhere, so a "which cues are expected" item has to source ranges from the textbook rather than Edapt. The module also calls vaso-occlusive crisis *"non-life-threatening"* while listing acute chest syndrome and stroke among its manifestations.
- **PEDS-35 · Sickle cell, absent content:** hydroxyurea, transcranial doppler stroke screening, and folic acid do not appear anywhere. Standard pediatric curriculum content — likely textbook or handout, but confirm the module has no section covering them.

---

# NR449 Evidence-Based Practice — Week 1

## Capture-suspect — check these first

### EBP-13 · Level III definition ends mid-phrase

`Week1_Research_as_Evidence_in_Nursing_Practice.md`

> *"Level III = evidence from case studies, studies of intact groups, non-randomized"*

The trailing *"non-randomized"* is a dangling adjective with no noun. Separately, Level III overlaps Level II, which already claims *"randomized or non-randomized control studies"* — so a non-randomized controlled study qualifies for both levels.

**Re-check:** likely a dropped trailing word (e.g. "non-randomized trials"). Recovering it may also resolve the overlap.

## Source-suspect — verify our capture is faithful, then report upstream

### EBP-14 · Nuremberg Code dated 1947 and 1949 in the same course

- `Week1_Historical_Events_in_Research.md` §3 timeline: *"1947: The Nuremberg Code"*
- Same file, §5: *"The Nuremberg Code, established in 1949, was used by American military judges…"*
- `Week1_Ethics_in_Research.md`: *"The ethical standards known as the Nuremberg Code were developed in 1949."*

The timeline and the prose disagree, and the prose date is repeated across two modules — so a student sees 1949 twice and 1947 once. (The Code was issued with the August 1947 verdict; 1949 is when it appeared in the published trial record. Both dates circulate, which is exactly why the guide should pick one and say why.)

**Report to authors:** an exam item asking when the Nuremberg Code was established is currently unanswerable from our own materials.

### EBP-15 · 1986 NIH nursing research body named wrong

`Week1_Introduction_to_Evidence_Based_Practice.md`

> *"**1986:** The National Center for Research for Nursing (NCRN) opened as part of the National Institutes of Health (NIH)."*

The body established in 1986 was the **National Center for Nursing Research (NCNR)**. Both the expansion and the acronym are wrong, and the error repeats in the next line — *"The NCRN became an institute…"*. The guide gets the 1993 successor right (NINR), which isolates the 1986 name as the defect.

**Report to authors:** verifiable against NINR's own published history. A "what was NINR called before 1993" item would currently be keyed to a name that never existed.

---

# NR449 Evidence-Based Practice — Week 3

**Partial.** `Week3_Research_Design.md` is fully captured (manifest reconciles 16/16, all 9 Explore sections present, no garbling) and is audited below. `Week3_Theory_and_Frameworks.md` was still being extracted when this round was written — its manifest claims 7 captured sections but only §1 and §3 are present. **Re-audit that module once extraction completes**; it is not covered here, and the Week 3 quiz currently keys Research Design only.

## Source-suspect — verify our capture is faithful, then report upstream

### EBP-16 · Qualitative research both has and does not have variables

`Week3_Research_Design.md`

§6, the section devoted to variables:

> *"Variables are not used in qualitative research, but are the basis of quantitative research."*

§14, in a passage whose worked example is explicitly *"a phenomenological study of nursing students who work 20 hours or more a week"*:

> *"Design variables are identified and defined"* … *"Are the students also parents? … How old are the students? These are all variables that may influence outcomes."*

The same qualitative study is said both to have no variables and to require identified, defined variables. This is the sharpest contradiction in the module — and it is squarely testable, since "do qualitative studies use variables" is exactly the kind of item that gets written.

**How the quiz handles it:** keyed to §6 (the section devoted to variables, and the more declarative statement), with a parenthetical in the rationale flagging the §14 position so a student is not blindsided if the exam keys the other side.

### EBP-17 · Survey and cross-sectional definitions overlap

Same file, §7:

- Survey — *"a single point in time or a single sample characteristic"*
- Cross-sectional — *"single point in time, sample characteristics differ on a key characteristic"*

The *"or"* in the survey definition makes it subsume cross-sectional, since a cross-sectional study is also conducted at a single point in time. Only the paired cancer-diagnosis examples actually disambiguate the two, so quiz items are built on the examples rather than the definitions.

**Report to authors:** the survey definition likely wants "and", or an explicit contrast naming the differing-characteristic criterion as what distinguishes cross-sectional.

### EBP-18 · One causality criterion defined without a mechanism

Same file, §12. Temporality and specificity each get a mechanism and an example; "influence" gets only a bare noun phrase:

> *"The statistical soundness of the effect that the independent variable has on the dependent variable"*

No threshold, no example, no contrast with the other two criteria. A "which criterion is unmet" item cannot fairly key influence, so the quiz keys specificity instead.

### EBP-19 · Article-evaluation criteria are partly circular

Same file, §14. Three of the five bullets restate the same phenomenology example rather than teaching a distinct criterion. The criterion *"The design selected can be clearly identified and linked to the research question"* is explained as:

> *"The reader should be able to identify the design used and this design should be a phenomenological design…"*

which asserts the answer to the worked example instead of stating the standard. The section is usable but thin — only two bullets (replication, and explaining decisions as a qualitative design emerges) carry transferable content.

**Same defect class as the FINER "Interesting" note in Round 1** — a criterion defined by restating itself. Worth reporting together as an editorial pattern.
