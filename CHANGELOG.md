# Changelog

All meaningful DEDAL Core architectural and behavioral changes should be recorded here.

## 0.12.0 — 2026-09-14

### Added
- `skills/security-engineering/` with trust/authority mapping, untrusted-input/persistence handling, and security verification references.
- `skills/project-bootstrap/` for compact executable project context maps, scoped instruction hierarchy, continuity, and drift control.
- `skills/release-engineering/` for source-to-artifact attribution, provenance, staged promotion, deployment/runtime evidence, and rollback.
- `docs/evolution/CAPABILITY_EXPANSION_ROADMAP.md` locking the eight-area capability campaign.
- `skills/skill-acquisition/references/first-wave-capability-audit-2026-09-14.md` covering the first-wave research/adaptation corpus.
- `evals/first-wave-capabilities/contract-v1.md` with routing and behavioral regression assertions.

### Changed
- Master routing and machine-readable registry now recognize Security Engineering, Project Bootstrap, and Release Engineering as independently routable generic domains.
- Security treats prompt/goal hijacking as an authority/capability-containment problem, treats persistent memory/context as an attack surface, and requires residual-risk language rather than absolute safety claims.
- Project onboarding now builds a minimal executable context adapter instead of a broad repository summary and separates stable project rules from volatile checkpoint state.
- Release work now distinguishes build success, artifact identity/provenance, publication/deployment, and runtime verification as separate evidence levels.
- Repo Integrity validates the three new skills, focused references, roadmap, first-wave audit, eval contract, and pinned OWASP / AGENTS.md / SLSA provenance.

### Source snapshots
- `OWASP/www-project-top-10-for-large-language-model-applications` @ `99f4395589bdbd120ae961f9cd179e79d7f9b27f`.
- `agentsmd/agents.md` @ `d001185d792eb6402a58e4cbef1c228b309ec25d`.
- `slsa-framework/slsa` @ `54b88b009fd45acb331c7e6578a526e0f36e0430`.
- Current OpenAI, Anthropic, GitHub, Sigstore and SemVer guidance was used conceptually where appropriate.

No third-party package, security scanner, signing tool, or release executable was installed or executed for this adaptation.

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
- Model-facing tool names, schemas, result shapes, errors, token footprint, and authority semantics are treated as part of agent performance.
- Agent loops require explicit completion, retry, non-progress, budget, authority, and escalation behavior appropriate to the workflow.
- Reflection/refinement is bounded and requires an evaluator, rubric, environment/tool feedback, source contradiction, test, or Creator feedback capable of changing the next attempt.
- Multi-agent systems are topology choices for independent breadth, specialization, or context separation—not default upgrades.
- Long-horizon agent state should be externalized into inspectable artifacts rather than hidden conversational memory.

### Source snapshots and conceptual corpus
- `humanlayer/12-factor-agents` @ `d20c728368bf9c189d6d7aab704744decb6ec0cc` — Apache-2.0.
- `stanfordnlp/dspy` @ `ecba33763316d2a4c6c756046a1118ecbff033e7` — conceptual use only.
- `SWE-agent/SWE-agent` @ `3ea751c087f32b16e039a2233dd6eefecef325d5` — conceptual use only.
- Anthropic and OpenAI official agent engineering guidance plus ReAct, Self-Refine, Reflexion, and AgentBench informed the DEDAL-native synthesis.

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

## 0.8.0 — 2026-09-14

Added the independent/high-signal ecosystem audit, Interface Design skill, and refinements to Decision Design and Research. Source snapshots: `obra/superpowers` @ `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`, `Leonxlnx/taste-skill` @ `ccbc15639c97057cbfcf32ecebc38ef716e4bb37`, `lllllllama/RigorPilot-Skills` @ `bd91195ad73199b95e24532b581ff12c07dcce09`, and `pbakaus/impeccable` @ `cb56ed6c19a07329a9fa0cd4e657bee040156593`.

## 0.7.0 — 2026-09-14

Added structured official-corpus auditing and skill authoring/evaluation/freshness guidance based on pinned Anthropic (`34040c9c568585f6929bedeaad110ad08f079624`), Vercel Labs (`063bee94c3f4df8453406c830b0a7df0f2860278`), and Microsoft (`903dc62b1e4c833235b54db918a9a51cb6d3cc8f`) snapshots.

## 0.6.0 — 2026-09-14

Added Matt Pocock deep audit, Decision Design, and focused Software Development references for debugging, testing, review, architecture/domain modeling, and multi-session delivery. Source: `mattpocock/skills` @ `3cca18b368ae95cdbdebbff572ccafa662551015`.

## 0.5.0 — 2026-09-14

Added Skill Acquisition and strengthened Software Development, GitHub operations, and Research around source provenance, security, verification, and external-skill adaptation.

## 0.4.0 — 2026-09-14

Added DEDAL-native Knowledge Archive (`$ika`) adapted from private `Ye-Shwethway/ianeo-knowledge-vault` @ `fbed860928c1a93261306f70a47fa700da56ce29` while keeping private archives/project data outside public Core.

## 0.3.0 — 2026-09-14

Added the formal Stable Kernel, first native generic skills, and integrity validation for kernel files, active skill entrypoints, and semantic version format.

## 0.2.0 — 2026-09-13

Added the BIOS/bootstrap architecture, machine-readable skill registry, and pinned MSA/PRA snapshots from `Ye-Shwethway/medicine-store-assistant` @ `6b8f35e4056f030a1ace2dac137cde1071a00051`.

## 0.1.0 — 2026-09-13

Initial DEDAL Core foundation: identity, operating contract, security boundary, capability registry, continuity checkpoint, improvement protocol, foundational architecture, and repository integrity workflow.
