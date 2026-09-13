# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.11.0`
- Purpose: durable public operational core for DEDAL

## Active Skills

Domain: `$msa`, `$pra`, `$ika`.
Generic/meta: GitHub, Files & Artifacts, Research, Software Development, Decision Design, Interface Design, **Agent Engineering**, Automations, Skill Acquisition.

## Agent Engineering self-application

DEDAL has now applied Agent Engineering to its own operating workflow. The baseline audit is `evals/agent-engineering/dedal-self-audit-v1.md`; the durable execution guidance is `skills/agent-engineering/references/dedal-self-application.md`.

Harness v1:

`frame work unit -> load minimal context -> inspect live state -> execute with bounded tools/loops -> verify at required evidence level -> report -> checkpoint only if durable`

### Current self-audit findings

- Existing source-of-truth, smallest-skill routing, truthful completion, Creator-authority, and public/private boundaries are strong.
- Coherent multi-file GitHub changes should choose one mutation path and prefer a single atomic tree/commit when available.
- Concurrent writes to the same state owner and force-based conflict bypass are rejected.
- CI/status polling should become run-ID/job scoped after registration and remain bounded.
- Stable constitutional/context files should not be repeatedly reread inside one coherent task unless state changes or conflict appears.
- Self-improvement claims now distinguish **design rationale**, **contract validation**, and **outcome validation**.
- Worthy long-horizon checkpoints should preserve accepted state, completed evidence, unresolved risk, and the next executable step.

Observed evidence for the transaction finding includes a recent standalone `noop` commit created while reconciling a mixed write path before the v0.9 atomic update. The lesson is encoded as a workflow regression, not merely remembered.

## Agent Engineering

Core model:

`agent outcome = model capability × instruction quality × context quality × tool/interface quality × loop/control quality × state/continuity × evaluation/feedback`

Durable rules remain:
- establish a capable-model baseline before adding orchestration complexity;
- keep deterministic constraints/execution in software where practical;
- treat context as a finite resource and prefer progressive/JIT retrieval;
- treat tool schemas/results/errors/output size as part of the model-facing interface;
- give loops explicit success/failure/retry/non-progress/budget/authority/escalation semantics;
- use reflection only when new evidence or a verifier can change the next attempt;
- prefer a single capable agent until parallelism/specialization/context separation justifies more;
- externalize long-horizon state into inspectable artifacts;
- revisit harness assumptions as models and tools improve.

## Verification

`repo-integrity.yml` validates foundational/kernel files, registries, all active skill entrypoints, imported/adapted provenance, Interface Design, Agent Engineering references/provenance/evals including the DEDAL self-audit, Skill Acquisition audits, and semantic version format.

Fresh-chat bootstrap E2E remains **PASS** (`evals/boot/minimal-bootstrap-v1.md`).

## Next Phase

1. Use Harness v1 on representative real tasks in at least three domains and capture actual outcome evidence versus current/baseline behavior.
2. Measure practical friction where observable: redundant context reads, tool-call count, failed/repeated calls, recovery quality, completion evidence, and Creator corrections.
3. Refine rules only from repeated/meaningful evidence; do not optimize one metric at the expense of correctness.
4. Keep ecosystem scans gap-driven and keep private/project operational state outside the public core.

Do not expand the Stable Kernel merely to encode temporary model limitations, framework fashion, or project-specific agent topology.
