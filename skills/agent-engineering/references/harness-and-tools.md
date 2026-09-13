# Harness and Tool Design

## Harness role

The harness is the executable environment around the model: tool schemas, dispatch, state, permissions, retrieval, error handling, retries, observability, budgets, and persistence. A better harness can materially improve the same model without changing its weights.

## Agent-computer interface

Design the action space for the model rather than exposing raw implementation detail by default.

Prefer tools that:
- map to meaningful agent goals or natural task subdivisions;
- have distinct, non-overlapping purposes;
- use precise parameter names and strict schemas;
- return high-signal results plus enough provenance/state to continue;
- provide actionable validation errors;
- support filtering, search, pagination, ranges, or targeted retrieval for large data;
- expose destructive/open-world effects clearly.

Sometimes one workflow-oriented tool is better than several low-level API wrappers when the low-level sequence is deterministic and repeatedly wastes model turns.

## Tool selection quality

More tools can reduce performance when descriptions overlap or the choice surface becomes ambiguous. Add a tool only when it expands useful action space or measurably improves an existing workflow.

Namespace related tools when it clarifies boundaries. Evaluate tool names/descriptions with real tasks rather than assuming developer-friendly APIs are also model-friendly.

## Result design

Tool output becomes model context. Return what is needed for the next decision, not every available field.

For potentially large results:
- search before list-all;
- return matches with compact surrounding context;
- paginate or range-read;
- preserve stable identifiers for follow-up fetches;
- signal truncation and tell the agent how to narrow the next request.

## Error design

Errors should identify:
- what was invalid or unavailable;
- which constraint was violated;
- how to correct the call when safe;
- whether retrying unchanged is pointless.

Opaque stack traces and generic `failed` responses force the model to guess.

## Authority and blast radius

Separate read-only/reversible actions from sensitive, destructive, financial, publishing, credential, or production-impacting actions. Use deterministic permission checks and human approval gates where authority requires them; do not rely only on a prompt reminder.

## Harness freshness

Harness assumptions can age as models and runtimes improve. Periodically challenge workarounds, mandatory decomposition, retry rituals, and tool abstractions. Remove scaffolding that no longer improves measured outcomes.
