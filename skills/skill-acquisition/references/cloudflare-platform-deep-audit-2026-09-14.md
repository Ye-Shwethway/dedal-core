# Cloudflare Platform deep audit — 2026-09-14

## Decision

**PROMOTE** a DEDAL-native `cloudflare-platform` top-level faculty.

The promotion is not justified by vendor popularity. It is justified by repeated Creator workflows and a distinct reasoning layer that spans Cloudflare product selection, bindings/configuration, edge/network topology, account/zone resources, platform-native data/coordination primitives, and Cloudflare-specific operational evidence.

## Primary source

- `cloudflare/skills`
- pinned baseline: `b052c32bab7dd493513260228a36c88294f343f1`
- license: Apache-2.0
- reviewed: first-party `skills/cloudflare/SKILL.md`, repository skill catalog, and representative product references
- current authoritative Cloudflare developer documentation reviewed for Workers, Pages, D1/R2, Wrangler, networking/access, and observability patterns

## Adapt

1. **Goal-first product composition.** Start from workload requirements, then choose a small coherent Cloudflare product set.
2. **Progressive product detail.** Keep durable routing principles in Core; load product docs/references only when needed.
3. **Live verification for drift-sensitive facts.** Availability, beta/stable status, limits, pricing, CLI/API syntax, plan requirements, and migration recommendations are current-doc questions.
4. **Incumbent architecture respect.** Preserve working Pages/Workers/Access/Tunnel/etc. during unrelated maintenance; a newer recommendation is not an automatic migration mandate.
5. **Control-plane separation.** Source/config, account resources, DNS/network routing, identity/access, data state, deployment state, and runtime observation are distinct evidence layers.
6. **Environment/binding explicitness.** Local/preview/production bindings and secrets must be verified rather than assumed to inherit.
7. **Platform-specific operational evidence.** Command success is weaker than readback plus target-route/resource/runtime evidence.
8. **Cross-faculty boundary.** Cloudflare Platform owns platform semantics; implementation, release authority, security policy, data integrity, QA readiness, and agent architecture retain their existing owners.

## Reject

- importing the entire Cloudflare product manual into Core;
- freezing current quotas/pricing/preview status as durable DEDAL truth;
- treating Cloudflare Platform as a replacement for Software Development or Release Engineering;
- automatically migrating Pages to Workers during unrelated work;
- selecting products because they are new or prominent rather than because the workload needs them;
- treating Cloudflare MCP/API/CLI availability as mutation authority;
- assuming a successful deployment command proves DNS, Access, Tunnel, origin, storage, or application behavior;
- duplicating product-specific subskills as top-level DEDAL faculties unless real work later proves independent ownership value.

## Ownership boundary

- `cloudflare-platform`: Cloudflare product/platform semantics and architecture composition.
- `software-development`: code implementation, debugging, developer tests.
- `release-engineering`: promotion, provenance, deployment evidence, rollback policy.
- `security-engineering`: trust boundaries, threat models, least privilege, credential policy.
- `data-operations` / future database owner: data correctness and database semantics.
- `quality-engineering`: independent acceptance/readiness evidence.
- `agent-engineering`: agent/harness design; Cloudflare agent products remain platform primitives.

## Evidence boundary

This audit supports architecture and routing promotion. It does not prove that the new faculty improves every Cloudflare task. Representative ordinary work must still provide outcome evidence, especially on routing cost, stale-fact avoidance, and cross-faculty handoff quality.
