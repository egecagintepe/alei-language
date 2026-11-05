# Help-root correction proposal: Mirav (not adopted)

**Status:** proposal, language target **v1.1-proposed**; software version is separate. This is a recommendation and migration design, not an owner decision to adopt it. The original v1.0 archive and its hash remain unchanged.

## Evidence

On 5 November 2026 the owner reported from the original language-design conversation that the originally proposed help root was **Mirav**, its derived verb **Miraven**, that the owner positively accepted the original vocabulary group, and that **Mivav** apparently appeared later during consolidation. This is owner-reported conversation evidence; the archived transcript has not been supplied, so its wording and chronology cannot be independently checked. The architectural proposal also reports a Mirav/Mivav discrepancy. v1.0 §7.2 line 520 records `Mivav` as `owner_accepted_working`, §8.1 line 800 records `Mivaven`, and §8.3 line 929 records `Mivavar`. §4.5 line 180 and examples 64–65, lines 1208–1209, attest `mivaven` with a direct person object.

## Recommendation

Prefer **Mirav** and the owner-reported derived **Miraven** in a prospective v1.1 correction, subject to explicit owner approval, source evidence and tests. Do not silently present either as adopted in the v1.0 registry. This recommendation is not acceptance. A candidate agent noun `Miravar` follows the existing derivational pattern but is a *new proposal*, not an attested or automatically accepted form. Check the near form `Mürav` (storage, v1.0 §7.10) and `Mir` (smallness, §7.2) for listening and spelling confusion; resemblance alone neither changes their meanings nor proves a collision.

## Proposed compatibility contract, subject to owner approval

1. Keep v1.0 `Mivav`, `Mivaven`, `Mivavar`, all v1.0 examples and derived JSONL intact in the pinned archive. Existing v1.0 lookup and translation remain reproducible.
2. In a separate v1.1 registry, propose Mirav and Miraven as preferred forms. Preserve Mivav and Mivaven as explicitly labeled **legacy aliases** with versioned provenance, rather than silently redirecting or deleting them. Alias status, meaning, display warnings and the end of any transition require owner approval; they do not apply yet.
3. Record v1.0 `Mivavar` unchanged. Propose whether it should remain a legacy agent noun and whether `Miravar` should be adopted as its replacement. Do not mark Miravar canonical solely by derivation.
4. Prepare new-version examples equivalent to v1.0 #64–65 using the approved future form; retain source quotations unchanged and cite their version. Review each glossary, documentation, agent skill, search index, source-derived record, example, schema, test fixture and translation mentioning either form. Preserve historical IDs and attach new versioned IDs instead of mutating old ones.
5. Before any adoption, test v1.0 exact lookups and existing `Mivav` regressions, v1.1 preferred and legacy lookup behavior, case/object inflection, both example translations, search results and provenance. Never treat an alias as an owner-locked root or fabricate agreement from CI.
6. If backward-compatible alias behavior is approved, v1.1 is a proposed compatible version. If the owner instead removes old forms or changes their accepted meaning, treat this as potentially breaking and choose a major version and migration schedule through a separate owner decision. No automatic deprecation or removal deadline is proposed.

## Decision and alternatives

Ask the owner to approve or reject the preferred spelling, Miraven, alias policy, proposed Miravar, version and transition separately in a recorded decision. Alternatives remain retaining the v1.0 spelling or accepting both as distinct/synonymous forms with explicit sense records. Until then only the unchanged v1.0 data is authoritative for that snapshot.
