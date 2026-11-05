# Grammar

Source §4 specifies gender-neutral Mei, Sai, Eli and respectful Elar; optional honorifics follow names. `-en` derives verbs, `-i` qualities, `-na` plural; objects take `-n` after vowels and `-an` after consonants. SVO and object-focused SOV are both permitted. Exact root lookup precedes suffix analysis.

See [the source](../standard/README.md) and [audit](audits/bootstrap-audit.md).
## Bounded sentence parsing

`python -m alei_language.cli parse-sentence "Sai yelen ke sileven tüvanan le?"` recognizes certain v1.0 patterns and records the embedded object separately. It returns `unsupported` for constructions it cannot analyze; that is not a grammar error. `semantic_correctness` remains `not_evaluated`. The original `parse-clause` command retains its narrower behavior. See [the review](audits/phase-2-integrity.md) for sentence-by-sentence human-independent and parser limitations.
