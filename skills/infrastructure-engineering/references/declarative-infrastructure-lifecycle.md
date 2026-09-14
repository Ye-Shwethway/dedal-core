# Declarative Infrastructure Lifecycle

Use this reference for Terraform/OpenTofu-style infrastructure lifecycles.

## Three-view model

Keep these distinct:

1. **Configuration** — declared desired infrastructure.
2. **State** — the tool's tracked mapping and last-known managed resource data.
3. **Live provider reality** — resources currently reported by the provider/control plane.

A plan reconciles these views and proposes actions; it does not mutate infrastructure. A final apply may differ from an earlier speculative plan if configuration, state, provider reality, variables, credentials, or dependencies changed.

## Change review

Before apply, classify every meaningful action as create, update-in-place, replace, destroy, import, move, or state-only reconciliation. Explicitly inspect replacements and destroys for identity, downtime, persistence, network, credential, and dependency effects.

For automation, prefer a reviewed saved/final plan when the operating model supports it. Interactive confirmation and `auto-approve` are UI mechanics, not substitutes for authorization.

## Drift and reconciliation

Drift means live resources no longer match tracked state/configuration. Determine whether the live change is authoritative before deciding what to reconcile. Refresh-only/state reconciliation can change tracked state without intentionally changing live infrastructure, so it still requires review.

## Imports and refactors

Importing a resource establishes management identity; it does not prove the configuration fully models the live resource. After import, plan again and reconcile configuration until the intended steady state is understood.

Use supported moved/import/refactor constructs when available instead of direct state surgery. Module refactors should preserve resource identity unless replacement is intentional.

## Freshness

Provider versions, backend behavior, CLI syntax, moved/import features, lock behavior, and compatibility are drift-sensitive. Verify current first-party documentation when material.
