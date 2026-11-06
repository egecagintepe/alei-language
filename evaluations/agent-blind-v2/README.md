# Alei Agent-to-Agent Blind Evaluation Protocol (v2)

**Status:** Framework and Fixtures Complete; Evaluation Results Pending Real Independent Agent Sessions  
**Target:** Rigorous empirical testing of Alei semantic translatability, morphological analyzability, and learning transfer between independent AI models.

---

## 1. Research Objectives & The Four Evaluation Tracks

This evaluation suite is designed to test our primary scientific hypothesis: **Can an independent second model (Agent B) reliably decode novel, well-formed Alei expressions using standard grammar documentation alone, without exposure to the encoder's source text or private thoughts?**

The suite provides 42 held-out cases divided across four controlled tracks:

1. **Track 1: Fixed-Lexicon Sentence Encoding & Back-Translation (12 cases)**  
   Turkish source -> Agent A (strictly canonical v1.1 words) -> Alei text -> Agent B -> Turkish & English back-translation. Tests how much source information is preserved under closed-vocabulary constraints.
2. **Track 2: Productive Form Decoding (10 cases)**  
   Grammatical compounds and productive derivations (`orai-el`, `fali`, `nasel-nerav`) presented to Agent B without an explicit dictionary of the novel forms. Tests morphological decomposition and semantic field inference.
3. **Track 3: Open-Semantic Description Decoding (10 cases)**  
   Novel hyphenated `HEAD-ROLE-VALUE` expressions including valid combinations, ambiguous double-specifications, and negative control type clashes (`meyar-li-hokar`, `jajaya-li-reş`). Tests semantic type safety and correct rejection.
4. **Track 4: Definition Learning and Transfer (10 cases)**  
   Agent B receives a newly specified experimental root definition (e.g., `Pol` = opposite, `Gor` = direction) exactly once, followed by unseen grammatical sentences. Tests one-shot lexical acquisition and compositional transfer.

---

## 2. Strict Blinding and Anti-Contamination Rules

To prevent benchmark leakage and invalid validation claims:

1. **Context Isolation:** Agent B must be a fresh, independent chat session. NEVER share conversation history, translator reasoning, omission logs, or source texts with Agent B.
2. **Gold Answer Insulation:** The file `evaluations/agent-blind-v2/gold-answers.jsonl` contains the private evaluation key. It must NEVER be fed to Agent A or Agent B.
3. **Prompt Purity:** Prompts in `cases.jsonl` provide only the necessary context and blinded input string.
4. **No Fictional Scores:** If model outputs have not been collected from a live session, the results are explicitly marked `not_run`. Never simulate or hallucinate benchmark scores.

---

## 3. Nontechnical User Protocol: How to Run the Experiment

Follow these simple steps to conduct an independent evaluation session:

### Step 1: Prepare Agent A (The Encoder)
1. Open a fresh chat session in **ChatGPT** (or another frontier LLM).
2. Upload or paste the official Alei standard: `adsiz_dil_acik_anlam_standardi_v1_0.md` and `docs/release-v1.1.0.md`.
3. Instruct Agent A: *"You are translating into the human language Alei. You must use ONLY attested canonical v1.1 vocabulary. If a concept cannot be expressed honestly, note the omission explicitly."*
4. Provide the source text. Save Agent A's output Alei text and note any reported omissions.

### Step 2: Prepare Agent B (The Decoder)
1. Open a fresh, separate chat session in **Gemini** (or a different model instance).
2. Upload ONLY the standard grammar files. **DO NOT upload the original Turkish source or Agent A's notes.**
3. Run `python evaluations/agent-blind-v2/run_blind_eval.py --print-prompts` to generate blinded test queries.
4. Paste the blinded prompt for each case into Agent B's chat.
5. Record Agent B's verbatim output and self-reported confidence.

### Step 3: Import and Score Results
1. Create a `responses.jsonl` file with format:
   ```json
   {"case_id": "BLIND-T1-001", "model": "gemini-1.5-pro", "output": "I saw the sweet fruit.", "evaluation_status": "evaluated"}
   ```
2. Run the report generator:
   ```bash
   python evaluations/agent-blind-v2/run_blind_eval.py --import-responses responses.jsonl --report evaluation-report.md
   ```

---

## 4. Multi-Dimensional Scoring Rubric

Responses are scored across four independent dimensions (Scale 0–3):

| Dimension | Description | Level 0 | Level 1 | Level 2 | Level 3 (Gold) |
|---|---|---|---|---|---|
| **D1: Propositional Retention** | Preservation of core Agent/Action/Patient relations. | Inverted roles or hallucinated arguments. | Core verb preserved, object blurred. | All core roles faithfully identified. | Complete semantic nuance captured. |
| **D2: Tense/Aspect/Polarity** | Accurate decoding of `da`, `va`, `ne`, `du`, `fa`, `su`. | Polarity reversed or tense omitted. | Tense correct, aspect confused. | Tense and polarity fully preserved. | Fine aspectual distinctions maintained. |
| **D3: Morphological Analyzability** | Decomposition of novel compounds and derivations. | Unanalyzed or opaque guessing. | Partial stem identified. | Both roots identified correctly. | Full compositional structure recovered. |
| **D4: Epistemic Calibration** | Appropriateness of confidence vs ambiguity. | Confident certainty on invalid/ambiguous input. | Uncalibrated guess without noting friction. | Correctly notes ambiguity or friction. | Disciplined abstention / flags type clash. |

---

## 5. Current Fixture Summary

- **Total Cases:** 42 held-out cases
- **Track 1:** 12 cases (Literal, logical, spatial, aspectual, social, minimal pairs)
- **Track 2:** 10 cases (Novel transparent compounds and derived forms)
- **Track 3:** 10 cases (Type safety checks, negative controls, invalid roots/roles)
- **Track 4:** 10 cases (One-shot definition transfer of proposed roots `Pol`, `Gor`, `Bav`, etc.)
- **Execution Status:** Ready for external model testing (`not_run` pending live sessions).
