# RFC-L6.1: HUMAN-FIRST GENERATIVE GRAMMAR ARCHITECTURE
## Formal Grammar Specification, Linguistic Trade-off Analysis, and Semantic Engine Schema

**Document ID:** RFC-2026-L6.1  
**Status:** Experimental Architecture Specification (L6.1 Hardened)  
**Author:** Antigravity Language Engineering Team  
**Authority:** Aligned with Alei v1.0 Standard and v1.1.0 Owner Adopted Overlay (AD-2026-001/002)  
**Target Repository:** `egecagintepe/alei-language`  
**Working Branch:** `l6/generative-grammar-architecture`  

---

## 1. Executive Summary & Purpose

The L6.1 generative grammar architecture develops the linguistic foundations necessary for Alei to function as an expressive, learnable, and aesthetically coherent **human language**.

This specification directly addresses and corrects the linguistic inconsistencies identified in L6:
1. Canonical additive conjunction is strictly **`ya`** ("and"). The postposition **`ve`** is comitative ("with/together"), never a clause-coordinating conjunction.
2. Canonical comparison is built upon **`peli`** ("more", `functions:1088`) and **`nera`** ("compared with / than", `functions:1089`). The postposition **`fi`** is ablative ("from"), not a comparative marker.
3. The root **`Lavar`** (`roots:488`) denotes "largeness" (yielding quality `lavari` = large/broad), not a general degree intensifier.
4. The root **`Pira`** (`roots:473`) denotes "child", not a grammatical comparative "less".
5. The root **`Tevar`** (`roots:626`) denotes "meeting / encounter", not gratitude. Canonical gratitude is the interjection **`Elai`** (`functions:1074`).
6. Unregistered tokens (`sam`, `den`, `pür`) are strictly quarantined: `sam` is an unadopted experimental proposal for universal quantification; `pür` is replaced by canonical **`sira`** ("because"); `den` is unrecorded and replaced by canonical coordination `ya`.
7. Subordinate clauses with **`ke`** are formally disambiguated into Verb Complement Clauses, Subject Relatives, and Object Relatives.

---

## 2. Core Linguistic Domains & Systematic Trade-off Analysis

### Domain 1: Verb Valency & Argument Structure

#### 1.1 Linguistic Problem
Alei requires an unambiguous argument structure that distinguishes Agent/Patient from Experiencer/Stimulus, Recipient, and Destination without creating double-object ambiguity.

#### 1.2 Registered Valency Frames
- **Transitive Verbs:**
  - `nesalen` (roots:525): Roles: `[Agent, Patient]`. Obligatory: `[Agent, Patient]`. Strictly transitive; omitting patient creates a valency defect.
  - `falen` (roots:516): Roles: `[Agent, Patient]`. Obligatory: `[Agent, Patient]`.
  - `dumen` (roots:517): Roles: `[Agent, Patient]`. Obligatory: `[Agent, Patient]`.
  - `sileven` (roots:508): Roles: `[Agent, Patient]`. Obligatory: `[Agent, Patient]`.
- **Perceptual & Experiential Verbs:**
  - `liren` (roots:514): Roles: `[Experiencer, Stimulus]`. Obligatory: `[Experiencer, Stimulus]`.
  - `vürelen` (roots:502): Roles: `[Experiencer, Stimulus]`. Obligatory: `[Experiencer]`, Optional: `[Stimulus]`.
- **Cognitive & Volitional Verbs:**
  - `aremen` (roots:434): Roles: `[Experiencer, Proposition]`. Obligatory: `[Experiencer]`.
  - `saelen` (roots:430): Roles: `[Experiencer, Patient]`. Obligatory: `[Experiencer, Patient]`.
- **Ditransitive Verbs:**
  - `davelen` (roots:527): Roles: `[Agent, Patient, Recipient]`. Recipient marked by `ta`.
  - `vesen` (roots:448): Roles: `[Agent, Recipient, Message]`. Recipient marked by `ta`.
- **Intransitive Verbs:**
  - `şürelen` (roots:659): Posture verb. Roles: `[Agent]`. Accusative patients are strictly rejected as unexpected arguments.
  - `avelen`, `pürelen`, `nelaren`: Motion verbs. Roles: `[Agent, Destination]`. Destination marked by `ta`.

#### 1.3 Recipient Marking
Recipient / Destination is consistently marked with postposition **`ta`**:
`Mei da davelen tüvanan sain ta.` (I gave the book to you).

---

### Domain 2: Voice System (Transitive, Intransitive, Reflexive, Middle/Passive, Inchoative)

#### 2.1 Distinguishing Four Non-Active Voices
1. **Reflexive Voice:** Agent acts upon oneself. Formed by co-referential accusative personal pronoun matching the subject (`Mei da miraven mein`, `Eli da liren elin`). Requires zero new morphemes; prevents collision with `samel` (friend).
2. **Passive Voice:** External Agent is suppressed; Patient is promoted to Subject. Regular verbal infix **`-il-`** (`Lüra da falilen` = The door was opened). Licensed strictly on transitive verbs; unlicensed on intransitives like `şürelen`.
3. **Middle Voice:** Spontaneous event without external agent. Analytic particle **`vo`** (`Vel ne va vo nesalen` = The path does not lose itself / get lost).
4. **Inchoative Voice:** Spontaneous transition into a state. Auxiliary `avelen` + stative quality (`Lüra da avelen fali` = The door became open). In this voice, the subject is the **Theme** undergoing change.

---

### Domain 3: State vs. Event vs. Completed-Result (Aktionsart & Aspect)

1. **Static State:** Nominal/Quality zero-copula predicate: `Lüra fali.` (The door is open.)
2. **Dynamic Process:** Progressive marker `du` + verb: `Lüra du falen.` (The door is opening.)
3. **Punctual Past Event:** Past marker `da` + verb: `Lüra da falen.` (The door opened.)
4. **Resultative / Completed State:** Completed aspect `fa` + verb: `Lüra fa falen.` (The door has opened / is opened.)

---

### Domain 4: Conditionals, Concessives, and Counterfactuals

1. **Hypothetical Condition (Real Conditional):** `şe` + unmarked/present:
   `Şe Sai avelen, Mei va miraven sain.` (If you come, I will help you.)
2. **Concessive Condition:** `şe-el` (even if):
   `Şe-el Sai vürelen, aremen!` (Even if you fear, think!)
3. **Counterfactual Past (Unreal Conditional):** Antecedent has past `da` + Consequent has past-future `da va`:
   `Şe Sai da avelen, Mei da va miraven sain.` (If you had come, I would have helped you.)
4. **Standalone Future-in-the-Past:** `da va` in a simple clause without a `şe` condition represents intended/unfulfilled future from a past perspective, NOT a counterfactual past:
   `Mei da va avelen.` (I was going to come / intended to come.)

---

### Domain 5: Negation Scope & Quantified Expressions

#### 5.1 Mathematical Quantifier Disambiguation
- **Universal Affirmative:** `sam lera da avelen` (All people arrived) -> Formula: $\forall x (\text{Person}(x) \to \text{Arrived}(x))$.
  *(Status: `sam` is an unadopted experimental proposal; canonical Alei has a lexical gap for universal quantifier).*
- **Partial Negation (NOT ALL):** `ne sam lera da avelen` (Not all people arrived) -> Formula: $\neg \forall x (\text{Person}(x) \to \text{Arrived}(x))$.
  *Note: Mathematically, $\neg \forall x$ does not entail existential $\exists x$.*
- **Total Negation (NONE):** `ne ena lera da avelen` (Not one person arrived = nobody arrived) -> Formula: $\forall x (\text{Person}(x) \to \neg \text{Arrived}(x))$.
  *Canonical formulation using canonical numeral `ena` (one).*

---

### Domain 6: Relative Clauses & Embedded Propositions with `ke`

To avoid treating all `ke` occurrences as relative clauses, the grammar formally disambiguates three structures:

1. **Verb Complement Clause:**
   Preceded by a communicative, epistemic, or modal verb (`vesen`, `naelen`, `yelen`, `ünaren`):
   $$\text{Matrix Verb} + \mathbf{ke} + [\text{Embedded Proposition}]$$
   - `Eli da vesen ke tüvan süli.` (He said that the book was good.)
2. **Subject Relative Clause (Post-nominal `ke`):**
   Preceded by a Head Noun; followed immediately by a finite verb + optional object:
   $$\text{Head Noun} + \mathbf{ke} + [\text{VP}]$$
   - `Lera ke sileven tüvanan da avelen.` (The person who reads the book arrived; Head `Lera` is Agent of `sileven`.)
3. **Object Relative Clause (Post-nominal `ke`):**
   Preceded by a Head Noun; followed by an overt embedded subject + transitive verb without an object:
   $$\text{Head Noun} + \mathbf{ke} + [\text{Subject} + \text{Transitive Verb}]$$
   - `Tüvan ke lera sileven fali.` (The book that the person reads is open; Head `Tüvan` is Patient of `sileven`.)

---

### Domain 7: Conjunctions and Coordination

1. **Additive Conjunction:** **`ya`** ("and", `functions:1082`). Joins words, phrases, and independent clauses:
   `Mei da lümalen lüran ya Sai da falen elin.` (I repaired the door and you opened it.)
   Coordinate clauses retain independent tenses, aspects, polarities, and argument frames.
2. **Comitative Postposition:** **`ve`** ("with / together", `functions:1079`). Modifies a nominal entity; **cannot** be used as a coordinating conjunction:
   `Mei avelen Sai ve.` (I am going with you.)
3. **Adversative Conjunction:** **`lia`** ("but / however", `functions:1083`).
4. **Causal Conjunction:** **`sira`** ("because", `functions:1084`).

---

### Domain 8: Canonical Comparison (`peli ... nera`)

Canonical comparison in Alei is established by Standard §4.9 and §8.6:
- **`peli`** = "more / to a higher degree" (`functions:1088`).
- **`nera`** = "compared with / than" (`functions:1089`).

#### 8.1 Comparison Structures
1. **Full Comparative:**
   $$\text{Subject} + \mathbf{peli} + \text{Quality} + \text{Standard} + \mathbf{nera}$$
   - `Eli peli süli Mei nera.` (He is better compared with me.)
   - `Mei ri lem peli lavari Sai ri lem nera.` (My home is larger compared with your home - §4.9).
2. **Short Comparative:**
   $$\text{Subject} + \mathbf{peli} + \text{Quality}$$
   - `Eli peli süli.` (He is better.)
   - `Eli ri lem peli lavari.` (His home is larger - Standard Ex. 44).
3. **Ablative Postposition `fi`:**
   `fi` is strictly ablative ("from", e.g. motion away from a source). It is not a comparative marker in canonical grammar.

---

## 3. Structural Semantic Representation (Typed AST Schema)

```json
{
  "status": "supported | ambiguous | unsupported | unknown_lexeme",
  "construction": "verbal | nominal_predicate | imperative | coordinate_sentence | embedded_clause | quotative | complex_conditional",
  "speech_act": "assertion | question | imperative | quotation",
  "polarity": true,
  "tense": "past | future | future_in_past | unmarked",
  "aspect": "progressive | completed | habitual | unmarked",
  "mood": "indicative | conditional | concessive | counterfactual | imperative",
  "subject": "Mei",
  "predicate": {
    "verb_lemma": "davelen",
    "voice": "active | passive | middle | reflexive | inchoative",
    "valency_class": "ditransitive",
    "arguments": [
      {"role": "Agent", "value": "Mei", "is_overt": true},
      {"role": "Patient", "value": "tüvanan", "is_overt": true},
      {"role": "Recipient", "value": "sain", "is_overt": true}
    ],
    "valency_satisfied": true
  },
  "subordinate_clauses": [
    {
      "type": "subject_relative_clause | object_relative_clause | complement_clause | conditional_antecedent | concessive_condition",
      "head_noun": "Tüvan",
      "embedded_role": "Patient"
    }
  ],
  "coordinate_clauses": [],
  "comparative": {
    "is_comparative": true,
    "marker": "peli",
    "quality": "lavari",
    "standard": "Sai ri lem",
    "standard_marker": "nera"
  },
  "quantifier_scope": null,
  "ambiguities": []
}
```

---

## 4. Summary of Proposed Governance Decisions for Owner Review

1. **Decision AD-2026-009 (Ditransitive Recipient `ta`):** Formalize postposition `ta` for recipient / addressee marking in ditransitive and communicative verbs.
2. **Decision AD-2026-010 (Reflexive Pronoun Co-reference):** Ratify accusative personal pronoun co-reference (`Mei miraven mein`, `Eli liren elin`) as official reflexive voice.
3. **Decision AD-2026-011 (Middle / Passive Voice):** Formally review verbal infix `-il-` for morphological passive and analytic particle `vo` for middle voice.
4. **Decision AD-2026-012 (Compositional Counterfactual):** Ratify `şe da [VP] ... da va [VP]` as compositional counterfactual conditional.
5. **Decision AD-2026-013 (Relative Clause Disambiguation):** Adopt post-nominal `ke` with explicit subject vs object relative role resolution.
