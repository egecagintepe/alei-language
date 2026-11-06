# v1.0 → v1.1.0 migration

Pin version explicitly. Existing scripts using `lookup(word)`, `analyze(word)` or a CLI command without `--version` continue using v1.0; that default has not changed. Use `--version 1.1.0` or `--version current` for the new interpretation. The `current` selector follows `standard/current.json`, so use a numeric version for reproducibility. `parse-semantic` remains the v1.0 semantic parser; this release changes no semantic roles.

```sh
python scripts/derive_data.py --check
python scripts/derive_v11.py --check
python -m alei_language.cli lookup Mirav --version 1.1.0
python -m alei_language.cli lookup Mivav --version 1.1.0
python -m alei_language.cli parse-sentence "Mei miraven sain." --version 1.1.0
```

Historical text `Mei mivaven sain.` remains recognizable. In v1.1.0 it produces a legacy warning; `Mei miraven sain.` uses the preferred form. Both convey the source's “Sana yardım ediyorum” reading, subject to context. Historical source text, source line and ID are retained, never silently rewritten. `Miravar` has no adopted exact entry; `Mivavar` is separately pending. An inferred morphology candidate is not an adopted lexeme.

Verify `data/versions/1.1.0/manifest.json` and the source checksum; do not replace v1.0 source IDs with new IDs. Test import consumers with their selected snapshot before any future change to the API default.
