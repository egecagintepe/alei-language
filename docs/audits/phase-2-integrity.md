> Historical report: statements about the then-open name/help decision describe the time of this report. See [owner decisions](../../governance/decisions/README.md) for the adopted v1.1.0 status.

# Phase 2.1 linguistic integrity review

The v1.0 archive remains unchanged and its SHA-256 is pinned by `standard/manifest.json`. No correction in this report is adopted. The [machine-readable review](../../audits/sentence-audit.jsonl) contains all 101 source IDs and lines; [role annotations](../../audits/sentence-roles.tsv) and [individual review assessments](../../audits/sentence-review.tsv) are inputs to `python scripts/build_sentence_audit.py`. Each assessment is authored by the project assistant against v1.0; it is not an independent human or speaker evaluation.

## Three separate outcomes

- `parser_status` describes only the extended deterministic recognizer. It parsed 71 examples and returned `unsupported` for 30. Unsupported does not mean ungrammatical. A parsed structure does not validate its interpretation or translation.
- `linguistic_review_status` records the assistant's source comparison of morphology, roles, syntax, interpretation and cross-example usage. It found 97 consistent with the working standard and identified context-dependent interpretation in 19, 35, 44 and 66. These are review judgments, not certified speaker usage.
- `translation_review_status` records the separate source-gloss review: 92 are assessed as accurate in context, while 19, 35, 44, 53, 56, 66, 67, 88 and 89 have a contextual reading or implicit information. Context dependence is not an error.

Each record includes the source spelling, tokens, possible segmentation, role annotations, tense/aspect/negation observations, literal component glosses, source Turkish translation, individually authored assessment, evidence and a correction field. A missing correction means no concrete replacement was proposed, not that the source has been proven error-free. Embedded objects in 58 and 82 belong to the inner verbs; 93 has two future clauses. The reviewer does not infer a specific object in 35 or automatically identify the addressee with Elora in 66. Word-by-word glosses are mechanical aids, not independent translations. Another linguist should review the judgments, particularly unresolved segmentation and pragmatics.

`status` and `deterministic_structure` are retained as legacy Phase 2 fields to preserve prior consumers and tests. They refer to the older narrow `parse_clause` routine, not the new parser or either review outcome. New consumers should use the three named fields above. `parse_sentence`/CLI `parse-sentence` recognizes a bounded set of source-supported nominal and location predicates, possession phrases, questions, marked noun objects and `ke` complements; other constructions remain unsupported. Semantic correctness is explicitly not evaluated by the parser.

## Mirav and Mivav

The owner now reports that the earlier proposed root was Mirav, derived verb Miraven, the vocabulary group received positive approval, and Mivav apparently appeared during consolidation. The historical transcript remains unavailable. The [v1.1-proposed correction and migration](../../proposals/mirav-mivav.md) recommends Mirav and Miraven and describes Mivav, Mivaven, Mivavar, examples, records and regression tests. Nothing is adopted until the owner explicitly approves the version and compatibility policy. Existing v1.0 lookups remain unchanged.

## Semantics and evaluation

Role type examples remain intentionally incomplete; unlisted types are unverified, and `meyar-li-hokar` is the source's explicit literal mismatch. The red/sweet/round tree-fruit description does not prove apple identity. The benchmark contains 28 reproducible prompts, including dialogue, complement clauses, ambiguous translations, morphology, literary language, unknown words and semantic decomposition. No independent model outputs, human linguistic judgments, scores, speaker trials or CEFR claim have been generated. See [evaluation instructions](../../evaluations/README.md).
