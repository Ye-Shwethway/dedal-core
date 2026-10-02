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
| Reliability engineering | SRE/observability/SLO/alerting/production incidents/service health | `skills/reliability-engineering/` | active | Live-service health, observability strategy, actionable alerting, incident response, recovery verification, or post-incident learning |
| Infrastructure engineering | `iac`, Terraform/OpenTofu/Packer/infrastructure lifecycle | `skills/infrastructure-engineering/` | active | Declarative configuration/state/live-resource reconciliation, plan/apply, drift, imports/moves/refactors, module/provider lifecycle, destructive-change review, and infrastructure recovery |
| Generative Video Direction | `generative-video-direction`, `video-generation-direction`, `ai-video-director` | `skills/generative-video-direction/` | active | Provider-neutral temporal shot design, motion/camera/performance choreography, reference-role planning, provider compilation, generated-take QA, and repair |
| Video Post-Production | `video-post-production`, `video-production`, `video-editing` | `skills/video-post-production/` | active | Existing-media take selection, timeline editing, subtitles/audio, effects, finishing, FFmpeg/Remotion orchestration, and media delivery |
| Facebook Page management | `facebook-page-management` | `skills/facebook-page-management/` | active | Authenticated Facebook Page content, media, scheduling, engagement, analytics, administration, and policy-gated Messenger operations |
| YouTube publishing | `youtube-publishing` | `skills/youtube-publishing/` | active | Verified multi-channel YouTube control, private-first resumable uploads, metadata/privacy/scheduling, playlists, analytics, and MCP-to-Gateway orchestration |
| YouTube SEO | `youtube-seo` | `skills/youtube-seo/` | active | YouTube discovery research, surface-specific packaging, analytics diagnosis, experiments, transparent opportunity evidence, and channel-learning synthesis |
| Candidate Video Finder | `candidate-video-finder`, `video-candidate-finder` | `skills/candidate-video-finder/` | active | Scene-level candidate discovery, source/scene verification, hard-gate evaluation, evidence-backed shortlisting, Creator selection, and production/SEO handoff |
| Presentation engineering | `presentation-engineering`, `pptx`, `slides` | `skills/presentation-engineering/` | active | Audience/argument framing, slide architecture, evidence mapping, visual hierarchy, editable PPTX strategy, speaker notes, template fidelity, and rendered deck QA |
| Decision design | deliberate plan/architecture/product stress-test | `skills/decision-design/` | active | Uncertainty/reversibility-aware decision design with dependency frontier, experiments, thresholds, premortems, and durable learning |
| Interface design | website/app/dashboard/frontend design or redesign | `skills/interface-design/` | active | Brief-aware UI/UX direction, scoped design-intelligence retrieval, redesign/audit discipline, durable design-system state, and bounded visual verification |
| Agent engineering | AI agent / harness / context / tools / loops / orchestration / evals | `skills/agent-engineering/` | active | Prompt/context engineering, model-facing tool design, harness control, agentic loops, orchestration, observability, and long-horizon continuity |
| Security engineering | security/threat/injection/privilege/secrets/supply-chain work | `skills/security-engineering/` | active | Trust boundaries, authority, containment, persistent-context risk, supply-chain security, and adversarial verification |
| Project bootstrap | new/resumed repo/project onboarding and context mapping | `skills/project-bootstrap/` | active | Compact executable project context, instruction hierarchy, drift control, source-of-truth mapping, and next-step continuity |
| Release engineering | release/build artifact/deploy/rollback tasks | `skills/release-engineering/` | active | Source-to-artifact attribution, provenance, staged promotion, runtime verification, release evidence, and rollback |
| Data operations | spreadsheet/data reconciliation/validation/staging/promotion work | `skills/data-operations/` | active | Record identity, reconciliation, data contracts, formula integrity, deterministic transforms, staged promotion, read-back verification, and auditability |
| Writing / editorial | draft/rewrite/translate/edit/publish prose | `skills/writing-editorial/` | active | Intent/audience fidelity, fact-expression separation, structure, voice, terminology, multilingual fidelity, revision, and publication QA |
| Story Weaver | fiction/canon/scene/beat/dialogue/character-arc work | `skills/story-weaver/` | active | Fiction canon, scene function, character causality, beats, dialogue, emotional continuity, setup/payoff, and structured downstream visual handoff |
| Visual Narrative Production | `visual-narrative-production`, `visual-direction` | `skills/visual-narrative-production/` | active | Narrative-to-shot planning, character/reference consistency, scene continuity, performance, cinematography, anatomy/contact QA, prompt compilation, visual QA, and accepted-anchor state |
| Knowledge / memory | memory/state/scope/freshness/contradiction/compaction/governance work | `skills/knowledge-memory/` | active | Memory-layer architecture, state ownership, provenance/freshness, contradiction handling, retrieval/compaction, scope isolation, and poisoning-resistant governance |
| Automations | reminder/schedule/watch tasks | `skills/automations/` | active | Scheduled, recurring, condition and event-triggered workflows |
| Self-improvement | `self-improvement`, `self-correction` | `skills/self-improvement/` | active | Failure/correction detection, same-turn repair orchestration, canonical-source reconciliation, regression guards, durable learning, and learning-closure enforcement |
| Skill acquisition | external skills / skill ecosystem / create or improve a skill | `skills/skill-acquisition/` | active | Discover, audit, author, adapt, baseline-test, evaluate, and promote skill patterns safely |

The machine-readable equivalent is `index/SKILL_REGISTRY.yaml`.

## Routing Rule

Do not load every skill by default. Select the smallest set that covers the current task. A named skill selects a primary faculty without disabling the Cognitive Runtime or genuinely necessary support.

Use `generative-video-direction` when accepted story/visual state must become generated motion: temporal shot design, motion/performance/camera choreography, reference-role strategy, provider capability matching, provider-specific generation contracts, generated-take inspection, and targeted repair. Pair with Story Weaver for narrative truth and Visual Narrative Production for authoritative still/keyframe state. Veo, Seedance, Runway, Firefly, Kling, Luma and successor generators are execution surfaces, not faculties.

Use `video-post-production` (aliases `video-production`, `video-editing`) after usable moving-image media exists: source/take inspection, editorial boundaries, timeline assembly, pacing, reframing/retiming, captions, audio, effects, color/finishing, encoding and delivery. Pair with Generative Video Direction for accepted generated takes and with Visual Narrative Production for still/keyframe/thumbnail assets.

Use `presentation-engineering` when the main deliverable is a slide deck/PPTX or when quality depends on audience/objective framing, narrative spine, slide roles, evidence mapping, chart/diagram choice, visual hierarchy, speaker notes, template fidelity, editability, or rendered slide QA. Pair with Research/domain owners for truth, Writing/Editorial for prose, Data Operations for source tables, Visual Narrative Production for custom visual assets, and Quality Engineering for independent readiness. Prefer the runtime's native slide tooling when available and follow higher-priority platform instructions.

Use `infrastructure-engineering` for declarative infrastructure lifecycle: configuration/state/live-resource reconciliation, plan/apply review, drift, imports/moves/refactors, module/provider lifecycle, destructive resource changes, state/backend safety, or infrastructure recovery.

Use `reliability-engineering` for live service health: SLI/SLO/error-budget reasoning, observability strategy, actionable alerting, production incident triage/mitigation, recovery verification, or post-incident learning.

Use `release-engineering` for source-to-artifact attribution, application/package promotion, rollout, deployment evidence, and rollback.

Use `quality-engineering` when the task is primarily to decide what evidence is needed to trust behavior/output, perform independent verification, characterize defects, or issue a readiness verdict.

Use `cloudflare-platform` for Cloudflare product/platform semantics; `database-engineering` for database-engine semantics; `security-engineering` for trust/authority/security policy; `software-development` for application implementation.

Use `data-operations` for record/data integrity, reconciliation, staging, deterministic transforms, formulas/tables, and audit trails.

Use `writing-editorial` when the main deliverable is prose and quality depends on semantic fidelity, structure, voice, terminology, translation/localization, or publication QA.

Use `story-weaver` when the primary problem is fictional narrative truth: canon, scene function, character motivation/knowledge, beat causality, dialogue, emotional continuity, setup/payoff, or story-state transitions. Pair with Visual Narrative Production when selected beats must become images; Story Weaver hands off story truth without prescribing model prompts or camera grammar.

Use `visual-narrative-production` (alias `visual-direction`) for still-image and visual-novel production where story beats must become purposeful shots while preserving character identity/physique, expression/performance, environment/spatial continuity, camera/screen direction, lighting, anatomy/contact, accepted anchors, or scene state. When the task becomes generated temporal motion direction, Generative Video Direction owns it; when usable moving-image takes must be assembled/finished, Video Post-Production owns that layer.

Use `candidate-video-finder` when the primary question is which specific scene/event should enter production next: discover, verify source/scene truth, apply eligibility gates, compare evidence, and produce a Creator-selected shortlist. After selection, Video Post-Production owns exact local cut truth; YouTube SEO owns discovery-surface packaging/measurement; Visual Narrative Production owns thumbnail image production; YouTube Publishing owns authenticated YouTube operations.

Use `facebook-page-management` for authenticated Facebook Page reads/writes, scheduling, media, comments, Page analytics, roles/settings, and Messenger only when fresh live messaging state is verified. Personal Facebook profiles remain outside this skill. Pair with Writing/Editorial, Visual Narrative Production, Generative Video Direction, Video Post-Production, Research, Automations, or Security Engineering only for those distinct layers.

Use `youtube-seo` when the primary problem is YouTube discovery intelligence: query/entity research, Search/Browse/Suggested/Shorts-feed surface strategy, packaging hypotheses, analytics diagnosis, experiment design/readout, or channel-specific discovery learning. Use `youtube-publishing` for authenticated YouTube reads/transport (including Analytics/Reporting), mutations, and channel operations. **For every new upload/publication whose exact title/description/tags/playlist/thumbnail promise are not already locked, compose YouTube Publishing as PRIMARY and YouTube SEO as SUPPORTING before upload transport; Shorts are explicitly included.** When authenticated analytics acquisition and diagnosis are both required, use YouTube Publishing as PRIMARY and YouTube SEO as SUPPORTING.

Use `self-improvement` when the primary problem is DEDAL learning from its own correction, regression, repeated failure, live/canonical drift, or a verified better recurring procedure. It owns learning-loop orchestration and closure, not all implementation: route repair to the domain owner, require canonical-source reconciliation and regression evidence, route private/public lessons correctly, and keep unresolved learning debt explicit.

Use `skill-acquisition` for explicit external skill discovery/comparison/audit, new-skill authoring, or material skill improvement. Expansion is evidence-gated; do not add skills merely because public repositories exist.

Generic domain skills are routing aids, not mandatory ceremony. If the current platform provides stronger native instructions for a format/tool, follow those higher-priority runtime instructions while preserving DEDAL's durable principles.

## Skill Independence Rule

Generative Video Direction owns generated temporal motion; Video Post-Production owns existing-media assembly/finishing. Neither owns canonical still-image authority or provider execution. Presentation Engineering owns deck architecture/production, not factual authority or prose truth. Infrastructure Engineering owns IaC/resource lifecycle; Reliability Engineering owns live-service reliability; Cloudflare Platform owns Cloudflare provider/product semantics; Database Engineering owns database semantics; Release Engineering owns shipping evidence; Software Development owns application implementation; Security Engineering owns trust/authority reasoning. Skill Acquisition influences another skill only through explicit reviewed adaptation.

## Plugin / MCP Rule

Skills describe **how** to use capabilities; plugins/MCP/apps/native artifact tools provide **execution surfaces**. Prefer the currently available native or connected capability and verify live capabilities before relying on them.

## Growth Rule

New skills may be added when modular, testable, useful, independently routable, and justified by real work. The Creator's demonstrated creative-production workflows reopened bounded expansion for Video Post-Production, Presentation Engineering, Visual Narrative Production, Story Weaver, and Generative Video Direction. Future additions remain evidence-gated.
