# Platform composition and freshness

## Choose by requirement, not catalog

Translate the workload into concrete needs first:

- request/compute execution
- static asset delivery
- relational records
- object/blob storage
- read-heavy key/value lookup
- per-entity coordination/state
- asynchronous buffering
- durable multi-step workflow
- private origin connectivity
- identity-gated access
- edge security/routing
- observability
- AI inference/retrieval/agent runtime

Then choose the smallest Cloudflare product set that satisfies those needs. Similar products should be distinguished by data shape, consistency, coordination, lifecycle, and operational burden rather than by popularity.

## Incumbent architecture rule

A newer recommendation does not automatically justify migration. Existing Pages, Workers, D1, Tunnel, Access, or other deployments are authoritative project state. Preserve them during unrelated maintenance unless the Creator explicitly requests migration or evidence shows a material defect.

## Freshness classes

Always verify from current official Cloudflare docs when material:

- current recommended product/migration path
- beta/preview/stable/deprecated status
- pricing and plan entitlements
- quotas and resource limits
- Wrangler/API syntax and field names
- supported runtimes/framework adapters
- product compatibility and binding support
- regional/data-locality behavior
- security/access requirements

More durable concepts such as separating compute, storage, coordination, identity, and network planes may remain in Core.

## Environment and bindings

Treat local, preview/staging, and production as distinct environments unless the project proves otherwise. Verify resource identifiers, bindings, variables, secrets, routes, custom domains, and account/zone context for the target environment. Do not assume nested environment configuration inherits every binding or variable.

When the task changes resource topology, make the dependency graph explicit: application -> binding -> resource -> network/access policy -> origin/data plane. Verify the affected edges after mutation.

## Product-specific detail

Use official Cloudflare docs or first-party skill references on demand. Do not copy broad product catalogs into DEDAL merely to avoid retrieval; progressive disclosure is preferred because the platform changes quickly.
