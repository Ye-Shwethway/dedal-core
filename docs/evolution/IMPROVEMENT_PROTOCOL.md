# DEDAL Improvement Protocol

## Purpose

DEDAL should improve through explicit system evolution rather than vague claims of becoming smarter.

## Improvement Loop

```text
1. Execute a real task
2. Observe the result
3. Identify success, failure, friction, or uncertainty
4. Decide whether the lesson is durable
5. Encode the lesson in the smallest useful layer
6. Validate the change
7. Preserve a checkpoint when the change is meaningful
```

## Where Improvements Belong

Use the narrowest durable layer that solves the problem:

- **Prompt/interaction habit** — small recurring communication correction;
- **Memory/personal context** — stable user-specific preference or history;
- **Project checkpoint** — project-specific state or accepted decision;
- **AGENTS.md** — high-level operating rule that should govern future agents;
- **Workflow/skill** — repeatable procedure;
- **Test/evaluation** — behavior that can be mechanically checked;
- **Tool/MCP integration** — missing external capability;
- **Automation** — useful repeated or conditional execution;
- **Architecture document** — durable system-level decision.

Do not escalate every lesson into a global rule.

## Evidence Standard

A claimed improvement should ideally answer:

- What failure or opportunity triggered it?
- What changed?
- Why should that change help?
- How was it verified?
- What is the rollback path?

Separate evidence maturity:

1. **Design rationale** — the change has a reasoned mechanism and addresses an observed failure/opportunity.
2. **Contract validation** — rules, tests, or structural checks show the change is internally coherent and regression-safe.
3. **Outcome validation** — representative real tasks show improvement against a meaningful baseline.

Do not present design rationale or contract validation as measured outcome improvement.

## Failure Taxonomy

When useful, classify failures as:

- continuity failure;
- retrieval failure;
- hallucinated state;
- tool-selection failure;
- execution failure;
- validation failure;
- security/privacy failure;
- UX/communication failure;
- creative canon drift;
- over-engineering;
- under-specification.

## Regression Principle

If a failure is important and testable, prefer adding a regression check rather than relying only on memory.

Examples:

- required foundational files exist;
- public repo contains no obvious secret files;
- YAML/JSON schemas parse;
- continuity checkpoint exists;
- project-specific tests pass.

## Review Principle

Periodically remove stale rules, duplicated instructions, obsolete capability claims, and workflow complexity that no longer provides value.

Self-improvement includes simplification.
## Learning Closure Principle

A material repair is not durably complete merely because the active task works again. For corrections, regressions, production hotfixes, or reusable better procedures, reconcile all applicable sinks before closure:

1. verified runtime/user-path repair;
2. canonical source capable of reproducing the repair;
3. regression guard or explicit not-testable rationale;
4. durable learning at the narrowest correct public/private scope;
5. continuity/checkpoint state when future work depends on the change;
6. independent verification and a rollback/recovery path.

When live behavior is changed outside canonical source, create explicit **source-sync debt**. The incident may be mitigated but is not durably closed until that debt is cleared.

Use `skills/self-improvement/` to orchestrate this loop. The skill may automatically detect/capture learning candidates, but it never expands authority or grants itself permission to rewrite governing state.

## Recurrence Principle

If the same failure returns after it was supposedly solved, first inspect whether the previous learning loop failed to reconcile source, tests, lessons, or continuity state. A repeated known failure is evidence of incomplete closure until proven otherwise.

