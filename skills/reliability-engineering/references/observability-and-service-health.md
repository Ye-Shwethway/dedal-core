# Observability and Service Health

Use this reference when the task is about monitoring strategy, service health, telemetry, dashboards, SLI/SLO design, or alerting.

## Start from user impact

- Define the critical user-visible function before choosing metrics.
- Prefer service indicators that represent successful requests/actions, latency, freshness, correctness, availability, or another directly meaningful outcome.
- Service-level objectives are useful when they create a decision boundary for reliability work; do not invent SLO ceremony for trivial systems.
- Error budgets are decision tools linking acceptable unreliability to change velocity; they are not a substitute for judgment.

## Signal selection

Use telemetry deliberately:
- **metrics** for rates, distributions, saturation, trends, and alertable aggregates;
- **logs** for discrete events and rich local context;
- **traces** for request paths and cross-service latency/dependency reasoning;
- **profiles/events** when code/resource behavior or specific event streams answer the question;
- **synthetic/black-box probes** for end-to-end user-facing checks;
- **provider-native signals** when they expose relevant platform behavior.

OpenTelemetry provides vendor-neutral telemetry generation/collection for traces, metrics, logs, and related context. It is an execution/instrumentation standard, not a reliability policy engine.

## Alerting

Prefer alerts that are:
- tied to meaningful user impact or imminent failure;
- timely enough to act;
- actionable by the receiver;
- low enough in noise that pages retain urgency.

Avoid paging on every internal threshold. Internal cause/resource alerts are justified when they predict near-term user impact or require specific human action.

## Dashboards and diagnosis

A useful dashboard should help answer:
1. Are users affected?
2. What changed?
3. Which dependency/component correlates with impact?
4. Is mitigation working?

Correlation is not causation. Compare timelines, deployments/config changes, dependency health, database/platform signals, and representative user behavior.

## Freshness

Provider-specific APIs, sampling defaults, retention, pricing, alert syntax, query languages, and feature availability drift. Verify current official docs when material.