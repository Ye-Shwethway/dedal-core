# Reliability Engineering / Observability-SRE Deep Audit — 2026-09-14

## Decision

**PROMOTE** a top-level `reliability-engineering` faculty.

This is not a monitoring-vendor skill. The distinct recurring ownership layer is production reliability: defining service-health objectives, selecting operational evidence, designing actionable alerting, coordinating and mitigating incidents, verifying recovery, and converting incidents into durable reliability learning.

## Sources reviewed

### Google SRE
Current Google SRE guidance reviewed 2026-09-14:
- Incident Management Guide
- Monitoring / Monitoring Distributed Systems
- Alerting on SLOs
- service reliability and rollout guidance

Durable patterns adapted:
- alert on symptoms/user impact rather than brittle implementation causes where practical;
- alerts should be timely and actionable;
- use service-level thinking to connect monitoring to user experience;
- incident response needs preparation, coordination, mitigation, and learning;
- blameless postmortems should improve detection, mitigation, coordination, and system design.

### OpenTelemetry
Current official OpenTelemetry documentation reviewed 2026-09-14.

Durable patterns adapted:
- observability requires intentional instrumentation;
- traces, metrics, logs, and related signals provide different views of system behavior;
- OpenTelemetry is vendor-neutral telemetry instrumentation/collection, not a reliability ownership model;
- telemetry generation and reliability decisions should remain conceptually separate.

### Sentry for AI
Pinned first-party source:
- repo: `getsentry/sentry-for-ai`
- commit: `2dc3b5d1232b38f88c881a07c1cddf825f1d4ffd`
- license: MIT

Useful patterns:
- production issue triage and instrumentation are distinct workflows;
- platform-specific setup belongs in progressive references rather than one enormous entrypoint;
- shared references can hydrate signal-specific knowledge on demand;
- current telemetry/provider details should be verified against provider documentation.

No third-party scripts or plugin installation were executed for this audit.

## Why a top-level owner is justified

Existing owners do not cleanly own the full operational loop:

- `software-development` builds/fixes code and instrumentation implementation.
- `quality-engineering` verifies acceptance/readiness before or around release.
- `release-engineering` owns artifact promotion, deployment evidence, and rollback mechanics.
- `security-engineering` owns security threats, policy, and security-incident authority.
- `cloudflare-platform` owns Cloudflare-specific product/platform semantics.
- `database-engineering` owns engine/database semantics.
- `agent-engineering` owns AI-agent traces/evals/harness observability when the agent system itself is the design target.

A recurring gap remains: **live service reliability** — what user-visible health means, which signals matter, when to page, how to coordinate/mitigate an outage, how to verify recovery, and what reliability learning should survive afterward.

That layer is independently routable and recurring across VPS services, Cloudflare systems, bots, APIs, databases, mobile backends, and agent-backed services.

## Ownership boundary

Reliability Engineering owns:
- SLI/SLO/error-budget reasoning when warranted;
- telemetry/observability strategy;
- actionable alerting and service-health dashboards;
- production incident triage/coordination/mitigation reasoning;
- recovery verification from the user/service perspective;
- post-incident reliability learning and follow-up structure.

It does **not** own:
- application implementation;
- release promotion authority;
- security policy;
- provider-specific platform semantics;
- database-engine semantics;
- independent pre-release QA;
- monitoring vendor configuration merely because a vendor is used.

## Negative findings / anti-patterns

Reject these as reliability evidence:
- `deploy succeeded -> service healthy`;
- `dashboard green -> users unaffected`;
- `alert cleared -> incident recovered`;
- `telemetry exists -> system observable`;
- `more logs/metrics -> better observability`;
- `every threshold should page`;
- `rollback -> all side effects undone`;
- `single human mistake -> sufficient root cause`.

## Promotion evidence boundary

This promotion is supported by strong first-party methodology, cross-project fit, explicit ownership separation, and an executable routing contract. It does **not** yet prove measurable DEDAL outcome improvement. Representative production/diagnostic work should supply outcome evidence naturally.

## Freshness rule

Provider-specific telemetry APIs, query syntax, retention, pricing, plan gates, sampling defaults, alert semantics, and feature status are drift-sensitive and require current authoritative documentation when material.