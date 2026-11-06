# RFC-2026-001: Valency, Voice, Stative Predicates, and Scope Clarification in Alei

- **RFC Identifier:** RFC-2026-001 (Audited Revision L5.1)
- **Author:** Alei Language Engineering Team (Autonomous Phase L5 / L5.1 Audit)
- **Status:** `PROPOSAL` / `EXPERIMENTAL` (Requires explicit human language-owner decision)
- **Target Version:** Post-v1.1.0 Evaluation (Proposed Candidate for Future RFC Review)
- **Supersedes:** RFC-2026-001 Draft 1
- **Dependencies:** v1.0 standard (`adsiz_dil_acik_anlam_standardi_v1_0.md`), v1.1.0 overlay (PR #8)

---

## 1. Motivation and Problem Statement

During the first blind-translation experiment between independent AI models (Agent A: ChatGPT, Agent B: Gemini) on stanzas K1–K5 of an original Turkish poem, significant literary meaning was lost or altered. The linguistic post-mortem (`docs/research/blind-translation-01-five-stanza-audit.md`) established that this loss was not merely an encoder hallucination, but the direct result of four fundamental structural gaps in Alei v1.0/v1.1:

1. **Underspecified Verbal Valency and Lack of Voice Marking:** Verbs of change (such as `nesalen` = lose, `roots:525`) are strictly transitive (`[Agent] nesalen [Patient-an]`). When an object is omitted or when an inanimate patient is placed in subject position (`Vel ne va nesalen`), the grammar fails to indicate whether the subject is an agent losing something or an inchoative patient disappearing/getting lost.
2. **Ambiguity Between Stative Predicates and Eventive Actions:** Phrases like `Lüra fal ve` attempt to express the stative property "the door is open" by compounding an action noun (`fal` = opening action, `roots:32`) with an associative marker (`ve` = with, `functions:1079`). This obscures the contrast between present states, past states, resultative achievements, and progressive actions.
3. **Conflation of Conditional and Concessive Scope:** Alei provides only `şe` ("if"). Concessive conditionals ("even if you fear / korksan bile"), which presuppose the likelihood or presence of the condition rather than its hypothetical doubt, are collapsed into pure conditionals, distorting imperative warnings into conditional permissions.
4. **Imperative and Quotative Parsing Scope:** In natural literary dialogue and poetry, commands (`Aremen!` / Think!) and direct quotes (`Elina da vesen: "Ne vürelen!"`) are natural human utterances. Canonical standard v1.0 §4.1 already allows omitting the person pronoun in clear imperatives (*"Kişi zamiri varsayılan olarak söylenir; kısa cevaplarda ve yönü çok açık emirlerde atılabilir"*), but machine parsers required an explicit rule to recognize subjectless commands and quotation frames without reporting syntactic failure.

This RFC outlines four principled proposals designed to address these challenges while maintaining 100% backward compatibility with archived v1.0 and v1.1.

---

## 2. Proposal 1: Middle/Inchoative Voice Particle (Collision Audit & Alternatives)

### 2.1 The Linguistic Problem
In Alei v1.0, verbs derived from roots with `-en` inherit the root's argument structure. For transitive roots, omitting the direct object (`-an`) creates unresolvable ambiguity:
- `Mei da nesalen tüvanan.` -> *I lost the tool.* (Transitive: Subject = Agent, Object = Patient)
- `Vel da nesalen.` -> *The path lost [something]?* OR *The path was lost / disappeared?*

Natural human languages resolve this through middle voice (Turkish: *-il/-in*, e.g., *kaybetmek* -> *kaybolmak*), reflexive markers (French: *se perdre*, Spanish: *perderse*), or ergative/unaccusative alternating verbs (English: *the ice melted*).

### 2.2 Critical Audit Finding: Collision with Canonical `se` (`functions:1080`)
Draft 1 of this RFC proposed an analytic middle voice particle `se`. **Independent linguistic audit revealed that `se` is already a canonical morpheme in Alei standard v1.0 §8.6 (`functions:1080`):**
$$\text{functions:1080: } \mathbf{se} \quad (\text{part of speech: postposition, gloss: "araçla/vasıtayla" / instrumental})$$

Example canonical usage: `tüvan se` = with a tool / by means of a tool.

Silently repurposing `se` as a pre-verbal middle voice particle creates an unacceptable syntactic collision with the canonical instrumental postposition.

### 2.3 Revised Voice Proposal & Candidate Options for Owner Review
To achieve Patient-promotion without colliding with canonical `functions:1080`, three alternatives are presented for owner decision:
- **Option A (Alternative Particle `ro`):** Use unallocated open CV particle `ro` placed immediately before the verb (`Vel ne va ro nesalen.`). `ro` has zero collision with existing roots or grammatical particles.
- **Option B (Positional Disambiguation of `se`):** Retain `se` as an experimental proposal only with a strict structural disambiguation rule: post-nominal `[Noun] se` is strictly instrumental postposition (`tüvan se`), whereas immediately pre-verbal `[Tense/Aspect] se [Verb]` is middle voice. *Caution: Increases parser complexity and human cognitive load.*
- **Option C (Reflexive Suffixation/Compound):** Derive middle forms using reflexive nominal marker `samel` (e.g. `nesalen-samel`).

### 2.4 Positive and Negative Minimal Pairs (Evaluated with Candidate Particle)
- **Pair 1A (Transitive Active):**
  - *Alei:* `Mei va nesalen velan.`
  - *Gloss:* `1SG FUT lose-VB path-ACC`
  - *Translation:* I will lose the path.
- **Pair 1B (Middle/Inchoative Candidate):**
  - *Alei:* `Vel ne va se nesalen.` *(or `Vel ne va ro nesalen.`)*
  - *Gloss:* `path NEG FUT MID lose-VB`
  - *Translation:* The path will not be lost / will not disappear.
- **Pair 1C (Defective Transitive Baseline):**
  - *Alei:* `*Vel ne va nesalen.`
  - *Analysis:* Valency clash; transitive verb `nesalen` lacks overt patient and lacks voice marking.

---

## 3. Proposal 2: Systematic Stative Quality Derivation via Suffix `-i`

### 3.1 The Linguistic Problem
Translators struggling to express stative adjectives ("open", "closed", "broken") have resorted to calquing nouns with postposition `ve` (`lüra fal ve` = *door opening with*). This construction lacks clear distinction between dynamic events and static states.

### 3.2 Canonical Basis: Derivation on Action Roots
Alei standard v1.0 §8.2 defines the productive suffix **`-i`** to derive qualities from nominal roots ending in a consonant:
- `sül` (goodness, `roots:441`) + `-i` -> `süli` (good / well)
- `sülar` (surprise / awe, `roots:482`) + `-i` -> `sülari` (surprised / astonished)

We propose regularizing this rule for physical action roots:
- Root `fal` (opening action / açılma, `roots:32`) + `-i` -> **`fali`** (open / açık [quality])

*(Correction from Draft 1: Root `vür` does not exist in Alei canon. `Vürel` (`roots:502`) is fear ("korku"). Derivations must strictly originate from attested roots.)*

When used in nominal predicates, derived qualities take standard pre-predicate tense markers:
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
In poetic and rhetorical discourse, concessive conditionals ("Even if you fear, think!") assert that the conclusion holds regardless of the condition's truth value. Canonical Alei only possesses `şe` ("if / eğer"), which implies uncertainty and turns an urgent exhortation into a contingent conditional.

### 4.2 Proposed Mechanism: Analytic Compound `şe-el`
In Alei v1.0, `şe` is "if" (`functions:1072`) and `el` is the additive focus particle ("also / even / dahi", `functions:1071`). We propose combining them into the transparent compound **`şe-el`**:

$$\mathbf{şe\text{-}el} + \text{Clause}_1 + [,] + \text{Clause}_2$$

- **IPA:** `/ʃe.el/`
- **Glosses:** `şe-el`: CONC (even if / -se bile)
- **Learnability:** Highly transparent; composed entirely of two certified v1.0 morphemes.

### 4.3 Minimal Pair Comparison (Canonical Lexicon)
- **Pure Conditional:**
  - *Alei:* `Şe Sai vürelen, aremen.`
  - *Gloss:* `if 2SG fear-VB , think-VB`
  - *Meaning:* If you fear, think. (Eğer korkarsan, düşün.)
- **Concessive Conditional:**
  - *Alei:* `Şe-el Sai vürelen, aremen!`
  - *Gloss:* `even-if 2SG fear-VB , think-VB !`
  - *Meaning:* Even if you fear, think! (Korksan bile düşün!)

---

## 5. Proposal 4: Imperative Speech Acts and Quotative Framing

### 5.1 The Linguistic Problem and Canonical Re-grounding
1. **Subjectless Imperatives:**
   Standard v1.0 §4.1 already explicitly permits omitting the person pronoun in commands:
   > *"Kişi zamiri varsayılan olarak söylenir; kısa cevaplarda ve yönü çok açık emirlerde atılabilir."*
   Therefore, bare verbs functioning as commands (`Aremen!` / Think! or `Ne vürelen!` / Do not fear!) are **already licensed by canonical grammar**. The AST parser has been updated to recognize them as valid canonical imperatives with implied 2nd-person addressee, rather than classifying them as ungrammatical fragments.

2. **Direct Quotative Framing:**
   Direct quotations following speech verbs (`Elina da vesen: "..."`) require parser recognition for colon and quotation mark delimiters without failing tokenization checks.

### 5.2 AST Representation
- `Aremen!` -> AST: `SentenceAST(status='supported', construction='imperative', speech_act='imperative', subject='implied_2nd_person', polarity=True)`
- `Ne vürelen!` -> AST: `SentenceAST(status='supported', construction='imperative', speech_act='imperative', subject='implied_2nd_person', polarity=False)`
- `Elina da vesen: "Ne vürelen!"` -> AST: `SentenceAST(status='supported', construction='quotative', speech_act='quotation', subject='elina')`

---

## 6. Backward Compatibility & Non-Canonical Governance Notice

> [!IMPORTANT]
> In strict adherence to Repository Governance:
> - Proposals 1, 2, and 3 remain **proposals** and are NOT canonical standard until adopted by official human-owner decision records (`AD-2026-xxx`).
> - Proposal 4 (Imperatives) is confirmed to be **canonical standard v1.0 §4.1 compliance**, while quotative clause framing remains experimental syntax.
> - The software implementation treats proposed features cleanly under `mode='experimental'`, without contaminating canonical tests.

---

## 7. High-Value Owner Decision Summary

1. **Decision AD-2026-003 (Voice Marker Selection):** Review middle voice particle choice (`se` with positional disambiguation vs collision-free `ro`).
2. **Decision AD-2026-004 (Stative Derivation):** Adopt regular `-i` quality derivation on attested action roots (`fal` -> `fali`).
3. **Decision AD-2026-005 (Concessives):** Adopt transparent compound `şe-el` for concessive conditionals.
4. **Decision AD-2026-006 (Quotative Framing):** Formalize colon and quotation-mark delimited direct speech syntax.
