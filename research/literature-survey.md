# Academic Literature Survey: Compositionality, Language Transmission, and Constructed Languages

**Author:** Alei Language Engineering & Research Initiative  
**Date:** 2026-11-06  
**Status:** Working Research Survey (Foundation for ACL/EMNLP Benchmark Proposals)

---

## 1. Introduction and Scope

Alei represents an unusual object of study in natural language processing and computational linguistics: an **open, human-first constructed literary language** featuring a dual architecture consisting of (1) a naturalistic phonotactically constrained root core with agglutinative morphology, and (2) an analytical **transparent semantics layer** allowing explicit perceptual and relational decomposition (`HEAD-ROLE-VALUE`).

Unlike toy synthetic languages designed solely for vector-space simulations, Alei is constrained by human cognitive ergonomics (penultimate stress, phoneme harmony, 28-letter Latin orthography, literary poetic cadence). At the same time, because Alei has minimal representation in public web-scraped pre-training corpora, it offers a pristine experimental substrate for investigating **in-context grammar acquisition, compositional generalization, and cross-model semantic transmission**.

This survey situates Alei within five key areas of contemporary NLP research.

---

## 2. Key Research Domains

### 2.1 ConlangCrafter and Computational Constructed Languages (ACL 2026)
- **Key Themes:** Automated and semi-automated conlang construction frameworks; evaluation of linguistic consistency in model-generated grammars; balance between grammatical productivity and cognitive learnability.
- **Critical Findings:** Purely LLM-generated languages tend to degenerate into relexified English or structurally unstable pidgins unless constrained by rigorous phonotactic filters, explicit valency registries, and formal derivation schemas.
- **Relevance to Alei:**
  - Alei avoids the "machine-pidgin" trap by maintaining a human-designed, immutable core (archived v1.0 standard, SHA-256 verified) and requiring explicit human language-owner decisions (AD-2026-001/002) for canonical adoption.
  - Alei provides an ideal evaluation ground for ConlangCrafter-style validation harnesses: can LLM agents adhere to strict conlang phonotactics without hallucinations?

### 2.2 Compositional Generalization: SCAN and COGS
- **Foundational Works:**
  - *SCAN (Lake & Baroni, 2018):* Systematic compositional generalization from primitive command sequences to held-out complex compositions (`jump around right twice`).
  - *COGS (Kim & Linzen, 2020):* A compositional benchmark based on human semantic representations, testing structural transformations (e.g., active-to-passive, modifier attachment, novel verb argument frames).
- **Critical Findings:** Modern transformer architectures frequently achieve near-perfect in-distribution accuracy while failing catastrophically on systematic out-of-distribution compositional splits (e.g., encountering a known verb in an unseen argument structure).
- **Relevance to Alei:**
  - Alei's transparent semantics (`meyar-ro-yenar-li-reş-ze-selim`) provides a human-readable equivalent of COGS logical forms.
  - In Alei, novel combinations of familiar roots (e.g., `orai-el` = time-also -> sometimes; `nasel-nerav` = place-model -> map) test whether models can infer the semantic class of transparent compounds without memorized lexical lookup.

### 2.3 In-Context Grammar Induction: Explicit Learning in Machine Translation (EMNLP 2025)
- **Key Themes:** Evaluating how effectively frontier large language models induce grammar rules, morphological paradigms, and lexicon tables provided strictly within the context prompt, without weight adaptation.
- **Critical Findings:** While frontier models can rapidly utilize in-context glossaries for lexical substitution, they frequently struggle with:
  1. Affix-conditioned morphophonemics.
  2. Valency mismatches (treating transitive verbs as inchoative without voice morphology).
  3. Strict negation scope across clause boundaries.
- **Relevance to Alei:**
  - Alei serves as a clean "zero-pretraining" benchmark. Because models have not memorized billions of Alei sentences during pre-training, all morphological segmentation (`-en`, `-i`, `-na`, `-an`) and syntax rules must be induced purely from in-context specifications.
  - The observed ChatGPT -> Gemini experiment (`docs/research/blind-translation-01-five-stanza-audit.md`) provided empirical proof that in-context translators omit critical aspectual/directional modifiers when confronted with lexical gaps.

### 2.4 Morphological Compositional Generalization
- **Key Themes:** The tension between root economy (storing fewer primitives) and expressive power (deriving complex concepts).
- **Linguistic Background:** Natural human languages balance synthetic morphological complexity (e.g., Turkish agglutination, Inuktitut polysynthesis) with analytic syntax (e.g., Mandarin, English).
- **Relevance to Alei:**
  - Alei adopts a disciplined middle ground: a conservative core of 270 attested roots, productive suffixation for parts of speech (`sül` -> `süli` [quality], `sülen` [verb], `sülna` [plural]), and analytical compounding for semantic expansion.
  - Testing whether AI models can correctly parse `base + derivation` without leaking false senses is a central benchmark task.

### 2.5 Emergent Communication & Cross-Model Transmission Bottlenecks
- **Key Themes:** Iterated learning (Kirby, 2001); semantic drift in multi-agent communication games; information transmission through communicative bottlenecks.
- **Critical Findings:** When Agent A encodes thought $T$ into language string $S$, and Agent B decodes $S$ back into thought $T'$, any structural ambiguity in the intermediate language $S$ leads to systematic hallucination or information loss unless the receiver is calibrated to report uncertainty.
- **Relevance to Alei:**
  - In the 5-stanza blind translation experiment, Gemini assigned subjective confidence scores of 95–99% even while misinterpreting omitted objects and unexpressed spatial vectors.
  - Alei offers an ideal medium to study **epistemic calibration**: training and evaluating decoders to output calibrated abstention when intermediate syntax is genuinely ambiguous.

---

## 3. Summary of Identified Theoretical Gaps

| Domain | Current Academic Focus | Alei Benchmark Contribution |
|---|---|---|
| **Synthetic Conlangs** | AI-generated toy dialects without human phonology. | Human-first constructed literary language with naturalistic constraints. |
| **Compositionality** | Artificial grid-world commands (SCAN). | Naturalistic literary, philosophical, and everyday human expressions. |
| **MT Induction** | Low-resource natural languages with noisy pre-training presence. | Pinned, zero-leakage in-context standard with verified byte hashes. |
| **Epistemic Calibration** | Confidence scores on multiple-choice QA. | Semantic ambiguity detection and disciplined abstention in linguistic translation. |

