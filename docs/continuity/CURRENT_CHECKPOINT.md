# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.4.0`
- Purpose: durable public operational core for DEDAL

## Architecture State

DEDAL Core has four working layers:

1. BIOS pointer in the Creator's Custom Instructions.
2. Stable Kernel in `AGENTS.md`, `docs/IDENTITY.md`, and `kernel/`.
3. Master routing via `index/MASTER_INDEX.md` and `index/SKILL_REGISTRY.yaml`.
4. Modular skills executed through currently available native tools, plugins/MCP, sandbox, GitHub Actions, external runners, or automations.

## Active Domain Skills

- `$msa` -> `skills/medicine-store-assistant/`
- `$pra` -> `skills/patient-report-assistant/`
- `$ika` -> `skills/ika/`

`$ika` is a DEDAL-native adaptation of the earlier private IANEO Knowledge Archive, not a verbatim public copy. The proven archive mechanics were retained while IANEO identity/runtime assumptions and private state were removed.

## Active Generic Skills

- GitHub -> `skills/github/SKILL.md`
- Files & Artifacts -> `skills/files/SKILL.md`
- Research -> `skills/research/SKILL.md`
- Software Development -> `skills/software-development/SKILL.md`
- Automations -> `skills/automations/SKILL.md`

## IKA Alignment Decisions

Preserved:

- live/primary state outranks summaries/memory;
- evidence-linked atomic records and stable IDs;
- Git-backed canonical provenance/history;
- bounded deterministic retrieval;
- preserved disputes/supersession rather than destructive rewriting;
- one-hop linked knowledge/change-impact review;
- serialized canonical mutation and read-back verification;
- truthful runtime capability reporting.

Refined/removed from the default `$ika` skill:

- IANEO-specific identity and `IANEO Core` promotion wording;
- fixed `IANEO Knowledge Archives` destinations;
- assumptions about native worker availability;
- Writing Chamber and Image Visualization Chamber as archive-core responsibilities;
- private scripts, fixtures, archives, registry contents, and project data.

The private legacy repository remains historical implementation/reference state.

## Routing Principles

- Load the smallest matching skill set.
- `$msa`, `$pra`, and `$ika` route directly to their entrypoints.
- Load references on demand, not globally.
- Generic skills remain provider-agnostic and verify the current execution surface before acting.
- Platform/system instructions outrank repository skill guidance when they conflict.
- Project/archive knowledge does not automatically become DEDAL Kernel behavior.

## Verification

`repo-integrity.yml` validates foundational/kernel files, secret-bearing filenames, YAML registries, all active skill entrypoints, MSA/PRA provenance/package structure, `$ika` adaptation/provenance/reference structure, and semantic version format.

## Next Phase

1. Use the three active domain skills in real workflows and capture failures/regressions as tests or durable rules.
2. Decide whether legacy Writing/Image Chambers deserve separate DEDAL skills only when a concrete workflow needs them.
3. Add further skills only when repeated real work justifies them.
4. Keep private/personal/project operational state outside the public core.

Do not expand the Stable Kernel merely to capture preferences or project-specific rules; route them into the correct skill/project/state layer.
