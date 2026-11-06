# Alei Academic Research Workspace

This directory contains the theoretical foundation, academic literature surveys, benchmark specifications, and publication roadmap for the **Alei Language Research Initiative**.

---

## Workspace Navigation

- 📚 **[Literature Survey](literature-survey.md):** Academic survey situating Alei within current NLP research on compositional generalization (SCAN, COGS), conlang engineering (ConlangCrafter, ACL 2026), in-context machine translation (EMNLP 2025), and cross-model emergent communication.
- 📐 **[Benchmark Design (Alei-Bench)](benchmark-design.md):** Formal specification of the 6-task evaluation benchmark:
  1. Unseen compositional word interpretation.
  2. Novel morphological combination decoding.
  3. Cross-model semantic transmission fidelity.
  4. Epistemic calibration & ambiguity handling.
  5. Propositional feature preservation.
  6. Human learnability and cognitive ergonomics.
- 📝 **[Paper Outline](paper-outline.md):** Complete academic paper outline targeting ACL / EMNLP 2026–2027.
- 🗺️ **[Research Roadmap (2026–2027)](roadmap.md):** Chronological milestones spanning Phase R1 (completed pilot audit) through Phase R5 (conference submission and public dataset release).

---

## Research Principles

1. **Human-First Ergonomics:** Alei is an expressive literary language designed for human cognition, not a synthetic vector-space dialect.
2. **Deterministic Verification:** Lexicon lookups, AST parsers, and valency schemas are deterministic software tools. Passing software tests is not conflated with natural human fluency.
3. **Zero-Fabrication Policy:** All benchmark results must stem from documented, reproducible model sessions. Missing or unrun splits remain marked `not_run`.
