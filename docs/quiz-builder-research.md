# Quiz Builder — Research Findings and Change Plan

**Date:** 2026-07-26
**Why:** We built an NCLEX *item* writer without ever researching *test assembly and delivery*. Every defect found this session — answer-position skew, guessable match ordering, stale letter references — is standard psychometric hygiene that testing programs solved decades ago. This is that research, plus what we changed and what we deliberately did not.

Four parallel research passes: test assembly, feedback design, platform delivery, psychometric QC. Plus direct inspection of **Elsevier Adaptive Quizzing (EAQ)**, which Chris had open live.

---

## 1. What the research validated

**Key-position balancing is the real industry standard.** Attali & Bar-Hillel (2003, *J. Educational Measurement* 40:2) document it as explicit policy at ETS (SAT/GRE) and Israel's NITE — *"the testing establishment has almost uniformly adopted key balancing."* Not pure randomization, not rigid quotas.

**Examinees genuinely exploit position.** In an embedded experiment (~4,000 examinees, 161 items), moving an option into a middle slot raised its selection rate ~30% relatively (p<.0001). Blind guessers pick middle positions 75–80% of the time. Fagley (1987) found positional bias plus test-wiseness explained 18% of score variance.

**Our skew was worse than the human baseline, and different in kind.** Human writers over-use *middle* positions (70–80% B/C). Ours piled onto *option A* at 55–100% — an LLM artifact of writing the key first. Same defect class, opposite direction.

**Elaborated feedback beats bare correctness, with a ceiling.** Van der Kleij (2015) meta-analysis: elaborated d=0.49, correct-answer-only d=0.32, bare right/wrong d=0.05. Ryan et al. (2020) RCT: explaining each *distractor* beats right/wrong, but deeper conceptual elaboration adds nothing beyond that. So one crisp sentence per distractor is the sweet spot.

**Immediate per-item feedback is fine.** Ryan et al. (2024) RCT found no significant learning difference vs. delayed, with immediate slightly more efficient. Our current design stands.

---

## 2. What the research contradicted — defects we had introduced

**Naturally-ordered options must never be shuffled.** NBME's Item-Writing Guide, under *Flaws Related to Irrelevant Difficulty*: numeric options should be listed in numeric order; illogical order causes confusion. Our shuffler had turned `Level 1/2/3/4` into `Level 1/4/2/3` and an infant-feeding cloze into `6 months / 4 months / 9 months`. **Fixed**; both the shuffler and linter now protect quantity series.

The distinction that matters: an option that **is** a quantity stays ordered; a clinical vignette that merely **contains** a number stays shuffled. Ordering vignettes by incidental age would itself become a cue. Of 14 candidates flagged by a naive numeric scan, only 2 were real.

**Rationales must not cite options by letter.** We had 13 doing so, and position balancing had silently invalidated every one. **Fixed**; now a hard linter error, since option order is deliberately unstable.

**Exact round-robin may be too rigid.** Monte Carlo analysis of real SAT/PET keys shows their balancing already produces *less* variance than chance. A strict A/B/C/D rotation would be its own detectable pattern. Ours deals round-robin then breaks runs, which is looser than strict rotation — acceptable, but worth revisiting if a pattern ever becomes visible.

---

## 3. Where the evidence is thin — flagged honestly

- **Run-length limits.** The only source is Bar-Hillel & Attali (2002), retrievable at abstract level only. Suppressing runs is real, but "cap at 2" is a sensible engineering default, *not* a citable standard. Do not claim NBME or NCSBN mandate it.
- **Retake reshuffling.** No study directly tests whether reshuffling prevents order-memorization in self-study. Adjacent literature (retrieval practice, CAT exposure control) points that way. Treat as a design default under uncertainty.
- **Bullets vs. prose in rationales.** Followed from Mayer's segmenting principle and every commercial product's convention, but no controlled test of formatting-only was found. **Notably we went further than the benchmark: Elsevier's rationales are prose, not bulleted.**

  *Resolved in practice (2026-07-26):* after shipping, Chris's unprompted reaction was that it is "SO MUCH easier to read," and he named the bullets specifically — "before it was just a mess of text inline." A sample of one, but it is the user the artifact exists for, and it settles a decision that the literature could not. Keep the bulleted `whyNot` list.
- **"The answer is usually C."** Folk version of a real effect. The bias is toward middle positions generally, direction varying with option count. Do not encode a single-letter rule.

---

## 4. Elsevier EAQ — observed directly

**Architecture.** One question at a time, server-side: `launchAssessment` → `getNextQuestion` → `submitEolsQuestion` → repeat. The answer key is **never in the client**. Supporting calls (`recommender/isbn/{isbn}/taxonomies`, `assessment/mastery/{isbn}/topic/{id}`) show an item bank tagged to a textbook taxonomy with per-topic mastery driving selection. Not replicable without a backend — **our quizzes ship all answers in the HTML**, which is worth knowing.

**Confidence rating instead of submit.** The commit buttons are **"Not Sure"** and **"Confident."** This splits results four ways rather than two:

| | Confident | Not Sure |
|---|---|---|
| **Correct** | solid | *guessed right — the dangerous one* |
| **Wrong** | *misconception* | known gap |

A percentage score hides both italicised cells. This is the single best idea observed, and it is essentially Anki's self-rated recall.

**Rationale format.** 88 words, 4–6 sentences, **one idea per sentence**: key rationale, then one sentence per distractor, then a closing. No option letters. Card constrained to ~992px in an 1889px viewport at 20px/28px type. Every option marked ✓/✗, with the user's own pick still distinguishable. Identical layout whether right or wrong.

**Ours by comparison:** 61 words but only 2.1 sentences — mean 29 words/sentence, longest 37, max 68, with semicolons doing paragraph work. **We are not too verbose; we are under-punctuated.**

Also present: `Report content error` per item, and a `Study Mode` toggle.

---

## 5. Change plan

### Done this session
- Balance key position; break runs >2 (`balance_answers.py`)
- Fix identity-mapped and clustered match/matrix rows
- Strip and forbid option-letter references in rationales
- Protect naturally-ordered quantity series from shuffling
- Linter: format mix, answer position, run length, row order, letter refs, natural order

### High priority — next
| Change | Why | Effort |
|---|---|---|
| **Restructure rationales**: one idea per sentence; distractors as separate lines | The measured difference vs. EAQ. Content is already right | Medium — mechanical re-punctuation, lintable (flag sentences >28 words) |
| **Confidence capture** ("Not Sure" / "Confident") | Four-quadrant results; surfaces guessed-right and misconceptions | Medium — engine + results screen |
| **Constrain rationale column width**, add ✓/✗ per option, correct/incorrect badge | Copies EAQ's readability directly | Low |
| **Flag-for-review + navigator grid** | Universal across every platform studied | Low |
| **Tutor / Timed mode toggle** | UWorld's documented pattern; answers the timer request cleanly | Low–Medium |
| **Timer with staged warnings** (2 min / 30 s / 10 s auto-submit) | Canvas New Quizzes' concrete cadence | Low |
| **"Retake missed only"** | Canvas *Build on Last Attempt* + Archer's reset model both converge here. Better than reshuffling — you re-drill 30 items, not 124 | Medium — needs `localStorage` |

### Medium
- Per-item time tracking surfaced in review
- Option strike-through (UWorld's signature practice aid)
- Report-a-bad-item mechanism — we found garbled Wong-Baker values and a misspelled "patent ductus arterioles" this session
- Linter: negative-stem-not-marked (34 real hits), vague frequency terms (40, needs tuning)

### Deliberately skipped
- **Images in rationales** — breaks the self-contained offline single-file property; our image transcripts are already text
- **Peer/percentile comparison** — needs a population; faking it would mislead
- **True CAT** — needs IRT-calibrated items; even ATI's flagship uses fixed pre-equated forms
- **Clang and mixed-numeric linter checks as drafted** — ~226 flags, mostly noise. A check that fires constantly is one people learn to ignore
- **Proctoring / lockdown** — out of scope for self-study

---

## 6. The transferable lesson

Three defects this session were invisible to per-module agents because **each linted only its own items**. Distribution problems — answer position, run length, format mix — only exist at the whole-quiz level. And the aggregate can lie: 55% option A sounded survivable; the actual sequence opened with **twelve consecutive A's**, which is what a person notices.

Check distributions *and* sequences, at assembly, mechanically.
