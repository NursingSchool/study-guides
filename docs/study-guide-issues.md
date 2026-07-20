# Study Guide Issues — Verified Defect Report

**Date:** 2026-06-22
**Courses reviewed:** NR327 Maternal-Child (Weeks 4–7) · NR228 Nutrition (Weeks 4–7) · NR328 Pediatric Nursing (Week 2, plus Week 3 where noted) · NR449 Evidence-Based Practice (Week 2)

## Scope and method

Every issue below was verified by opening the source file and reading the surrounding text. Each entry gives the file, the section(s), and short verbatim quotes of **both** conflicting passages so the location can be checked directly.

**In scope**
- **Internal contradiction** — the material states X in one place and not-X in another, including a worked example or practice question that contradicts the guide's own stated rule.
- **Terminology error** — an abbreviation expanded wrongly, or one term used with two meanings.
- **Capture defect** — garbled, truncated, duplicated, or missing text; content promised but absent; media referenced with no transcript; malformed references.

**Explicitly out of scope**
- Content that is merely behind current evidence-based practice. Textbooks lag, and that is expected. Nothing in this report is a "your source is out of date" complaint.

**Confidence** is marked `high` (unambiguous on the page) or `medium` (real, but may have author context we can't see). Items examined and found *consistent* are listed at the end so they are not re-reported.

## Summary

| Course | Contradictions | Terminology | Capture | Total |
|---|---|---|---|---|
| NR228 Nutrition | 20 | 13 | 18 | **51** |
| NR327 Maternal-Child | 9 | 5 | 3 | **17** |
| NR328 Pediatrics | 4 | 4 | 7 | **15** |
| NR449 EBP | 6 | 2 | 4 | **12** |
| | | | | **95 line items / ~65 distinct defects** |

---

## Priority issues

These are the ones most likely to produce a wrong answer or a wrong clinical action. Start here.

| # | Course | Issue |
|---|---|---|
| P1 | NR228 | Constipation defined so that "1 bowel movement every 3 days" is simultaneously healthy and constipated |
| P2 | NR228 | Diarrhea section recommends dairy/apples/apricot and prohibits them, in the same section |
| P3 | NR328 | Peak flow zones overlap — 80% is both Green and Yellow, 50% is both Yellow and Red |
| P4 | NR327 | Epidural space definition contradicts itself within one sentence |
| P5 | NR228 | Glycemic index prose contradicts its own chart (corn, pasta); all five bands overlap |
| P6 | NR327 | PPROM cutoff is <37 weeks in one section, <36 in the next — 36 0/7–36 6/7 belongs to neither |
| P7 | NR327 | SGA worked example ("10th percentile → SGA") contradicts the definition stated two lines above |
| P8 | NR449 | Evidence hierarchy: narrative ranking and levels table give different answers for the same study |
| P9 | NR228 | Digoxin case study: stated mechanism (reduced absorption) is the opposite of its outcome (toxicity) |
| P10 | NR449 | "Complete" search template uses `AND` to join a term with its own synonym, reversing the guide's own OR rule |
| P11 | NR327 | PROM expanded as both "prolonged" and "premature" rupture of membranes in the same week |
| P12 | NR328 | Croup peak age given as "<5 years" in one Week 2 module and "6 months to 3 years" in another |
| P13 | NR228 | Blood glucose threshold written as "250 **ml**/dL" |
| P14 | NR327 | "Phenylalanine **hydrolase**" (twice) — the enzyme is phenylalanine hydroxylase |

---

# NR327 Maternal-Child Nursing (Weeks 4–7)

### MC-01 · Active-phase contraction frequency stated two ways in one self-check
`Week4_Process_and_Stages_of_Labor.md` §12 "Self-Check: Three Phases of Dilation"
- Matching table: *"Active Phase | 4-7 cm; ... contractions every 3-5 minutes lasting 40-60 seconds."*
- Feedback/rationale, same item: *"Active phase: 4-7 cm, contractions every 2-3 minutes lasting 40-60 seconds."*

The same question gives two frequencies, and the feedback makes active phase identical to transitional phase, erasing the distinction being tested. A separate Reflect item uses 3–5 minutes, so 2–3 is the outlier.
`material error` · **high**

### MC-02 · IUPC intensity and resting tone differ between text and strip
`Week4_Fetal_Assessment_and_Monitoring.md` §6 "Explore: Internal Electronic Fetal Monitoring"
- Body: *"these contractions measure 55 mmHg with a 20 mmHg resting tone between contractions."*
- Image transcript (IUPC strip), same section: *"these contractions measure 50 mmHg with a 5 mmHg resting tone between contractions."*

Not cosmetic: a 20 mmHg resting tone is clinically abnormal, 5 mmHg is normal.
`material error` · **high**

### MC-03 · AROM expanded as "augmented rupture of membranes"
- `Week4_Nursing_Care_Intrapartum_Period.md` §3 flashcards: *"AROM: Augmented (also called artificial) rupture of membranes"*
- `Week4_Operative_Delivery.md` §5: *"This procedure is called an amniotomy or an artificial rupture of membranes (AROM)."*

"Augmented" is not a rupture-of-membranes term (augmentation refers to labor augmentation).
`terminology error` · **high**

### MC-04 · TSB attached to "transcutaneous bilirubin"
`Week7_Hyperbilirubinemia.md`
- §4: *"when the transcutaneous bilirubin (TSB) rises more rapidly..."*
- §1: *"when the total serum bilirubin (TSB) rises quickly..."* · §7: *"transcutaneous bilirubin (TcB) measurements using a bilirubinometer"* and *"a blood level measurement (invasive) called total serum bilirubin (TSB)."*

§4 is a near-verbatim restatement of §1 with "total serum" swapped for "transcutaneous," keeping the TSB abbreviation.
`terminology error` · **high**

### MC-05 · Baseline bradycardia/tachycardia duration appears inverted
`Week4_Fetal_Assessment_and_Monitoring.md` §11, Accordion 2
- *"Bradycardia: < 110 bpm, for < 10 minutes"* / *"Tachycardia: > 160 bpm, for < 10 minutes"*
- Same accordion: *"Baseline fetal heart rate is the approximate mean fetal heart rate ... during a 10 minute segment."* · Accordion 5: *"Prolonged Decelerations | Lasting > 2 minutes, but < 10 minutes"*

A baseline defined over 10 minutes cannot be established by a change lasting under 10 minutes, and sub-10-minute drops are already classified as prolonged decelerations. Reads as an inverted `>`.
`material error` · **medium**

### MC-06 · Epidural space definition self-contradictory *(P4)*
`Week4_Pain_and_Labor.md` §5, "Epidural Nerve Block"
> *"The epidural space is the area outside the dura mater, between the dura and the spinal cord."*

"Outside the dura" and "between the dura and the spinal cord" are opposite compartments; as written it describes the subdural/subarachnoid space.
`material error` · **high**

### MC-07 · PROM given two incompatible expansions *(P11)*
- `Week4_Operative_Delivery.md` §5: *"After 24 hours, this situation is referred to as prolonged rupture of membranes (PROM)."*
- `Week4_Nursing_Care_Intrapartum_Complications.md` §16: *"Premature rupture of membranes (PROM) refers to the rupture of the amniotic membranes before true labor has started."* (also "premature" in the Week 4 terminology flashcards)

`terminology error` · **high**

### MC-08 · PPROM cutoff <37 vs <36 weeks *(P6)*
`Week4_Nursing_Care_Intrapartum_Complications.md`
- §16: *"When this occurs prior to 37 weeks gestation ... preterm premature rupture of membranes (PPROM)."*
- §17, both scenarios: *"If the pregnancy is preterm (<36 weeks, PPROM)..."* paired with *"term (>37+ weeks)"*

Leaves 36 0/7–36 6/7 in neither category. §10 separately defines preterm labor as 20–36 6/7 weeks.
`material error` · **high**

### MC-09 · SGA worked example contradicts the stated percentile rule *(P7)*
`Week6_Nursing_Care_Newborn_Assessment.md` §11
- Rules: *"Small for Gestational Age (SGA): the newborn's size is below the 10th percentile"* / *"Appropriate for Gestational Age (AGA): ... between the 10th and 90th percentiles"*
- Example, same section: *"Alex's measurements are in the 10th percentile..."* → *"Alex is SGA, small for gestational age..."*

By the module's own definitions, a newborn *at* the 10th percentile is AGA.
`material error` · **high**

### MC-10 · New Ballard component count
`Week6_Nursing_Care_Newborn_Assessment.md` §11, Tab "New Ballard Score"
- *"the newborn's responses to 6 tests of neuromuscular maturity and 7 tests of physical maturity are scored."*
- Next paragraph: *"The 13 areas of physical characteristics are assessed..."*

The 13 total items are relabeled as all-physical.
`material error` · **medium**

### MC-11 · Contraceptive implant failure rate vs effectiveness
`Week5_Family_Planning.md` §2 feedback
> *"The failure rate of this device during the first year of use is 0.05% (99.5% effective)."*

0.05% failure = 99.95% effective. §8 repeats "highly effective (99.5%)", so one figure is propagated wrong.
`material error` · **medium**

### MC-12 · Natural family planning: 24% "all types" vs 54% coitus interruptus
`Week5_Family_Planning.md` §5
- Lead: *"These methods (all types) have a 24% failure rate during the first year of use."*
- Same section: *"[Coitus interruptus is] the least reliable of all methods, with a 54% failure rate in the first year of use."*

`material error` · **medium**

### MC-13 · Phenylalanine "hydrolase" *(P14)*
`Week6_Nursing_Care_Newborn_Assessment.md` §12, Tab "PKU Screening"
> *"...converted to tyrosine by the liver enzyme phenylalanine hydrolase..."* and *"...phenylalanine hydrolase is deficient."*

The enzyme is phenylalanine **hydroxylase**; a hydrolase is a different enzyme class. Misspelled twice, so not a one-off typo.
`terminology error` · **medium**

### MC-14 · Garbled "(CAN)" abbreviation
`Week7_Nursing_Care_High-Risk_Newborn_Acquired_Conditions.md` §7
> *"...subjected to the forces of labor, which can also be caused by a cord around the neck (CAN)."*

"CAN" is not a recognized abbreviation (standard term: nuchal cord); the clause is grammatically detached and reads as spliced content.
`capture defect` · **medium**

### MC-15 · WET FROG mnemonic entry garbled
`Week7_Nursing_Care_High-Risk_Newborn_Acquired_Conditions.md` §11
> *"E = effort (head bobbing contractions)"* — while *"R = retractions"* is a separate letter in the same list.

"head bobbing contractions" is not a clinical phrase; appears truncated.
`capture defect` · **medium**

### MC-16 · Safe sleep: no blankets vs blanket wraps
`Week6_Nursing_Care_Newborn.md` §13, Tab "Activity and Safe Sleep"
- *"...ensuring that there are no extra linens, blankets, or stuffed toys in the newborn's crib..."*
- Immediately after: *"...including the use of clothing and blanket wraps to keep the newborn warm, with a cap on..."*

Adjacent clauses, no distinction drawn between swaddling and loose bedding.
`ambiguous / needs author context` · **medium**

---

# NR228 Nutrition (Weeks 4–7)

## Internal contradictions

### NUT-01 · Constipation definition overlaps the healthy range *(P1)*
`Week7_Diarrhea_and_Constipation.md` §6
- *"A healthy bowel eliminates stool between 3 times each day to 1 time every 3 days."*
- Next sentence: *"A person is considered constipated when they have fewer than three bowel movements per week..."*

One movement every 3 days is ~2.3/week — healthy and constipated at once.
`material error` · **high**

### NUT-02 · Diarrhea diet recommends and prohibits the same foods *(P2)*
`Week7_Diarrhea_and_Constipation.md` §16, within one section
- Small Meals: *"Include oranges, grapefruit, bananas, apples, potatoes, dairy products, apricot nectar, baked squash, and sweet potatoes."*
- Liquids: *"Avoid milk products."*
- Additional Food Recommendations: *"Avoid polyols ... found in apples, apricots, nectarines, pears, plums, prunes, and mushrooms."*

Dairy, apples, and apricot are on the recommend and avoid lists simultaneously.
`material error` · **high**

### NUT-03 · Glycemic index prose contradicts its own chart *(P5)*
`Week7_Nutrition_and_Diabetes.md` §7
- Prose: high-GI list includes *"corn"*; low-GI list includes *"pasta"*
- Chart, 50–70 band: *"Muesli, corn, couscous, brown rice, spaghetti, popcorn, yams"*

Corn is keyed high but charted mid; pasta keyed low but spaghetti charted mid. Additionally every band boundary overlaps (70–100 / 50–70 / 30–50 / 10–30 / 0–10) and milk appears twice (*"Milk & soy milk"* 30–50; *"Whole milk"* 10–30).
`material error` · **high**

### NUT-04 · Digoxin case study mechanism is the opposite of its outcome *(P9)*
`Week6_Food_and_Medication_Interactions.md` §5
- *"The client was warned of decreased medication absorption and possible failure of medication associated with the consumption of calcium."*
- *"Two weeks later, the client presented to the emergency department with a diagnosis of digoxin toxicity."*

Reduced absorption was predicted; excess drug effect resulted. §7's table never pairs digoxin with calcium: *"| Digoxin | Magnesium and vitamin E | ..."*
`material error` · **high**

### NUT-05 · Full liquid diet allows and excludes fruit/vegetables in consecutive sentences
`Week6_Special_Diets.md` §7
- *"...vegetable juice, pureed vegetables, fruit juices, sherbets, puddings, and frozen yogurt."*
- Immediately following: *"Foods not included are solids such as nuts, seeds, fruit, vegetables, and meat."*

`material error` · **high**

### NUT-06 · Calcium timing: blanket rule vs drug-specific rule
`Week4_Nursing_Application_Vitamins_Antioxidants_and_Minerals.md`
- §12 Tab Calcium: *"Calcium citrate ... is best absorbed without food."*
- §20: *"Take calcium supplements with food – Stomach acid produced while eating helps your body absorb calcium."*

`material error` · **high**

### NUT-07 · Grapefruit interaction count: 40 vs 50
`Week6_Food_and_Medication_Interactions.md` §7
- Body: *"There are over 40 medications that can have an adverse effect with grapefruit."*
- FDA video transcript introduced by that sentence: *"More than 50 drugs have been identified..."*

`material error` · **high**

### NUT-08 · IDDSI Level 1 descriptor contradicts its example
`Week7_Dysphagia.md` §5, Tab Drink
> *"| 1 | Drink | Slightly thick liquid | ...can drink through any type of straw... | Honey |"*

Honey is not drinkable through any straw; honey-thick is the legacy term for Level 3.
`material error` · **high**

### NUT-09 · Childhood calorie requirements: stated direction reverses the table
`Week5_Childhood_and_Adolescent_Nutrition.md` §3
- *"As children transition from toddlers to about age 10, their calorie requirements decrease due to slowing growth rates."*
- Table below: *"| Male | 1-3 | 1,046 |"* … *"| Male | 9-13 | 2,279 |"*

`material error` · **high**

### NUT-10 · Gestational timeline doesn't add up
`Week5_Nursing_Application_Nutrition_and_the_Lifespan.md`
- §3: *"- 9 weeks pregnant"*
- §11: *"The home care nurse completes a follow-up visit 6 months later."* and *"Kaya (mother) is at the end of her pregnancy and is due next week."*

9 weeks + 6 months ≈ 35 weeks, about 5 weeks short of term.
`material error` · **high**

### NUT-11 · Low-fat diet after cholecystectomy: 1 week vs several weeks
`Week7_Nursing_Application_Biliary_Health.md`
- §8: *"...a gradual return to normal activities and a low-fat diet for several weeks."*
- §10 Tab Limit Fats: *"Avoid high-fat foods ... for at least 1 week after surgery."*

`material error` · **high**

### NUT-12 · Magnesium: hypomagnesemia given both depressant and excitatory signs
`Week4_Nursing_Application_Vitamins_Antioxidants_and_Minerals.md` §12 Tab Magnesium
- *"When magnesium levels get too low (hypomagnesemia), it can lead to respiratory muscle paralysis, coma, and heart arrest."*
- Next sentence: *"Symptoms aggravate the central nervous system (CNS) ... strong reflexes (nerve excitability)."*
- Next paragraph: *"When magnesium levels get too high (hypermagnesemia), it can depress the central nervous system (CNS)."*

Paralysis/coma/arrest assigned to *hypo*magnesemia, then CNS depression to *hyper*.
`material error` · **medium**

### NUT-13 · Vegetarianism defined by exclusion, then two listed types include fish/poultry
`Week6_Special_Diets.md` §5
- *"Vegetarianism is the exclusion of meat, poultry, and fish from the diet."*
- *"Semivegetarians or Pesce/Pollo Vegetarians: People who include fish or chicken in the diet..."*

`material error` · **medium**

### NUT-14 · IDDSI: foods start at Level 3 or after Level 3
`Week6_Special_Diets.md` §8
- *"Drinks are measured from Levels 0–4, while foods are measured from Levels 3–7."*
- Two sentences later: *"Only after level 3 can clients consume foods."*

`material error` · **medium**

### NUT-15 · Nursing process worked example runs planning before diagnosis
`Week6_Assessment_and_Care.md`
- §6: *"...assessment, diagnosis, planning, implementation, and evaluation."*
- §3: *"Step 3: A plan of care needs to be developed..."* then *"Step 4: Appropriate nursing diagnoses include..."*

`material error` · **medium**

### NUT-16 · Swallowing called involuntary, then coached as voluntary
- `Week7_Nutrition_for_Gastrointestinal_Health.md` §16: *"...swallowing is an involuntary action that occurs without thought."*
- `Week7_Dysphagia.md` §9: *"Encourage frequent, dry swallows or coughing to help clear food..."*

`material error` · **medium**

### NUT-17 · Cirrhosis as cause of hepatitis, and as its consequence
`Week7_Nutrition_and_Biliary_Health.md`
- §12: *"Acute hepatitis can occur as a result of infectious mononucleosis, cirrhosis, toxic chemicals, or viral infection."*
- §6: *"Over time, the liver becomes inflamed and scar tissue develops, often progressing to cirrhosis."*

`material error` · **medium**

### NUT-18 · Pancreatitis as a cause of gallstones, and as their effect
- `Week7_Nursing_Application_Biliary_Health.md` §4: *"Risk factors include pregnancy, hormonal birth control, diabetes mellitus, cirrhosis, pancreatitis, and celiac disease."*
- `Week7_Nutrition_and_Biliary_Health.md` §16: *"Gallstone pancreatitis is a type of pancreatitis caused by a blockage of the pancreas duct by a gallstone."*

`ambiguous / needs author context` · **medium**

### NUT-19 · Selenium: RDA given, then said not to be on the DRI list
`Week4_Antioxidants.md` §8
> *"Selenium RDA for an adult is 55 mcg. ... This antioxidant is one not listed on the DRI list."*

An RDA *is* a DRI value. Likely means "not in the linked vitamins table," but as written it is self-contradictory.
`ambiguous / needs author context` · **medium**

### NUT-20 · Renal diet limits protein, then substitutes high-protein foods
`Week6_Special_Diets.md` §14
- *"They require a diet that limits sodium, potassium, phosphorus, protein, and fluid intake..."*
- Substitution table: *"| Protein | ...avoid peanut butter, nuts, seeds... | Lean high-protein meat, fish, poultry, fresh pork, or eggs |"*

`ambiguous / needs author context` · **medium**

## Terminology errors

| ID | File · § | Issue | Conf. |
|---|---|---|---|
| NUT-21 | `Week7_Nutrition_for_Gastrointestinal_Health.md` §4 | *"irritable bowel disease (IBD)"* — IBD is **inflammatory** bowel disease; irritable bowel *syndrome* is IBS | high |
| NUT-22 | `Week7_Nutrition_for_Gastrointestinal_Health.md` §11 | NHLBI expanded as *"National Heart, Lung, and Blood institute"* in the transcript and *"National Health, Lung and Blood Institute"* in the reference, same section | high |
| NUT-23 | `Week7_Nursing_Application_GI_Health.md` §9 | *"P-Pain"* in the PQRST pain mnemonic — P is Provocation/Palliation; as written the mnemonic defines itself | high |
| NUT-24 | `Week7_Nursing_Application_Biliary_Health.md` §4 | *"total parental nutrition"* → parenteral | high |
| NUT-25 | `Week7_Nutrition_and_Diabetes.md` §13 | *"Steviocide"* → stevioside; same paragraph calls it a sweetener while saying it *"cannot be marketed or sold as a sweetener in the United States"* | high |
| NUT-26 | `Week7_Nutrition_and_Diabetes.md` §15 | *"Kussmal's respirations"* → Kussmaul | high |
| NUT-27 | `Week7_Nutrition_and_Diabetes.md` §15 | HHNS given as *"hyperglycemic hyperosmolar nonketotic"* in the intro and *"Hyperosmolar Hyperglycemic Nonketotic"* in the tab heading | medium |
| NUT-28 | `Week5_Maternal_and_Infant_Nutrition.md` §13 | *"vitamins such as iron and vitamin C"* — iron is a mineral, and §3 correctly lists it under Minerals | high |
| NUT-29 | `Week4_Minerals.md` §4/§5 | *"Chloride"* in the table vs *"Chlorine"* in the electrolyte image transcript | medium |
| NUT-30 | `Week5_*` (3 files) | USDA agency named *"Food and Nutrition Administration"*, *"Food and Nutrition Service"*, and *"Food and Nutrition Services"* | high |
| NUT-31 | `Week6_Nursing_Application_Assessment_and_Care.md` §3 | Lactose intolerance recorded under *"Allergies:"* though §6 correctly calls it an intolerance | medium |
| NUT-32 | `Week6_Special_Diets.md` §4 | *"Nothing by mouth (NPO), a Latin abbreviation for nil per os, is a diet order that means 'nothing by mouth.'"* — defines the term with itself | medium |
| NUT-33 | `Week6_Assessment_and_Care.md` §4 | *"anemia (e.g., iron, B12, thiamine)"* — the third marker is folate | medium |

Also: `Week6_Assessment_and_Care.md` §10 says PEG/PEJ *"deposits nutrition directly into the stomach or small intestine"* then states the intervention is used *"when the upper gastrointestinal (GI) system needs to be bypassed"* — a gastrostomy does not bypass the stomach. `terminology error` · medium

## Capture defects

| ID | File · § | Issue | Conf. |
|---|---|---|---|
| NUT-34 | `Week4_Vitamins.md` §3 | *"they act as precursors and turn vitamins into active chemicals"* — circular; the parallel guide reads correctly: *"they are considered precursors until the body turns them into active chemicals"* | high |
| NUT-35 | `Week4_Fat_Soluble_Vitamins.md` §21 | *"clients taking isotretinoin (Accutane) ... Women of childbearing age who take **either of these drugs**"* — only one drug named; a second was dropped | high |
| NUT-36 | `Week7_Diarrhea_and_Constipation.md` §7 vs §10 | §7 is titled "Constipation Causes" but duplicates §10's care recommendations verbatim, including the same opening sentence and six-bullet list | high |
| NUT-37 | `Week7_Diarrhea_and_Constipation.md` §14 | *"- tolerance to medications"* listed as a diarrhea cause (parallel bullet reads *"intolerance to foods"*) | high |
| NUT-38 | `Week7_Nursing_Application_Nutrition_and_Diabetes.md` §11 | Tab "Renal Insufficiency or Failure" opens *"Retinopathy is also a very common complication..."* — retinopathy has its own tab in the same section | high |
| NUT-39 | `Week7_Nursing_Application_Nutrition_and_Diabetes.md` §7 | *"blood glucose level is greater than 250 **ml/dL**"* — every other value uses mg/dL *(P13)* | high |
| NUT-40 | `Week7_Nutrition_and_Diabetes.md` §6 | *"low-carbohydrate diets are an important source of energy, fiber, vitamins, and minerals"* followed by *"these foods"* with no antecedent — reads as a bad substitution for "carbohydrate-containing foods" | medium |
| NUT-41 | multiple | Word-substitution typos: *"altercations"* → alterations; *"alternations"* → alterations; *"chocking"* → choking; *"Everyone bought a dish to pass"* → brought; *"Greatly alternating intake levels"* → altering; *"almost 38% percent"*; plus dropped words in `Week7_Dysphagia.md` §3 (*"even the client does not have dysphagia"*) and §4 (*"...structure of the esophagus can be caused by:"*) | high |
| NUT-42 | `Week7_Nutrition_and_Biliary_Health.md` §15 | Conditional-mood rationale text with no referent client (*"The white blood cells would be elevated..."*) appears in the lesson body — reads as a Self-Check rationale that leaked in. Same section: *"a digestive fluid that gets released into the small intestine called bile"* (misplaced modifier) | medium |
| NUT-43 | `Week7_Nutrition_for_Gastrointestinal_Health.md` §14 | Tab titled "Gas Locations" but its bullets list symptom types (bloating, eructation, flatus), not locations | medium |
| NUT-44 | `Week4_Nursing_Application_Vitamins_Antioxidants_and_Minerals.md` §18 | Lead-in names four factors affecting calcium absorption; only two bullets follow, and one of them (Medications) isn't in the lead-in | medium |
| NUT-45 | multiple | **Reference year mismatches:** in-text *"(CDC, 2020)"* vs entry dated 2023; *"(Grodner et al., 2020)"* vs entry dated 2023 (3 files); `Week6_Food_Safety.md` §3 cites *"U.S. Department of Health and Human Services (2019)"* with no such entry | high |
| NUT-46 | multiple | **Corrupted reference titles:** *"Journal of Client Experience"* (should be Patient Experience) and *"Cancer clients at risk of herb/food supplement-drug interactions"* — a global patient→client substitution corrupted source titles; *"Momentum Press"* vs *"Monument Press"* for the same work (same OCLC); adult-obesity CDC entry carries the childhood URL; Grodner title varies *"clinical applications"* / *"clinical application"*; *"Davidson, H."* vs *"Davidson, T."*; *"Tish, D. M."* vs *"Tish, D. A."* | high |
| NUT-47 | `Week4_Fat_Soluble_Vitamins.md` §7 | *"[NEEDS MANUAL REVIEW] — Video content with no text transcript available."* — the entire section (Sunlight and Sunscreen) has no content | high |
| NUT-48 | multiple | Media referenced but not transcribed: 3D model "Probiotics in the Gut"; 3D gallbladder/gallstones model; `Week7_Nursing_Application_GI_Health.md` §7 Tab Dysphagia contains only an image description and no instructional text; `Week6_Food_Safety.md` §6 image not transcribed | high |
| NUT-49 | `Week6_Food_Safety.md` §10 | The "Cook" list gives only holding/reheating temps; the minimum internal cooking temperatures its own transcript points to are never provided | high |
| NUT-50 | `Week4_Fat_Soluble_Vitamins.md` §5 | Vitamin A food list breaks its own descending order (*"Liver – 2,520"* then *"Prunes – 3,604"*) and states no unit (IU? mcg RAE?) or serving size | medium |
| NUT-51 | `Week5_Maternal_and_Infant_Nutrition.md` §12 | Breast-milk storage table row has empty refrigerator and freezer cells: *"| Leftover From a Feeding ... | Use within 2 hours ... | | |"* | medium |

Also: `Week4_Nursing_Application_Vitamins_Antioxidants_and_Minerals.md` §16 lists weakness as both a common and a *"(rarely)"* finding of hypokalemia in one sentence (`capture defect`, medium); and §12/§4 of the two Week 4 vitamin guides carry near-identical text where the population scope silently changes from *"Active adults"* to *"Active male adults, which includes middle-aged males"* (`ambiguous`, medium).

---

# NR328 Pediatric Nursing (Week 2; Week 3 where noted)

### PEDS-01 · Peak flow zones overlap *(P3)*
`Week2_Pediatric_Respiratory_Alterations.md` §15, Tab Therapeutic Management
- *"Green Zone: 80-100% of normal peak flow indicates good control"*
- *"Yellow Zone: 50-80% of normal peak flow indicates caution and worsening symptoms"*

80% falls in both Green and Yellow, 50% in both Yellow and Red — a boundary reading has two contradictory actions. The source (American Lung Association) uses 50–79%.
`material error` · **medium**

### PEDS-02 · Croup peak age differs across two Week 2 modules *(P12)*
- `Week2_Croup_and_Bacterial_Epiglottitis.md` §4: *"Acute laryngotracheobronchitis ... primarily affects infants and children less than 5 years old."*
- `Week2_Pediatric_Respiratory_Alterations.md` §8 table: *"| Acute Laryngotracheobronchitis | Upper | Children 6 months to 3 years |"*

Epiglottitis is stated as 2–5 years in both, so the inconsistency is specific to LTB.
`material error` · **high**

### PEDS-03 · Laryngotracheobronchitis classified "Upper" against the section's own definition
`Week2_Pediatric_Respiratory_Alterations.md` §8
- Definition: *"upper airway (affecting the oronasopharynx, pharynx, larynx, and upper part of the trachea) or lower airway (affecting the lower trachea, bronchi, bronchioles, and alveoli)"*
- Table: *"| Acute Laryngotracheobronchitis | Upper | ... |"*

The definition assigns bronchi to the lower airway. (Pertussis and bacterial tracheitis are also tabled "Upper" — medium confidence on those.)
`material error` · **high**

### PEDS-04 · Immunization section promises content it doesn't contain
`Week2_Communicable_Diseases_and_Immunizations.md` §15
- *"Below are the recommended vaccines for birth to 6 years and 7 years and older."*
- What follows: only *"Download and review the [2025 Recommended Immunizations for Children From Birth Through 6 Years Old](...)"*

Zero ages, doses, or intervals appear; the single link covers only birth–6, so the 7-and-older schedule is entirely absent. This is the module's only schedule content, and §16 assumes the reader knows the schedule.
`capture defect` (with internal contradiction) · **high**

### PEDS-05 · CFTR expanded two ways
`Week2_Cystic_Fibrosis.md`
- §3 and §5: *"cystic fibrosis transmembrane regulator (CFTR) gene"*
- §9: *"cystic fibrosis transmembrane conductance regulator (CFTR) modulators"*

§9 is correct; §3 and §5 drop "conductance."
`terminology error` · **high**

### PEDS-06 · *Haemophilus influenzae* misspelled within one paragraph
`Week2_Croup_and_Bacterial_Epiglottitis.md` §4, consecutive sentences
> *"is often caused by haemophilus influenzae. The haemophilus influenza type B vaccine has dramatically reduced cases"*

"influenzae" then "influenza"; neither capitalized or italicized; the vaccine is *Haemophilus influenzae* type **b** (Hib), not "type B."
`terminology error` · **high**

### PEDS-07 · "Airborne Precautions" tab whose signage says "Airborne Contact"
`Week2_Communicable_Diseases_and_Immunizations.md` §4
- *"### Tab: Airborne Precautions"* / *"- For illnesses transmitted by airborne particles."*
- Signage transcript in the same tab: *"Airborne Contact Precautions (in addition to standard precautions)"*

The module never presents standalone airborne precautions, yet later sections cite "airborne contact" as if it were the defined category.
`terminology error` · **high**

### PEDS-08 · Five-stage disease model established, never applied; no incubation periods
`Week2_Communicable_Diseases_and_Immunizations.md`
- §3 defines five stages including *"Incubation period: the initial stage after exposure before symptoms are apparent"*, *"Decline stage"*, *"Convalescence"*
- §§5–9 (chickenpox, measles, mumps, German measles, whooping cough) present only *"Prodromal phase:"* and *"Acute phase:"* (pertussis alone adds a convalescent stage)

No incubation period is given for any disease — the number needed for exposure and isolation decisions.
`ambiguous / needs author context` (likely capture defect) · **medium**

### PEDS-09 · CDC citation garbled, in-text suffix unmatched
`Week2_Communicable_Diseases_and_Immunizations.md` §15
- In-text: *"(CDC, 2025b)"*
- Reference list: *"Centers for Disease and Control (2025). Recommended vaccines for young children."*

Agency name garbled; no lettered entry matches `2025b`.
`terminology error` (citation defect) · **high**

### PEDS-10 · RSV summary card bullet nesting garbled
`Week2_Pediatric_Respiratory_Alterations.md` §13
> *"- Contagious 3-8 days:"* / *"  - Up to 4 weeks in infants and immunocompromised"* / *"  - Resolves on own 1-2 weeks"*

Illness duration is nested under contagious period, so 3–8 days, 1–2 weeks and 4 weeks read as competing values for one attribute. Card statistics ("2.1 million outpatient visits," "57,527 hospitalizations") carry no year or source.
`capture defect` · **medium**

### PEDS-11 · Adult respiratory rate presented as normal in a pediatric module
`Week3_Kawasaki_Disease_and_Multisystem_Inflammatory_Syndrome.md`, COVID-19 3D model transcript, three separate places
> *"A normal respiratory rate is between 12 and 20 breaths per minute."*

12–20 is the adult range (infants ~30–60, toddlers ~24–40). Internally consistent, so the defect is an adult 3D-model asset reused in a pediatric course without a pediatric qualifier.
`material error` · **medium**

### PEDS-12 – PEDS-15 · Media referenced with no transcript
| File · § | Missing asset |
|---|---|
| `Week2_Cystic_Fibrosis.md` §4 (Respiratory tab) | audio *"16_Cystic_Fibrosis"* — the tab is the module's only coverage of CF respiratory findings |
| `Week2_Communicable_Diseases_and_Immunizations.md` §9 | audio *"Pertussis_Symptoms_Sound"* — the pathognomonic whoop exists only as sound |
| `Week2_Croup_and_Bacterial_Epiglottitis.md` §4 | audio *"03_..._Croup"* and *"04_..._Epiglottitis"* — the two comparison exemplars for a module whose purpose is telling them apart |
| `Week2_Pediatric_Respiratory_Alterations.md` §3 | video *"respiratory assessment of pediatric clients"* |

Raised primarily as an **accessibility** matter: findings taught only as audio are unavailable to deaf and hard-of-hearing students, and unavailable to anyone reviewing from notes.
`capture defect` · **high**

### Lower confidence, flagged for author context
- `Week2_Communicable_Diseases_and_Immunizations.md`: German measles narrative says *"spread through direct contact with nasopharyngeal secretions"* but its card lists droplet only, while mumps (saliva) gets *"droplet and contact"*; chickenpox narrative says *"transmitted through the air, direct contact, and through contaminated objects"* but its card lists *"respiratory secretions"* only; whooping cough's card alone appends *"and standard"*. **medium**
- `Week2_Pediatric_Respiratory_Alterations.md` §3: stridor is *"associated with epiglottitis, foreign body, and tracheitis"* — croup omitted, though the next bullet ties barking cough to croup; that bullet also locates barking cough at *"the trachea and bronchi"* while the croup module locates croup at *"the larynx"*. **medium**
- `Week2_Cystic_Fibrosis.md` §4: *"The most common symptoms are respiratory, gastrointestinal, growth failure, and diabetes symptoms"* — the section has five tabs including Reproductive and Integumentary. **medium**

---

# NR449 Evidence-Based Practice (Week 2)

### EBP-01 · Evidence hierarchy: narrative ranking vs levels table *(P8)*
`Week2_Sources_and_Levels_of_Evidence.md`
- §8 transcript: *"1. Clinical practice guidelines 2. Meta-analyses 3. Systematic reviews 4. Randomized clinical trials 5. Cohort studies 6. Outcome research 7. Case-controlled studies 8. Expert opinion"*
- §15 table: *"| Level 1 | Multiple randomized controlled trials that are part of a systematic review, meta-analysis, or practice guidelines |"* … *"| Level 3 | Case-controlled or cohort studies... |"*

§8 ranks guidelines > meta-analyses > systematic reviews and cohort above case-control; §15 puts all three aggregated forms at Level 1 and cohort and case-control together at Level 3. A student grading the same study gets two different answers. §10 reinforces §8: *"[Clinical practice guidelines are] the most comprehensive quality and highest strength evidence."*
`material error` · **high**

### EBP-02 · "Complete" search template uses AND where the guide teaches OR *(P10)*
`Week2_Literature_Review.md`
- §13 template: *"Parentheses: (post-menopausal women) AND (\"hormone replacement therapy\" AND HRT) AND (breast cancer)"*
- §11 Tab Parentheses: *"grouping (hormone replacement therapy OR HRT) tells the database to look for either term."*
- §11 worked example: *"| Parentheses | (\"hormone replacement therapy\" OR HRT) |"*

The final template joins a term with its own abbreviation using AND, which §9 defines as requiring both (*"AND will reduce your results and only show sources that contain both keywords"*). Run as written, the search returns almost nothing.
`material error` · **high**

### EBP-03 · Hard-coded date range contradicts the five-year rule
`Week2_Literature_Review.md`
- §11 and §13: *"| Date range | 2016-2021 |"*
- §11 Tab Search Filters: *"...typically within the last five years."* · §§7 and 14 criteria tables: *"| Year of publication | Within the last five years | None |"*

2016–2021 inclusive is a **six**-year span, so it never satisfied the rule even at authoring time, and it is now stale besides.
`material error` · **high**

### EBP-04 · Worked example exceeds the stated limiter maximum
`Week2_Literature_Review.md` §11
- *"It is best to apply no more than one to two limiters initially."*
- Worked example immediately following: *"| Date range | 2016-2021 | Language | English | Peer reviewed | Yes, or checked |"*

Three filters plus quotation marks and parentheses on the first pass.
`material error` · **medium**

### EBP-05 · Research-process table missing the step the prose calls final
`Week2_The_Research_Process.md` §6
- Body: *"...communication is the final step in both the nursing and research process."*
- Table's last row: *"| Evaluation | Analyze data |"*

No communication row exists, though §4 lists "Communicate Findings" as phase 7 of 8 — a row appears to have been dropped. (Separately, communication is not the final step of the ANA five-step nursing process, where evaluation is.)
`capture defect` · **medium**

### EBP-06 · Mislabeled Boolean "common mistake"
`Week2_Literature_Review.md` §9 Tab Connectors
> *"Placing the Connecting Word in the Wrong Place: Correct: post-menopausal women AND hormone replacement therapy AND breast cancer / Incorrect: post-menopausal women OR hormone replacement therapy AND breast cancer"*

The heading describes a *placement* error; the example demonstrates a *substitution* error — the connector sits in the same position in both lines, only AND→OR changed.
`terminology error` · **high**

### EBP-07 · Search-terms row silently loses a synonym
`Week2_Literature_Review.md`
- §9: *"Terms: post-menopausal women / older women | hormone replacement therapy / HRT | breast cancer / cancer"*
- §13 final template: *"Terms: post-menopausal women / — | ..."*

"older women" is replaced by an em dash with no explanation while the other pairs carry through. Quoting is also inconsistent between the two templates.
`capture defect` · **medium**

### EBP-08 · Social media: conditional acceptance vs categorical rejection
`Week2_Sources_and_Levels_of_Evidence.md` §15
> *"Most researchers will not accept popular media or social media as evidence except under specific conditions."* … *"nothing should be accepted ... unless it is linked to an appropriate website and is verifiable."* … *"**Social media have a high risk of disinformation; therefore, they are not a credible source.**"*

Two conditional carve-outs (plus a Twitter example offered as a possible level 5 primary source) followed by a bolded unconditional rejection.
`ambiguous / needs author context` · **medium**

### EBP-09 · PICOT worked answer supplies a comparison absent from the source
`Week2_The_PICOT_Question.md` §8
- Quoted purpose statement: *"...to evaluate the effects of an oral hygiene protocol (consisting of 2% chlorhexidine and manual brushing) in a heterogeneous population of ICU patients on the VAP incidence..."*
- Provided answer: *"...compared to placebo gel with toothbrushing (comparison)..."*

"Placebo gel" appears nowhere in the statement students are told to derive the PICOT from.
`ambiguous / needs author context` · **medium**

### EBP-10 · Hypothesis criteria conflict with nondirectional hypotheses
`Week2_The_PICOT_Question.md` §15 Tab Elements of a Good Hypothesis
- *"- Identified direction of interest"* listed as a required element
- Same tab: *"A **nondirectional** hypothesis is one in which the researcher is interested in a change in any direction."*

The section's own primary worked example is a null hypothesis, which has no direction.
`ambiguous / needs author context` · **medium**

### EBP-11 · Truncated DOI and wrong journal name
`Week2_The_PICOT_Question.md` §8, reference block
> *"...Clinical Research, 24(4). https://doi.org/10.1590/S"*

The DOI terminates at a bare prefix plus one character. "Clinical Research" is a section label, not a periodical; the 2012;24(4) citation belongs to *Revista Brasileira de Terapia Intensiva*. No page or article number given.
`capture defect` · **high** (DOI) / medium (journal)

### EBP-12 · Journal title error, repeated
`Week2_Identifying_Practice_Problems.md` §§8 and 9 (identical reference blocks)
> *"Workplace Health & Safety Journal, 63(10)."*

The journal is *Workplace Health & Safety*; "Journal" is appended in error. Both instances omit page/article numbers, so a fix must be applied twice.
`capture defect` · **medium**

### Minor, low priority
- §4 of `Week2_Identifying_Practice_Problems.md` is headed "Nurse-Sensitive Concepts" but the body alternates "nursing-sensitive indicators," "nurse-sensitive concept," and "medically-sensitive concept" without distinguishing indicators from concepts.
- `Week2_Literature_Review.md` §6: *"Limiting the number of databases searched can result in publication bias..."* — the described effect is retrieval/selection bias; publication bias concerns what gets published.
- `Week2_The_Research_Process.md` §11: *"Correlation research"* → correlational research.
- `Week2_The_PICOT_Question.md` §12 FINER: *"Interesting: Is the question interesting?"* is circular and carries no criterion unlike the other four — possible truncation.

---

## Candidates examined and NOT confirmed

Listed so they are not reported in error.

| Candidate | Finding |
|---|---|
| NR327 newborn weight-loss practice question (11.94% → "12%") | Arithmetic is correct and the item is a pure calculation with **no** clinical interpretation — it never calls the result normal. The only fair criticism is editorial: the worked value lands above both stated thresholds without comment. Suggest as an improvement (use a value under 7%, or add a follow-up asking what action is indicated), not a defect. |
| NR449 "replication is essential" vs FINER "Novel" | Reconcilable, not a contradiction — the guide's own Novel criterion admits studies that *"confirm or refute previous findings."* The residual issue is that "Replication of previous studies is essential" sits under a slide headed "Review the literature" and reads as a non sequitur. Editorial clarity only. |
| NR327 medroxyprogesterone "15 weeks" vs "every 13 weeks" | Not contradictory — a 15-week duration with 13-week dosing is the standard 2-week grace window. However the guide never explains this, so it reads as an unexplained mismatch. Suggest adding "provides a 2-week grace period." |
| NR228 fat-soluble vitamins "stored ... for 3 to 6 weeks" | Stated identically in two guides; no competing figure anywhere in Week 4. Not a defect. |
| NR228 `Week7_Nutrition_for_Gastrointestinal_Health.md` title vs content | Content matches the title throughout. Not a defect. |

## Verified consistent — do not re-report

- **NR328:** epiglottitis age (2–5 years in both modules); epiglottitis 24-hour antibiotic timeline; pertussis stage durations; RSV precautions; chickenpox precautions; no section-numbering gaps in any Week 2 module.
- **NR327:** postpartum lochia categories; newborn vital-sign ranges across Week 6 guides (HR 120–160, RR 30–60, axillary 97.7–99.5 °F); SGA/AGA/LGA percentile definitions across Weeks 6–7; wet-diaper minimums in `Week5_Breastfeeding.md`.
- **NR228:** food-safety temperatures and storage windows across Week 6 (140 °F hot-hold, 165 °F microwave, 40 °F refrigeration, 2-hour rule, 3–4 day / 3–4 month leftovers); BMI cutoffs; sodium tiers; cholesterol limit; very-low-calorie range.
- **NR449:** all five module manifests account for every section number with no gaps.

## Low-severity formatting notes

Bundle rather than filing individually: `Week7_Dysphagia.md` uses different metadata and manifest conventions from every other guide; `Week7_Nutrition_for_Gastrointestinal_Health.md` drops the "Explore:" prefix from section headings after §3 despite its own manifest listing them with it; four Week 7 nutrition files end with "Module N Completion" instead of "Module Completion"; `Week7_Nursing_Application_GI_Health.md` §10 leaves one nursing-process step unbolded while the other four are bolded; `Week2_Croup_and_Bacterial_Epiglottitis.md`'s manifest lists "Explore: Types of Croup (3)" against an actual heading of "Explore: Types of Croup Syndromes"; `Week2_Cystic_Fibrosis.md` §6 places a figure transcript several items away from the bullet it belongs to.
