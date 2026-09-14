# Failure recovery / compensation audit — 2026-09-14

## Scope

Final agent-refinement slice before pausing this campaign. Reviewed current distributed-workflow recovery patterns and adapted only small, provider-agnostic rules relevant to DEDAL.

## Sources

- AWS Prescriptive Guidance: saga patterns, orchestration, continuation vs compensation, idempotency, observability, eventual consistency.
- Microsoft Architecture Center: compensating transaction pattern for eventually consistent operations.
- Current agent-pattern literature used only as secondary corroboration.

## ADAPT

1. **Recovery is a decision, not a reflex.** On failure choose retry, compensate, preserve-partial, or escalate from evidence about side effects and reversibility.
2. **Safe retry requires repeatability evidence.** Prefer idempotent operations, idempotency keys, or otherwise proven safe repetition.
3. **Compensation is semantic, not atomic rollback.** Across services, a compensator is a new inverse/counter-action; irreversible effects prevent a truthful full-rollback claim.
4. **Reverse unwind where appropriate.** Compensate completed reversible steps in reverse dependency/completion order when that matches workflow semantics.
5. **Partial completion is first-class.** Record residual effects, blocked work, and resume evidence rather than collapsing every non-complete run into generic failure.
6. **Compensation failure escalates.** Do not label recovery complete if a compensator fails; preserve residual state and require manual intervention when needed.
7. **Prefer prevention over expensive compensation.** Preflight validation, staging, scoped authority, and verification can avoid recovery complexity.

## ALREADY COVERED

- bounded retries and explicit exit conditions;
- transactional repository writes where one atomic mechanism exists;
- evidence-linked state promotion;
- task-scoped authority and delegation attenuation;
- privacy-minimal trajectory metadata.

## REJECT AS DEFAULT

- full saga/orchestrator infrastructure for ordinary tasks;
- blanket automatic rollback claims across third-party services;
- blind retries of side-effecting actions;
- treating partial completion as success without residual-state disclosure;
- adding recovery machinery where a local atomic transaction already solves the problem.

## Evidence boundary

This audit supports design rationale and the executable contract added with v0.18.8. It does not prove reduced incident rate or improved task success on representative real work.
