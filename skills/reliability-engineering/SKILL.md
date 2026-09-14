---
name: reliability-engineering
description: Keep production systems reliably useful through service-level thinking, observability strategy, actionable alerting, incident response, production diagnosis, resilience, and post-incident learning.
---

# Reliability Engineering

Own the operational question: **is the production service healthy enough for users, and what should we do when it is not?**

## Core workflow

1. **Define the user-visible service** — identify critical journeys/functions, dependencies, and failure boundaries.
2. **Choose reliability objectives** — use SLIs/SLOs or another explicit service-health contract when scale/risk warrants it; avoid vanity metrics.
3. **Design observability for questions** — select the smallest useful combination of metrics, logs, traces, profiles/events, synthetic probes, and provider-native signals.
4. **Alert on actionable user impact** — prefer symptom/SLO-oriented alerts; use cause/resource alerts only when they predict imminent user harm or enable a specific action.
5. **Diagnose with correlated evidence** — start from impact/time window, recent changes, service topology, telemetry, dependency health, and database/platform evidence. Separate correlation from causation.
6. **Mitigate before perfect explanation when impact is active** — reduce blast radius, rollback/disable/reroute when authorized and safer, then continue diagnosis.
7. **Verify recovery from the user perspective** — alert clearance alone is not proof; check representative service behavior and residual degradation.
8. **Learn durably** — capture timeline, impact, contributing conditions, detection/response gaps, corrective actions, and bounded follow-up without blame theater.

## Ownership boundaries

- `release-engineering` owns build/promotion/rollback mechanics; Reliability owns production health and incident response after/between releases.
- `software-development` owns code changes and instrumentation implementation; Reliability owns what operational questions/signals are needed.
- `quality-engineering` owns independent acceptance/readiness before promotion; Reliability owns live-service behavior and incident evidence.
- `security-engineering` owns security threat/policy/incident authority; Reliability may support availability/telemetry/coordination during security incidents.
- `cloudflare-platform` and `database-engineering` own provider/engine semantics; Reliability composes their evidence into service-health diagnosis.
- `agent-engineering` owns agent traces/evals as an AI-system concern; Reliability owns production service reliability when an agent is part of the service.

## Durable rules

- Telemetry is evidence, not truth by itself; missing telemetry is not evidence of health.
- A green dashboard, cleared alert, or successful deploy is not sufficient proof of user-visible recovery.
- Instrumentation should answer real operational questions; do not maximize telemetry volume by default.
- Prefer actionable alerts over noisy coverage. Alert fatigue is a reliability defect.
- Distinguish detection, diagnosis, mitigation, recovery, and root-cause learning as separate evidence stages.
- During active incidents, preserve a concise timeline and decisions; do not let documentation block urgent mitigation.
- Postmortems should improve detection, mitigation, architecture, coordination, or runbooks—not merely assign a single human cause.
- SLOs/error budgets are tools, not mandatory ceremony for every small/local system.
- Tool availability (Sentry, OTel, provider dashboards, shell access, MCP) does not grant mutation authority.
- Version/provider-specific telemetry APIs, retention, pricing, limits, query syntax, and alert semantics require current authoritative docs when material.

## Load references on demand

- SLI/SLO, telemetry, dashboards, alerts -> `references/observability-and-service-health.md`
- Outage/incident response, mitigation, recovery, postmortem -> `references/incidents-and-reliability-learning.md`

Use the smallest sufficient set of signals and supporting faculties for the active subgoal.