# Failure Recovery and Compensation

Use this reference for multi-step workflows that can leave externally visible partial state.

## First classify the failed step

Before retrying, ask whether repeating the action is safe. Prefer retry only when the operation is idempotent, guarded by an idempotency key, or otherwise proven safe to repeat. Unknown repeatability is not a retry signal.

## Recovery choices

Choose among four explicit paths:

- **retry** — transient failure and safe repetition;
- **compensate** — prior committed effects are reversible through explicit semantic compensators;
- **preserve partial** — the achieved state is useful/acceptable and residual effects plus blocked work are recorded;
- **escalate** — automatic recovery is unsafe, unavailable, or itself failed.

## Compensation is not atomic rollback

Across external services, already committed actions usually cannot be ACID-rolled back. A compensation is a new action that semantically counteracts an earlier action. Run compensators for completed reversible steps in reverse dependency/completion order where that reflects the workflow semantics.

Never claim full rollback when an irreversible effect remains, such as a sent message, external publication, irreversible billing event, or destructive action without a trustworthy inverse.

## Partial-state truthfulness

If the workflow stops partially complete, record:

- which steps succeeded;
- which effects remain externally visible;
- which compensations succeeded or failed;
- blocked or unexecuted actions;
- whether manual intervention is required;
- the evidence/reference needed to resume safely.

A compensation failure is not successful recovery. Mark the workflow `manual_required` or equivalent and preserve the residual effects explicitly.

## Design guidance

When practical, design side-effecting tools with idempotency keys, read-back verification, bounded retries, and explicit compensators. Preflight checks and staging are preferable to compensation when they can cheaply prevent the risky effect in the first place.

Do not add saga machinery to simple read-only or locally atomic tasks. Recovery architecture should match actual side effects and failure risk.
