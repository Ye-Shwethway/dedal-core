---
name: cloudflare-platform
description: Design, build, configure, troubleshoot, and evolve systems on Cloudflare by selecting and composing the right platform products while keeping drift-sensitive facts live-verified.
---

# Cloudflare Platform

Own Cloudflare-specific platform reasoning: product selection, service composition, bindings/configuration, edge/network topology, and platform-native operational semantics.

## Core workflow

1. **Start from the workload.** Identify compute, state, storage, coordination, networking, security, observability, deployment, and data-locality requirements before naming products.
2. **Respect incumbent truth.** Preserve an existing Pages/Workers/Access/Tunnel/D1/R2 architecture unless the task explicitly calls for migration or a material defect requires change.
3. **Choose the smallest coherent product set.** Add a Cloudflare product only when it solves a concrete requirement. Prefer a simple composition over stacking services by novelty.
4. **Verify drift-sensitive facts live.** Current product availability, beta/stable status, limits, pricing, CLI syntax, API fields, compatibility, recommended migration paths, and plan requirements must come from current authoritative Cloudflare docs when material.
5. **Separate control planes.** Distinguish code/config, account resources, DNS/network routing, identity/access policy, data/storage state, and deployment state. A successful change in one plane is not proof of another.
6. **Plan environment/binding semantics explicitly.** Know which resources and secrets exist in local, preview, staging, and production; do not assume environment inheritance or binding identity.
7. **Execute with the appropriate surface.** Use current native/plugin/MCP/API/CLI capabilities when authorized; tool availability does not grant mutation authority.
8. **Verify the real target.** Read back resource/config state and, where appropriate, exercise the deployed route, binding, storage path, access rule, or tunnel. Do not equate command success with end-to-end correctness.
9. **Verify execution-surface fidelity.** A connector that can discover/read resources may still rewrite or reject raw/multipart/source-upload requests. Validate the required request semantics before production mutation and change execution surface rather than distorting correct application code.
10. **Automate before delegating manual edits.** Within granted authority, exhaust practical native/direct/API/CLI paths before asking the Creator to edit production source by hand; manual dashboard editing is a last resort unless human review is explicitly desired.

## Ownership boundary

- **Software Development** owns application implementation, debugging, and developer tests. Cloudflare Platform supplies platform constraints and Cloudflare-native implementation guidance.
- **Release Engineering** owns artifact/source attribution, staged promotion, deployment evidence, and rollback policy. Cloudflare Platform owns Cloudflare deployment/version semantics and resource topology.
- **Security Engineering** owns threat models, least privilege, credential policy, and trust boundaries. Cloudflare Platform owns how Access, Tunnel, WAF, Zero Trust, secrets, and related Cloudflare controls actually compose.
- **Data Operations / future Database Engineering** own data integrity and database semantics. Cloudflare Platform owns D1/R2/KV/Queues/DO/Hyperdrive product fit, bindings, platform limits, and Cloudflare-specific operational behavior.
- **Quality Engineering** owns independent acceptance/readiness evidence. Cloudflare Platform provides Cloudflare-native observability/testing surfaces and deployment facts.
- **Agent Engineering** owns agent/harness design. Cloudflare Platform owns Cloudflare Agents SDK, Workers AI, Vectorize, AI Gateway, Sandbox, and MCP hosting only as platform primitives.

## Durable rules

- Do not freeze volatile product manuals into Core; retrieve current official docs for facts likely to drift.
- Prefer official Cloudflare documentation and first-party skills over community snippets when they conflict.
- Preserve working existing architecture during unrelated maintenance; migration is an explicit product decision.
- Distinguish local emulation, preview, deployed Worker/Pages state, DNS propagation, Access policy, Tunnel connectivity, and origin health as separate evidence layers.
- Never expose secrets in source, logs, screenshots, or public Core. Use supported secret/binding mechanisms.
- Treat destructive resource deletion, DNS changes, Access-policy changes, production deploys, billing-affecting changes, and data migrations as higher-impact mutations requiring the corresponding authority and recovery thinking.
- Treat deployed Worker source, repository source, build artifacts, and sanitized public reconstructions as distinct identities until equivalence is proven. Never overwrite a newer live Worker with stale repository source merely because the repository is easier to access.
- If a mutation may have committed before a connector/read-back failure, verify state before retrying. Avoid blind retries for operations that can duplicate or destructively repeat effects.
- Cloudflare product recommendations must follow the workload; do not route by brand familiarity.

## Progressive references

- `references/platform-composition-and-freshness.md` — product-selection method, live-doc policy, incumbent architecture, and environment/binding reasoning.
- `references/operations-and-verification.md` — deploy/config/network/data-plane verification, observability, troubleshooting, and recovery evidence.
- `references/worker-deployment-and-connector-recovery.md` — live Worker source identity, connector/aggregation transport fidelity, source upload recovery, outcome-unknown mutations, and automation-first mobile-friendly operations.

Load product-specific Cloudflare documentation only when the active task needs it.
