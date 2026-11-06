# RFC-2026-001: Valency, Voice, Stative Predicates, and Scope Clarification in Alei

- **RFC Identifier:** RFC-2026-001
- **Author:** Alei Language Engineering Team (Autonomous Phase L5)
- **Status:** `PROPOSAL` / `EXPERIMENTAL` (Requires explicit human language-owner decision)
- **Target Version:** Post-v1.1.0 Evaluation (Proposed Candidate for Future RFC Review)
- **Supersedes:** None
- **Dependencies:** v1.0 standard (`adsiz_dil_acik_anlam_standardi_v1_0.md`), v1.1.0 overlay (PR #8)

---

## 1. Motivation and Problem Statement

During the first blind-translation experiment between independent AI models (Agent A: ChatGPT, Agent B: Gemini) on stanzas K1–K5 of an original Turkish poem, significant literary meaning was lost or altered. The linguistic post-mortem (`docs/research/blind-translation-01-five-stanza-audit.md`) established that this loss was not merely an encoder hallucination, but the direct result of four fundamental structural gaps in Alei v1.0/v1.1:

1. **Underspecified Verbal Valency and Lack of Voice Marking:** Verbs of change (such as `nesalen` = lose) are strictly transitive (`[Agent] nesalen [Patient-an]`). When an object is omitted or when an inanimate patient is placed in subject position (`Vel ne va nesalen`), the grammar fails to indicate whether the subject is an agent losing something or an inchoative patient disappearing/getting lost.
2. **Ambiguity Between Stative Predicates and Eventive Actions:** Phrases like `Lüra fal ve` attempt to express the stative property "the door is open" by compounding an action noun (`fal` = opening action) with an associative marker (`ve` = with). This obscures the contrast between present states, past states, resultative achievements, and progressive actions.
3. **Conflation of Conditional and Concessive Scope:** Alei provides only `şe` ("if"). Concessive conditionals ("even if you cross / geçsen bile"), which presuppose the likelihood of the condition rather than its hypothetical doubt, are collapsed into pure conditionals, distorting imperative warnings into conditional permissions.
4. **Unlicensed Imperative and Quotative Speech Acts:** In natural literary dialogue and poetry, commands (`Aremen!` / Return!) and direct quotes (`Elina da vesen: "Ne vürelen!"`) are natural human utterances, yet current parsing grammar categorizes them as ungrammatical fragments due to the absence of explicit pronoun subjects.

This RFC outlines four principled, minimal-friction proposals designed to resolve these gaps using Alei's existing root inventory and phonological constraints, while preserving 100% backward compatibility with archived v1.0 and v1.1.

---

## 2. Proposal 1: Middle/Inchoative Voice Particle `se`

### 2.1 The Linguistic Problem
In Alei v1.0, verbs derived from roots with `-en` inherit the root's argument structure. For transitive roots, omitting the direct object (`-an`) creates unresolvable ambiguity:
- `Mei da nesalen tüvanan.` -> *I lost the tool.* (Transitive: Subject = Agent, Object = Patient)
- `Vel da nesalen.` -> *The path lost [something]?* OR *The path was lost / disappeared?*

Natural human languages resolve this through middle voice (Turkish: *-il/-in*, e.g., *kaybetmek* -> *kaybolmak*), reflexive markers (French: *se perdre*, Spanish: *perderse*), or ergative/unaccusative alternating verbs (English: *the ice melted*).

### 2.2 Proposed Mechanism: Analytic Voice Particle `se`
Rather than introducing synthetic infixation or mutating root definitions, we propose an analytic middle/inchoative particle **`se`**, placed immediately preceding the main verb (and following tense/aspect markers):

$$\text{Subject} + [\text{ne}] + [\text{da} \mid \text{va}] + [\text{du} \mid \text{fa} \mid \text{su}] + [\mathbf{se}] + \text{Verb}$$

- **Semantic Role:** Promotes the Patient/Theme to subject position and suppresses the external Agent role.
- **Morphological Form:** `se` (open CV syllable, phonotactically legal in Alei, distinct from pronoun `sai` and particle `su`).
- **Phonological Safety Check:** No homophony with existing grammatical particles. `su` is habitual aspect; `şe` is conditional; `se` is middle/reflexive.

### 2.3 Positive and Negative Minimal Pairs
- **Pair 1A (Transitive):**
  - *Alei:* `Mei va nesalen velan.`
  - *Gloss:* `1SG FUT lose-VB path-ACC`
  - *Translation:* I will lose the path.
- **Pair 1B (Middle/Inchoative with `se`):**
  - *Alei:* `Vel ne va se nesalen.`
  - *Gloss:* `path NEG FUT MID lose-VB`
  - *Translation:* The path will not be lost / will not disappear.
- **Pair 1C (Ungrammatical/Ambiguous Baseline):**
  - *Alei:* `*Vel ne va nesalen.`
  - *Analysis:* Ambiguous or defective; missing transitive patient.

---

## 3. Proposal 2: Systematic Stative Quality Derivation via Suffix `-i`

### 3.1 The Linguistic Problem
Translators struggling to express stative adjectives ("open", "closed", "broken") have resorted to calquing nouns with postposition `ve` (`lüra fal ve` = *door opening with*). This construction lacks tense, aspect, and clear grammatical categorization.

### 3.2 Proposed Mechanism: Regularized Quality Derivation on Action Roots
Alei standard v1.0 §8.2 already defines the productive suffix **`-i`** to derive qualities from nominal roots ending in a consonant:
- `sül` (goodness) + `-i` -> `süli` (good / well)
- `sülar` (surprise / awe) + `-i` -> `sülari` (surprised / astonished)

We propose regularizing this rule for physical action/state roots:
- Root `fal` (opening action / açılma) + `-i` -> **`fali`** (open / açık [quality])
- Root `vür` (crossing action / geçiş) + `-i` -> **`vüri`** (crossed / passable)

When used in nominal predicates, these derived qualities take standard pre-predicate tense markers:
- `Lüra fali.` -> *The door is open.* (Present state)
- `Lüra da fali.` -> *The door was open.* (Past state)
- `Lüra da falen.` -> *The door opened.* (Past dynamic event)

### 3.3 Semantic Contrast Table

| Construction | Alei Form | English Meaning | Turkish Meaning | Semantic Type |
|---|---|---|---|---|
| Dynamic Event | `Lüra da falen.` | The door opened. | Kapı açıldı. | Eventive Achievement |
| Stative Present | `Lüra fali.` | The door is open. | Kapı açık. | Stative Property |
| Stative Past | `Lüra da fali.` | The door was open. | Kapı açıktı. | Past Stative |
| Inchoative Change | `Lüra da se falen.` | The door became open. | Kapı açılmaya başladı. | Inchoative Event |

---

## 4. Proposal 3: Concessive Conditional Compound `şe-el` ("Even if")

### 4.1 The Linguistic Problem
In poetic and rhetorical discourse, concessive conditionals ("Even if you cross, return!") assert that the conclusion holds regardless of the condition's truth value. Canonical Alei only possesses `şe` ("if / eğer"), which implies uncertainty and turns an urgent exhortation into a contingent conditional.

### 4.2 Proposed Mechanism: Analytic Compound `şe-el`
In Alei v1.0, `şe` is "if" and `el` is the additive focus particle ("also / even / dahi"). We propose combining them into the transparent compound **`şe-el`** (or pre-clausal `şe ... el`):

$$\mathbf{şe\text{-}el} + \text{Clause}_1 + [,] + \text{Clause}_2$$

- **IPA:** `/ʃe.el/`
- **Glosses:**
  - `şe-el`: CONC (even if / -se bile)
- **Learnability:** Highly transparent; composed entirely of two certified v1.0 morphemes.

### 4.3 Minimal Pair Comparison
- **Pure Conditional:**
  - *Alei:* `Şe Sai vürelen, aremen.`
  - *Meaning:* If you cross, return. (You might not cross; but if you do, return).
- **Concessive Conditional:**
  - *Alei:* `Şe-el Sai vürelen, aremen!`
  - *Meaning:* Even if you cross, return! (You may well cross, but regardless, you must return!).

---

## 5. Proposal 4: Imperative Speech Acts and Quotative Framing

### 5.1 The Linguistic Problem
Alei v1.0 sentence grammar strictly mandates an overt subject pronoun (`mei`, `sai`, `eli`, etc.). Consequently:
1. Bare verbs functioning as commands or pleas (`Aremen!` / Return!) fail parser validation.
2. Direct quotations following speech verbs (`Elina da vesen: "..."`) fail validation because punctuation and embedded clause boundaries are blocked.

### 5.2 Proposed Grammar Extensions
1. **Subjectless Imperative/Hortative:**
   A bare infinitive/verb stem with an optional vocative or exclamation mark is formally parsed as an **imperative speech act** with an implied 2nd-person addressee (`[Addressee: sai/saina]`):
   - `Aremen!` -> Parse: `{'construction': 'imperative', 'verb': 'aremen', 'addressee': 'implied_2nd_person', 'negation': false}`
   - `Ne vürelen!` -> Parse: `{'construction': 'imperative', 'verb': 'vürelen', 'addressee': 'implied_2nd_person', 'negation': true}`
2. **Direct Quotative Frame:**
   The speech verb `vesen` (to say/speak) followed by a colon and quotation marks (`vesen: "..."`) is recognized as a quotative matrix frame:
   - Parse: `{'construction': 'quotative', 'speaker': 'elina', 'verb': 'vesen', 'quote_content': '...'}`

---

## 6. Backward Compatibility & Non-Canonical Governance Notice

> [!IMPORTANT]
> This document is an **RFC proposal** generated as part of L5 linguistic engineering. In strict adherence to CODEX Principles 3 and 4:
> - None of these proposed rules (`se`, `fali`, `şe-el`, subjectless imperatives) are part of official Alei canon until explicitly approved and ratified by the repository owner in an official Decision Record (`AD-2026-xxx`).
> - The software implementation in L5 must treat these constructions as **experimental/proposed**, reporting them cleanly with appropriate status annotations without contaminating canonical v1.0 or v1.1.0 regression tests.

---

## 7. High-Value Owner Decision Summary

If the language owner wishes to adopt this RFC in a future release, the decision packet consists of:
1. **Decision AD-2026-003 (Voice):** Adopt analytic particle `se` for middle/inchoative/reflexive voice modulation.
2. **Decision AD-2026-004 (Stative Derivation):** Adopt regular `-i` quality derivation on action roots (e.g., `fal` -> `fali`).
3. **Decision AD-2026-005 (Concessives):** Adopt `şe-el` for "even if" concessive conditionals.
4. **Decision AD-2026-006 (Imperatives & Quotes):** Adopt subjectless imperative syntax and quotative punctuation frames.
