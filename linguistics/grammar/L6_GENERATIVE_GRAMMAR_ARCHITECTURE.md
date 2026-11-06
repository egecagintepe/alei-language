# ALEI — L6: HUMAN-FIRST GENERATIVE GRAMMAR ARCHITECTURE

**Status:** Working Linguistic Specification & Experimental Architecture (Phase L6)  
**Date:** 2026-11-06  
**Authoritative Base:** Alei v1.1.0 (`main` @ SHA `931ca8c`)  
**Standard Governance:** Non-canonical experimental layer. v1.0 standard and v1.1 owner decisions remain immutable.

---

## 1. Executive Summary & Design Philosophy

The mission of Phase L6 is to develop the generative linguistic foundations necessary for Alei to function as a natural, expressive, highly learnable human literary language. 

Alei must not remain a restricted lexicon of isolated sentence patterns; it must support:
- Fluid everyday conversation and personal dialogue
- Nuanced literary fiction, poetry, and character interiority
- Multi-party relationships, affection, conflict, and reconciliation
- Complex philosophical arguments, counterfactual reasoning, and truth conditions
- Systematic creation and transparent comprehension of novel concepts

### Core Architectural Principles
1. **Human Learnability First:** Prefer minimal, regular, and predictable rules over intricate exceptions or excessive morphological paradigms.
2. **Compositional Elegance:** Build complex meanings by combining existing canonical function words and roots rather than multiplying arbitrary affixes.
3. **No Hidden Syntactic-Semantic Confusion:** A sentence that parses cleanly in an AST is not valid unless its semantic argument roles, valency constraints, and truth conditions are coherent.
4. **Transparent Ambiguity Modeling:** When a natural sentence permits multiple valid structural readings, the grammar engine must explicitly represent the ambiguity graph rather than arbitrarily selecting one reading.
5. **Strict Governance Separation:** All L6 mechanisms are implemented experimentally under `mode='experimental'` or `mode='l6'`, keeping canonical v1.0 and approved v1.1 untouched.

---

## 2. The 11 Core Grammatical Domains: Design & Alternative Analysis

---

### Domain 1: Verb Valency & Argument Structure

#### 1.1 Linguistic Problem
Alei v1.0 standard §4 defines default SVO word order with object marking (`-n` on vowel stems, `-an` on consonant stems). However, ditransitive verbs (giving, saying, showing) and destination verbs require clear argument differentiation between Theme/Patient and Goal/Recipient.

#### 1.2 Competing Alternatives
- **Alternative 1.A (Postpositional Dative Flagging via `ta`):**
  - Theme/Patient is marked with canonical accusative (`-n`/`-an`).
  - Goal/Recipient/Beneficiary is marked with canonical directional/dative postposition `ta` (`functions:1077`).
  - *Example:* `Mei da davelen tüvanan sain ta.` (I gave the book to you.)
- **Alternative 1.B (Double Object / Serial Prepositional Frame):**
  - Rigid word order: Subject - Verb - Recipient - Theme (no case marker on recipient).
  - *Example:* `Mei da davelen sai tüvanan.`

#### 1.3 Scientific Evaluation Matrix

| Evaluation Criterion | Alternative 1.A (Postposition `ta`) | Alternative 1.B (Double Object) |
|---|---|---|
| **Human Learnability** | **Very High** (transparent, mirrors Turkish *-e/-a* and Romance *a*). | Moderate (strict position-dependent rules). |
| **Pronounceability** | High (natural rhythmic cadence). | High. |
| **Literary Elegance** | **High** (flexible word order: recipient can precede or follow). | Low (rigid, mechanical position dependency). |
| **Semantic Precision** | **Absolute** (no confusion between Patient and Goal). | Moderate (potential clash with adjectival modifiers). |
| **Ambiguity Risk** | **Zero Collision** (`ta` is already goal postposition). | High if nouns are adjacent. |
| **Compatibility** | **100% Canonical** (v1.0 §8.6). | Deviates from v1.0 postposition system. |
| **Parser Complexity** | Low. | Moderate. |

> **L6 Decision:** **Adopt Alternative 1.A.** Ditransitive recipient/goal is consistently marked with postposition `ta`.

---

### Domain 2: Voice System (Transitive, Intransitive, Reflexive, Middle/Passive, Inchoative)

#### 2.1 Linguistic Problem
The language previously struggled with verbs like `nesalen` (roots:525, transitive "to lose"), where speakers wished to say "the path was lost" without an overt external agent, or "I helped myself" without conflating the noun `samel` (friend).

#### 2.2 Distinguishing Five Voice Functions
1. **Active Transitive:** Agent intentionally acts upon Patient (`Mei da falen lüran` = I opened the door).
2. **Active Intransitive:** Single participant motion or action (`Eli da avelen` = He went).
3. **Reflexive:** Agent acts upon oneself; Agent and Patient are co-referential (`Mei da miraven mein` = I helped myself).
4. **Middle / Passive:** Patient is promoted to Subject; Agent is demoted or omitted (`Lüra da falilen` / `Lüra da vo falen` = The door was opened).
5. **Inchoative / Decausative:** Spontaneous transition into a state without an agent (`Lüra da avelen fali` = The door became open).

#### 2.3 Competing Reflexive Alternatives
- **Alternative 2.R.A (Pronominal Co-reference):**
  Use canonical accusative personal pronouns matching the subject (`Mei da miraven mein`, `Eli da liren elin`).
- **Alternative 2.R.B (Dedicated Reflexive Morpheme):**
  Introduce a new reflexive particle `ze` (collides with role `ze`) or `sel` (collides with roots).

> **L6 Decision for Reflexive:** **Adopt Alternative 2.R.A.** Elegant, 100% canonical, zero collisions.

#### 2.4 Competing Middle/Passive Alternatives
- **Alternative 2.M.A (Verbal Suffix/Infix `-il-`):**
  `[Root] + -il- + -en` -> `nesalilen` (to be lost), `falilen` (to be opened).
- **Alternative 2.M.B (Analytic Particle `vo`):**
  Preverbal particle `vo` -> `Vel da vo nesalen` (The path was lost).
- **Alternative 2.M.C (Contextual Zero-Alternation):**
  Inanimate subject automatically interprets transitive verb as passive.

#### 2.5 Scientific Evaluation Matrix for Middle/Passive

| Evaluation Criterion | Alternative 2.M.A (`-il-` Suffix) | Alternative 2.M.B (`vo` Particle) | Alternative 2.M.C (Zero-Alternation) |
|---|---|---|---|
| **Human Learnability** | **Very High** (agglutinative regular affix). | High (analytic particle). | Moderate (requires animacy checks). |
| **Pronounceability** | Euphonic, natural syllabification (`fe-li-len`). | Clean CV particle. | Unchanged. |
| **Literary Elegance** | **Very High** (compact poetic phrasing). | High. | Ambiguous. |
| **Semantic Precision** | **Absolute** (marked morphological status). | Absolute. | **Poor** (ambiguous with missing object). |
| **Collision Risk** | **Zero** (isolated inside verbal morphology). | Zero (`vo` is unallocated). | Zero. |
| **Compatibility** | Extends regular verb morphology. | Adds 1 functional particle. | 100% identical surface text. |
| **Generalization** | Applies uniformly to all transitive verbs. | Applies to all verbs. | Fails on animate patients. |

> **L6 Proposal:** **Alternative 2.M.A (`-il-`)** is recommended for morphological elegance; **Alternative 2.M.B (`vo`)** is retained as analytic option for owner review.

---

### Domain 3: State vs. Event vs. Completed-Result (Aktionsart & Aspect)

#### 3.1 Linguistic Problem
Alei text must clearly differentiate between:
- "The door is open" (Static quality / current configuration)
- "The door is opening" (Dynamic process in progress)
- "The door opened" (Past event / transition)
- "The door has opened and remains open" (Resultative state)

#### 3.2 Competing Alternatives
- **Alternative 3.A (Aspectual-Stative Composition):**
  - **Static State:** Nominal/Quality predicate: `Lüra fali.` (The door is open.)
  - **Dynamic Process:** Progressive marker `du` + verb: `Lüra du falen.` (The door is opening.)
  - **Past Event:** Past marker `da` + verb: `Lüra da falen.` (The door opened.)
  - **Resultative:** Completed aspect `fa` + stative quality: `Lüra fa fali.` (The door is in an opened state) or `Lüra da fa falen.` (The door has opened [and remains so]).
- **Alternative 3.B (Dedicated Resultative Suffix `-av`):**
  - `falaven` = to be in resultant open state.

> **L6 Decision:** **Adopt Alternative 3.A.** Uses existing canonical particles `du` (functions:1066), `da` (functions:1069), `fa` (functions:1067) and semantically licensed stative `-i` without inventing redundant affixes.

---

### Domain 4: Conditionals, Concessives, and Counterfactuals

#### 4.1 Linguistic Problem
Expressing hypothetical reasoning, concessions, and regret/counterfactual past:
- "If you come, I will speak." (Pure conditional)
- "Even if you fear, think!" (Concessive conditional)
- "If you had come yesterday, we would have won." (Counterfactual past)

#### 4.2 Competing Alternatives
- **Alternative 4.A (Compositional Tense Stacking):**
  - **Conditional:** `Şe` ("eğer", functions:1072): `Şe Sai avelen, Mei va vesen.`
  - **Concessive:** `Şe-el` ("-sa bile", şe + el): `Şe-el Sai vürelen, aremen!`
  - **Counterfactual:** Tense stacking in antecedent (`şe da`) and consequent (`da va` / past of future):
    - Antecedent: `Şe Sai da avelen Dora, ...` (If you had arrived yesterday, ...)
    - Consequent: `... Meina da va miraven.` (... we would have helped.)
- **Alternative 4.B (Dedicated Irrealis Mood Particle `vei`):**
  - `Vei Sai avelen, Meina vei miraven.`

#### 4.3 Scientific Evaluation Matrix

| Evaluation Criterion | Alternative 4.A (Compositional Stacking) | Alternative 4.B (Dedicated Particle `vei`) |
|---|---|---|
| **Human Learnability** | **Very High** (builds logically on past `da` + future `va`). | Moderate (new function word to memorize). |
| **Compositional Transparency** | **Very High** (`past + future` = conditional past). | Moderate. |
| **Literary Elegance** | Poetic and philosophically transparent. | Compact. |
| **Collision Risk** | **Zero** (100% approved canonical particles). | Low. |
| **Grammar Economy** | **Optimal** (0 new particles). | Requires 1 new particle. |

> **L6 Decision:** **Adopt Alternative 4.A.** Compositional stacking `şe da ... da va` is maximally regular and economical.

---

### Domain 5: Negation Scope & Quantified Expressions

#### 5.1 Linguistic Problem
Avoiding ambiguity between:
- "Everyone did not come" (Nobody came vs. Not all came)
- Negating the event versus negating a specific argument

#### 5.2 Competing Alternatives
- **Alternative 5.A (Positional Scope Rule):**
  - Predicate Negation: `ne` immediately precedes the predicate/verb:
    `Mei ne da liren.` (I did not see.)
  - Constituent Negation: `ne` immediately precedes the negated noun phrase:
    `Ne Mei da avelen, lia Sai.` (Not I arrived, but you.)
  - Universal Quantifier: `sam` (every / all, roots:470):
    - `Sam lera da avelen.` (Every person arrived.)
    - `Ne sam lera da avelen.` (Not every person arrived -> Partial negation).
    - `Sam lera ne da avelen.` (Every person did not arrive = None arrived -> Total negation).
  - Existential Quantifier: `ena` (one / a person):
    - `Ne ena lera da avelen.` (Not a single person arrived = Nobody arrived).
- **Alternative 5.B (Dedicated Negative Quantifiers):**
  - Coin new roots for "nobody", "nothing", "nowhere".

> **L6 Decision:** **Adopt Alternative 5.A.** Strict positional scope eliminates the need for separate negative pronouns while preserving absolute semantic clarity.

---

### Domain 6: Relative Clauses & Embedded Propositions

#### 6.1 Linguistic Problem
Alei requires a systematic way to modify nouns with full clauses ("The person who brought the letter") and embed declarative propositions ("She knows that the path is long").

#### 6.2 Competing Alternatives
- **Alternative 6.A (Post-nominal Complementizer `ke`):**
  - Noun modification (Relative Clause):
    $$\text{Head Noun} + \mathbf{ke} + [\text{Subordinate Clause}]$$
    - *Subject Relativization:* `Lera ke da avelen Dora samel ve.` (The person who arrived yesterday is a friend.)
    - *Object Relativization:* `Tüvan ke Mei du sileven (elin) süli ve.` (The book that I am reading is good.)
  - Propositional Embedding (Complement Clause):
    $$\text{Matrix Verb} + \mathbf{ke} + [\text{Proposition Clause}]$$
    - `Mei ünaren ke vel lavari ve.` (I know that the path is long.)
- **Alternative 6.B (Preposed Participial Framing):**
  - `[Dora da avelen] lera samel ve.`

#### 6.3 Scientific Evaluation Matrix

| Evaluation Criterion | Alternative 6.A (`ke` Clause) | Alternative 6.B (Preposed Participial) |
|---|---|---|
| **Human Learnability** | **Very High** (mirrors Romance *que*, English *that*, Persian *ke*). | Moderate (requires parsing complex left-branching). |
| **SVO Alignment** | **Natural right-branching** (consistent with head-initial NPs). | Inconsistent with Alei head-initial syntax. |
| **Recursive Nesting** | **Effortless** (clauses can nest cleanly). | High cognitive load on deep nesting. |
| **Parser Complexity** | Deterministic with explicit boundary. | High ambiguity with adjectives. |

> **L6 Decision:** **Adopt Alternative 6.A.** Canonical `ke` (functions:1070) seamlessly unifies relative and complement clauses.

---

### Domain 7: Temporal Ordering & Narrative Discourse Aspect

#### 7.1 Linguistic Problem
Narrative storytelling requires ordering events in time without repeating clumsy temporal adverbials:
"First he woke up, then he crossed the bridge, before night fell."

#### 7.2 Core Discourse Connectives
- `den`: then / afterwards (sonra / ardından)
- `pür`: before / earlier (önce)
- `orai lo`: at that moment / meanwhile (o sırada / o vakitte)
- `orai fi`: since that time (o vakitten beri)

#### 7.3 Narrative Structure Example
```text
Eli da pürelen vümar ta; den eli da falen lüran; mora avelen pür.
(He reached the bridge; then he opened the door; before night arrived.)
```

---

### Domain 8: Comparatives, Superlatives, and Ordinals

#### 8.1 Linguistic Problem
Comparing qualities and ranking entities:
- "The mountain is taller than the tree."
- "She is the wisest among all."
- "The third gate was closed."

#### 8.2 Competing Alternatives
- **Alternative 8.A (Ablative Comparison via `fi`):**
  - **Comparative:** `[Entity A] + [Quality] + [Entity B] + \mathbf{fi}`
    - `Lümar lavari nasel fi.` (The mountain is bigger than the forest.)
    - Optional intensifier: `lavar` (more) / `pira` (less): `Lümar lavar lavari nasel fi.`
  - **Superlative:** `[Entity A] + [Quality] + \mathbf{sam\ fi}` (than all):
    - `Eli süli sam fi.` (He is better than all = the best.)
  - **Ordinals:** Cardinal Number + `-i` (Standard §8.7):
    - `Ena-i` (first), `Davi-i` (second), `Teli-i` (third), `Pora-i` (fourth).
- **Alternative 8.B (Morphological Suffixation):**
  - Coin comparative affix `*-ek` and superlative affix `*-em`.

> **L6 Decision:** **Adopt Alternative 8.A.** The ablative comparison with `fi` is universal across many human language families (Turkic, Semitic, Romance *de*) and requires zero new morphology.

---

### Domain 9: Pronoun Reference, Anaphora, and Reciprocal Relations

#### 9.1 Paradigm Alignment
- **Personal Pronouns:**
  - 1SG: `mei` (Nom) / `mein` (Acc)
  - 2SG: `sai` (Nom) / `sain` (Acc)
  - 3SG: `eli` (Nom) / `elin` (Acc) [Gender-neutral]
  - 1PL: `meina` (Nom) / `meinan` (Acc)
  - 2PL: `saina` (Nom) / `sainan` (Acc)
  - 3PL: `elina` (Nom) / `elinan` (Acc)
- **Demonstrative Pronoun:**
  - `so` (functions:1053): this / that (`so lera` = this person; `so tüvan` = this tool).
- **Reciprocal Construction:**
  - Two agents acting upon each other:
    `Davi samel da miraven elinan.` (The two friends helped each other [them].)
    Or with distributive modifier `davi-ta` (to each other): `Elina da vesen davi-ta.`

---

### Domain 10: Questions, Requests, Commands, and Reported Speech

#### 10.1 Speech Act System
1. **Polar Question (Yes/No):** Sentence-final particle `le` (`functions:1068`):
   `Sai süli le?` (Are you well?)
2. **Content Questions (Wh-):**
   - `Keli`: who / which (`Keli lera da avelen?` = Which person came?)
   - `Meli`: what (`Sai du liren melian?` = What are you seeing?)
   - `Orai`: when (`Sai va avelen orai?` = When will you come?)
   - `Lem lo`: where (`Eli lem lo?` = Where is he?)
   - `Sira`: why (`Sai da avelen sira?` = Why did you come?)
3. **Imperatives:**
   - Overt or implied 2nd person subject + verb stem: `Aremen!` or `Sai aremen!`
   - Prohibitive (Negative command): `Ne aremen!`
4. **Reported Speech:**
   - **Direct Quotation:** `[Speaker] da vesen: "[Direct Words]"`
     `Elina da vesen: "Ne vürelen!"`
   - **Indirect Speech:** `[Speaker] da vesen ke [Reported Proposition]`
     `Eli da vesen ke va avelen.` (He said that he will come.)

---

### Domain 11: Coordination & Complex Sentence Syntax

#### 11.1 Conjunction Inventory
- **Additive:** `ve` (and / with) — coordinates phrases and clauses.
- **Adversative:** `lia` (but / whereas) — marks sharp contrast.
- **Causal:** `sira` (because / since) — introduces reasons.
- **Conditional:** `şe` (if).
- **Concessive:** `şe-el` (even if / although).

#### 11.2 Complex Sentence Example
```text
Mei da naelen ke avelen lem ta, lia nüra ne da pemaren; sira nasel da şuli mora lo.
(I wanted to go to the dwelling, but the moon did not shine; because the forest was silent in the night.)
```

---

## 3. Structural Semantic Representation (IR / Graph)

Every valid Alei sentence maps deterministically into an explicit Typed Semantic Frame:

```json
{
  "speech_act": "assertion | question | imperative | quote",
  "polarity": true,
  "tense": "past | unmarked | future",
  "aspect": "progressive | completed | habitual | stative",
  "mood": "indicative | conditional | concessive | counterfactual",
  "predicate": {
    "lemma": "falen",
    "voice": "active | middle | passive | inchoative | reflexive",
    "arguments": [
      {"role": "Agent", "value": "Mei", "status": "overt"},
      {"role": "Patient", "value": "lüra", "status": "overt"},
      {"role": "Recipient", "value": "sain", "status": "overt"}
    ]
  },
  "subordinate_clauses": [
    {
      "type": "relative | complement | conditional | concessive",
      "connective": "ke | şe | şe-el | sira",
      "content": { ... }
    }
  ],
  "discourse_connectives": ["den", "pür", "lia"],
  "ambiguities": []
}
```

---

## 4. Summary of Proposed Governance Escalations

The following 5 decisions represent genuine foundational additions for language owner review:
1. **Decision AD-2026-009 (Middle/Passive Voice):** Adopt verbal infix `-il-` (`falilen`) as regular morphological passive, with preverbal `vo` as analytic alternative.
2. **Decision AD-2026-010 (Reflexive Voice):** Ratify canonical pronoun accusative co-reference (`Mei miraven mein`, `Eli liren elin`) as the official reflexive mechanism.
3. **Decision AD-2026-011 (Relative Clause Architecture):** Adopt post-nominal `ke` clauses for noun modification.
4. **Decision AD-2026-012 (Compositional Counterfactual):** Ratify `şe da [VP] ... da va [VP]` as the counterfactual conditional paradigm.
5. **Decision AD-2026-013 (Ablative Comparison):** Ratify postposition `fi` for comparatives (`A süli B fi`) and superlatives (`A süli sam fi`).
