# DEDAL Master Index

This is the primary human-readable routing index for DEDAL Core. The machine-readable companion is [`SKILL_REGISTRY.yaml`](SKILL_REGISTRY.yaml).

## Boot Sequence

1. Read `AGENTS.md`.
2. Read `docs/IDENTITY.md`.
3. Read `docs/architecture/BIOS_AND_LAYER_MODEL.md` when architectural context is needed.
4. Read this master index and consult `index/SKILL_REGISTRY.yaml` for exact aliases, paths, status, and provenance.
5. Identify the task domain.
6. Load only the relevant skill package(s).
7. Verify current tools/capabilities before execution.
8. Consult project-specific authoritative state before relying on memory.

## Skill Registry

| Skill | Invocation / aliases | Path | Status | Purpose |
|---|---|---|---|---|
| Medicine Store Assistant | `medicine-store-assistant`, `$msa` | `skills/medicine-store-assistant/` | active / imported | Medical-store inventory intake, reconciliation, usage, expiry lifecycle, reorder review, and workbook-safe operations |
| Patient Report Assistant | `patient-report-assistant`, `$pra` | `skills/patient-report-assistant/` | active / imported | Monthly OPD/IPD transcription, workbook protection, report validation, and month preparation |
| GitHub operations | — | `skills/github/` | scaffold | Repository inspection, commits, branches, PRs, Actions, artifacts |
| Files & artifacts | — | `skills/files/` | scaffold | Library, document, spreadsheet, PDF, artifact workflows |
| Research | — | `skills/research/` | scaffold | Current web research, source synthesis, evidence handling |
| Software development | — | `skills/software-development/` | scaffold | Architecture, coding, testing, build orchestration |
| Automations | — | `skills/automations/` | scaffold | Scheduled and condition-triggered workflows |
| Knowledge archive | `$ika` | `skills/ika/` | planned | Integration patterns and reusable knowledge-archive workflows derived from IKA experience |

## Routing Rule

Do not load every skill by default. Select the smallest set that covers the current task.

Explicit aliases such as `$msa`, `$pra`, or future `$ika` are direct routing signals. When an alias is used, load that skill's `SKILL.md` first and then only the task-specific references it requires.

If no existing skill matches, operate normally, then consider whether the repeated task deserves a new skill package.

## Imported Skill Rule

Imported skill packages are snapshots, not live mirrors. Their `IMPORT_SOURCE.md` records the source repository and pinned source commit. Before replacing an imported package, compare against that provenance so local DEDAL-specific evolution is not overwritten accidentally.

## Skill Independence Rule

Separate skills remain separate operational domains unless a skill explicitly declares a dependency. In particular, Patient Report Assistant does not inherit Medicine Store Assistant inventory rules merely because both originated in the same source repository.

## Plugin / MCP Rule

Skills describe **how** to use capabilities; plugins/MCP/apps provide **execution surfaces**. A skill may reference more than one provider and should prefer the currently available native or connected tool when equivalent.

## Growth Rule

New skills may be added freely when they are modular, testable, and useful. Kernel-level changes require a higher standard because they affect all future tasks.
