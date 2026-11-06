# Alei language v1.1.0 release candidate

The owner adopted the name **Alei** and the preferred help forms **Mirav** (help) and **Miraven** (to help) on 2026-11-05, decisions AD-2026-001 and AD-2026-002. The greeting `Alei!` retains its meaning. This is a language version, separate from software 0.1.0. The RC does not change grammar or other roots.

The versioned overlay is [`standard/versions/1.1.0.json`](../standard/versions/1.1.0.json); reproducibly generated data and hashes are in [`data/versions/1.1.0/`](../data/versions/1.1.0/). The immutable v1.0 file and its original data are unchanged. `current` explicitly selects 1.1.0. **For compatibility, an omitted CLI/API version still selects 1.0**; any future default change requires release communication and compatibility review.

- `Mirav` and `Miraven`: owner-adopted preferred forms in v1.1.0.
- `Mivav` and `Mivaven`: recognized v1.0 legacy aliases with explicit warnings and historical IDs; not extra v1.1 canonical roots.
- `Mivavar`: historical v1.0 agent noun, v1.1 treatment unresolved; recognized as `historical_v1_pending`, not a preferred alias.
- `Miravar`: not owner-adopted. `Mir` (smallness) and `Mürav` (storage) remain separate; similarity requires listening tests, not semantic changes.

The generated view contains 270 roots, 273 current lexeme rows and three separate compatibility records (two aliases plus Mivavar pending). The v1.0 source still has 270 roots and 274 derivative/compound records. The one-row difference reflects the unresolved Mivavar treatment, not deletion of the historical record. See [migration](migration-v1.0-v1.1.md) and [decisions](../governance/decisions/README.md).

The manifest hashes generated JSONL as UTF-8/LF. The overlay, decision and inherited-function text hashes are normalized to UTF-8/LF without BOM for cross-platform reproduction; the archived v1.0 source hash is over its original bytes.
