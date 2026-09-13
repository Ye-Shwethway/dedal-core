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

## Trace the control surface

Capture enough structured trace data to answer:
- which instructions/context were active;
- which tools were available;
- which action was selected and why it was eligible;
- tool inputs/results/errors;
- state transitions and retries;
- guardrail/handoff events;
- final verification signal.

Protect private/sensitive data in traces; observability does not override the data boundary.

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

For subjective outputs, use an explicit rubric and Creator/human review where appropriate. For objectively checkable work, prefer tests, schemas, source verification, or environment results over model self-rating.

## Optimization loop

`observe failure -> classify layer -> make smallest plausible change -> rerun comparable eval -> inspect regressions -> retain or revert`

Automated prompt/tool optimization is appropriate only when the metric actually represents desired behavior and the evaluation set is not being overfit.
