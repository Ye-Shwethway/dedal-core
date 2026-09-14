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
| Quality engineering | QA/test strategy/exploratory/E2E/regression/readiness | `skills/quality-engineering/` | active | Independent acceptance truth, risk-based verification, test oracles, defect evidence, regression analysis, and readiness verdicts |
| Cloudflare platform | Workers/Pages/D1/R2/Access/Tunnel/Wrangler/Cloudflare architecture | `skills/cloudflare-platform/` | active | Cloudflare product selection/composition, bindings/configuration, edge/network topology, platform-native operations, and live-verified product semantics |
| Database engineering | schema/index/query-plan/transaction/migration/database performance work | `skills/database-engineering/` | active | Engine-aware schema invariants, indexes/access paths, query plans, transaction/isolation/locking semantics, migration safety, connection behavior, and database recovery reasoning |
| Reliability engineering | SRE/observability/SLO/alerting/production incidents/service health | `skills/reliability-engineering/` | active | Live-service health, observability strategy, actionable alerting, incident response, recovery verification, and post-incident reliability learning |
| Infrastructure engineering | `iac`, Terraform/OpenTofu/Packer/infrastructure lifecycle | `skills/infrastructure-engineering/` | active | Declarative configuration/state/live-resource reconciliation, plan/apply, drift, imports/moves/refactors, module/provider lifecycle, destructive-change review, and infrastructure recovery |
| Decision design | deliberate plan/architecture/product stress-test | `skills/decision-design/` | active | Uncertainty/reversibility-aware decision design with dependency frontier, experiments, thresholds, premortems, and durable learning |
| Interface design | website/app/dashboard/frontend design or redesign | `skills/interface-design/` | active | Brief-aware UI/UX direction, scoped design-intelligence retrieval, redesign/audit discipline, durable design-system state, and bounded visual verification |
| Agent engineering | AI agent / harness / context / tools / loops / orchestration / evals | `skills/agent-engineering/` | active | Prompt/context engineering, model-facing tool design, harness control, agentic loops, orchestration, observability, and long-horizon continuity |
| Security engineering | security/threat/injection/privilege/secrets/supply-chain work | `skills/security-engineering/` | active | Trust boundaries, authority, containment, persistent-context risk, supply-chain security, and adversarial verification |
| Project bootstrap | new/resumed repo/project onboarding and context mapping | `skills/project-bootstrap/` | active | Compact executable project context, instruction hierarchy, drift control, source-of-truth mapping, and next-step continuity |
| Release engineering | release/build artifact/deploy/rollback tasks | `skills/release-engineering/` | active | Source-to-artifact attribution, provenance, staged promotion, runtime verification, release evidence, and rollback |
| Data operations | spreadsheet/data reconciliation/validation/staging/promotion work | `skills/data-operations/` | active | Record identity, reconciliation, data contracts, formula integrity, deterministic transforms, staged promotion, read-back verification, and auditability |
| Writing / editorial | draft/rewrite/translate/edit/publish prose | `skills/writing-editorial/` | active | Intent/audience fidelity, fact-expression separation, structure, voice, terminology, multilingual fidelity, revision, and publication QA |
| Visual direction | image generation/editing/character/reference/series visual work | `skills/visual-direction/` | active | Reference authority, canonical trait locks, shot/set planning, targeted edits, drift detection, visual QA, and accepted-anchor continuity |
| Knowledge / memory | memory/state/scope/freshness/contradiction/compaction/governance work | `skills/knowledge-memory/` | active | Memory-layer architecture, state ownership, provenance/freshness, contradiction handling, retrieval/compaction, scope isolation, and poisoning-resistant governance |
| Automations | reminder/schedule/watch tasks | `skills/automations/` | active | Scheduled, recurring, condition and event-triggered workflows |
| Skill acquisition | external skills / skill ecosystem / create or improve a skill | `skills/skill-acquisition/` | active | Discover, audit, author, adapt, baseline-test, evaluate, and promote skill patterns safely |

The machine-readable equivalent is `index/SKILL_REGISTRY.yaml`.

## Routing Rule

Do not load every skill by default. Select the smallest set that covers the current task.

Explicit aliases such as `$msa`, `$pra`, `$ika`, and `iac` are direct routing signals. A named skill selects a primary faculty without disabling the Cognitive Runtime or genuinely necessary support.

Use `infrastructure-engineering` when the primary problem is declarative infrastructure lifecycle: configuration/state/live-resource reconciliation, plan/apply review, drift, imports/moves/refactors, module/provider lifecycle, destructive resource changes, state/backend safety, or infrastructure recovery. Pair with Cloudflare Platform or another provider owner for provider-native architecture, Security Engineering for authority/credential/trust policy, Release Engineering for application promotion, Reliability Engineering for post-change service health, Database Engineering for database-engine semantics, and Software Development for application code. A plan is not an apply; apply success is not service-health proof.

Use `reliability-engineering` when the primary problem is live service health: SLI/SLO/error-budget reasoning, observability strategy, actionable alerting, production incident triage/mitigation, recovery verification, or post-incident learning. Infrastructure changes that trigger an incident may make Infrastructure Engineering supporting, but live-service impact remains Reliability Engineering's layer.

Use `release-engineering` when producing or shipping APK/AAB/binaries/packages/images, changing CI/CD/release pipelines, attributing artifacts to source, staging rollout, verifying deployment, or planning application/artifact rollback. Infrastructure resource lifecycle belongs to Infrastructure Engineering even when changes are executed by the same pipeline.

Use `quality-engineering` when the task is primarily to decide what evidence is needed to trust product behavior, design/risk-weight a verification plan, perform independent exploratory/E2E/regression/visual/accessibility checks, characterize defects/flakes, or issue a readiness verdict.

Use `cloudflare-platform` when the primary problem is Cloudflare product selection/composition, Workers/Pages/storage/coordination bindings, DNS/Access/Tunnel/edge topology, Wrangler/platform configuration, Cloudflare-native observability, or platform-specific troubleshooting. If Terraform/OpenTofu manages those resources, Cloudflare Platform supplies provider semantics while Infrastructure Engineering owns IaC lifecycle/reconciliation.

Use `database-engineering` when correctness/performance depends on schema invariants, keys/constraints, indexes/access paths, query plans, transaction/isolation/locking behavior, migrations/backfills, connection/session/pooling semantics, or engine-specific concurrency/recovery. Infrastructure provisioning of a database resource does not transfer database-engine semantics to Infrastructure Engineering.

Use `security-engineering` when security risk, trust/authority boundaries, untrusted content, secrets, privilege, prompt/goal hijacking, persistent-context poisoning, supply-chain risk, or destructive capability is a primary concern. Infrastructure automation never creates mutation authority by itself.

Use `project-bootstrap` when entering an unfamiliar repository/project, resuming after significant context loss, or creating/refining agent-facing project context. Pair it with GitHub/Files for evidence and with Software Development only when implementation begins.

Use `data-operations` when spreadsheet/table/CSV work depends on source authority, record identity, reconciliation/deduplication, schema/invariant validation, formula integrity, staging/review/promotion, deterministic transforms, or audit trails.

Use `writing-editorial` when the main deliverable is prose and quality depends on intent/audience fit, semantic fidelity, structure, voice, terminology, translation/localization, or publication QA. Pair with Research for externally verifiable/current claims and with domain skills for specialized truth.

Use `visual-direction` when image generation/editing depends on subject identity, canonical traits, reference hierarchy, composition/shot planning, series continuity, targeted edits, or rendered visual QA. Pair it with the current image tool for execution.

Use `knowledge-memory` when the primary problem is what DEDAL should remember, where state belongs, project-vs-global scope, provenance/freshness, contradiction resolution, memory poisoning, retrieval/compaction, or forgetting/governance.

Use `decision-design` deliberately when the Creator asks to stress-test a plan/idea or when high-impact unresolved decisions materially block a safe design.

Use `interface-design` when visual/UX quality of a user-facing software surface is a primary part of the task. Pair it with Software Development for implementation mechanics and Quality Engineering for independent acceptance verification.

Use `agent-engineering` when the task is about improving or designing an AI agent system itself: instructions/context, model-facing tools, harness state, run loops, retries, orchestration, handoffs, guardrails, tracing/evals, or long-horizon agent continuity.

Use `skill-acquisition` for explicit external skill discovery/comparison/audit, new-skill authoring, or material skill improvement. The current proactive expansion wave is closed: do not reopen expansion merely because more public skills exist. Reopen when ordinary work exposes a concrete uncovered gap, a current faculty materially underperforms, or the Creator explicitly asks.

Generic domain skills are routing aids, not mandatory ceremony. If the current platform already provides stronger native instructions for a format/tool, follow those higher-priority runtime instructions while preserving DEDAL's durable principles.

## Skill Independence Rule

Separate skills remain separate operational domains unless a skill explicitly declares a dependency. Infrastructure Engineering owns IaC/resource lifecycle but not application implementation, release promotion, service health, provider product architecture, database semantics, security policy, or QA. Reliability Engineering owns live-service reliability but not infrastructure plan/apply authority. Cloudflare Platform owns Cloudflare provider/product semantics; Database Engineering owns database semantics; Release Engineering owns shipping evidence; Software Development owns application implementation; Security Engineering owns trust/authority reasoning. Skill Acquisition may influence another skill only through explicit reviewed adaptation.

## Plugin / MCP Rule

Skills describe **how** to use capabilities; plugins/MCP/apps provide **execution surfaces**. Prefer the currently available native or connected tool when equivalent and verify live capabilities before relying on them.

## Growth Rule

New skills may be added when modular, testable, useful, independently routable, and justified by real work. The v0.24.0 capability wave is closed; ordinary-work outcome validation is now preferred over proactive expansion. Future additions require a concrete uncovered capability gap or explicit Creator request. Kernel-level changes require a higher standard.
