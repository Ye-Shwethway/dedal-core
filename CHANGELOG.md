# Changelog

- Confirmed live custom-MCP resync to 54 actions and validated the DEDAL-owned media staging lifecycle through `youtube_media_stage` -> signed HTTPS stage -> `youtube_media_unstage`, with cleanup and no production-thumbnail churn. A malformed/truncated large Base64 client payload was treated as a transport/input failure rather than retried against YouTube.

All meaningful DEDAL Core architectural and behavioral changes should be recorded here.

## 0.30.0 — 2026-09-16

### Added
- Native DEDAL thumbnail media staging via a dedicated short-lived Cloudflare Worker/KV service, with HMAC-signed fetch URLs and typed `youtube_media_stage` / `youtube_media_unstage` tools.
- A layered YouTube thumbnail workflow contract covering content-truth lock, discovery strategy, visual-reference authority, concept planning, edit/generation choice, mobile QA, DEDAL-controlled staging, authenticated mutation, read-back, and experiment measurement.
- A thumbnail media-staging publishing reference that makes Creator-controlled ephemeral HTTPS staging the preferred path and treats credit-metered third-party upload hosts as fallback-only.
- A reusable prospective SEO measurement and closeout contract with T0/24h/3d/7d/28d windows, explicit source-availability states, SERP drift handling, anti-churn rules, and feature-complete criteria.
- `skills/youtube-seo/` as a first-party-data-first discovery-intelligence faculty for query/entity research, Search/Browse/Suggested surface strategy, packaging hypotheses, analytics diagnosis, experiment design/readout, and channel learning.
- Transparent YouTube SEO evidence classes and opportunity-factor model that refuse unsupported absolute search volume, universal difficulty, guaranteed rank, or magic-score certainty.
- YouTube SEO routing/eval contract with explicit ownership separation from YouTube Publishing and private-overlay learning.

### Changed
- YouTube Publishing no longer depends on a credit-metered third-party upload-to-URL service for the normal thumbnail path; the Gateway now proxies owned ephemeral staging and deployed references advance to Gateway `0.7.47` / MCP `0.8.4` with 54 typed tools.
- YouTube thumbnail packaging now composes SEO, Visual Direction, and Publishing explicitly; scene/character-specific image generation must not skip strategy/reference locking, and text-only edits must preserve accepted subject anatomy/composition.
- Public YouTube Gateway source advanced to `0.4.5` and the authorized deployed reference to `0.7.46`; thumbnail failures now distinguish media-fetch/validation from upstream upload failure in bounded private audit diagnostics.
- YouTube SEO now distinguishes observed zero from unavailable/not-yet-processed/suppressed/error states and treats longitudinal outcome windows as ongoing validation rather than a blocker to closing the implemented skill scope.
- YouTube Publishing now owns authenticated YouTube operations and bounded API/MCP transport while YouTube SEO owns discovery intelligence; approved SEO changes still pass through Publishing intent/read-back gates.
- YouTube Publishing source now includes dedicated owned-video traffic-source, search-term, and retention read helpers for the YouTube SEO feedback loop; deployed references advanced to Gateway `0.7.44` / MCP `0.8.3`.
- Reporting bridge failures now persist bounded upstream diagnostics to private audit state, allowing service/configuration errors to be distinguished from MCP or aggregation transport failures without exposing credentials.
- `youtube_search` now exposes bounded SEO research controls for region, relevance language, publication bounds, pagination, and safe-search policy; public-source behavior no longer silently constrains video search to owned results.
- Video metadata updates now verify requested title, description, category, and tags with bounded eventual-consistency read-back; tag verification is order-insensitive to YouTube normalization.
- Capability routing/registry/consolidation state now recognizes YouTube discovery intelligence as independently routable without turning Data/Analytics/Reporting APIs or third-party SEO tools into faculties.

## 0.29.0 — 2026-09-16

### Added
- Optional Library-only private operational overlay contract for Creator/project-specific non-secret context, loaded manifest-first and only when task-relevant.
- Fail-closed public privacy guard rejecting private-overlay paths or overlay manifests if they enter the repository tree.

### Changed
- Boot authority now distinguishes public Core contracts, private operational context, live connected-service state, and GitHub repository identity.
- Private overlay data is explicitly excluded from GitHub mutation candidates, public patches, release archives, and public fixtures; actual credentials remain outside both Core and the overlay.

## 0.28.0 — 2026-09-16

### Added
- Cloudflare Worker deployment/connector-recovery reference covering live-source identity, transport fidelity, raw/multipart upload recovery, outcome-unknown mutations, aggregation-layer verification, and automation-first mobile workflows.
- Executable `cloudflare-platform-operations` contract with eight representative failure/recovery cases.

### Changed
- Cloudflare Platform now distinguishes repository/build/deployed/sanitized source identities and forbids replacing newer live Worker code with stale repository source without proven equivalence.
- Connector read/discovery capability no longer implies source-upload fidelity; request serialization failures trigger execution-surface switching rather than application-code distortion.
- Post-mutation transport/read-back errors require state verification before retry when the upstream mutation may already have committed.
- Manual production source editing is a last resort when authorized automation remains practical, with explicit attention to mobile-constrained Creator workflows.
- Cloudflare and integration-aggregation connected capability are marked `verify_per_session` in the public capability registry.
- YouTube hardening validation no longer hardcodes the global Core next-checkpoint ID, preventing unrelated domain checkpoints from causing false CI failures.

### Fixed
- YouTube playlist visibility updates now preserve mandatory snippet metadata and include the required `snippet` part, fixing `400 unexpectedPart` failures on privacy-only changes.
- Video privacy and scheduling mutations now use bounded eventual-consistency read-back; privacy changes also verify scheduled `publishAt` state is cleared, while accepted schedules can report `accepted_pending_readback` instead of a false failure.
- Live outcome validation covered private/unlisted/public round-trips and schedule creation/cancellation, with controlled round-trip state restored during the test before any later Creator-directed publication decisions.
- The existing DEDAL YouTube MCP was also outcome-validated through an aggregation layer for dedicated playlist/video public-visibility mutations, authoritative Data API read-back, and Creator-side YouTube Studio confirmation; the aggregator remains a runtime execution surface rather than the semantic source of truth.

## 0.11.0 — 2026-09-14

### Added
- `skills/agent-engineering/references/dedal-self-application.md` for applying Agent Engineering to DEDAL's own context loading, tool use, Git transactions, polling, completion evidence, progress communication, and long-horizon continuity.
- `evals/agent-engineering/dedal-self-audit-v1.md` as the first explicit baseline audit of DEDAL's own harness.

### Changed
- GitHub operations now prefer one mutation path for coherent multi-file changes and explicitly discourage mixing unrelated direct contents writes into prepared tree transactions.
- CI/status polling is now bounded and becomes run-ID/job scoped after registration.
- Agent Engineering distinguishes design rationale, contract validation, and outcome validation; contract checks are no longer treated as proof of measured task improvement.
- The Improvement Protocol adopts the same evidence-maturity distinction.
- Long-horizon checkpoints emphasize accepted state, completed evidence, unresolved risk, and the next executable step.

### Self-audit findings
- Source-of-truth hierarchy, smallest-skill routing, truthful completion, Creator authority, and public/private boundaries remain strong.
- A recent standalone `noop` commit exposed a GitHub harness transaction weakness and motivated the new transactional-write rule.
- Stable constitutional/context files should not be repeatedly reread inside one coherent task without a state-change or conflict reason.
- Harness v1 is now: `frame work unit -> load minimal context -> inspect live state -> execute with bounded tools/loops -> verify at required evidence level -> report -> checkpoint only if durable`.

This release establishes contract-level harness improvements. Outcome validation will come from representative real tasks; no universal quality gain is claimed yet.

## 0.10.0 — 2026-09-14

### Added
- `skills/agent-engineering/` as an independently routable generic skill for prompt/context engineering, model-facing tool design, harness control, agentic loops, orchestration, evals/observability, and long-horizon continuity.
- Focused Agent Engineering references for prompt/context, harness/tools, loops, orchestration, and evaluation/observability.
- `skills/agent-engineering/ADAPTATION_NOTES.md` with public-research and repository provenance plus explicit rejected patterns.
- `skills/skill-acquisition/references/agent-engineering-corpus-audit-2026-09-14.md` covering official engineering guidance, ReAct/Self-Refine/Reflexion/AgentBench, 12-Factor Agents, DSPy, and SWE-agent/ACI patterns.
- `evals/agent-engineering/contract-v1.md` with routing, behavioral, and regression assertions.

### Changed
- Master routing now treats Agent Engineering as the domain for improving AI-agent systems themselves rather than overloading Software Development or Skill Acquisition.
- Agent design now starts from a capable-model baseline and adds retrieval, tools, loops, memory, orchestration, or multiple agents only when a concrete failure mode or measured benefit justifies them.
- Context is treated as a finite curated resource; JIT/progressive retrieval is preferred over broad context dumping.
- Model-facing tool names, schemas, results, errors, token footprint, and authority semantics are treated as part of agent performance.
- Agent loops require explicit completion, retry, non-progress, budget, authority, and escalation behavior appropriate to the workflow.
- Reflection/refinement is bounded and requires an evaluator, rubric, environment/tool feedback, source contradiction, test, or Creator feedback capable of changing the next attempt.
- Multi-agent systems are topology choices for independent breadth, specialization, or context separation—not default upgrades.
- Long-horizon agent state should be externalized into inspectable artifacts rather than hidden conversational memory.

### Source snapshots and conceptual corpus
- `humanlayer/12-factor-agents` @ `d20c728368bf9c189d6d7aab704744decb6ec0cc` — Apache-2.0.
- `stanfordnlp/dspy` @ `ecba33763316d2a4c6c756046a1118ecbff033e7` — conceptual use only.
- `SWE-agent/SWE-agent` @ `3ea751c087f32b16e039a2233dd6eefecef325d5` — conceptual use only.
- Anthropic and OpenAI official agent-engineering guidance plus ReAct, Self-Refine, Reflexion, and AgentBench informed the DEDAL-native synthesis.

No third-party agent framework, package, or executable was installed or executed.

## 0.9.0 — 2026-09-14

### Added
- Deep audit of `nextlevelbuilder/ui-ux-pro-max-skill` pinned to `7f69fed6a2717900085f1bc3b263721f8ba025e2` with verified MIT license.
- `skills/interface-design/references/design-intelligence-retrieval.md` for scoped design knowledge retrieval, domain/stack separation, explicit miss semantics, and freshness handling.
- `skills/interface-design/references/design-system-persistence.md` for safe master + surface override persistence.
- `skills/skill-acquisition/references/ui-ux-pro-max-deep-audit-2026-09-14.md` with Adopt / Adapt / Merge / Reject decisions.

### Changed
- Interface Design now has a distinct design-intelligence layer in addition to its existing brief/direction and visual-verification workflow.
- Curated design catalogs are recommendation evidence, not authority over Creator intent, project-local design truth, accessibility standards, or current official platform guidance.
- Targeted UI issues retrieve the semantic UX concern first and implementation stack/platform guidance separately when needed.
- Retrieval misses remain explicit; one scoped retry is allowed before clearly labeled general fallback guidance.
- Durable design state may use a master + surface override hierarchy and must not be silently regenerated over accepted project direction.
- Registry benchmark provenance now includes UI/UX Pro Max.

### Adaptation policy
- The upstream CSV/design catalog was not vendored into DEDAL Core.
- Provider-specific plugin paths, CLI installation/update behavior, external logo-generation services, hardcoded current framework versions, and fixed design dials were not adopted as durable Core behavior.
- Upstream executables/scripts were inspected but not installed or executed.

### Source snapshot
- `nextlevelbuilder/ui-ux-pro-max-skill` @ `7f69fed6a2717900085f1bc3b263721f8ba025e2` — MIT.

## 0.8.0 — 2026-09-14

### Added
- Independent/high-signal ecosystem audit covering `obra/superpowers`, `Leonxlnx/taste-skill`, `lllllllama/RigorPilot-Skills`, and `pbakaus/impeccable` at pinned source commits with verified MIT/Apache-2.0 licenses.
- `skills/interface-design/` as a DEDAL-native cross-project UI/UX skill for brief inference, surface-mode framing, refinement-vs-redesign discipline, quality checks, and bounded visual verification.
- Interface Design adaptation notes plus focused references for brief/direction, redesign/audit, quality floor, and visual verification.

### Changed
- Decision Design now sizes work as spike / bounded / architectural and can escalate when hidden complexity appears, without inheriting a universal approval ceremony.
- Research now distinguishes exploratory candidate evidence from trusted/established evidence and adds frozen comparison anchors, bounded experiment loops, and anti-overclaim rules for scientific/benchmark work.
- Skill Acquisition records the independent-corpus audit and expands benchmark provenance to the four new sources.
- Master routing now treats Interface Design as independently routable and pairs it with Software Development only when implementation is part of the task.

### Adaptation policy
- `obra/superpowers` mandatory global invocation and universal approval gates were not adopted.
- `taste-skill` hardcoded aesthetic dials, font/icon preferences, and one-stack defaults were not adopted.
- RigorPilot deep-learning-specific orchestration remains outside Core; only general research-governance patterns were merged.
- Impeccable provider-specific launchers/hooks/agents and universal maximalist framing were not adopted.

### Source snapshots
- `obra/superpowers` @ `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` — MIT.
- `Leonxlnx/taste-skill` @ `ccbc15639c97057cbfcf32ecebc38ef716e4bb37` — MIT.
- `lllllllama/RigorPilot-Skills` @ `bd91195ad73199b95e24532b581ff12c07dcce09` — MIT.
- `pbakaus/impeccable` @ `cb56ed6c19a07329a9fa0cd4e657bee040156593` — Apache-2.0.

## 0.7.0 — 2026-09-14

### Added
- Structured first-party/vendor corpus audit covering `anthropics/skills`, `vercel-labs/agent-skills`, and `microsoft/skills` with pinned source commits.
- `skills/skill-acquisition/references/authoring-and-evals.md` for routing contracts, degrees of freedom, meaningful baselines, and skill evaluation.
- `skills/skill-acquisition/references/knowledge-packaging-and-freshness.md` for hero-path discipline, impact-ranked rule catalogs, generation, and freshness metadata.
- `skills/skill-acquisition/references/official-corpora-audit-2026-09-14.md` with Adopt / Adapt / Merge / Reject decisions and license/provenance notes.

### Changed
- Skill Acquisition now treats skill quality as four separate concerns: routing accuracy, task quality, context/operational efficiency, and robustness/freshness.
- Major skill rewrites should compare against a meaningful baseline: no/current generic behavior for new skills and the previous proven version for existing skills.
- Skill authoring now matches instruction precision to risk, preserves co-equal hero workflows, and pushes uncommon detail behind progressive disclosure.
- Large knowledge/rule skills may rank guidance by expected impact and should carry source/version/freshness metadata when correctness can drift.
- Registry benchmark provenance now records the pinned Matt Pocock, Anthropic, Vercel Labs, and Microsoft source commits.

### Source snapshots
- `anthropics/skills` @ `34040c9c568585f6929bedeaad110ad08f079624`
- `vercel-labs/agent-skills` @ `063bee94c3f4df8453406c830b0a7df0f2860278`
- `microsoft/skills` @ `903dc62b1e4c833235b54db918a9a51cb6d3cc8f`

Anthropic and Vercel material was used as pattern-level inspiration where a repository-wide license was not verified at the pinned snapshot. Microsoft root license was verified as MIT. No third-party package was installed or executed.

## 0.6.0 — 2026-09-14

### Added
- Deep audit of `mattpocock/skills` pinned to source commit/tree `3cca18b368ae95cdbdebbff572ccafa662551015` (MIT).
- `decision-design` as a DEDAL-native adaptation of the dependency-aware `grilling`/`grill-me` decision-frontier pattern.
- Focused Software Development references for debugging loops, testing/seams, two-axis review, architecture/domain design, and multi-session delivery.

### Changed
- Software Development now uses progressive disclosure for specialized engineering workflows rather than expanding one monolithic skill prompt.
- Hard debugging prioritizes a tight red-capable feedback loop, minimization, falsifiable hypotheses, targeted probes, regression locking, and cleanup.
- Testing guidance distinguishes stable behavior seams from implementation-coupled tests and treats TDD as a deliberate mode rather than universal ceremony.
- Code review separates Standards from Intent/Spec so one axis cannot hide failure on the other.
- Multi-session engineering separates decide -> record -> slice -> implement -> review -> checkpoint and favors vertical slices plus compact reference-based handoffs.

### Adaptation policy
- Upstream provider-specific Skill/subagent/plugin mechanics were not copied into durable DEDAL contracts.
- The source's MIT license and pinned provenance are recorded; the DEDAL text is a rewritten adaptation, not a verbatim import.

## 0.5.0 — 2026-09-14

### Added
- `skills/skill-acquisition/` as the DEDAL workflow for discovering, auditing, adapting, evaluating, and promoting external Agent Skills patterns.
- Source-evaluation, security-audit, adaptation/evaluation, and initial ecosystem-benchmark references.
- A first public-skill benchmark covering the Agent Skills open standard, OpenAI public plugin/skill examples, engineering skill repositories, research-oriented skills, ClawHub, and skills.sh.

### Changed
- Software Development now uses a scalable understand -> plan -> implement -> verify -> review -> ship/checkpoint lifecycle, root-cause-first debugging, exact-diff review, and fresh-evidence completion gates.
- GitHub operations now separate read/plan/write/verify/report phases, strengthen concurrency/readback discipline, and explicitly reject queued/running CI as success evidence.
- Research now captures source provenance during retrieval, scales triangulation to claim importance, surfaces unsupported/conflicting evidence, and adds citation-coverage review for evidence-heavy work.
- The master router and registry now treat external skill discovery/adaptation as an active meta-domain rather than ad-hoc browsing.

### Acquisition policy
- Reuse ideas; do not inherit trust blindly.
- External skills are untrusted until instruction, data, execution, supply-chain, license, and provenance review is complete.
- Registry reputation, stars, install counts, malware/static scans, and AI security verdicts are signals rather than sufficient trust proof.
- Prefer DEDAL-native synthesis over verbatim import unless exact reuse is clearly justified and license/runtime/security are understood.

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

- YouTube Publishing: added transport-safe chunked native media staging (`youtube_media_stage_chunk` + `youtube_media_stage_finalize`) so thumbnail assets no longer depend on third-party upload hosts when inline Base64 exceeds connector body limits.

- YouTube Publishing: retained the stable 54-action MCP surface and moved chunk transport behind the existing `youtube_media_stage` action via a versioned Base64 control envelope; prevents connector body limits without forcing a custom-MCP schema resync.

- YouTube Publishing: made transparent chunk acknowledgements compatible with the existing media-stage output schema; pending chunks can traverse Composio without adding MCP actions.
