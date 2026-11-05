# Phase 2 linguistic integrity report

Scope: the archived v1.0 standard is unchanged; its SHA-256 is pinned by the existing manifest. Source content and examples are data. No language decision in this report is adopted. The machine-readable initial review is `../../audits/sentence-audit.jsonl` and its manually authored role annotations are `../../audits/sentence-roles.tsv`; regenerate with `python scripts/build_sentence_audit.py`.

## Sentence review

The 101 source rows are linked by source ID and line, with tokenization, recorded lexical analyses or explicitly candidate analyses, word-by-word lexical gloss aids, manually assigned subject/predicate/object/other roles, markers, order, source Turkish gloss and review notes. The `valid` status means this initial review found no definite conflict with the cited working standard; it is not a proof of naturalness, lexical meaning, or independent human validation. `ambiguous` marks contextual ambiguity in 19, 35, 44 and 66. A fragment is labeled as such rather than forced into a full sentence. No source correction is silently applied. In 58 and 82 the marked object is inside the embedded action. In 93 the two predicates and subjects are recorded separately; the shared future marking requires clause-level care. All analyses, especially the gloss aid and candidate morpheme boundaries, warrant independent linguistic review; `valid` is not an automatic sentence-parser result.

The implemented deterministic clause recognizer covers only pronoun subjects, marked pronoun objects and attested verbs in SVO/SOV, optionally with `ne`, a tense and an aspect in source §4.3 order. Unsupported constructions are not judged invalid. Its successful syntactic result explicitly says semantics was not evaluated. It cannot validate all 101 sentences. Negation, tense and aspect at sentence level in the audit are surface observations; see clause-level notes for complex sentences.

## Help-root decision

See the [unadopted decision proposal](../../proposals/mirav-mivav.md). `Mivav`, its attested derivations and examples remain exactly as in the archive. The prior `Mirav` claim is reported by the owner and the architecture proposal, but no primary historical conversation is present. An owner decision and history are needed for any future change.

## Transparent meanings

The parser uses attested roots only. Its type inventory and source-derived role/head examples are deliberately incomplete; an unlisted combination is `unverified`, not automatically invalid. The source explicitly rules out literal `meyar-li-hokar`, which is rejected. Multiple typical values trigger a warning without declaring a logical contradiction. Repeated exact pairs are reported. Unknown and proposed names cannot enter through this parser. Compose/decompose preserves roles and strengths, not any proof of unique identity or real-world truth. The source describes `ro` as `source_from` and its example as `produced_by`; this distinction remains for owner review.

## Independent evaluation and limitations

`../../evaluations/` contains adversarial semantic cases and reproducible skill prompts for speak, translate, tutor and audit. No independent model, speaker study, or external skill evaluation was run; there are no model results or scores. The local skill checker is not `skills-ref`. Human feedback, source-aware review of every record, and an explicit decision on the historical root remain open. No CEFR certification or fluency result is claimed.
