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
| Research | current research / verification / governed exploration | `skills/research/` | active | Live-source research, provenance, synthesis, freshness, comparability, and exploratory-evidence discipline |
| Software development | coding/debugging/architecture/build work | `skills/software-development/` | active | Repository-aware engineering lifecycle with focused debugging/testing/review/architecture/multi-session references |
| Decision design | deliberate plan/architecture/product stress-test | `skills/decision-design/` | active | Process-sized decision design with dependency-aware frontier resolution |
| Interface design | website/app/dashboard/frontend design or redesign | `skills/interface-design/` | active | Brief-aware UI/UX direction, scoped design-intelligence retrieval, redesign/audit discipline, durable design-system state, and bounded visual verification |
| Agent engineering | AI agent / harness / context / tools / loops / orchestration / evals | `skills/agent-engineering/` | active | Prompt/context engineering, model-facing tool design, harness control, agentic loops, orchestration, observability, and long-horizon continuity |
| Security engineering | security/threat/injection/privilege/secrets/supply-chain work | `skills/security-engineering/` | active | Trust boundaries, authority, containment, persistent-context risk, supply-chain security, and adversarial verification |
| Project bootstrap | new/resumed repo/project onboarding and context mapping | `skills/project-bootstrap/` | active | Compact executable project context, instruction hierarchy, drift control, source-of-truth mapping, and next-step continuity |
| Release engineering | release/build artifact/deploy/rollback tasks | `skills/release-engineering/` | active | Source-to-artifact attribution, provenance, staged promotion, runtime verification, release evidence, and rollback |
| Data operations | spreadsheet/data reconciliation/validation/staging/promotion work | `skills/data-operations/` | active | Record identity, reconciliation, data contracts, formula integrity, deterministic transforms, staged promotion, read-back verification, and auditability |
| Automations | reminder/schedule/watch tasks | `skills/automations/` | active | Scheduled, recurring, condition and event-triggered workflows |
| Skill acquisition | external skills / skill ecosystem / create or improve a skill | `skills/skill-acquisition/` | active | Discover, audit, author, adapt, baseline-test, evaluate, and promote skill patterns safely |

The machine-readable equivalent is `index/SKILL_REGISTRY.yaml`.

## Routing Rule

Do not load every skill by default. Select the smallest set that covers the current task.

Explicit aliases such as `$msa`, `$pra`, and `$ika` are direct routing signals. When an alias is used, load that skill's `SKILL.md` first and then only task-specific references it requires.

Use `project-bootstrap` when entering an unfamiliar repository/project, resuming after significant context loss, or creating/refining agent-facing project context. Pair it with GitHub/Files for evidence and with Software Development only when implementation begins.

Use `security-engineering` when security risk, trust/authority boundaries, untrusted content, secrets, privilege, prompt/goal hijacking, persistent-context poisoning, supply-chain risk, or destructive capability is a primary concern. Pair it with Agent Engineering for AI-system security and Release Engineering for supply-chain/deployment controls.

Use `release-engineering` when producing or shipping APK/AAB/binaries/packages/images, changing CI/CD/release pipelines, attributing artifacts to source, staging rollout, verifying deployment, or planning rollback. Do not use CI success as a substitute for runtime/deployment evidence.

Use `data-operations` when spreadsheet/table/CSV work depends on source authority, record identity, reconciliation/deduplication, schema/invariant validation, formula integrity, staging/review/promotion, deterministic transforms, or audit trails. Pair it with Files/spreadsheet tools for mechanics. Specialized domain skills keep their accepted business rules; Data Operations must not silently replace them.

Use `decision-design` deliberately when the Creator asks to stress-test a plan/idea or when high-impact unresolved decisions materially block a safe design. Scale process to spike/bounded/architectural work rather than imposing one ceremony level.

Use `interface-design` when visual/UX quality of a user-facing software surface is a primary part of the task. Pair it with Software Development for implementation mechanics. Do not load it for backend-only work.

Use `agent-engineering` when the task is about improving or designing an AI agent system itself: instructions/context, model-facing tools, harness state, run loops, retries, orchestration, handoffs, guardrails, tracing/evals, or long-horizon agent continuity. Do not invoke it merely because ordinary software happens to call an LLM once.

Use `skill-acquisition` for external skill discovery/comparison/audit, new-skill authoring, or material skill improvement. External skills remain untrusted inputs until reviewed; discovery never implies installation or execution.

Generic domain skills are routing aids, not mandatory ceremony. If the current platform already provides stronger native instructions for a format/tool, follow those higher-priority runtime instructions while preserving DEDAL's durable principles.

If no existing skill matches, operate normally, then consider whether repeated work deserves a new skill package.

## Skill Independence Rule

Separate skills remain separate operational domains unless a skill explicitly declares a dependency. PRA does not inherit MSA inventory rules. IKA does not silently convert project facts into Kernel rules. Interface Design does not replace Software Development. Agent Engineering does not replace domain logic or security controls. Security Engineering owns threat/authority reasoning but does not replace project-specific policy. Project Bootstrap maps project context but does not become permanent hidden memory. Release Engineering governs shipping evidence but does not replace implementation/testing. Data Operations supplies generic data-integrity mechanics but does not override specialized domain rules. Skill Acquisition may influence another skill only through explicit reviewed adaptation.

## Plugin / MCP Rule

Skills describe **how** to use capabilities; plugins/MCP/apps provide **execution surfaces**. Prefer the currently available native or connected tool when equivalent and verify live capabilities before relying on them.

## Growth Rule

New skills may be added when modular, testable, useful, independently routable, and justified by real work. Follow `docs/evolution/CAPABILITY_EXPANSION_ROADMAP.md` for the current planned capability campaign. Prefer adapting proven public patterns while preserving provenance, licensing, security, routing quality, context efficiency, and freshness. Kernel-level changes require a higher standard.
