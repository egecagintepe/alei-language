# Blind Translation Experiment 01: Five-Stanza Linguistic Audit

**Experiment Date:** 2026-11-05 / 2026-11-06  
**Language Standard Under Test:** Alei v1.1.0-RC (PR #8 overlay)  
**Agent A (Encoder):** ChatGPT (temporary chat; taught Alei v1.1.0 standard, strictly instructed to use only existing canonical vocabulary and report omissions)  
**Agent B (Decoder):** Gemini (independent chat; provided only with the Alei text output of Agent A and Alei v1.1.0 standard; blinded to original Turkish source, notes, and translator omissions)  
**Corpus Scope:** 5 preserved stanzas (K1–K5) of an original 10-stanza Turkish poem.  
**Provenance & Integrity Status:** Real empirical observation of ONE model-pair interaction. Stanzas K6–K10 and full prompt logs were lost due to temporary session termination and are explicitly recorded as pending in `blind-translation-01-pending-manifest.json`. No data has been fabricated.

---

## 1. Executive Summary & Experimental Methodology

The primary objective of this experiment was to test whether Alei v1.1.0 can transmit nuanced human literary meaning across independent cognitive agents when the encoder is strictly restricted to verified canonical vocabulary.

### Key Empirical Findings:
1. **Severe Lexical Bottleneck Forced Information Omission:** Agent A, when denied permission to coin new words, routinely dropped critical qualitative, adverbial, and relational modifiers (e.g., "sometimes", "direction", "opposite ends", "third night").
2. **Grammatical Underspecification Caused Systemic Guessing:** Where Alei lacked distinct morphology for voice (transitive vs. middle/inchoative), state vs. event (open vs. opening), or scope (conditional vs. concessive), Agent B was forced to guess between plausible readings.
3. **LLM Self-Confidence Is Dangerously Uncalibrated:** Gemini reported subjective confidence levels of ~95–99% while simultaneously noting structural ambiguities or picking single narrow interpretations of heavily ambiguous sentences. Such confidence scores are uncalibrated self-reports and must never be treated as validation metrics.

---

## 2. Traceability Matrix: 12 Observed Linguistic Cases

The following table documents each observed case of semantic friction or meaning loss, classifying the root causes:
- **(a) Encoder Omission:** Source information dropped by Agent A due to vocabulary scarcity or structural difficulty.
- **(b) Alei Grammar/Lexicon Deficiency:** Missing morphological markers, undefined valency frames, or missing lexical roots in canonical Alei v1.1.0.
- **(c) Decoder Misparsing/Guessing:** Agent B misconstruing syntax or arbitrarily resolving ambiguities without textual support.
- **(d) Contextual Uncertainty:** Inherent ambiguity of unanchored pronouns or zero-anaphora arguments.

| ID | Verbatim Alei Excerpt | Original Source Intent (TR) | Agent B Back-Translation (TR) | Primary Causes | Severity | Proposed Remediation | Review State |
|---|---|---|---|---|---|---|---|
| C01 | `Lüra fal ve.` | Kapı açık (The door is open) | Kapı açık | (b), (c) | Medium | Distinguish stative predicates from eventive nouns; define predicative participle/stative marker (e.g. `fali` or `ve` predicative role). | Observed single pair |
| C02 | `Vel ne va nesalen.` | Yol kaybolmayacak (The path will not be lost/disappear) | Yol kaybetmeyecek / Yol kaybolmayacak (Uncertain subject role) | (a), (b) | High | `nesalen` is strictly transitive (`Agent loses Patient`). Define middle/inchoative voice or intransitive root distinction. | Observed single pair |
| C03 | `Nave ri növi lürana. Teli lüra fal ve.` | Dokuz kapıdan yedisi... Yalnızca o kapı açık | Dokuz kapının yedisi... Sadece kapı açık | (b), (c) | High | Formalize quantifier partitives (`X ri Y`), numeral noun agreement (singular vs plural), and scope of focus particle `teli`. | Observed single pair |
| C04 | `Ena pira da lüfaren deiran. Eli ne da liren deiran.` | Çocuk düşen yıldızı görmüştü; o [daha önce hiç] görmemişti... | Çocuk düşen yıldızı gördü. O yıldızı görmedi. | (a), (b) | High | Distinguish experiential perfect negation ("never seen") from simple past negation (`ne da`); define prenominal participial derivation. | Observed single pair |
| C05 | `Mei ne da belemen. Mei da hüvaren.` | Saymadım / hesaplamadım; [düşen yıldızı] aradım | Hesaplamadım. Aradım. (Object lost) | (a), (d) | Medium | Anaphoric object pronoun or overt zero-object licensing rule so decoders do not hallucinate or lose thematic roles. | Observed single pair |
| C06 | `Sira pemar el da yelen ke miraven.` | Çünkü bazen kaybolan ışık da yön göstermeye yardım edebilirdi | Çünkü parlaklık da yardım edebilirdi | (a), (b) | Critical | 4 distinct details lost: "bazen" (frequency adverb), "kaybolan" (participle), "yön" (spatial direction), "göstermek" (predicate). Propose temporal/spatial roots. | Observed single pair |
| C07 | `Mei ne da yelaren Mei ri siman liman lo. Mei da yelaren liman lo.` | Taştaki hatamı yazmadım; taşa yazdım... | Taşta yazmadım; taşa yazdım... | (a), (b) | High | Disambiguate `lo` (in/at vs. on a surface); define direct/indirect object retention in coordinated clauses. | Observed single pair |
| C08 | `Davi samel da pürelen vümar ta.` | İkisi aynı köprüye zıt uçlardan vardı | İki kişi aynı köprüye ulaştı | (a), (b) | High | Spatial vector "from opposite ends" unencoded. Introduce reciprocal/opposite spatial relation terms (`polar / zıt`). | Observed single pair |
| C09 | `Elina ne da vesen: “Ne vürelen!” ... “Şe Sai vürelen, aremen!”` | Geçme demediler; geçsen bile dön dediler | "Geçme!" demediler... "Eğer geçersen, dön!" dediler | (b), (c) | Critical | Concessive ("even if" / geçsen bile) conflated with conditional (`şe` / if). Introduce explicit concessive marker or compound. | Observed single pair |
| C10 | `Meina da nivaren. Lüra fal ve. Lia Meina ne da avelen.` | Üçüncü gece bekledik. Kapı açıktı, ama girmedik. | Gece bekledik. Kapı açık. Ama girmedik. | (a), (b) | High | Missing ordinal numeral ("third"); stative tense mismatch (past eventive `da nivaren` vs tenseless `fal ve`). | Observed single pair |
| C11 | `Ena nerav.` | Yanlış bir yerin haritası / temsili | Bir temsil / model | (a), (b) | High | `nerav` denotes abstract model/structure; not geographical map. "Untruth/falsity of representation" cannot be expressed without predicative syntax. | Observed single pair |
| C12 | `Meina da sülari.` | Şaşırmıştık / dehşete düşmüştük (We were astonished) | Şaşırdık / korktuk | (b), (c) | Medium | Canonical `sülari` is quality "şaşkın". Verify whether `da` marks past state ("we were surprised") or inchoative change of state ("we became surprised"). | Observed single pair |

---

## 3. In-Depth Linguistic Deconstructions & Minimal Pairs

### Case 1: `Lüra fal ve.` — Stative Predicate vs. Instrumental Action
- **Observed String:** `Lüra fal ve.`
- **Canonical Status:** `fal` is root `roots:32` ("açılma eylemi / opening action"). `ve` is associative postposition ("ile / with").
- **Analysis:** In Alei v1.0, nominal predicates require a quality or nominal head (`Mei süli.`). Using an action noun + postposition (`fal ve`, literally "opening-action with") is a colloquial calque attempting to mirror "with opening = open". However, it does not distinguish:
  1. *Stative present:* "The door is open" (Durum)
  2. *Resultative past:* "The door has been opened" (Sonuç)
  3. *Inchoative:* "The door is opening / becoming open" (Süreç)
  4. *Habitual/Instrumental:* "The door functions with an opening action"
- **Minimal Pair Contrast:**
  - Standard candidate: `Lüra fal ve.` (Ambiguous colloquial state)
  - Proposed morphological resolution: `Lüra fali.` (Using approved quality derivation suffix `-i` on root `fal` -> *fali* = open/açık).
  - Proposed dynamic verbal contrast: `Lüra da falen.` (The door opened).

### Case 2: `Vel ne va nesalen.` — Valency and Missing Middle/Inchoative Voice
- **Observed String:** `Vel ne va nesalen.`
- **Canonical Status:** `nesalen` is derived verb from root `nesal` (`roots:525`, "kaybetme / losing"). Its documented valency is transitive: `[Agent] nesalen [Patient-an]` (e.g. `Mei nesalen tüvanan` = I lose the tool).
- **Analysis:** Placing `vel` (way/path) in the subject position without an object produces a syntactic clash. Does the path actively lose something (`Vel nesalen [X]`), or does the path become lost (`Vel nesalen` as inchoative/passive)?
- **Minimal Pair Contrast:**
  - Canonical transitive: `Mei da nesalen velan.` (I lost the path — Subject: Agent, Object: Path).
  - Unmarked ambiguous: `Vel da nesalen.` (Ill-formed or ambiguous: Did the path lose something?).
  - Proposed middle/passive voice candidate: `Vel da se-nesalen.` or particle-marked `Vel da nesalen ro.` (The path was lost / disappeared).

### Case 3: `Nave ri növi lürana. Teli lüra fal ve.` — Quantification, Partitives, and Focus Scope
- **Observed String:** `Nave ri növi lürana. Teli lüra fal ve.`
- **Analysis:**
  1. *Numeral + Plural agreement:* v1.0 is ambiguous on whether cardinal numerals take singular stems (`növi lüra`) or plurals (`növi lürana`). Cross-linguistic efficiency favors singular (`növi lüra`), while Turkish permits singular and English requires plural.
  2. *Partitive construction:* `nave ri növi lürana` ("seven of nine doors") relies on genitive `ri`.
  3. *Focus scope of `teli`:* In `Teli lüra fal ve`, does `teli` (only) scope over `lüra` (only the doors, not the windows), over the numeral (only [one/these] door[s]), or over the predicate (the door is only open, not unlocked)?
- **Minimal Pair Contrast:**
  - Nominal focus: `Teli lüra fal ve.` (Only the door is open; other things are not).
  - Cardinal focus: `Teli nave lürana fal ve.` (Only seven doors are open).
  - Predicate focus: `Lüra teli fal ve.` (The door is only open [barely cracked]).

### Case 4: `Ena pira da lüfaren deiran. Eli ne da liren deiran.` — Experiential Negation vs. Simple Past
- **Observed String:** `Ena pira da lüfaren deiran. Eli ne da liren deiran.`
- **Analysis:**
  - In Turkish, "hiç görmemişti" carries experiential perfect aspect (in his/her lifetime, not once had the event occurred).
  - Canonical Alei `ne da liren` encodes simple past negation: "did not see". It lacks aspectual quantification ("never / hiç").
  - Prenominal verb modifier `lüfaren deiran` (falling star) treats an uninflected verb as a participial adjective, which is outside the documented grammar of v1.0.
- **Minimal Pair Contrast:**
  - Simple past negative: `Eli ne da liren deiran.` (He did not see the star [on that occasion]).
  - Proposed experiential negative: `Eli ne fa liren deiran deiran-el.` or `Eli ne liren el-orai.` (He has never seen the star).

### Case 9: Concessive ("Even if") vs. Conditional ("If")
- **Observed String:** `“Şe Sai vürelen, aremen!”`
- **Analysis:**
  - Agent A used `şe` (conditional particle: "if / eğer").
  - Source intent: "Geçsen bile dön!" (Concessive conditional: "Even if you cross, return!").
  - Semantic difference:
    - Conditional: If you cross (you might not), then return.
    - Concessive: Even granting that you cross (which you may well do), you must still return.
- **Minimal Pair Contrast:**
  - Pure conditional: `Şe Sai vürelen, aremen.` (Eğer geçersen dön.)
  - Proposed concessive candidate: `Şe-el Sai vürelen, aremen.` or `Lia Sai vürelen, aremen.` (Geçsen bile dön.)

---

## 4. Evaluation of Model Self-Confidence & Calibration

In the experiment, Agent B (Gemini) attached an estimated confidence score of **95–99%** to its back-translation.

### Why This Score Is Empirically Uncalibrated:
1. **Masked Ambiguities:** In Case 02 (`Vel ne va nesalen`), Gemini selected "Yol kaybolmayacak" without indicating that `nesalen` is structurally transitive.
2. **Ignored Information Gaps:** In Case 06 (`Sira pemar el da yelen ke miraven`), Gemini reported high confidence despite four missing core semantic components.
3. **No Risk-Adjusted Abstention:** Current LLMs default to confident completion rather than calibrated epistemic abstention.

### Proposed Alei Calibration Rubric (Scale 0–3):

| Level | Designation | Operational Definition | Target Criterion |
|---|---|---|---|
| **0** | **Hallucinated Certainty** | High subjective confidence (>90%) on ambiguous, underspecified, or grammatically conflicting input. | Defect; penalize in evaluations. |
| **1** | **Uncertain Guess** | Medium confidence (50–89%); produces a translation but notes possible alternative readings. | Baseline acceptable for informal chat. |
| **2** | **Calibrated Structural Parsing** | Accurately identifies the single supported reading OR explicitly enumerates the 2–3 valid syntactic parses. | Standard required for linguistic tools. |
| **3** | **Disciplined Epistemic Abstention** | Formally flags missing arguments, underspecified aspect, or unanchored referents, and states what evidence is needed to resolve them. | Gold standard for high-fidelity evaluation. |

---

## 5. Methodological Protocols for Independent Blind Evaluation

To ensure future evaluations meet scientific standards:
1. **Prompt Isolation:** Evaluator models must receive ONLY the source-language string and pinned standard documentation. Never provide translator notes, glosses, or source reference texts in the same session.
2. **No Pre-Trained Contamination:** Gold benchmark texts must be novel, unpublished creative writing, not well-known public literature.
3. **Reproducibility:** Session parameters (temperature, model snapshot, system prompt hash) must be recorded in machine-readable JSONL.

