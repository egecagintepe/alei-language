# Alei-Bench: A Comprehensive Benchmark for Compositional Transmission, Epistemic Calibration, and Human Learnability

**Specification Version:** 1.0.0-PROPOSAL  
**Author:** Alei Language Engineering & Research Initiative  
**Target Conferences:** ACL / EMNLP / COLING 2026–2027  
**Integrity Rule:** No fabricated empirical results. Deterministic parser tests are strictly decoupled from model and human evaluations.

---

## 1. Benchmark Overview & Research Questions

Alei-Bench evaluates cognitive language models and human learners across six core dimensions of linguistic competence:

1. **Task 1: Unseen Compositional Word Interpretation (Open Semantics)**  
   *Research Question:* Can a model correctly identify the semantic class, typical attributes, and physical constraints of novel `HEAD-ROLE-VALUE` expressions without guessing an exact opaque real-world identity?
2. **Task 2: Novel Morphological Combination Decoding**  
   *Research Question:* Given only the pinned morphological rules (`-i`, `-en`, `-an`, `-na`) and root dictionary, can a model reliably segment and interpret novel, unattested compounds and derivations?
3. **Task 3: Cross-Model Asymmetric Semantic Transmission**  
   *Research Question:* When Agent A (Encoder) translates a nuanced human prompt into Alei, how much propositional content can an independent Agent B (Decoder, distinct architecture) reconstruct without access to Agent A's prompt or reasoning?
4. **Task 4: Epistemic Calibration & Ambiguity Handling**  
   *Research Question:* Does a model correctly report ambiguity or abstain when presented with structurally underspecified syntax (e.g. omitted transitive objects, tenseless verbless predicates), or does it express hallucinated certainty (>90%)?
5. **Task 5: Controlled Propositional Information Preservation**  
   *Research Question:* Which semantic features (thematic roles, polarity, tense, aspect, numeral quantification, spatial vectors) degrade most rapidly under communicative bottlenecks?
6. **Task 6: Human Learnability and Cognitive Ergonomics**  
   *Research Question:* How rapidly can human second-language learners acquire Alei's 28-letter phonotactics, core 270 roots, and SVO/SOV constituent ordering compared to synthetic baseline grammars?

---

## 2. Benchmark Architecture & Task Specifications

```
                       ┌──────────────────────────────────────────────┐
                       │           Alei-Bench Core Protocol           │
                       └──────────────────────┬───────────────────────┘
                                              │
         ┌───────────────────┬────────────────┴───────────────────┬───────────────────┐
         ▼                   ▼                                    ▼                   ▼
   ┌───────────┐       ┌───────────┐                        ┌───────────┐       ┌───────────┐
   │  Task 1   │       │  Task 2   │                        │  Task 3   │       │  Task 4   │
   │   Open    │       │Morphology │                        │Cross-Model│       │Epistemic  │
   │ Semantics │       │Decoding   │                        │Transmission│      │Calibration│
   └───────────┘       └───────────┘                        └───────────┘       └───────────┘
```

### Task 1: Unseen Open-Semantic Interpretation
- **Input:** Valid, ambiguous, or invalid hyphenated descriptions (e.g., `meyar-ro-yenar-li-reş-ze-selim-mu-molir`).
- **Hidden Split:** 50 unseen items:
  - 30 valid descriptions combining known classes.
  - 10 ambiguous items (e.g., conflicting color values `li-reş-li-lüven`).
  - 10 negative control invalid items (e.g., type clash `li-hokar`, disabled role `no`).
- **Evaluation Metric:** 
  - *Macro F1* on Validity Classification (`valid` / `ambiguous` / `invalid`).
  - *Constraint Satisfaction Rate (CSR):* Proportion of inferred attributes that match the semantic ontology (`concepts-vnext-proposal.jsonl`).
  - *Epistemic Abstention Score:* Rejection rate on negative controls without hallucinating an identity.

### Task 2: Novel Morphological Combination Decoding
- **Input:** Unseen but grammatically regular compounds and derived words (e.g., `orai-el`, `fali`, `nasel-nerav`, `dei-pemar`, `morven`).
- **Hidden Split:** 60 items balanced across:
  - Part of speech derivation (Root -> Quality `-i`, Root -> Verb `-en`).
  - Case/Number inflection (Plural `-na`, Accusative `-an`).
  - Analytic compounding (Noun-Noun, Noun-Quality, Adverbial).
- **Evaluation Metric:**
  - Exact match on constituent stem recovery.
  - Semantic Field Accuracy (WordNet / ConceptNet hypernym overlap with human gold reference).

### Task 3: Cross-Model Transmission Fidelity
- **Protocol:**
  1. Source Sentence $S_{tr}$ (Turkish / English) fed to Agent A.
  2. Agent A outputs Alei sentence $A_{alei}$ under pinned v1.1.0 lexicon constraints.
  3. $A_{alei}$ (and ONLY $A_{alei}$, with grammar reference) fed to Agent B.
  4. Agent B outputs back-translation $S'_{tr}$.
- **Models Evaluated:** Heterogeneous pairs across distinct model families:
  - GPT-4o $\rightarrow$ Gemini 1.5 Pro
  - Claude 3.5 Sonnet $\rightarrow$ GPT-4o
  - LLaMA-3-70B $\rightarrow$ Claude 3.5 Sonnet
- **Evaluation Metric:**
  - *Encoder Information Ratio ($EIR$):* Proportion of source propositions expressible by Agent A under Alei vocabulary constraints.
  - *Decoder Reconstruction Ratio ($DRR$):* Proportion of encoded propositions successfully recovered by Agent B.
  - *End-to-End Retention ($EER = EIR \times DRR$):* Overall semantic survival rate.

### Task 4: Epistemic Calibration & Uncertainty Handling
- **Dataset:** 40 sentences deliberately balanced between:
  - 20 fully specified, unambiguous sentences.
  - 10 sentences with omitted obligatory arguments (e.g. `Mei da hüvaren.`).
  - 10 sentences with underspecified aspect/tense (e.g. `Lüra fal ve.`).
- **Evaluation Metric:**
  - *Expected Calibration Error (ECE)* between subjective confidence (0–100%) and objective propositional accuracy.
  - *Abstention Quality Score (AQS):* Scoring whether the model explicitly identifies missing arguments rather than inventing them.

### Task 5: Propositional Feature Preservation
- **Granular Evaluation:** Evaluates which grammatical categories survive transmission:
  - Thematic Roles (Agent, Patient, Recipient)
  - Polarity (Affirmative vs. Negative)
  - Tense (Past `da`, Future `va`, Unmarked)
  - Aspect (Progressive `du`, Completed `fa`, Habitual `su`)
  - Modality & Condition (Pure conditional `şe` vs. Concessive `şe-el`)
  - Spatial Relations (Destination `ta`, Location `lo`, Origin `ra`, Opposing vector `pol-ra`)
- **Metric:** Per-category retention percentage.

### Task 6: Human Learnability & Cognitive Ergonomics
- **Methodology (Future Pilot):**
  - 24 human participants (balanced across native agglutinative [Turkish] and non-agglutinative [English] speakers).
  - 3-hour micro-course covering phonology, core 50 roots, and SVO/SOV ordering.
  - Periodic testing: recall of vocabulary, grammaticality judgments on minimal pairs, and reading comprehension speed.
- **Metric:** Error rates, response latency (ms), and subjective cognitive load ratings (NASA-TLX).

---

## 3. Experimental Controls & Anti-Contamination Guarantees

1. **Strict Context Insulation:** Evaluator models must run in clean, zero-history sessions. No shared thread, system prompt caching, or translator notes.
2. **Hidden Test Split:** All benchmark gold answers (`gold-answers.jsonl`) are strictly excluded from public training sets and prompt payloads.
3. **Reproducibility Manifest:** Every evaluation run logs:
   - Git commit hash of Alei standard and benchmark fixtures.
   - Exact model version string (e.g., `gemini-1.5-pro-002`, `gpt-4o-2024-08-06`).
   - Temperature, top-p, seed, and decoding parameters.
4. **Fair Baselines:**
   - *Direct Translation Baseline:* Translating source directly without intermediate Alei bottleneck.
   - *Relexified English Baseline:* Word-for-word substitution conlang without agglutinative morphology or transparent semantics.
   - *Pure Synthetic Baseline:* Toy vector-space language without human phonotactics.

---

## 4. Benchmark Scoring and Failure Analysis Framework

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        Alei-Bench Composite Index                      │
│                                                                        │
│   Score = 0.25*(Task 1 CSR) + 0.25*(Task 2 SemAcc)                     │
│         + 0.30*(Task 3 EER) + 0.20*(Task 4 AQS)                        │
└────────────────────────────────────────────────────────────────────────┘
```

### Categorization of Failure Modes:
- **Type I (Encoder Lexical Deficit):** Concept completely omitted due to missing vocabulary.
- **Type II (Encoder Calque Friction):** Encoder forces an illicit grammatical construction (e.g., prenominal bare verb `lüfaren deiran`).
- **Type III (Decoder Syntactic Misparse):** Decoder fails to parse a valid SVO/SOV clause.
- **Type IV (Decoder Hallucinatory Resolution):** Decoder invents an argument or chooses one reading with unwarranted 99% certainty.
- **Type V (Type Violation):** Semantic role assigned to an invalid ontological category.
