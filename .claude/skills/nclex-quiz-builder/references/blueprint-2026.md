# 2026 NCLEX-RN Blueprint, NCJMM, and Terminology

Reference for classifying items. The exact `cat` and `lvl` strings below are what
the quiz engine groups on for the results-screen coverage table — copy them verbatim.

## Client Needs categories (effective April 1, 2026)

Percentages are unchanged from the 2023 plan. Use these as the target blend; the
assembler prints actual coverage against these ranges.

| `cat` value (use verbatim) | Major category | Target % |
|---|---|---|
| `Management of Care` | Safe & Effective Care Environment | 15–21% |
| `Safety & Infection Prevention and Control` | Safe & Effective Care Environment | 10–16% |
| `Health Promotion & Maintenance` | Health Promotion & Maintenance | 6–12% |
| `Psychosocial Integrity` | Psychosocial Integrity | 6–12% |
| `Basic Care & Comfort` | Physiological Integrity | 6–12% |
| `Pharmacological & Parenteral Therapies` | Physiological Integrity | 13–19% |
| `Reduction of Risk Potential` | Physiological Integrity | 9–15% |
| `Physiological Adaptation` | Physiological Integrity | 11–17% |

**What changed in 2026 (don't propagate the old terms):**
- "Safety and Infection Control" → **"Safety and Infection Prevention and Control"**.
- "Substance abuse" → **"substance misuse"** (use patient-centered, non-stigmatizing language throughout).
- New emphasis on **unbiased treatment and equal access to care** regardless of
  culture/ethnicity, sexual orientation, gender identity, and gender expression.
  Reflect this in scenarios where relevant (e.g., affirming, inclusive phrasing).

## Cognitive level (`lvl`)

Use `Application`, `Analysis`, or `Evaluation`. Most items should be Application or
higher — the candidate must interpret data and decide, not just recall a fact. The
assembler warns if fewer than 80% are at Application+.

- **Application** — apply a known principle to a specific client situation.
- **Analysis** — interpret/compare data, distinguish among competing explanations, prioritize.
- **Evaluation** — judge whether an intervention worked or which evidence best supports a decision.

## NCJMM — the six cognitive skills (Layer 3)

An unfolding case study is **exactly six linked items**, one per step, evolving the
same patient. Label each item's stem `CASE (n/6) <step>.` (or `CASE 2 (n/6) ...` for
a second case in the same file). The assembler verifies each case group has all six.

1. **Recognize cues** — pick out the relevant/abnormal findings from the data.
2. **Analyze cues** — link cues to the client's situation; form the likely explanation.
3. **Prioritize hypotheses** — rank the most likely / most urgent problem.
4. **Generate solutions** — decide which actions and expected outcomes fit (often the **bowtie**).
5. **Take action** — implement the priority interventions (often a SATA).
6. **Evaluate outcomes** — judge whether the interventions worked.

Map item types to steps naturally: Recognize → matrix/SATA highlight-style; Analyze →
single-best; Prioritize → single-best; Generate solutions → bowtie; Take action →
SATA; Evaluate → single-best. A **bowtie** itself spans steps: the central condition
= analyze/prioritize, the two actions = take action, the two parameters = evaluate.

## Prioritization frameworks (for first/priority/most-important items)

When an item asks for the first or priority action, the keyed answer must be defensible
by an explicit framework — state it in the rationale (`rat`):
- **ABCs** (airway → breathing → circulation) — outranks everything.
- **Maslow** — physiologic needs before psychosocial.
- **Safety / risk reduction**.
- **Acute over chronic; unstable over stable.**
- **Assess before intervene** (unless an ABC emergency demands immediate action).

## Accuracy rule — the guide is the tested content

**Key items to what the guide teaches.** Roughly 90% of Chris's quiz and exam questions come
straight from the Edapt modules (his professors don't write them; a smaller share comes from
the textbook). So the guide's content *is* the exam content. Write items that prepare him for
that exam.

This means: **do not substitute current evidence-based practice for the guide's version, and
do not skip a topic because the guide lags current standards.** If the guide teaches cool mist
for croup, bronchodilators for RSV, palivizumab as RSV prophylaxis, or a particular evidence
hierarchy — key those, because that is what he will be asked. Silently "correcting" the guide
produces a quiz that trains the wrong answer.

Two narrow exceptions:
- **Blatantly wrong or unsafe** content — don't key it. Flag it to Chris instead.
- **A bad capture** — garbled, truncated, or self-contradictory extraction. Key the guide's
  clearest/dominant version if you safely can, and flag the ambiguity.

When the guide is merely *less current* than today's practice, key the guide's version and may
add one short "current practice now favors X" clause to the rationale — the keyed answer still
follows the guide. Always report any discrepancy you noticed in your summary.
