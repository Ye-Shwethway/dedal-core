# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.5.0`
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

## Active Generic / Meta Skills

- GitHub -> `skills/github/SKILL.md`
- Files & Artifacts -> `skills/files/SKILL.md`
- Research -> `skills/research/SKILL.md`
- Software Development -> `skills/software-development/SKILL.md`
- Automations -> `skills/automations/SKILL.md`
- Skill Acquisition -> `skills/skill-acquisition/SKILL.md`

## Skill Acquisition Phase

DEDAL no longer treats skill development as an isolated from-scratch exercise. Public Agent Skills standards, vendor examples, mature GitHub repositories, and registries such as ClawHub/skills.sh may be used as discovery inputs.

External skills remain untrusted until reviewed. The active pipeline is:

`capability gap -> discover -> shortlist -> security/license/provenance audit -> extract patterns -> DEDAL adaptation -> evaluation -> promote/reject -> regression capture`

Key policy: **reuse ideas; do not inherit trust blindly.**

The first benchmark is recorded in `skills/skill-acquisition/references/initial-benchmark-2026-09-14.md`.

## First Benchmark Changes

Software Development, GitHub, and Research were the first generic skills refined from the public ecosystem survey.

Accepted patterns include:

- progressive disclosure and focused skill entrypoints;
- scalable engineering lifecycle gates rather than ad-hoc coding;
- root-cause-first debugging;
- exact-diff/final-artifact review;
- fresh evidence before completion claims;
- source provenance captured during research;
- primary-source preference, proportional triangulation, and visible evidence gaps;
- semantic security/privacy review in addition to malware/static scanning.

Rejected patterns include:

- global mandatory skill invocation on weak relevance;
- automatic install/execute of discovered third-party packages;
- fixed worker/subagent assumptions;
- treating stars/install counts/registry badges/scanner results as trust;
- copying provider-specific runtime syntax into durable DEDAL contracts without need.

## Routing Principles

- Load the smallest matching skill set.
- `$msa`, `$pra`, and `$ika` route directly to their entrypoints.
- Use `skill-acquisition` for external skill discovery, comparison, audit, adaptation, or skill improvement.
- Load references on demand, not globally.
- Generic skills remain provider-agnostic where practical and verify current execution surfaces before acting.
- Platform/system instructions outrank repository skill guidance when they conflict.
- Project/archive knowledge does not automatically become DEDAL Kernel behavior.

## Verification

`repo-integrity.yml` validates foundational/kernel files, secret-bearing filenames, YAML registries, all active skill entrypoints, MSA/PRA provenance/package structure, `$ika` adaptation/provenance/reference structure, Skill Acquisition references, and semantic version format.

Fresh-chat bootstrap E2E test: **PASS**.

- Regression spec/evidence: `evals/boot/minimal-bootstrap-v1.md`
- Re-run after bootstrap, kernel, routing, or repository-layout changes.

## Next Phase

1. Use `skill-acquisition` against concrete repeated DEDAL capability gaps rather than catalog-browsing for its own sake.
2. Continue benchmarking generic skills when a better public pattern is found, with accepted/rejected decisions recorded.
3. Build evaluation fixtures for major skill rewrites before replacing proven behavior.
4. Consider new skills such as separate Writing/Visual evolution only when repeated workflows justify them.
5. Keep private/personal/project operational state outside the public core.

Do not expand the Stable Kernel merely to capture preferences, ecosystem fashions, or project-specific rules; route them into the correct skill/project/state layer.
