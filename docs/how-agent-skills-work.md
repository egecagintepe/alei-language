# Agent Skills

A skill is a set of instructions and supporting references loaded by a compatible agent, not a model weight update or an autonomous background service. The seven skill directories live in `.agents/skills/`; run a compatible client from this checkout. Other clients may require copying the repository and configuring their skill directory; preserve the repository layout and relative links. Consult that client's install documentation. Their behavior and permissions vary. Use `python scripts/validate_skills.py` to check local metadata; this does not establish model performance.
