# DEDAL Master Index

This is the primary routing index for DEDAL Core.

## Boot Sequence

1. Read `AGENTS.md`.
2. Read `docs/IDENTITY.md`.
3. Read `docs/architecture/BIOS_AND_LAYER_MODEL.md` when architectural context is needed.
4. Identify the task domain below.
5. Load only the relevant skill package(s).
6. Verify current tools/capabilities before execution.
7. Consult project-specific authoritative state before relying on memory.

## Skill Registry

| Skill | Path | Status | Purpose |
|---|---|---|---|
| GitHub operations | `skills/github/` | scaffold | Repository inspection, commits, branches, PRs, Actions, artifacts |
| Files & artifacts | `skills/files/` | scaffold | Library, document, spreadsheet, PDF, artifact workflows |
| Research | `skills/research/` | scaffold | Current web research, source synthesis, evidence handling |
| Software development | `skills/software-development/` | scaffold | Architecture, coding, testing, build orchestration |
| Automations | `skills/automations/` | scaffold | Scheduled and condition-triggered workflows |
| Knowledge archive | `skills/ika/` | planned | Integration patterns derived from IKA experience |
| Medicine store | `skills/msa/` | planned | Integration patterns derived from Medicine Store Assistant experience |

## Routing Rule

Do not load every skill by default. Select the smallest set that covers the current task.

If no existing skill matches, operate normally, then consider whether the repeated task deserves a new skill package.

## Plugin / MCP Rule

Skills describe **how** to use capabilities; plugins/MCP/apps provide **execution surfaces**. A skill may reference more than one provider and should prefer the currently available native or connected tool when equivalent.

## Growth Rule

New skills may be added freely when they are modular, testable, and useful. Kernel-level changes require a higher standard because they affect all future tasks.
