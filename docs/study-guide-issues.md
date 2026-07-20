# Study Guide Issues — NR328 Pediatrics & NR449 Evidence-Based Practice

**Date:** 2026-06-22
**Courses covered:** NR328 Pediatric Nursing (Week 2; Week 3 where noted) · NR449 Evidence-Based Practice (Week 2)
**Not covered:** NR327 Maternal-Child and NR228 Nutrition were reviewed separately and are out of scope here.

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

### PEDS-02 · Five-stage disease model established, then never applied — no incubation periods
`Week2_Communicable_Diseases_and_Immunizations.md`
- §3 defines five stages: *"**Incubation period:** the initial stage after exposure before symptoms are apparent"* … *"**Decline stage:** symptoms gradually improve"* … *"**Convalescence:** symptoms resolve"*
- §§5–9 (chickenpox, measles, mumps, German measles, whooping cough) present only *"Prodromal phase:"* and *"Acute phase:"* — pertussis alone adds a convalescent stage.

No incubation period is given for any disease, though that's the number needed for exposure and isolation decisions.

**Re-check:** each disease almost certainly had an incubation/communicability row or tab that wasn't captured. Re-open each disease section and check for additional tabs, a summary card row, or a table column we dropped.

### PEDS-03 · "Airborne Precautions" tab whose only signage says "Airborne Contact"
`Week2_Communicable_Diseases_and_Immunizations.md` §4 "Explore: Infection Control"
- *"### Tab: Airborne Precautions"* / *"- For illnesses transmitted by airborne particles."*
- Signage transcript in that same tab: *"**Transcript (isolation signage):** Airborne Contact Precautions (in addition to standard precautions)"*

The module never actually presents standalone airborne precautions, yet later sections cite "airborne contact" as if it were a defined category.

**Re-check:** likely a signage image attached to the wrong tab, or a separate airborne-only sign that wasn't captured. Confirm which signage images exist in §4 and which tab each belongs to.

### PEDS-04 · RSV summary card bullet nesting garbled
`Week2_Pediatric_Respiratory_Alterations.md` §13 "Explore: Respiratory Syncytial Virus"
> *"- Contagious 3-8 days:"*
> *"  - Up to 4 weeks in infants and immunocompromised"*
> *"  - Resolves on own 1-2 weeks"*

"Resolves on own 1–2 weeks" is illness duration, not contagious period, but it's captured as a child of "Contagious 3-8 days" — so 3–8 days, 1–2 weeks, and 4 weeks read as competing values for the same attribute.

**Re-check:** indentation/nesting lost on capture. Re-open the summary card and confirm the real hierarchy. Also note the card's statistics (*"2.1 million outpatient visits," "57,527 hospitalizations"*) carry no year or source — check whether a citation line was dropped.

### PEDS-05 · Peak flow zone thresholds overlap
`Week2_Pediatric_Respiratory_Alterations.md` §15 "Explore: Asthma" → Tab Therapeutic Management, peak-flow transcript
> *"- Green Zone: 80-100% of normal peak flow indicates good control"*
> *"- Yellow Zone: 50-80% of normal peak flow indicates caution and worsening symptoms"*

80% sits in both Green and Yellow (and 50% in both Yellow and Red), so a boundary reading has two contradictory actions.

**Re-check:** the American Lung Association source this is drawn from states Yellow as **50–79%**. A one-character capture slip (79 → 80) would explain it exactly. Verify the transcript against the on-screen figure before assuming the source is wrong.

### PEDS-06 · CDC citation garbled, in-text suffix unmatched
`Week2_Communicable_Diseases_and_Immunizations.md` §15
- In-text: *"(CDC, 2025b)"*
- Reference list: *"- Centers for Disease and Control (2025). *Recommended vaccines for young children*."*

The agency name is garbled ("Centers for Disease **and** Control"), and `2025b` has no matching lettered entry — the list has two unlettered 2025 CDC entries plus one n.d.

**Re-check:** confirm the reference block was captured completely; a lettered entry (2025a/2025b) may have been dropped or merged.

### PEDS-07 · Media referenced with no transcript
| File · § | Missing asset | Why it matters |
|---|---|---|
| `Week2_Cystic_Fibrosis.md` §4 (Respiratory tab) | audio *"16_Cystic_Fibrosis"* | that tab is the module's **only** coverage of CF respiratory findings |
| `Week2_Communicable_Diseases_and_Immunizations.md` §9 | audio *"Pertussis_Symptoms_Sound"* | the pathognomonic whoop exists only as sound |
| `Week2_Croup_and_Bacterial_Epiglottitis.md` §4 | audio *"03_..._Croup"* and *"04_..._Epiglottitis"* | the two comparison exemplars for a module whose whole purpose is telling them apart |
| `Week2_Pediatric_Respiratory_Alterations.md` §3 | video *"respiratory assessment of pediatric clients"* | — |

**Re-check:** audio transcription isn't currently available, so these may stay gaps. But confirm whether any of them ship with **captions, a transcript panel, or alt text** that we could capture as text instead. If not, note them as known gaps and move on — this is also worth raising with the authors as an accessibility issue, since findings taught only as sound are unavailable to deaf and hard-of-hearing students.

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

### EBP-02 · "Complete" search template uses AND where the guide teaches OR
`Week2_Literature_Review.md`
- §13 "Ready to Search" → Complete Literature Search Strategy Template: *"Parentheses: (post-menopausal women) AND (\"hormone replacement therapy\" **AND** HRT) AND (breast cancer)"*
- §11 Tab Parentheses: *"grouping (hormone replacement therapy **OR** HRT) tells the database to look for either term."*
- §11 worked example: *"| Parentheses | (\"hormone replacement therapy\" **OR** HRT) |"*

§9 defines AND as requiring both terms (*"AND will reduce your results and only show sources that contain both keywords it connects"*), so the final template reverses the rule taught two sections earlier and contradicts the earlier worked example in the same file. Run as written, the search returns almost nothing.

**Re-check:** the template is likely an image or formatted block — a single OR→AND transcription slip would explain it entirely. Verify against the on-screen template before reporting.

### EBP-03 · Search-terms row silently loses a synonym
`Week2_Literature_Review.md`
- §9: *"Terms: post-menopausal women / **older women** | hormone replacement therapy / HRT | breast cancer / cancer"*
- §13 final template: *"Terms: post-menopausal women / **—** | hormone replacement therapy / HRT | breast cancer / cancer"*

"older women" is replaced by an em dash with no explanation while the other two pairs carry through unchanged. Quoting is also inconsistent between the two templates (§13 quotes only "hormone replacement therapy" and leaves post-menopausal women unquoted).

**Re-check:** an em dash in one cell of an otherwise-complete table is a classic empty-cell capture artifact. Confirm what that cell actually contains.

### EBP-04 · PICOT worked answer supplies a comparison absent from the source quote
`Week2_The_PICOT_Question.md` §8 "Explore: PICOT and Purpose Statements"
- Quoted purpose statement: *"The aim of the present study was to evaluate the effects of an oral hygiene protocol (consisting of 2% chlorhexidine and manual brushing) in a heterogeneous population of ICU patients on the VAP incidence…"*
- Provided answer: *"…compared to **placebo gel** with toothbrushing (comparison)…"*

Students are told to build the PICOT from the quoted statement, but "placebo gel" appears nowhere in it — so the answer can't be derived from the material given.

**Re-check:** the quoted purpose statement may have been truncated mid-capture (the ellipsis is suspicious). Verify whether the full on-screen quote includes the comparison arm.

### EBP-05 · Truncated DOI and wrong journal name
`Week2_The_PICOT_Question.md` §8, reference block
> *"de Avila Meinberg, M. C., … & Lobo, S. M. (2012). The use of 2% chlorhexidine gel and toothbrushing for oral hygiene of patients receiving mechanical ventilation: Effects on ventilator-associated pneumonia. *Clinical Research, 24*(4). https://doi.org/10.1590/S"*

The DOI terminates at `10.1590/S` — a bare prefix plus one character, not resolvable. The italicized journal title reads "Clinical Research," which is a section label rather than a periodical; that 2012;24(4) citation belongs to *Revista Brasileira de Terapia Intensiva*. No page or article number is given.

**Re-check:** the truncated DOI is almost certainly ours — verify and recapture the full reference string.

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

## Examined and NOT confirmed — do not chase these

| Candidate | Finding |
|---|---|
| NR449 "replication is essential" vs FINER "Novel" | Reconcilable, not a contradiction — the guide's own Novel criterion admits studies that *"confirm or refute previous findings."* The only residual issue is that *"Replication of previous studies is essential"* sits under a slide headed "Review the literature" and reads as a non sequitur. Editorial clarity at most. |

## Verified consistent — do not re-report

- **NR328:** epiglottitis age (2–5 years in both modules); epiglottitis 24-hour antibiotic timeline (§8 and §9 agree); pertussis stage durations (prodromal 1–2 wks, acute 4–6 wks, convalescent 1–2 wks); RSV precautions (droplet and contact); chickenpox precautions (airborne contact, narrative and card agree); **no section-numbering gaps** in any Week 2 module — captured plus skipped sections account for every number.
- **NR449:** all five module manifests account for every section number with no gaps.

## Low-severity formatting notes

Bundle rather than filing individually: `Week2_Croup_and_Bacterial_Epiglottitis.md`'s manifest lists *"Explore: Types of Croup (3)"* against an actual heading of *"Explore: Types of Croup Syndromes"*; `Week2_Cystic_Fibrosis.md` §6 places the *"Transcript (figure: 'Huff Coughing')"* several items below the huff-coughing bullet it belongs to.
