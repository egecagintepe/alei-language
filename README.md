# Alei — An Open Human-First Constructed Language

[![License: Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-blue.svg)](LICENSE)
[![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey.svg)](LICENSE-DOCS)
[![Standard: v1.0 / v1.1.0-RC](https://img.shields.io/badge/Standard-v1.1.0--RC-green.svg)](standard/README.md)
[![Language: Alei](https://img.shields.io/badge/Language-Alei-teal.svg)](governance/decisions/README.md)

**Alei** is an open, human-first constructed literary language engineered for clear expression, transparent semantic composition, and poetic elegance. **Alei** is the official owner-approved name of the language ([AD-2026-001](governance/decisions/README.md)); `Alei!` serves as its universal greeting ("Hello!").

The language combines a productive, easy-to-learn grammatical root core with an analytical **transparent semantics layer** that allows concepts to be described through explicit attribute roles (such as source, color, taste, purpose, or material) without resorting to opaque or arbitrary naming.

> [!NOTE]
> **Human Alei first:** Alei is designed for human speakers, writers, and learners. The separate *AleiFlow* project is an isolated experimental programming-language track and is not the primary mission of this repository.

[Türkçe Tanıtım (README.tr.md)](README.tr.md) · [Start Here Guide](docs/start-here.md) · [Grammar Reference](docs/grammar.md) · [Standard Specification](standard/README.md) · [Interactive Docs Site Preview](docs/site/index.html)

---

## 1. Quick Dialogue & Pronunciation

Here is a typical everyday conversation in verified Alei v1.1.0:

```text
A: Alei! Sai süli le?
   [aˈlei̯ | sai̯ ˈsy.li le]
   "Hello! Are you well?"
   (hello | 2SG good-ADJ Q)

B: Alei! Mei süli. Sai yelen ke miraven Meian le?
   [aˈlei̯ | mei̯ ˈsy.li || sai̯ ˈje.len ke miˈra.ven ˈmei̯.an le]
   "Hello! I am well. Can you help me?"
   (hello | 1SG good-ADJ || 2SG can-VB COMP help-VB 1SG-ACC Q)

A: Ei, Mei yelen ke miraven Saian. Süli vel!
   [ei̯ | mei̯ ˈje.len ke miˈra.ven ˈsai̯.an || ˈsy.li vel]
   "Yes, I can help you. Have a good journey!"
   (yes | 1SG can-VB COMP help-VB 2SG-ACC || good-ADJ path)
```

### Pronunciation at a Glance
- **28-letter Latin alphabet** (8 vowels: `a e ı i o ö u ü`; 20 consonants: `b d f g h j k l m n ñ ŋ p r s ş t v y z`).
- `ı` (back unrounded, like Turkish *ı*) and `i` (front unrounded) are strictly distinct.
- `ñ` is palatal nasal [ɲ] (like Spanish *ñ*); `ŋ` is velar nasal [ŋ] (like English *sing*).
- Diphthongs `ai`, `ei`, `ae`, `au` are pronounced as single gliding syllables.
- Regular stress: penultimate syllable (second from end).

---

## 2. What Makes Alei Interesting?

1. **Root Economy with Productive Morphology:** A carefully conserved vocabulary of 270 attested roots forms the foundation for regular noun, verb (`-en`), adjective (`-i`), and plural (`-na`) inflections.
2. **Transparent Open Semantics:** Beyond everyday vocabulary, complex or unfamiliar concepts can be composed analytically using hyphenated `HEAD-ROLE-VALUE` expressions. For instance:
   - `meyar` = fruit
   - `meyar-ro-yenar-li-reş-ze-selim-mu-molir` = a fruit originating from a tree (`ro-yenar`), typically red (`li-reş`), sweet (`ze-selim`), and spherical (`mu-molir`).
   *This does not magically claim to define every real-world apple, but it transparently communicates key perceptual properties.*
3. **Epistemic Discipline:** Alei tools explicitly reject arbitrary name deduction. An unknown term like `Jajaya` cannot be inferred without a shared definition.
4. **Governed Human Language Evolution:** Language rules, roots, and official decisions follow a strict, public human-governed RFC process.

---

## 3. Get Started in 60 Seconds

Alei requires **Python 3.11+**. You can clone and inspect the tools in one minute:

```bash
# 1. Clone the repository
git clone https://github.com/egecagintepe/alei-language.git
cd alei-language

# 2. Install the library in editable mode
python -m pip install -e .

# 3. Look up an owner-approved root in v1.1.0 (preferred help root Mirav)
python -m alei_language.cli lookup mirav --version 1.1.0

# 4. Check a legacy alias (Mivav returns with a deprecation warning)
python -m alei_language.cli lookup mivav --version 1.1.0

# 5. Parse a full grammatical sentence into a typed AST with valency checks
python -m alei_language.cli parse-ast "Mei da sileven tüvanan." --version 1.1.0

# 6. Parse an open-semantics hyphenated description
python -m alei_language.cli parse-semantic "meyar-li-reş-ze-selim"

# 7. Run the test suite (58 verified deterministic tests)
python -m unittest discover -s tests
```

---

## 4. Learning Pathways & Documentation

- 📖 **[Start Here Guide](docs/start-here.md):** Step-by-step introduction to grammar, word order, and cases.
- 📐 **[Grammar Reference](docs/grammar.md):** SVO/SOV constituent structure, nominal predicates, questions with `le`, and modal complements with `ke`.
- 🗂️ **[Full Glossary](docs/glossary.md):** Attested v1.0 roots, v1.1.0 additions, and grammatical functions.
- 🎭 **[Experimental Literature](linguistics/corpus/experimental-literature.md):** Original prose scenes, poems, and 12 minimal pairs demonstrating scope, aspect, and valency contrasts.
- 💬 **[Communicative Dialogues](linguistics/corpus/experimental-dialogues.md):** 30 practical conversational turns and 8 multi-turn dialogues with persistent characters.
- 🔬 **[L5 Linguistic Research Report](docs/research/blind-translation-01-five-stanza-audit.md):** Analysis of the first ChatGPT-to-Gemini blind back-translation experiment.

---

## 5. For Developers and Agent Systems

Alei includes seven procedural **Agent Skills** located in `.agents/skills/`:
- `alei-speak`: Conversational generation and dialogue practice.
- `alei-tutor`: Step-by-step human language instruction.
- `alei-translate`: Translation between Alei, Turkish, and English with uncertainty tracking.
- `alei-audit`: Structural validation of syntax and transparent semantics.
- `alei-propose`: Drafting candidate root proposals according to phonotactic rules.
- `alei-research`: Exploring lexical neighborhoods and historical provenance.
- `alei-literary`: Composing original poetry and expressive prose.

> [!IMPORTANT]
> Agent Skills are deterministic procedural guidelines; they do not alter model weights or act autonomously without a runner harness.

---

## 6. How to Contribute

We welcome contributions from linguists, conlangers, writers, educators, and software engineers!

- **Suggest a New Word or Idiom:** Submit an issue using our [Word Proposal Template](.github/ISSUE_TEMPLATE/idiom-proposal.yml). Propose transparent compounds from existing roots first before proposing new roots.
- **Report a Grammar Friction Point:** Open an issue using our [Grammar Gap Report Form](.github/ISSUE_TEMPLATE/grammar-gap.yml).
- **Contribute Creative Writing:** Submit short stories, dialogues, or poems to our experimental corpus.
- **Join the Community:** Participate in [GitHub Discussions](https://github.com/egecagintepe/alei-language/discussions).

*Note: All proposed words and rules remain categorized as `proposal` until explicitly adopted by the repository owner in an official Decision Record.*

---

## 7. Current Project State & Release Roadmap

| Layer | Branch / Status | Key Features |
|---|---|---|
| **v1.0 (Archived)** | `main` | Original foundation (SHA-256 `265fcc0...`); 270 roots, 101 example sentences. |
| **Integrity Checks** | PR #7 (`phase-2/linguistic-integrity`) | 101-sentence audit, conservative parser, semantic type checking. |
| **v1.1.0-RC** | PR #8 (`owner/alei-v1.1-pr`) | Official name **Alei** ([AD-2026-001](governance/decisions/README.md)); preferred help root **Mirav** ([AD-2026-002](governance/decisions/README.md)); versioned overlay. |
| **Phase L5 (Active)** | Branch `l5/linguistic-engineering-community` | Typed AST, valency verification, blind translation audit, 42-case held-out suite, experimental literature corpus. |

---

## 8. License & Citation

- **Software & Skills:** Licensed under [Apache-2.0](LICENSE).
- **Linguistic Data, Standards & Documentation:** Licensed under [CC BY 4.0](LICENSE-DOCS).

If citing Alei in linguistic research or conlang corpora:
```bibtex
@misc{alei2026,
  author = {Tepe, Ege Çağın and Alei Contributors},
  title = {Alei: An Open Human-First Constructed Language with Transparent Semantics},
  year = {2026},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/egecagintepe/alei-language}}
}
```
