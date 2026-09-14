# Evals and Observability

Agent engineering is incomplete without evidence that the harness improved the system.

## Evaluate the system, not only the final answer

Useful dimensions include:
- task success / correctness;
- tool selection and parameter correctness;
- recovery from tool/environment failure;
- instruction and authority adherence;
- context efficiency / unnecessary retrieval;
- number of turns and retries;
- latency and cost where measurable;
- robustness across task variants;
- handoff / continuity quality for long-running work.

Do not collapse these into one score unless the weighting is explicit and justified.

## Baselines

For a new harness, establish a simple capable-model baseline first. For a revision, compare against the previous proven harness on the same task set where feasible.

A more elaborate agent is not better merely because it uses more steps, agents, tools, or tokens.

## Separate tracing from evaluation

A trace records what happened; an eval decides whether what happened was acceptable. Do not treat rich telemetry as evidence of correctness by itself.

Prefer deterministic trajectory assertions when the behavior is structurally checkable: required tool use, forbidden tools, call order, argument constraints, retry bounds, guardrail outcomes, verification steps, and state-promotion evidence. Use model or human judgment only for genuinely semantic or subjective dimensions that deterministic checks cannot represent well.

## Trace the control surface

Capture enough structured trace data to answer:
- which context class was loaded, without persisting private hidden reasoning;
- which tools/actions were selected;
- tool success/failure and mutation status;
- state transitions and retries;
- guardrail/handoff events;
- final verification signal and evidence reference;
- token/cost/latency when the runtime exposes them and they matter to the decision.

For DEDAL Core, default to privacy-minimal typed metadata rather than raw prompts, raw responses, or chain-of-thought. A useful event vocabulary includes `context_read`, `tool_call`, `tool_result`, `guardrail`, `retry`, `state_transition`, `verification`, and `handoff`.

Protect private/sensitive data in traces; observability does not override the data boundary.

## Replay and regression

Record/replay is useful only when a stable execution seam exists. A replay fixture should fail loudly when the request contract changes rather than silently serving an old response to a new prompt/tool shape.

Replay proves reproducibility against a recorded dependency; it does not prove the live model/provider has not drifted. Pair offline replay with representative live canaries when live-model drift matters.

Promote real failures into regression cases. Prefer small, reviewable cases that assert the failed invariant rather than permanently storing an entire private conversation.

## Failure taxonomy

Classify failures before changing prompts:
1. model/task reasoning;
2. missing or polluted context;
3. bad tool affordance/schema/description;
4. retrieval failure;
5. orchestration/delegation error;
6. loop/termination error;
7. stale state or continuity loss;
8. permission/guardrail design;
9. environment/runtime failure;
10. evaluator/metric weakness.

Fix the owning layer. Prompt edits are the wrong repair for many harness failures.

## Evaluation tasks

Use representative tasks including normal cases, edge cases, tool failures, ambiguous requests, insufficient evidence, and authority boundaries. Add regressions from real failures.

For subjective outputs, use an explicit rubric and Creator/human review where appropriate. For objectively checkable work, prefer tests, schemas, source verification, environment results, or deterministic trajectory assertions over model self-rating.

## Optimization loop

`observe failure -> classify layer -> make smallest plausible change -> rerun comparable eval -> inspect regressions -> retain or revert`

Automated prompt/tool optimization is appropriate only when the metric actually represents desired behavior and the evaluation set is not being overfit.
