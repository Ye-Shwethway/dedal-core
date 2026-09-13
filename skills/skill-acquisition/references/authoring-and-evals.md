# Skill Authoring and Evaluation

Use this reference when creating a new DEDAL skill or materially revising an existing one.

## Authoring contract

### Capture intent before prose
Define:
- capability and expected outcome;
- trigger contexts and non-trigger contexts;
- authoritative inputs and required tools;
- output shape;
- owner decisions versus agent-resolvable facts;
- objective success criteria when available.

Recover answers from the current workflow/history before asking the Creator to repeat known facts.

### Match instruction precision to risk
Use the least restrictive instruction form that remains reliable:
- **high freedom** — principles/heuristics when several good approaches exist;
- **medium freedom** — preferred workflow/pseudocode when variation is acceptable;
- **low freedom** — exact schema/script/order when deviation would cause failure, data loss, or incompatibility.

Do not turn preferences into rigid laws, and do not leave dangerous deterministic steps vague.

### Write for routing
The description is part of the routing contract. It should state both what the skill does and the contexts that should activate it. Avoid descriptions so broad that they steal unrelated tasks or so narrow that normal phrasing never triggers them.

Explicit aliases may be used for reliable owner invocation, but implicit routing should still be understandable from the description.

### Progressive disclosure
Keep the entrypoint focused on common decisions and the dominant workflow. Push specialized branches, long examples, schemas, large rule catalogs, and rare edge cases into references/scripts/assets that load only when needed.

A concise skill is not automatically better. The goal is **minimum context that preserves correct behavior**.

## Evaluation contract

A major rewrite should be compared against a meaningful baseline:
- new skill -> no-skill/current generic behavior when practical;
- revised skill -> previous proven version;
- imported/adapted skill -> current DEDAL behavior plus the candidate-derived version.

Use realistic prompts, not prompts written merely to make the skill look good.

### Evaluate four dimensions
1. **Routing** — does it trigger when useful and stay out when irrelevant?
2. **Task quality** — does it improve correctness, usefulness, safety, or consistency?
3. **Efficiency** — does the benefit justify added context, latency, tool work, or ceremony?
4. **Robustness** — does it hold across variants, edge cases, and different execution surfaces?

### Quantitative vs qualitative evidence
Use objective assertions when the outcome can be checked independently: file contents, schema, build result, extracted values, workflow gates, tool side effects, or known-good behavior.

Do not invent pseudo-objective scores for inherently subjective outputs. Use Creator review or clearly stated qualitative criteria for writing, design, aesthetics, or open-ended judgment.

### Variance and discriminating power
A benchmark that both versions always pass teaches little. Add cases that exercise the behavior the skill is meant to change. Re-run unstable cases before treating a small difference as evidence.

Record regressions as durable fixtures only when they represent behavior worth preserving.

## Promotion rule

Promote a rewrite when evidence indicates meaningful net improvement and no unacceptable regression. If the result is merely longer, more elaborate, or more fashionable, keep the proven version.