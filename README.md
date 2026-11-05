# Alei Language Project (working title)

An open, human-first constructed language with transparent semantics and Agent Skills for speaking, learning, and carefully governed evolution. **Alei** is a greeting, not the language's official name; naming is open. The source v1.0 is a working standard, not proof of natural fluency or CEFR certification. [Türkçe giriş](README.tr.md) · [Start here](docs/start-here.md) · [Standard](standard/README.md)

A: **Alei!** — Hello!  
B: **Sai süli le?** — Are you well?  
A: **Ei, mei süli.** — Yes, I am well.

The Latin-based alphabet has 28 letters, including eight vowels. **ñ** sounds like Spanish ñ; **ŋ** is the final sound in English “sing”. `ı` and `i` are distinct. The source describes `ai`, `ei`, `ae`, `au` as diphthongs and normally stresses the penultimate syllable. See the original standard §2 for details and exceptions.

Daily speech and hyphenated transparent descriptions are two uses of the same language. `meyar` means fruit; `meyar-ro-yenar-li-reş-ze-selim-mu-molir` describes a tree fruit typically red, sweet and round, but cannot uniquely identify an apple. An unknown name such as `Jajaya` requires a shared definition. This is not encryption.

## Try the tools

With Python 3.11+ in a checkout:

```sh
python -m pip install -e .
python -m alei_language.cli lookup sael
python -m alei_language.cli analyze sain
python -m alei_language.cli parse-semantic meyar-ro-yenar-li-reş-ze-selim-mu-molir
python -m alei_language.cli validate
python -m unittest discover -s tests
```

The tools are intentionally partial: a candidate parse is not an adopted word, and a successful type example does not verify the world. The checkout is required for source data. [Agent Skills](docs/how-agent-skills-work.md) describes how to use the seven procedural skills; they neither change model weights nor run on their own. Independent model and speaker evaluations remain future work.

Anyone can read, discuss a name, propose a word or report a grammar problem without coding. Once Issues and Discussions are available, use the appropriate form and give an example and source section. See [contributing](CONTRIBUTING.md), [governance](GOVERNANCE.md), [roadmap](ROADMAP.md) and [audit](docs/audits/bootstrap-audit.md). Human owner and community contributions are credited in project history; canonical changes require owner adoption.

## Licenses

Code, scripts and Agent Skills are licensed under [Apache-2.0](LICENSE). Original language prose, specifications, examples, and derived lexical data are licensed under [CC BY 4.0](LICENSE-DOCS); give appropriate credit, link the license, and indicate changes. Third-party materials retain their own terms. The language standard's original author and project contributors should be credited.
