# Changelog

All meaningful DEDAL Core architectural and behavioral changes should be recorded here.

## 0.4.0 — 2026-09-14

### Added
- DEDAL-native Knowledge Archive skill at `skills/ika/` with `$ika` routing.
- Public archive, retrieval, relationship/change-impact, and orchestration contracts derived from the earlier IANEO Knowledge Archive experience.
- `ADAPTATION_NOTES.md` documenting provenance and deliberate differences from the private legacy source.

### Changed
- `$ika` is now active instead of planned.
- The legacy IANEO archive design was refined rather than copied verbatim: fixed IANEO destinations, IANEO-only identity wording, and assumed orchestration behavior were removed/generalized.
- Writing Chamber and Image Visualization Chamber are no longer treated as default knowledge-archive responsibilities; they remain historical/private experiments unless later promoted as separate DEDAL skills.
- Private archives, registry contents, scripts, fixtures, and project data remain outside the public DEDAL Core repository.

### Adaptation provenance
- Source repository: private `Ye-Shwethway/ianeo-knowledge-vault`
- Source commit: `fbed860928c1a93261306f70a47fa700da56ce29`
- Legacy source path: `skills/ianeo-knowledge-archive/`

## 0.3.0 — 2026-09-14

### Added
- Formal Stable Kernel directory with `KERNEL.md`, `BOOT_CONTRACT.md`, and `STATE_BOUNDARY.md`.
- First native generic DEDAL skill entrypoints for GitHub, Files & Artifacts, Research, Software Development, and Automations.
- Integrity validation for kernel files, active generic skill entrypoints, and semantic version format.

### Changed
- `MASTER_INDEX.md` now boots through the formal kernel before routing to skills.
- `SKILL_REGISTRY.yaml` version 2 registers the five generic skills as active instead of scaffolds.
- Generic skills are intentionally provider-agnostic and verify current execution surfaces before acting.

## 0.2.0 — 2026-09-13

### Added
- Reconstructed BIOS/bootstrap architecture for Custom Instructions -> DEDAL Core -> master index routing.
- Stable-kernel / growable-skills / operations-layer model.
- `index/SKILL_REGISTRY.yaml` as a machine-readable routing registry.
- Full pinned snapshots of Medicine Store Assistant (`$msa`) and Patient Report Assistant (`$pra`).
- Import provenance records for both migrated skills.
- Integrity checks for the master index, skill registry, skill entrypoints, provenance files, agent metadata, and minimum reference-package completeness.

### Changed
- DEDAL Core now has its first real growable skill layer rather than only scaffolding.
- Skill routing prefers explicit aliases and loads references on demand to reduce prompt/context bloat.

### Migration provenance
- Source repository: `Ye-Shwethway/medicine-store-assistant`
- Source commit: `6b8f35e4056f030a1ace2dac137cde1071a00051`
- Imported packages: `skills/medicine-store-assistant/`, `skills/patient-report-assistant/`

## 0.1.0 — 2026-09-13

Initial DEDAL Core foundation: identity, operating contract, security boundary, capability registry, continuity checkpoint, improvement protocol, foundational architecture, and repository integrity workflow.
