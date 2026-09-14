# Self-Improvement Discipline Audit — 2026-09-14

## Sources
- OpenAI practical guidance: prompt/workflow/model changes should be treated as experiments and validated against evals before shipping.
- Self-Harness (arXiv:2606.09498 / public repository): keeps model/evaluator fixed, mines failure trajectories, proposes bounded harness edits, and promotes only after held-in plus held-out regression checks.
- `harrystamatoukos/self-improving-agent-harness`: isolated git experiments, fixed eval suite, keep/discard loop, and explicit anti-benchmaxxing rules.

No external package, script, or runtime was installed or executed for this audit.

## ADAPT
### Evaluation is the control layer
Self-modification without independent evaluation is not self-improvement. DEDAL should require a frozen comparable baseline and explicit acceptance evidence for material self-changes.

### Failure-driven hypotheses
Start from an observed failure, measurable friction, explicit Creator request, or demonstrated capability gap. Make the smallest plausible owning-layer change instead of broad speculative rewrites.

### Experiment isolation
A candidate change should be attributable and reversible. Repository changes remain transactional; experimental candidates must not silently become accepted state before evaluation.

### Protected evaluation
The candidate should not rewrite the evaluator that decides whether the candidate passes. Material changes should include both failure-targeted held-in cases and held-out/regression coverage where feasible.

### Promotion / revert / inconclusive
Retain only when comparable evidence supports the intended improvement without material regression. Revert on regression. Mark inconclusive when the available surface cannot support a trustworthy comparison.

### Anti-benchmaxxing
Do not add named-task special cases or memorize fixed eval answers. A change must generalize to the owning behavior, not merely turn a benchmark green.

## ALREADY COVERED
DEDAL already separates design rationale, contract validation, and outcome validation; uses atomic Git transactions; preserves real regressions as evidence; and requires live/source verification for consequential state.

## REJECT AS DEFAULT
- autonomous unbounded self-rewrite loops;
- allowing a candidate to weaken its own guardrail/evaluator to pass;
- promoting upstream benchmark gains as DEDAL gains;
- automatically retaining every change that improves one metric while degrading correctness, authority, safety, or continuity;
- letting self-improvement expand Creator or platform permissions.

## Decision
- New skill: NO.
- Primary owner: Agent Engineering.
- Skill Acquisition remains the intake/audit path for external patterns.
- Add an executable self-improvement contract to CI.
- Evidence level: external-pattern audit plus contract validation only; real-task DEDAL improvement remains unmeasured.
