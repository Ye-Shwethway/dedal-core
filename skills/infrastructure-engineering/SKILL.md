---
name: infrastructure-engineering
description: Design, review, evolve, and reconcile declarative infrastructure safely across configuration, state, live resources, plans, applies, imports, drift, modules, providers, and machine-image workflows.
---

# Infrastructure Engineering

Own infrastructure lifecycle semantics, not every technology involved in infrastructure.

## Core workflow

1. **Identify the infrastructure authority model** — declarative configuration, state backend/workspace, provider/account/project, environment, and live resources.
2. **Establish current reality** — inspect configuration, state, provider-visible resources, and recent changes before proposing mutation.
3. **Classify the change** — create/update/replace/destroy/import/move/refactor/drift reconciliation/image build/state-only repair.
4. **Plan before mutation** — review proposed resource actions, dependencies, blast radius, credentials, data/state effects, and expected replacement/destruction.
5. **Apply only with authority** — treat plan/apply/import/state manipulation as side-effecting operations subject to task-scoped authorization.
6. **Verify multiple layers** — configuration intent, state reconciliation, provider/live resource result, and downstream service health are separate evidence layers.
7. **Preserve recovery** — know how to restore state/backend access, recover from partial applies, reverse safe configuration changes, and escalate irreversible effects.

## Durable rules

- Desired configuration, IaC state, and live provider reality are three related but distinct views. Do not silently collapse them.
- A speculative plan is not an applied change. A successful apply is not proof that the resulting service is healthy.
- Review replace/destroy actions explicitly when they may cause data loss, downtime, identity changes, or dependency churn.
- Treat state backends as sensitive operational assets; state may contain identifiers or secrets and should not be edited casually.
- Prefer supported import/move/refactor mechanisms over ad-hoc state surgery. Direct state mutation is a recovery-grade action.
- Drift can be intentional or accidental. Detect it, classify its authority, then decide whether configuration, state, or live resources should change.
- Module/provider abstractions should reduce repetition without hiding ownership, lifecycle, or destructive effects.
- `auto-approve` and unattended automation do not create authority; they only remove an interactive confirmation step.
- Version/provider/backend-specific syntax, capabilities, defaults, and migration behavior require current authoritative documentation when material.
- Terraform, OpenTofu, Packer, cloud CLIs, provider APIs, and MCP/tools are execution/reference surfaces, not authority sources.

## Ownership boundaries

- Application code and ordinary debugging -> `software-development`.
- Source-to-artifact/application release promotion -> `release-engineering`.
- Live-service health, incidents, SLOs and operational recovery -> `reliability-engineering`.
- Cloudflare product/platform semantics -> `cloudflare-platform`.
- Database schema/query/transaction semantics -> `database-engineering`.
- Security policy, trust boundaries, credentials and destructive-risk authority -> `security-engineering`.
- Independent acceptance/readiness verification -> `quality-engineering`.

## Load focused references on demand

- Terraform/OpenTofu state, plan/apply, imports, moves, drift, modules -> `references/declarative-infrastructure-lifecycle.md`
- High-risk changes, partial apply, recovery, provider boundaries and image workflows -> `references/change-safety-and-recovery.md`

Do not load infrastructure references for ordinary application coding merely because deployment eventually uses infrastructure.
