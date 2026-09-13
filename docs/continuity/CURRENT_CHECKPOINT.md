# Current Checkpoint

_Date: 2026-09-13_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.2.0`
- Purpose: durable public operational core for DEDAL

## Foundation Established

The core foundation now includes:

- `README.md` — purpose and repository map;
- `AGENTS.md` — operating contract and source-of-truth hierarchy;
- `SECURITY.md` — public-repository security boundary;
- `CHANGELOG.md` — versioned architectural history;
- `docs/IDENTITY.md` — stable DEDAL identity definition;
- `docs/architecture/FOUNDATION.md` — layered system architecture;
- `docs/architecture/BIOS_AND_LAYER_MODEL.md` — Custom Instructions BIOS pointer, Stable Kernel, Growable Skills, and Operations layer model;
- `docs/capabilities/CURRENT_CAPABILITIES.md` — current capability snapshot;
- `docs/evolution/IMPROVEMENT_PROTOCOL.md` — externalized self-improvement loop;
- `state/capability-registry.yaml` — sanitized machine-readable capability registry;
- `index/MASTER_INDEX.md` — human-readable boot and skill router;
- `index/SKILL_REGISTRY.yaml` — machine-readable skill routing and provenance registry;
- `.github/workflows/repo-integrity.yml` — structural, YAML, secret-file, and imported-skill validation.

The temporary write-capable migration workflow used to import legacy skills was removed after successful verification. It is not part of the permanent runtime surface.

## Active Imported Skills

### Medicine Store Assistant

- Invocation: `medicine-store-assistant` or `$msa`
- Path: `skills/medicine-store-assistant/`
- Imported from: `Ye-Shwethway/medicine-store-assistant`
- Pinned source commit: `6b8f35e4056f030a1ace2dac137cde1071a00051`
- Package includes `SKILL.md`, `agents/openai.yaml`, provenance, and the complete pinned task-specific reference set.

### Patient Report Assistant

- Invocation: `patient-report-assistant` or `$pra`
- Path: `skills/patient-report-assistant/`
- Imported from: `Ye-Shwethway/medicine-store-assistant`
- Pinned source commit: `6b8f35e4056f030a1ace2dac137cde1071a00051`
- Package includes `SKILL.md`, `agents/openai.yaml`, provenance, and the complete pinned task-specific reference set.
- PRA remains operationally independent from MSA despite sharing the historical source repository.

Both imported directories contain `IMPORT_SOURCE.md` provenance records. Future updates must compare against the recorded source commit before replacing local files.

## Locked Principles

1. DEDAL Core is public architecture, not a private-memory dump.
2. Live authoritative state outranks remembered summaries.
3. Custom Instructions act as a small BIOS/bootstrap pointer rather than containing the whole DEDAL system.
4. Stable kernel material stays small; growable skills stay modular; operational execution surfaces stay replaceable.
5. Load the smallest relevant skill set instead of loading all skills into every task.
6. Explicit skill aliases such as `$msa` and `$pra` are direct routing signals.
7. Model weights are not treated as self-modifiable by DEDAL; improvement occurs through context, tools, skills, persistent state, evaluations, workflows, automation, and feedback loops.
8. Sensitive/private state remains external and explicitly authorized.
9. Work/cloud-computer capability is useful but quota-expensive and is not an always-on dependency.
10. Changes should remain inspectable, attributable, versioned, and reversible where practical.
11. Imported skills are pinned snapshots, not silently auto-synced mirrors.

## Verification State

- Pinned MSA/PRA migration workflow run: PASS.
- Exact imported-tree comparison against pinned source: PASS.
- MSA reference package: complete pinned reference tree.
- PRA reference package: complete pinned reference tree.
- Human and machine-readable skill registries route `$msa` and `$pra` to their canonical DEDAL Core packages.
- Permanent repo-integrity workflow now validates both core and imported-skill structure.

## Immediate Next Phase

1. Finalize the Stable Kernel files and boot contract.
2. Create the smallest useful native DEDAL sub-skills for GitHub, Files/Artifacts, Research, Software Development, and Automations rather than leaving them as scaffolds.
3. Bring IKA into the same canonical skill architecture after inspecting its current source package.
4. Draft the concise Custom Instructions BIOS pointer only after reviewing the Creator's current Custom Instructions text.
5. Add regression/evaluation checks as repeated real-world failures reveal durable lessons.

Do not build a large agent swarm or private-state backend merely because the architecture permits it. Add infrastructure only when a concrete workflow benefits from it.
