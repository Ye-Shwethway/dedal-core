---
name: release-engineering
description: Safely turn verified source into attributable artifacts and deployed releases: versioning, reproducible builds, artifact provenance, CI/CD, staged rollout, deployment verification, rollback, release notes, and post-release evidence. Use when shipping software, producing APK/AAB/binaries/images/packages, or changing production delivery pipelines.
---

# Release Engineering

A release is not complete when a build command exits zero. It is complete when the intended source produces the intended artifact, the artifact is attributable and verified, the target environment receives the intended version, and rollback/ownership are understood.

## Core workflow

1. **Define release unit** — source ref/commit, version, target environment/channel, artifact(s), compatibility/migration constraints.
2. **Verify source readiness** — required tests/review/security gates and repository state are satisfied at the exact source ref.
3. **Build deterministically enough for the risk** — pin relevant inputs, avoid hidden workstation-only state, record tool/runtime assumptions when material.
4. **Bind artifact to source** — capture hashes/digests, workflow/run identity, source commit, build metadata, and provenance/attestation when supported and worthwhile.
5. **Promote deliberately** — development/testing/staging/closed tracks/canary before broad production when the product/risk warrants it.
6. **Verify deployment/runtime** — prove the intended version reached the target and smoke-check critical behavior; CI success alone is not deployment proof.
7. **Preserve rollback** — know the previous known-good version/state and migration reversibility before high-impact rollout.
8. **Record release evidence** — version, commit, artifact identity, verification result, deployment target, known residual risk, and rollback point.

## Durable rules

- Never present an artifact without knowing which source commit/ref produced it when attribution matters.
- Distinguish `build succeeded`, `artifact exists`, `artifact verified`, `deployment completed`, and `runtime healthy` as separate evidence levels.
- Tags and filenames are labels; use digests/hashes/attestations for stronger artifact identity when supported.
- Provenance proves origin/process claims, not that the software is vulnerability-free or correct.
- Prefer short-lived/OIDC deployment credentials over long-lived secrets when the platform supports them and the migration cost is justified.
- Release automation should be idempotent or safely retryable where practical; partial deployment needs explicit recovery semantics.
- Database/schema migrations require forward/backward compatibility and rollback thinking separate from application artifact rollback.
- Versioning should communicate compatibility intent, but project ecosystem rules outrank generic SemVer when they differ.
- Generated release notes must be checked against the actual diff/release scope.
- Production completion claims require target-environment evidence, not only repository or CI evidence.

## Pairing

Pair with `software-development` for implementation/testing, `github` for Actions/releases/artifacts, `security-engineering` for supply-chain/credential controls, and `project-bootstrap` to discover project-specific release paths.

Load references on demand:
- `references/artifact-identity-and-provenance.md`
- `references/staged-release-and-rollback.md`
