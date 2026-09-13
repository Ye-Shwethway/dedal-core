# Staged Release and Rollback

Use staged delivery to reduce blast radius when a failure would be expensive, difficult to detect, or difficult to reverse.

## Promotion model

Possible stages include:
- local/dev;
- automated test/build;
- internal/preview;
- closed/beta/staging;
- canary/percentage rollout;
- general production.

Not every project needs every stage. Add stages only when they buy meaningful risk reduction or evidence.

## Promotion gate

Before promotion, know:
- exact artifact/version/digest;
- target environment/channel;
- required test/security/review evidence;
- compatibility and migration state;
- smoke/health checks;
- rollback or forward-fix strategy;
- owner/authority for proceeding.

## Runtime verification

After deploy, verify the intended target rather than assuming the pipeline did so. Evidence may include:
- deployment revision/version readback;
- service health/endpoint behavior;
- mobile track/release status;
- checksum/image digest;
- smoke tests on critical flows;
- logs/metrics for known failure modes.

## Rollback

A rollback plan should name:
- last known-good release;
- how to restore it;
- data/schema compatibility;
- configuration/secret changes that must also revert;
- conditions that trigger rollback vs forward fix.

For irreversible data migrations, `redeploy old binary` is not a complete rollback plan.

## Release claim language

Keep states distinct:
- `built`;
- `verified artifact`;
- `published`;
- `deployed`;
- `runtime verified`;
- `fully rolled out`.

Report the highest state actually evidenced.
