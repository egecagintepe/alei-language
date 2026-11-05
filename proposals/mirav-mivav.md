# Historical help root: decision proposal (not adopted)

Status: proposal; no spelling change or synonym has been adopted. The user reports that historical design conversations favored `Mirav`. The earlier conversation is not present in the repository, so this is a report of history rather than independently verified approval. Architecture proposal §1.7 also reports an apparent `Mirav` → `Mivav` discrepancy. The supplied v1.0 standard is the only available authoritative snapshot and records `Mivav` as owner_accepted_working at §7.2, line 520. It records `Mivaven` (§8.1, line 800), `Mivavar` (§8.3, line 929), and explicitly permits direct-person objects in §4.5, line 180. Examples 64 and 65 (lines 1208–1209) use `mivaven`. Derived data IDs are `roots:520`, `lexemes:800`, `lexemes:929`, `example-sentences:1208`, and `example-sentences:1209`. The existing regression `tests/test_project.py::test_attested_words` checks Mivav; no source-attested Mirav form is currently registered.

## Options for owner decision

1. Retain Mivav in a future standard; record the historical evidence and rationale.
2. Adopt Mirav in a separately versioned standard with an explicit compatibility and migration policy for Mivav, Mivaven, Mivavar, examples, source-derived data, references, search and tests. Whether an old form remains accepted or deprecated must be separately decided; neither is assumed.
3. Adopt both only if the owner specifies whether they are synonyms or distinct senses and how lookup and translation distinguish them.

All options preserve the immutable v1.0 snapshot. Request the historical primary source and explicit owner decision before updating any canonical language record. Existing conversations and models using Mivav could otherwise fail exact lookup or lose meaning; a new form cannot silently replace it. Candidate derived forms based on Mirav require separate linguistic validation, and are not adopted by this proposal.
