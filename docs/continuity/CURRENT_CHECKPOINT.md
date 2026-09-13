# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.3.0`
- Purpose: durable public operational core for DEDAL

## Architecture State

DEDAL Core now has four working layers:

1. BIOS pointer in the Creator's Custom Instructions.
2. Stable Kernel in `AGENTS.md`, `docs/IDENTITY.md`, and `kernel/`.
3. Master routing via `index/MASTER_INDEX.md` and `index/SKILL_REGISTRY.yaml`.
4. Modular skill packages executed through currently available native tools, plugins/MCP, sandbox, GitHub Actions, external runners, or automations.

## Stable Kernel

Formalized files:

- `kernel/KERNEL.md` — invariants and constitutional references;
- `kernel/BOOT_CONTRACT.md` — minimal boot/recovery sequence;
- `kernel/STATE_BOUNDARY.md` — public-core/private-state ownership rules.

Kernel changes are intentionally held to a higher standard than skill changes.

## Active Skills

Imported standalone domain skills:

- `$msa` -> `skills/medicine-store-assistant/`
- `$pra` -> `skills/patient-report-assistant/`

Native generic DEDAL skills:

- GitHub -> `skills/github/SKILL.md`
- Files & Artifacts -> `skills/files/SKILL.md`
- Research -> `skills/research/SKILL.md`
- Software Development -> `skills/software-development/SKILL.md`
- Automations -> `skills/automations/SKILL.md`

`$ika` remains planned pending inspection of its current source package.

## Routing Principles

- Load the smallest matching skill set.
- Explicit aliases route directly to their skill entrypoints.
- Load references on demand, not globally.
- Generic skills remain provider-agnostic and must verify the current execution surface before acting.
- Platform/system instructions outrank repository skill guidance when they conflict.

## Verification

`repo-integrity.yml` validates:

- foundational/kernel files;
- obvious secret-bearing filenames;
- YAML registries;
- all active skill entrypoints;
- imported MSA/PRA package structure and provenance;
- semantic version format.

## Next Phase

1. Inspect and import/normalize IKA into `skills/ika/` if its current architecture remains useful.
2. Add focused references/sub-skills only when real workflows justify them.
3. Add evaluation/regression fixtures from observed failures rather than speculative tests.
4. Continue keeping private/personal operational state outside the public core.

Do not expand the Stable Kernel merely to capture preferences or project-specific rules; route those into the correct skill/project/state layer.
