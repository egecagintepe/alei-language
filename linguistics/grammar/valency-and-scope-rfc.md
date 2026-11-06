# RFC-2026-001: Valency, Voice, Stative Predicates, and Scope Clarification in Alei (Audited L5.2 Edition)

- **RFC Identifier:** RFC-2026-001 (Audited Revision L5.2)
- **Author:** Alei Language Engineering Team (Autonomous Phase L5 / L5.2 Research Audit)
- **Status:** `PROPOSAL` / `EXPERIMENTAL` (Requires explicit human language-owner decision)
- **Target Version:** Post-v1.1.0 Evaluation (Proposed Candidate for Future RFC Review)
- **Supersedes:** RFC-2026-001 Draft 1 & L5.1 Draft
- **Dependencies:** v1.0 standard (`adsiz_dil_acik_anlam_standardi_v1_0.md`), v1.1.0 overlay (PR #8)

---

## 1. Motivation and Problem Statement

During the first blind-translation pilot experiment between independent AI models (Agent A: ChatGPT, Agent B: Gemini) on stanzas K1–K5 of an original Turkish poem, significant literary meaning was lost or altered. The linguistic post-mortem established that this loss was not model hallucination of canonical roots, but the direct result of structural gaps in Alei v1.0/v1.1:

1. **Underspecified Verbal Valency and Lack of Voice Marking:** Verbs of change (such as `nesalen` = lose, `roots:525`) are strictly transitive (`[Agent] nesalen [Patient-an]`). When an object is omitted or when an inanimate patient is placed in subject position (`Vel ne va nesalen`), the grammar fails to indicate whether the subject is an agent losing something or an inchoative patient disappearing/getting lost.
2. **Ambiguity Between Stative Predicates and Eventive Actions:** Phrases like `Lüra fal ve` attempt to express the stative property "the door is open" by compounding an action noun (`fal` = opening action, `roots:32`) with an associative marker (`ve` = with, `functions:1079`). This obscures the contrast between present states, past states, resultative achievements, and progressive actions.
3. **Conflation of Conditional and Concessive Scope:** Alei provides only `şe` ("if"). Concessive conditionals ("even if you fear / korksan da"), which presuppose the reality or likelihood of the condition rather than its hypothetical doubt, are collapsed into pure conditionals, distorting urgent exhortations into conditional permissions.
4. **Imperative Parsing Scope:** Canonical standard v1.0 §4.1 already explicitly allows omitting the person pronoun in clear imperatives (*"Kişi zamiri varsayılan olarak söylenir; kısa cevaplarda ve yönü çok açık emirlerde atılabilir"*). The AST parser has been updated to recognize subjectless commands (`Aremen!` / Think!) in standard mode.

---

## 2. Proposal 1: Middle/Inchoative Voice — Full Strategy Comparison & Collision Audit

### 2.1 The Linguistic Problem
In Alei v1.0, verbs derived from roots with `-en` inherit the root's argument structure. For transitive roots, omitting the direct object (`-an`) creates unresolvable ambiguity:
- `Mei da nesalen velan.` -> *I lost the path.* (Transitive: Subject = Agent, Object = Patient)
- `Vel da nesalen.` -> *The path lost [something]?* OR *The path was lost / disappeared?*

### 2.2 Exhaustive Collision Audit (`se` and `ro`)
Previous drafts proposed candidate particles for middle voice that produced unacceptable cross-layer collisions:
1. **Collision with Canonical `se` (`functions:1080`):**
   `se` is the certified **instrumental postposition** ("araçla/vasıtayla", e.g., `tüvan se` = with a tool). Using `se` as a pre-verbal middle voice particle creates severe syntactic ambiguity against post-nominal instrumental phrases.
2. **Collision with Transparent Semantics `ro` (Standard v1.0 §5.4, `data/semantic-roles.json`):**
   `ro` is the established role marker for **`source_from`** (origin/source: `meyar-ro-nasel` = fruit from the forest). Repurposing `ro` in the grammar layer contaminates the transparent semantics parser.

### 2.3 Evaluation of 4 Alternative Voice Strategies

To resolve voice modulation without creating hidden collisions, four distinct strategies are evaluated across six design criteria:

| Evaluation Dimension | Strategy 1: Unallocated Analytic Particle (`vo`) | Strategy 2: Dedicated Voice Infix/Suffix (`-il-` / `-in-`) | Strategy 3: Periphrastic Reflexive (`samel` / `avelen`) | Strategy 4: Contextual Valency Alternation |
|---|---|---|---|---|
| **Mechanism** | Open CV particle preceding verb: `Vel ne va vo nesalen.` | Suffix/infix before verb ending: `Vel ne va nesalilen.` | Canonical reflexive root or auxiliary: `Vel da avelen nesali.` | Inanimate subjects automatically license patient reading without marker. |
| **Learnability** | High (analytic, isolated word). | Very High (mirrors Turkic `-il-` / Romance passive). | High (uses existing v1.0 vocabulary). | Moderate (requires learning implicit semantic rules). |
| **Collision Risk** | Low (only if verified against all 270 roots, 63 functions, and 10 roles). `vo` is currently free. | **Zero Collision.** Derivation morphology is fully isolated from function words and semantic roles. | **Zero Collision.** 100% composed of approved canonical roots. | **Zero Collision.** No new morphemes. |
| **Compositional Transparency** | Medium | High | Very High (`samel` = self/same). | Low (unmarked structural ambiguity). |
| **Backward Compatibility** | Adds new function word to v1.0 grammar. | Adds regular verb infix rule to morphology. | **100% Backward Compatible.** No syntax or morphology change required. | **100% Backward Compatible.** |
| **Parser Complexity** | Low | Low (regex pattern `r'(\w+)(?:il|in)en'`). | Very Low | High (requires semantic animacy check on subject). |

### 2.4 Owner Decision Options
- **Option A (Dedicated Verbal Infix `-il-`):** Regularizes `[Root] + -il- + -en` for middle/passive verbs (`nesalilen` = kaybolmak, `falilen` = açılmak). Eliminates particle collisions permanently.
- **Option B (Periphrastic `samel`):** Requires no grammar extension; uses existing reflexive root `samel` (`Vel da nesalen samel lo`).
- **Option C (Analytic Particle `vo`):** If an analytic particle is strictly preferred by the owner, `vo` is phonologically legal and free of collisions across roots, functions, and semantic roles.

---

## 3. Proposal 2: Systematic Stative Quality Derivation via Suffix `-i`

### 3.1 The Linguistic Problem
Translators struggling to express stative adjectives ("open", "closed", "broken") have resorted to calquing nouns with postposition `ve` (`lüra fal ve` = *door opening with*). This construction lacks clear distinction between dynamic events and static states.

### 3.2 Semantic Boundary Rule for `-i` Derivations
Standard v1.0 §8.2 defines `-i` to derive qualities from nominal roots (`sül` -> `süli`). Extending `-i` to action roots requires an explicit semantic boundary rule:

> **Rule (Spatial/Physical Configuration Licensing):**  
> Stative quality derivation via `-i` is semantically licensed **exclusively on action roots denoting physical, spatial configuration or reversible state** (e.g., `fal` opening action -> `fali` open).  
> It is **NOT licensed** on dynamic processes, speech acts, or cognitive verbs:
> - `fal` (opening) -> `fali` (open / açık [licensed stative property]).
> - `lum` (repairing) -> `lumi` (repaired / onarılmış [licensed stative property]).
> - `ves` (speaking) -> `*vesi` (UNLICENSED; cannot mean "spoken").
> - `arem` (thinking) -> `aremi` (licensed under §8.2, but means "thoughtful / düşünceli", NOT "thought-out state").

### 3.3 Semantic Contrast Minimal Pairs

| Construction | Alei Form | English Meaning | Turkish Meaning | Semantic Type |
|---|---|---|---|---|
| **Stative Present Property** | `Lüra fali.` | The door is open. | Kapı açık. | Stative Property |
| **Stative Past Property** | `Lüra da fali.` | The door was open. | Kapı açıktı. | Past Stative |
| **Progressive Event** | `Lüra du falen.` | The door is opening. | Kapı açılıyor. | Progressive Dynamic |
| **Completed Achievement** | `Lüra da fa falen.` | The door has opened. | Kapı açıldı / açılmış bulunuyor. | Resultative Event |
| **Instrumental Relation** | `Lüra fal-tüvan ve.` | The door has an opening mechanism. | Kapının açılma düzeneği var. | Nominal Compound |

---

## 4. Proposal 3: Concessive Conditional Compound `şe-el` ("Even if")

### 4.1 The Linguistic Problem
In poetic and rhetorical discourse, concessive conditionals ("Even if you fear, think!") assert that the conclusion holds regardless of the condition's truth value. Canonical Alei only possesses `şe` ("if / eğer"), which implies uncertainty and turns an urgent exhortation into a contingent conditional.

### 4.2 Proposed Mechanism: Analytic Compound `şe-el`
In Alei v1.0, `şe` is "if" (`functions:1072`) and `el` is the additive focus particle ("also / even / dahi", `functions:1071`). We propose combining them into the transparent compound **`şe-el`**:

$$\mathbf{şe\text{-}el} + \text{Clause}_1 + [,] + \text{Clause}_2$$

- **IPA:** `/ʃe.el/`
- **Glosses:** `şe-el`: CONC (even if / -se bile)
- **Logical Transparency:** Strictly compositional (`şe` + `el`). It introduces no hidden metaphysical or modal assumptions; it straightforwardly denotes that the consequent holds *even granting* the antecedent.

### 4.3 Minimal Pair Comparison (Canonical Lexicon)
- **Pure Conditional:**
  - *Alei:* `Şe Sai vürelen, aremen.`
  - *Gloss:* `if 2SG fear-VB , think-VB`
  - *Meaning:* If you fear, think. (Eğer korkarsan, düşün — belki korkmazsın, ama korkarsan düşün).
- **Concessive Conditional:**
  - *Alei:* `Şe-el Sai vürelen, aremen!`
  - *Gloss:* `even-if 2SG fear-VB , think-VB !`
  - *Meaning:* Even if you fear, think! (Korksan bile düşün — korku gelse dahi tefekkürü bırakma!).

---

## 5. Lexical Gap Notice: Star (`GAP-LEX-STAR`)

### 5.1 Verification
An exhaustive survey of `roots.jsonl`, `lexemes.jsonl`, and `functions.jsonl` confirms:
- `Sümei` (`roots:496`): sun (güneş).
- `Nüra` (`roots:497`): moon / celestial body (ay, gök cismi). Semantic anchor: `moon`.
- **Alei v1.0/v1.1 has NO root for "star" (yıldız).**

### 5.2 Resolution Options for Owner Review
- **Option 1 (Compositional Compound):** `siril-pemar` (sky-brightness / gökyüzü ışığı) or `siril-nüra` (sky celestial body / gök cismi).
- **Option 2 (Candidate Root Proposal):** Propose candidate root `Sir` (IPA `/sir/`, CVC, "yıldız / star") in `proposed-lexemes.jsonl` subject to owner adoption.
- In all standard documents, `Nüra` remains canonically **moon**, never star.

---

## 6. Backward Compatibility & Non-Canonical Governance Notice

> [!IMPORTANT]
> - All proposals in this document (`vo` / `-il-`, `fali`, `şe-el`, candidate roots) remain **non-canonical proposals** until ratified by the language owner in an official Decision Record (`AD-2026-xxx`).
> - The software implementation treats proposed features cleanly under `mode='experimental'`, without contaminating canonical tests.
