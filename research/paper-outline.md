# Paper Outline: Evaluating Compositional Transmission and Epistemic Calibration in an Open Human-First Constructed Language

**Working Title:** *Alei: Evaluating Compositional Transmission and Epistemic Calibration in an Open Human-First Constructed Language*  
**Target Venue:** ACL / EMNLP 2026 / 2027 (Long Paper, Main Conference)  
**Authors:** Alei Language Research Working Group  
**Status:** Working Draft Paper Structure (No Fabricated Data or Premature Claims)

---

## Abstract
- **Context:** Large language models exhibit remarkable in-context translation abilities, yet struggle with systematic compositional generalization and epistemic calibration when operating in low-resource or novel linguistic systems.
- **Problem:** Existing benchmarks (e.g., SCAN, COGS) rely either on synthetic grid-world commands or artificially relexified English, lacking the naturalistic phonotactics, morphological richness, and literary expressiveness required for human communication.
- **Proposal:** We introduce **Alei**, an open, human-first constructed language combining an agglutinative 270-root naturalistic core with an analytical transparent semantics layer (`HEAD-ROLE-VALUE`).
- **Empirical Protocol:** We evaluate cross-model semantic transmission across heterogeneous frontier models (GPT-4o, Gemini 1.5, Claude 3.5) in a strictly blinded transmission bottleneck, evaluating proposition retention, morphological decomposition, and epistemic uncertainty handling.
- **Key Findings:** Models achieve high lexical reconstruction but exhibit severe calibration failures under syntactic ambiguity, assigning 95–99% confidence to underspecified structures while dropping critical aspectual and directional modifiers.
- **Conclusion:** We release Alei-Bench (42 held-out balanced evaluation cases, typed AST evaluation suite, and human baseline protocol) as a public benchmark for linguistic compositionality and calibrated communication.

---

## 1. Introduction
- The challenge of compositional generalization beyond pre-training memory.
- Why human-centric conlangs provide a superior evaluation testbed compared to toy synthetic grammars.
- Overview of Alei: design philosophy, immutable core standard (v1.0), and governed evolution.
- Summary of core contributions:
  1. The formal specification and typed AST implementation of Alei.
  2. Alei-Bench: A 6-task benchmark measuring compositionality, cross-model transmission, and epistemic calibration.
  3. Empirical post-mortem of real model-pair transmission friction.
  4. Open-source, reproducible tooling and held-out test fixtures.

---

## 2. Related Work
- **Compositional Generalization:** SCAN (Lake & Baroni 2018), COGS (Kim & Linzen 2020).
- **Constructed Languages & NLP:** ConlangCrafter (ACL 2026), Esperanto/Lojban in NLP corpora.
- **In-Context MT Induction:** Explicit Learning in LLMs (EMNLP 2025).
- **Emergent Communication & Transmission Bottlenecks:** Iterated learning, signaling games, communicative drift.
- **Epistemic Calibration in NLP:** Expected Calibration Error, abstention in generation.

---

## 3. The Alei Language Architecture
- **Phonotactics & Orthography:** 28 Latin letters, 8 vowels, penultimate stress, CV/CVC syllable economy.
- **Morphological Derivations:** Regular affixation (`-i` quality, `-en` verb, `-na` plural, `-an` marked patient).
- **Syntactic Word Order:** Flexible SVO / SOV constituent ordering, nominal/verbless predicates.
- **Transparent Semantics Layer:** Analytical `HEAD-ROLE-VALUE` compounding with ontological constraints.
- **Formal AST & Valency Schema:** Deterministic parsing, argument frames, and ambiguity categorization.

---

## 4. The Cross-Model Blind Transmission Protocol
- **Asymmetric Transmission Bottleneck:** Agent A (Encoder) $\rightarrow$ Alei String $\rightarrow$ Agent B (Decoder) $\rightarrow$ Reconstruction.
- **Zero-Contamination Rules:** Strict isolation of encoder reasoning, translator omission reports, and source text.
- **Rubrics:** Propositional retention, morphological analyzability, tense/aspect survival, and calibration scoring.

---

## 5. Experimental Setup & Benchmark Tasks
- **Task 1:** Unseen Open-Semantic Interpretation.
- **Task 2:** Novel Morphological Combination Decoding.
- **Task 3:** Cross-Model Propositional Transmission.
- **Task 4:** Epistemic Calibration & Ambiguity Handling.
- **Task 5:** Thematic Role & Modifier Preservation.
- **Task 6:** Human Pilot Learnability Study.

---

## 6. Empirical Findings & Qualitative Analysis
- Analysis of observed transmission friction (the 5-stanza blind translation case study).
- Where meaning is lost: voice/valency shifts, stative vs. dynamic conflation, concessive vs. conditional scope.
- Quantitative calibration analysis: LLM overconfidence under structural ambiguity.
- Failure mode taxonomy (Types I–V).

---

## 7. Discussion & Linguistic Implications
- The tension between root economy and descriptive precision.
- How analytical transparent semantics mitigates vocabulary bottlenecks.
- Lessons for human language learning and cognitive conlang design.

---

## 8. Limitations, Ethics, and Governance
- Linguistic caveats: synthetic vs. natural conlang trade-offs.
- Provenance and CC BY 4.0 / Apache-2.0 licensing.
- Prohibition of fabricated results; transparent recording of unrun test splits.

---

## References
*(Comprehensive academic citations across conlangs, compositional generalization, and LLM translation).*

