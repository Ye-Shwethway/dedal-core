# Changelog

All meaningful DEDAL Core architectural and behavioral changes should be recorded here.

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
