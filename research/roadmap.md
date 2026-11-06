# Alei Academic Research & Publication Roadmap (2026–2027)

**Goal:** Establish Alei as a recognized, rigorous academic benchmark for compositional generalization, in-context language learning, and epistemic calibration in computational linguistics.

---

## Timeline & Phased Milestones

```text
2026 Q4 (Current)        2027 Q1                 2027 Q2                 2027 Q3
  Phase R1 ──────────────► Phase R2 ─────────────► Phase R3/R4 ──────────► Phase R5
  [Pilot & Theory]       [Multi-Model Suite]     [Human Trials & Bench]  [Publication & Release]
```

### Phase R1: Theoretical Grounding & Pilot Audit (Completed — Q4 2026)
- [x] Ingest and audit real empirical ChatGPT $\rightarrow$ Gemini 5-stanza blind translation experiment (`docs/research/blind-translation-01-five-stanza-audit.md`).
- [x] Establish taxonomy of meaning loss (voice/valency, stative predicates, concessives, spatial vectors).
- [x] Implement deterministic typed AST parser, valency register, and non-throwing semantic analyzer.
- [x] Create 42-case balanced, leak-resistant evaluation suite (`evaluations/agent-blind-v2/`).
- [x] Complete academic literature survey (`research/literature-survey.md`) and benchmark design (`research/benchmark-design.md`).

### Phase R2: Multi-Model Transmission Suite Execution (Target: Q1 2027)
- [ ] Run the 42-case evaluation suite across four frontier model families:
  - OpenAI GPT-4o (`gpt-4o-2024-08-06`)
  - Google Gemini 1.5 Pro (`gemini-1.5-pro-002`)
  - Anthropic Claude 3.5 Sonnet
  - Open-weights baseline: Meta LLaMA-3-70B-Instruct
- [ ] Record verbatim responses, calibration scores, and abstention behavior without data contamination.
- [ ] Compute Expected Calibration Error (ECE), Encoder Information Ratio (EIR), and Decoder Reconstruction Ratio (DRR).
- [ ] Publish empirical observations in an open, reproducible research report.

### Phase R3: Human Subject Learnability & Cognitive Trials (Target: Q2 2027)
- [ ] Design IRB-compliant psycholinguistic protocol for human learners (24 participants).
- [ ] Conduct 3-hour micro-course on Alei phonology (28 letters), core 50 roots, and SVO/SOV ordering.
- [ ] Measure vocabulary acquisition speed, reaction latency on grammaticality judgments, and cognitive load (NASA-TLX).
- [ ] Compare human learnability against synthetic baseline grammars lacking phonotactic harmony.

### Phase R4: Alei-Bench Public Packaging & Tooling (Target: Q2 2027)
- [ ] Package `alei-bench` as an installable Python package (`pip install alei-bench`).
- [ ] Provide a zero-configuration CLI runner for custom model evaluation (`alei-bench evaluate --model <model-endpoint>`).
- [ ] Implement an automated, static HTML leaderboard generator for cross-model comparisons.
- [ ] Freeze official benchmark test split v1.0 with cryptographically signed hashes.

### Phase R5: Conference Submission & Public Archiving (Target: Q3 2027)
- [ ] Complete full academic manuscript following `research/paper-outline.md`.
- [ ] Target submissions: **ACL 2027** / **EMNLP 2027** (Long Paper track).
- [ ] Deposit benchmark datasets and reproduction code on Zenodo and Hugging Face Datasets with CC BY 4.0 license.
- [ ] Present findings at international computational linguistics and conlang forums.

---

## Required Research Governance Principles

1. **No Fabricated Evidence:** Benchmark scores must reflect real, logged evaluations from specific model checkpoints. Unrun evaluations remain explicitly marked `not_run`.
2. **Deterministic vs. Generative Separation:** Deterministic software unit tests (`test_l5_engineering.py`) test code correctness; they must never be presented as proof of human language fluency or LLM mastery.
3. **Open Access:** All benchmark fixtures, annotations, and analysis code remain open source under Apache-2.0 and CC BY 4.0.
