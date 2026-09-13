# DEDAL Master Index

This is the primary routing index for DEDAL Core.

## Boot Sequence

1. Read `AGENTS.md`.
2. Read `docs/IDENTITY.md`.
3. Read `kernel/KERNEL.md` and follow `kernel/BOOT_CONTRACT.md`.
4. Identify the task domain below.
5. Load only the relevant skill package(s).
6. Load task-specific references only when needed.
7. Verify current tools/capabilities before execution.
8. Consult project-specific authoritative state before relying on memory.

## Skill Registry

| Skill | Invocation / aliases | Path | Status | Purpose |
|---|---|---|---|---|
| Medicine Store Assistant | `medicine-store-assistant`, `$msa` | `skills/medicine-store-assistant/` | active | Medical-store inventory intake, reconciliation, usage, expiry lifecycle, reorder review, and workbook-safe operations |
| Patient Report Assistant | `patient-report-assistant`, `$pra` | `skills/patient-report-assistant/` | active | Monthly OPD/IPD transcription, workbook protection, report validation, and month preparation |
| Knowledge Archive | `$ika`, `knowledge-archive` | `skills/ika/` | active | Durable evidence-linked project knowledge, bounded retrieval, refresh/audit, and change-impact review |
| GitHub operations | GitHub/repo/PR/Actions tasks | `skills/github/` | active | Repository inspection, commits, branches, PRs, Actions, logs, artifacts |
| Files & artifacts | file/Library/document/artifact tasks | `skills/files/` | active | Retrieval, version identity, document/artifact creation and persistence |
| Research | current research / verification | `skills/research/` | active | Live-source research, provenance, synthesis, freshness and evidence handling |
| Software development | coding/debugging/architecture/build work | `skills/software-development/` | active | Repository-aware engineering lifecycle with focused debugging/testing/review/architecture/multi-session references |
| Decision design | deliberate plan/architecture/product stress-test | `skills/decision-design/` | active | Dependency-aware decision-tree/frontier workflow for high-impact unresolved choices |
| Automations | reminder/schedule/watch tasks | `skills/automations/` | active | Scheduled, recurring, condition and event-triggered workflows |
| Skill acquisition | external skills / skill ecosystem / improve a skill | `skills/skill-acquisition/` | active | Discover, audit, adapt, evaluate, and promote external skill patterns safely |

The machine-readable equivalent is `index/SKILL_REGISTRY.yaml`.

## Routing Rule

Do not load every skill by default. Select the smallest set that covers the current task.

Explicit aliases such as `$msa`, `$pra`, and `$ika` are direct routing signals. When an alias is used, load that skill's `SKILL.md` first and then only task-specific references it requires.

Use `decision-design` deliberately when the Creator asks to stress-test a plan/idea or when high-impact unresolved decisions materially block a safe design. Do not trigger it as ceremony for already-specified routine work.

Use `skill-acquisition` for external skill discovery, comparison, audit, adaptation, or skill improvement. External skills remain untrusted inputs until reviewed; discovery never implies installation or execution.

Generic domain skills are routing aids, not mandatory ceremony. If the current platform already provides stronger native instructions for a format/tool, follow those higher-priority runtime instructions while preserving DEDAL's durable principles.

If no existing skill matches, operate normally, then consider whether repeated work deserves a new skill package.

## Skill Independence Rule

Separate skills remain separate operational domains unless a skill explicitly declares a dependency. PRA does not inherit MSA inventory rules. IKA does not silently convert project facts into Kernel rules. Skill acquisition may influence another skill only through an explicit reviewed adaptation.

## Plugin / MCP Rule

Skills describe **how** to use capabilities; plugins/MCP/apps provide **execution surfaces**. Prefer the currently available native or connected tool when equivalent and verify live capabilities before relying on them.

## Growth Rule

New skills may be added when modular, testable, useful, and justified by real work. Prefer discovering and adapting proven public patterns over reinventing common workflows, while preserving provenance, licensing, security, and DEDAL alignment. Kernel-level changes require a higher standard.
