# Maintainer review checklist — v1.1.0 release candidate

- [ ] Review owner decisions AD-2026-001 and AD-2026-002, their date and historical-evidence distinction.
- [ ] Run `python scripts/derive_data.py --check` and `python scripts/derive_v11.py --check`; compare source checksum.
- [ ] Run `python scripts/build_sentence_audit.py --check`, `python scripts/validate_skills.py`, and `python -m unittest discover -s tests`.
- [ ] Verify preferred and legacy lookup, warnings, historical examples, and unchanged implicit v1.0 API default.
- [ ] Confirm Mivavar remains historical/pending and Miravar is not owner-adopted.
- [ ] Review versioned docs, manifest hashes, PR and GitHub CI. Do not close historical issues or discussion prematurely.
- [ ] Obtain integration review before merge or any final public release/tag.
