# Blind Translation Experiment 01: Five-Stanza Linguistic Audit (Audited L5.1 Edition)

**Experiment Date:** 2026-11-05 / 2026-11-06  
**Language Standard Under Test:** Alei v1.1.0-RC (PR #8 overlay)  
**Agent A (Encoder):** ChatGPT (temporary chat; taught Alei v1.1.0 standard, instructed to use only existing canonical vocabulary and report omissions)  
**Agent B (Decoder):** Gemini (independent chat; provided only with the Alei text output of Agent A and Alei v1.1.0 standard; blinded to original Turkish source, notes, and translator omissions)  
**Corpus Scope:** 5 preserved stanzas (K1–K5) of an original 10-stanza Turkish poem.  
**Provenance & Integrity Status:** Real empirical observation of ONE model-pair interaction. Stanzas K6–K10 and full prompt logs were lost due to temporary session termination and are explicitly recorded as pending in `blind-translation-01-pending-manifest.json`. No data has been fabricated.

---

## 1. Executive Summary & Critical Audit Findings

The primary objective of this experiment was to test whether Alei v1.1.0 can transmit nuanced human literary meaning across independent cognitive agents when the encoder is restricted to verified canonical vocabulary.

### Exhaustive Linguistic Audit Findings:
1. **Severe Lexical Bottleneck Forced Information Omission:** Agent A, when denied permission to coin new words, dropped critical qualitative, adverbial, and relational modifiers (e.g., "sometimes", "direction", "opposite ends", "third night").
2. **Cascading Model Hallucination on Lexical Stems:** Because Agent A lacked grounded real-time lexicon lookup, it substituted phonotactically plausible Alei roots under entirely false semantic glosses. Crucially, Agent B (Gemini), blinded to the Turkish source, uncritically echoed Agent A's false meanings:
   - **`Vürel / Vürelen`:** Agent A used `vürelen` as "geçmek" (to cross). Canonical status: `roots:502` `Vürel` is strictly **"korku" (fear)**; `lexemes:787` `Vürelen` is **"korkmak" (to fear)**.
   - **`Arem / Aremen`:** Agent A used `aremen` as "dönmek" (to return). Canonical status: `roots:434` `Arem` is strictly **"düşünce" (thought / mental reflection)**; `lexemes:757` `Aremen` is **"düşünmek" (to think)**. Canonical return is `roots:656` `Nelar` -> `Nelaren`.
   - **`Nave`:** Agent A used `nave` as cardinal "dokuz" (nine). Canonical status: `roots:476` `Nave` is **"şehir" (city)**! Canonical nine is `functions:1108` **`Vüni`**.
   - **`Dei`:** Agent A used `dei` as "yıldız" (star). Canonical status: `roots:454` `Dei` is strictly **"gün" (day)** (antonym to `Mora` = night). Star in Alei is `nüra` (`roots:458`) or `nüra-pemar`.
   - **`Nivar / Nivaren`:** Agent A used `nivaren` as "gecelemek / gece beklemek" (nightwatch). Canonical status: `roots:721` `Nivar` is **"öğrenme" (learning)**; `lexemes:921` `Nivaren` is **"öğrenmek" (to learn)**.
3. **Grammatical Underspecification Caused Systemic Guessing:** Where Alei lacked distinct morphology for voice (transitive vs. middle/inchoative) and scope (conditional vs. concessive), decoders had to guess between conflicting readings.
4. **LLM Self-Confidence Is Dangerously Uncalibrated:** Gemini reported subjective confidence levels of ~95–99% while simultaneously guessing on fabricated lexical definitions and unresolved ambiguities.

---

## 2. Traceability Matrix: 12 Observed Linguistic Cases

| ID | Verbatim Alei Excerpt | Original Source Intent (TR) | Agent B Back-Translation (TR) | Canonical Truth & Lexical Audit | Primary Causes | Severity |
|---|---|---|---|---|---|---|
| C01 | `Lüra fal ve.` | Kapı açık (The door is open) | Kapı açık | `fal` is opening action (`roots:32`); `ve` is associative postposition ("ile"). Lacks tense/state distinction. | Grammar gap | Medium |
| C02 | `Vel ne va nesalen.` | Yol kaybolmayacak | Yol kaybetmeyecek / Yol kaybolmayacak | `nesalen` is transitive (`roots:525` Agent loses Patient). Missing patient creates valency clash. | Grammar gap | High |
| C03 | `Nave ri növi lürana. Teli lüra fal ve.` | Dokuz kapıdan yedisi... Yalnızca o kapı açık | Dokuz kapının yedisi... Sadece kapı açık | **Severe Lexical Error:** `Nave` is "şehir" (city, `roots:476`), not nine! Nine is `Vüni` (`functions:1108`). Agent A wrote "Şehrin yedi kapısı". | Lexical hallucination | Critical |
| C04 | `Ena pira da lüfaren deiran. Eli ne da liren deiran.` | Çocuk düşen yıldızı görmüştü; o [daha önce hiç] görmemişti... | Çocuk düşen yıldızı gördü. O yıldızı görmedi. | **Lexical Error:** `Dei` is "gün" (day, `roots:454`), not star! Star is `nüra`. Also lacks experiential aspect marker ("hiç görmemişti"). | Lexical error + Aspect gap | High |
| C05 | `Mei ne da belemen. Mei da hüvaren.` | Saymadım / hesaplamadım; [düşen yıldızı] aradım | Hesaplamadım. Aradım. | `belemen` (count) and `hüvaren` (search) are transitive (`roots:446`, `524`). Unexpressed zero-object drops patient. | Pragmatic omission | Medium |
| C06 | `Sira pemar el da yelen ke miraven.` | Çünkü bazen kaybolan ışık da yön göstermeye yardım edebilirdi | Çünkü parlaklık da yardım edebilirdi | 4 details lost: "bazen" (frequency), "kaybolan" (inchoative), "yön" (spatial path `vel`), "göstermek" (predicate). | Lexical scarcity | Critical |
| C07 | `Mei ne da yelaren Mei ri siman liman lo. Mei da yelaren liman lo.` | Taştaki hatamı yazmadım; taşa yazdım... | Taşta yazmadım; taşa yazdım... | Disambiguation of `lo` (substrate vs location); omission of object `siman` in second clause. | Grammar / Preposition | High |
| C08 | `Davi samel da pürelen vümar ta.` | İkisi aynı köprüye zıt uçlardan vardı | İki kişi aynı köprüye ulaştı | "From opposite ends" unencoded. Proposed suffix `-ra` in draft was uncanonized; canonical ablative is postposition `fi`. | Vocabulary gap | High |
| C09 | `Elina ne da vesen: “Ne vürelen!” ... “Şe Sai vürelen, aremen!”` | Geçme demediler; geçsen bile dön dediler | "Geçme!" demediler... "Eğer geçersen, dön!" dediler | **Double Lexical Hallucination:** `Vürelen` = fear (`roots:502`), NOT cross! `Aremen` = think (`roots:434`), NOT return! The canonical text says: "Korkma demediler; korksan bile düşün dediler!" Also conflates conditional (`şe`) with concessive ("even if"). | Lexical hallucination + Scope gap | Critical |
| C10 | `Meina da nivaren. Lüra fal ve. Lia Meina ne da avelen.` | Üçüncü gece bekledik. Kapı açıktı, ama girmedik. | Gece bekledik. Kapı açık. Ama girmedik. | **Lexical Error:** `Nivaren` is to learn (`roots:721`), NOT nightwatch! Night is `Mora` (`roots:455`). Missing ordinal ("third"). | Lexical error + Grammar gap | High |
| C11 | `Ena nerav.` | Yanlış bir yerin haritası / temsili | Bir temsil / model | `nerav` denotes model/structure (`roots:681`). "Falsity of representation" cannot be expressed without predicative modifier. | Lexical scarcity | High |
| C12 | `Meina da sülari.` | Şaşırmıştık / dehşete düşmüştük | Şaşırdık / korktuk | Canonical `sülari` is quality "şaşkın" (`roots:482`). Tense marker `da` marks past state ("we were surprised"). | Stative aspect | Medium |

---

## 3. In-Depth Linguistic Deconstructions & Canonical Solutions

### Case C09: `Elina ne da vesen: "Ne vürelen!" ... "Şe Sai vürelen, aremen!"`
- **Observed Surface:** `Elina ne da vesen: "Ne vürelen!" ... "Şe Sai vürelen, aremen!"`
- **Canonical Meanings of Roots:**
  - `Ves / Vesen`: to say / speak (`roots:448`, `lexemes:770`).
  - `Vürel / Vürelen`: fear / to fear (`roots:502`, `lexemes:787`). Not "cross"!
  - `Arem / Aremen`: thinking / to think (`roots:434`, `lexemes:757`). Not "return"!
- **The True Canonical Interpretation:**
  - In Alei canon, this sentence literally translates to:
    $$\text{Onlar "Korkma!" demediler; "Eğer korkarsan, düşün!" dediler.}$$
    *(They did not say: "Do not fear!" They said: "If you fear, think!")*
- **The Human Intent in the Turkish Source:**
  - The human poet wrote: "Geçme demediler; geçsen bile dön dediler."
  - Agent A mistakenly grabbed `vürelen` (imagining it sounded like "pass/cross") and `aremen` (imagining it meant "return").
  - Agent B, hallucinating without a lexicon check, echoed "geçme" and "dön".
- **Linguistic Lesson for Agent Pair Systems:**
  - Model confidence is completely decoupled from lexicon grounding.
  - Blind translation cannot be verified without independent lexicon AST validation.

### Case C03: `Nave ri növi lürana.`
- **Observed Surface:** `Nave ri növi lürana.`
- **Lexical Reality:**
  - `Nave` is `roots:476`: "şehir" (city).
  - Nine is `Vüni` (`functions:1108`).
  - Seven is `Növi` (`functions:1106`).
- **Correction:** To express "seven of the nine doors", canonical Alei requires:
  $$\text{Vüni lüra ri növi lürana} \quad (\text{nine door GEN seven door-PL})$$

### Case C02: `Vel ne va nesalen.` (Transitivity & Middle Voice)
- **Observed Surface:** `Vel ne va nesalen.`
- **Lexical Reality:** `nesalen` is transitive: `[Agent] nesalen [Patient-an]` (e.g., `Mei da nesalen velan` = I lost the path).
- **Valency Clash:** Having an inanimate Patient (`Vel`) in subject position without an object creates a defective transitive clause.
- **Remediation:** RFC-2026-001 proposes a middle voice marker (`ro` or disambiguated `se`) to promote Patient to subject and suppress the external Agent.

---

## 4. Methodological Protocols for Future Benchmarks

1. **Strict Lexical Grounding:** Every generated word must pass automated lookup against the canonical registry (`records(version)`). Words not attested or not derived via productive rules must trigger immediate `unknown_lexeme` rejection.
2. **Deterministic Pre-Parsing:** Evaluation pipelines must reject sentences before passing them to decoder models if they fail AST valency checks.
3. **No Metric Inflation via LLM Self-Reports:** Gemini's 98% self-confidence score on hallucinatory sentences proves that model self-evaluations must never be used as scientific validation metrics.
