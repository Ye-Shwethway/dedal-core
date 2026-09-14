# Incidents and Reliability Learning

Use this reference for active outages/degradation, production diagnosis, recovery verification, and post-incident learning.

## Incident phases

1. **Detect** — confirm scope, start time, affected users/functions, and evidence quality.
2. **Coordinate** — establish one working incident thread/timeline and explicit ownership for high-impact response when multiple people/systems are involved.
3. **Mitigate** — prioritize reducing user impact over completing root-cause analysis. Roll back, disable, reroute, shed load, or fail over only when authorized and evidence supports the action.
4. **Diagnose** — correlate recent changes, service topology, telemetry, dependency/platform/database behavior, and representative requests.
5. **Recover** — verify critical user-visible behavior, not only internal metrics or alert clearance.
6. **Learn** — document impact, timeline, contributing conditions, detection/response gaps, and concrete follow-ups.

## Reliability response rules

- Do not automatically retry a failed side-effecting recovery action unless idempotency/safety is known.
- A rollback is a new production action, not a magical undo. Database/data effects may require separate compensation/recovery.
- Preserve partial-state truth: note what changed, what did not, and what residual effects remain.
- If evidence is ambiguous, prefer reversible blast-radius reduction over speculative destructive fixes.
- Escalate when authority, access, or expertise is insufficient; do not convert tool availability into authorization.

## Postmortems

Use blameless analysis to improve the system, not to erase accountability or factual causality. Good follow-ups may improve:
- detection and alert quality;
- mitigation speed and runbooks;
- dependency isolation/resilience;
- deployment safeguards;
- observability/instrumentation;
- ownership/escalation paths;
- automated regression/quality checks.

Avoid a single-root-cause story when multiple conditions were necessary. Distinguish trigger, contributing factors, latent weaknesses, and response gaps.

## Recovery evidence ladder

`command executed` < `platform reports healthy` < `telemetry normalizing` < `representative user path succeeds` < `sustained recovery over relevant window`

Use the strongest feasible level and state residual uncertainty.