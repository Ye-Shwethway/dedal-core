# Transactions, migrations, concurrency, and connections

Load this reference when correctness depends on transaction boundaries, isolation, locks, migrations, connection/session behavior, or recovery.

## Transaction reasoning

Start from the invariant that must survive concurrent activity. Then choose the narrowest transaction/isolation mechanism that protects it.

For PostgreSQL:
- MVCC usually allows readers and writers to proceed without blocking each other, but row/table locks, serialization failures, and deadlocks still matter;
- retry logic must be bounded and tied to retryable failures, not blanket exception loops;
- explicit locks are a specialized tool, not the default substitute for understanding isolation.

For SQLite:
- ordinary SQLite permits multiple readers but effectively one writer at a time;
- WAL mode can allow readers and a writer concurrently, but it changes files/checkpoint behavior and remains subject to single-writer constraints;
- SQLite transaction/locking behavior must not be inferred from PostgreSQL semantics.

## Migration safety model

Before production mutation classify:
- additive vs destructive schema change;
- online/backward-compatible vs coordinated cutover;
- lock and rewrite cost;
- data backfill/transformation requirements;
- old/new application compatibility window;
- rollback feasibility for schema and for data separately;
- backup/restore or point-in-time recovery evidence when blast radius warrants it.

Prefer expand -> migrate/backfill -> verify -> contract for high-risk schema evolution when practical.

A `down` migration is not proof of recoverability. If data was deleted, truncated, irreversibly transformed, or overwritten, report the residual effect explicitly.

## Connection semantics

Connection mode is part of database behavior:
- pooled connections suit many request/response workloads but may not preserve session state;
- direct/session connections may be required for migrations, administrative work, temp/session objects, certain prepared-statement modes, LISTEN/NOTIFY, or engine/provider-specific features;
- serverless and edge runtimes can amplify connection storms; use provider/driver guidance and verify current limits when material.

## Safe execution and evidence

Before mutation:
1. confirm target environment/database/branch;
2. inspect current schema/version/migration state;
3. prefer a production-like branch/staging copy or dry-run for risky migrations;
4. define success and rollback/recovery checks;
5. execute only with task-scoped mutation authority.

After mutation, verify more than command success: schema state, constraints, representative reads/writes, migration history, query plans where affected, and runtime behavior. Pair with Release Engineering when this is a production promotion and Quality Engineering for independent readiness evidence.
