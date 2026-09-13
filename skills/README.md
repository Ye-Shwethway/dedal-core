# DEDAL Skills

Skills are modular, growable instruction packages loaded through `index/MASTER_INDEX.md`.

A skill should normally contain:
- `SKILL.md` — purpose, triggers, workflow, constraints;
- optional `references/` — stable reference material;
- optional `schemas/` — machine-readable contracts;
- optional `scripts/` — supporting automation or validation;
- optional `tests/` — regression checks.

Skills should not contain credentials, private memories, or sensitive operational data.

The stable kernel should not absorb domain-specific instructions merely because a skill becomes important. Importance and stability are different concerns.
