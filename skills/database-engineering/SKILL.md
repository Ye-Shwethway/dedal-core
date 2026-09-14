---
name: database-engineering
description: Design, evolve, diagnose, and verify database semantics: schemas, keys/constraints, indexes/access paths, query plans, transactions/isolation/locking, migrations, connection behavior, and engine-specific operational tradeoffs across PostgreSQL, SQLite/D1, and related SQL systems.
---

# Database Engineering

Use this skill when correctness or performance depends on database semantics rather than ordinary application code or record reconciliation.

## Core lifecycle

`identify engine/workload -> model invariants -> design schema/access paths -> reason about transactions/concurrency -> plan migration -> execute with scoped authority -> verify plans/locks/invariants/runtime -> record residual risk`

## Rules

1. **Engine before advice** — identify database engine, major version where material, deployment model, connection path, and workload shape before applying engine-specific guidance.
2. **Invariants before schema syntax** — define identity, nullability, uniqueness, referential rules, lifecycle constraints, and consistency requirements before selecting tables, types, or constraints.
3. **Indexes are workload claims** — add, remove, or reorder indexes because observed/query-plan evidence and access patterns justify them, not because a column looks important.
4. **Query plans outrank intuition** — for performance work, inspect the strongest available planner/runtime evidence (`EXPLAIN`, `EXPLAIN ANALYZE`, engine-native diagnostics, representative timing) before claiming improvement.
5. **Transactions are business correctness** — choose transaction boundaries and isolation from the invariants that must remain true under concurrency; understand retries, conflicts, deadlocks, and engine-specific writer behavior.
6. **Migration safety is asymmetric** — schema rollback does not imply data rollback. Classify destructive transforms, backfills, type rewrites, lock impact, compatibility windows, and recovery before production mutation.
7. **Connections have semantics** — pooled vs direct/session connections, prepared statements, session state, temp objects, connection limits, and serverless execution can materially change correctness or performance.
8. **Provider layer is separate** — provider bindings, account resources, networking, plans, CLI/API syntax, and platform deployment remain with the provider specialist; this skill owns database behavior inside that environment.
9. **Data operations are separate** — reconciliation, deduplication, spreadsheet/table staging, row-level business cleanup, and source authority remain Data Operations/domain-owner work unless database semantics are the blocking concern.
10. **Freshness where material** — verify current official documentation for engine-version features, provider extensions, migration commands, compatibility, and changed defaults before relying on frozen instructions.

## Load focused references on demand

- Schema/constraints/indexes/query plans/performance -> `references/schema-index-query.md`
- Transactions/isolation/locking/migrations/connections/recovery -> `references/transactions-migrations-concurrency.md`

Do not load both references for a trivial database task.

## Pairing

Pair with Software Development for ORM/application implementation, Data Operations for record reconciliation and staged data cleanup, Cloudflare Platform for D1/Hyperdrive/bindings/provider semantics, Release Engineering for production migration/promotion, Quality Engineering for independent acceptance/readiness, and Security Engineering for database trust/access policy.

## Completion evidence

A database change is not proven because SQL parsed, an ORM schema compiled, or a migration command returned success. Use evidence appropriate to the claim: schema introspection, constraints/invariant checks, query plans, migration dry-runs/branch tests, lock/concurrency behavior, representative workload measurements, data readback, runtime observation, and recovery/rollback evidence where relevant.
