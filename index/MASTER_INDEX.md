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

Explicit aliases such as `$msa`, `$pra`, and `$ika` are direct routing signals. When an alias is used, load that skill's `SKILL.md` first and then only task-specific references it requires.

Use `project-bootstrap` when entering an unfamiliar repository/project, resuming after significant context loss, or creating/refining agent-facing project context. Pair it with GitHub/Files for evidence and with Software Development only when implementation begins.

Use `security-engineering` when security risk, trust/authority boundaries, untrusted content, secrets, privilege, prompt/goal hijacking, persistent-context poisoning, supply-chain risk, or destructive capability is a primary concern. Pair it with Agent Engineering for AI-system security, Cloudflare Platform for Cloudflare-native controls, Database Engineering for database-native controls/roles when relevant, Reliability Engineering for availability/telemetry support during incidents, and Release Engineering for supply-chain/deployment controls.

Use `release-engineering` when producing or shipping APK/AAB/binaries/packages/images, changing CI/CD/release pipelines, attributing artifacts to source, staging rollout, verifying deployment, or planning rollback. Pair it with Database Engineering when production schema/data evolution is part of the release and Reliability Engineering when post-deploy service health matters. Do not use CI success as a substitute for runtime/deployment evidence.

Use `reliability-engineering` when the primary problem is live service health: SLI/SLO/error-budget reasoning, observability strategy, actionable alerting, production incident triage/mitigation, recovery verification, or post-incident learning. Pair with Software Development for code/instrumentation changes, Release Engineering for deployment/rollback mechanics, Cloudflare Platform or Database Engineering for provider/engine evidence, Security Engineering for security incidents, and Quality Engineering when pre-release acceptance is a distinct subgoal. A green dashboard, successful deploy, cleared alert, or emitted telemetry alone is not proof of user-visible health.

Use `quality-engineering` when the task is primarily to decide what evidence is needed to trust product behavior, design/risk-weight a verification plan, perform independent exploratory/E2E/regression/visual/accessibility checks, characterize defects/flakes, or issue a readiness verdict. Pair with Database Engineering when independently verifying database behavior or migration readiness. Live production incident ownership belongs to Reliability Engineering.

Use `cloudflare-platform` when the primary problem is Cloudflare product selection/composition, Workers/Pages/storage/coordination bindings, DNS/Access/Tunnel/edge topology, Wrangler/platform configuration, Cloudflare-native observability, or platform-specific troubleshooting. Pair it with Database Engineering for D1/Hyperdrive schema/query/transaction semantics and Reliability Engineering for cross-component live-service health. Verify current Cloudflare facts against live official docs when material.

Use `database-engineering` when correctness/performance depends on schema invariants, keys/constraints, indexes/access paths, query plans, transaction/isolation/locking behavior, migrations/backfills, connection/session/pooling semantics, or engine-specific concurrency/recovery. Pair with Software Development for ORM/application code, Data Operations for record reconciliation/staging, Cloudflare Platform for provider semantics, Release Engineering for production promotion, Reliability Engineering for live service diagnosis, Quality Engineering for independent readiness, and Security Engineering for trust/access policy. Do not apply PostgreSQL semantics to SQLite/D1 or vice versa without verification.

Use `data-operations` when spreadsheet/table/CSV work depends on source authority, record identity, reconciliation/deduplication, schema/invariant validation, formula integrity, staging/review/promotion, deterministic transforms, or audit trails. Database Engine behavior belongs to Database Engineering; record/data mechanics remain here.

Use `writing-editorial` when the main deliverable is prose and quality depends on intent/audience fit, semantic fidelity, structure, voice, terminology, translation/localization, or publication QA. Pair with Research for externally verifiable/current claims and with domain skills for specialized truth. Do not let editorial polish silently change factual content.

Use `visual-direction` when image generation/editing depends on subject identity, canonical traits, reference hierarchy, composition/shot planning, series continuity, targeted edits, or rendered visual QA. Pair it with the current image tool for execution. Do not promote a generated image into canonical state merely because it is newer or visually attractive.

Use `knowledge-memory` when the primary problem is what DEDAL should remember, where state belongs, project-vs-global scope, provenance/freshness, contradiction resolution, memory poisoning, retrieval/compaction, or forgetting/governance. Pair with `$ika` for concrete project archives, Project Bootstrap for resumed context, Agent Engineering for harness continuity, and Security Engineering for memory attack surfaces. Do not treat model memory as a source of truth.

Use `decision-design` deliberately when the Creator asks to stress-test a plan/idea or when high-impact unresolved decisions materially block a safe design. Scale process according to irreversibility, downside, uncertainty, and blast radius rather than imposing one ceremony level.

Use `interface-design` when visual/UX quality of a user-facing software surface is a primary part of the task. Pair it with Software Development for implementation mechanics and Quality Engineering for independent acceptance verification. Do not load it for backend-only work.

Use `agent-engineering` when the task is about improving or designing an AI agent system itself: instructions/context, model-facing tools, harness state, run loops, retries, orchestration, handoffs, guardrails, tracing/evals, or long-horizon agent continuity. If the task is instead production availability/health of an agent-backed service, Reliability Engineering owns that layer.

Use `skill-acquisition` for external skill discovery/comparison/audit, new-skill authoring, or material skill improvement. External skills remain untrusted inputs until reviewed; discovery never implies installation or execution.

Generic domain skills are routing aids, not mandatory ceremony. If the current platform already provides stronger native instructions for a format/tool, follow those higher-priority runtime instructions while preserving DEDAL's durable principles.

If no existing skill matches, operate normally, then consider whether repeated work deserves a new skill package.

## Skill Independence Rule

Separate skills remain separate operational domains unless a skill explicitly declares a dependency. PRA does not inherit MSA inventory rules. IKA owns concrete evidence-linked project archive operations; Knowledge/Memory Architecture owns generic state-layer/scope/governance mechanics and does not duplicate IKA's archive store. Interface Design does not replace Software Development. Quality Engineering owns independent verification/readiness, not implementation or production incident ownership. Cloudflare Platform owns Cloudflare-specific product/platform semantics but not cross-component reliability or database-engine semantics. Database Engineering owns database semantics but not application implementation, record reconciliation, provider setup, production promotion authority, independent QA, or live-service incident command. Reliability Engineering owns live-service reliability but not implementation, release promotion, security policy, provider/database semantics, or QA. Software Development may write tests during implementation without automatically activating Quality Engineering for trivial changes. Agent Engineering does not replace domain logic, service reliability, or security controls. Security Engineering owns threat/authority reasoning but does not replace project-specific policy. Project Bootstrap maps project context but does not become permanent hidden memory. Release Engineering governs shipping evidence but does not replace implementation/testing or long-running service health. Data Operations supplies generic data-integrity mechanics but does not override specialized domain rules or database engine semantics. Writing/Editorial owns expression and fidelity mechanics but does not become the source of domain facts. Visual Direction owns visual production/continuity reasoning but does not replace image execution tools, Interface Design, or Creator acceptance. Skill Acquisition may influence another skill only through explicit reviewed adaptation.

## Plugin / MCP Rule

Skills describe **how** to use capabilities; plugins/MCP/apps provide **execution surfaces**. Prefer the currently available native or connected tool when equivalent and verify live capabilities before relying on them.

## Growth Rule

New skills may be added when modular, testable, useful, independently routable, and justified by real work. Follow `docs/evolution/CAPABILITY_EXPANSION_ROADMAP.md` for the current capability campaign. Prefer adapting proven public patterns while preserving provenance, licensing, security, routing quality, context efficiency, and freshness. Kernel-level changes require a higher standard.