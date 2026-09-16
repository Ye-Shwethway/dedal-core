# Operations and verification

## Evidence layers

Cloudflare changes often span several independent layers. Verify only the layers relevant to the claim, but do not collapse them:

1. **source/config** — intended code and config are correct;
2. **resource control plane** — account/zone resource exists with expected settings;
3. **deployment state** — intended version/config reached the target environment;
4. **routing/identity/network** — DNS, route, Access, Tunnel, WAF, or network policy resolves the request as intended;
5. **data/service plane** — D1/R2/KV/Queue/DO/AI/service binding behaves as expected;
6. **runtime observation** — logs, traces, analytics, health checks, or direct requests support the claim.

A Wrangler/API success response is not automatically end-to-end proof.

## Troubleshooting order

Prefer the narrowest failing boundary:

- confirm account/zone/project/environment identity;
- inspect current config and bindings;
- confirm deployment/version state;
- confirm DNS/routes/custom-domain mapping;
- confirm Access/Tunnel/origin reachability when present;
- confirm resource binding and permissions;
- inspect current Cloudflare logs/analytics/observability evidence;
- reproduce the smallest failing request or data operation.

Avoid changing several control planes at once unless the dependency requires it.

## Mutation and recovery

Before high-impact changes, record the known-good state or recovery point where practical. DNS, Access policy, production deployment, resource deletion, database migration, and origin-routing changes can have different rollback semantics. A code rollback does not restore mutated storage or deleted resources.

Use idempotent/safely retryable operations when supported. If a partial change leaves residual effects, report them explicitly and choose retry, compensation, preserve-partial, or escalation according to the Cognitive Runtime recovery contract.


## Execution-surface failures

When a connector, MCP, aggregator, CLI, or API wrapper fails, identify whether the failure is in authentication, discovery/schema, serialization/transport, Cloudflare API validation, deployment, runtime, or read-back. Do not change correct application logic merely to accommodate a transport wrapper defect.

Read capability and write capability are separate evidence. A surface that lists Workers or downloads source may still be unable to preserve multipart boundaries, raw request bodies, module metadata, or large response bodies during upload. Verify the required transport semantics before consequential writes and switch to a more faithful surface when needed.

If the Creator is mobile-constrained, prefer automated connector/API recovery over asking for manual code editing. Manual dashboard edits are appropriate only after reasonable automated paths fail or when explicit human review is intended.

## Ambiguous write outcomes

An error returned after an upstream mutation is not proof that the mutation failed. Eventual consistency, post-write verification, timeout, or connector response handling can produce a false-negative result.

Before retrying a non-trivially idempotent mutation, read back state. If the desired state already exists, preserve it and do not retry. If the state remains unknown and retry could duplicate or destroy data, report an outcome-unknown condition with retry safety explicitly characterized.

## Observability

Use current Cloudflare-native logs, analytics, traces, tailing, build/deploy evidence, and product-specific diagnostics when available. Observability is evidence, not authority: a missing log line does not by itself prove a request never happened, and a healthy edge response does not prove downstream data correctness.

## Testing

Pair with Quality Engineering when the objective is independent acceptance/readiness. Local simulation or preview evidence should not be reported as production evidence. Prefer target-environment checks for claims about deployed behavior.
