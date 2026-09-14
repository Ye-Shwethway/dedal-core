# Database Engineering deep audit — 2026-09-14

## Question

Does DEDAL need a top-level Database Engineering faculty, or are Software Development + Data Operations + provider specialists sufficient?

## Sources reviewed

### PostgreSQL official documentation
- PostgreSQL 18 concurrency-control documentation: MVCC, transaction isolation, explicit locking, serialization failures, and consistency under concurrent access.
- PostgreSQL index/query-planning documentation and operational guidance where relevant.

Durable signal: transaction/isolation/locking semantics are application-correctness concerns, not merely SQL syntax or generic implementation detail.

### SQLite official documentation
- transaction semantics;
- isolation and single-writer behavior;
- rollback journal vs WAL mode;
- locking/concurrency and checkpoint implications.

Durable signal: engine choice materially changes concurrency/recovery behavior. PostgreSQL advice cannot be mechanically transferred to SQLite/D1.

### neondatabase/postgres-skills
Pinned baseline: `27fe45e0f71ea89a6eaf9ea4d2e4068957c81c26`.

The corpus separates schema design, indexing, query optimization, performance diagnostics, transaction isolation, backup/restore, pooling, upgrades, and replication into dedicated references. Useful pattern: progressive disclosure around stable database concerns rather than one giant SQL manual.

### supabase/agent-skills
Pinned baseline: `8331f910845103c08d51f6ca1d86ebb7d1f745e3`.

Useful signal: first-party Supabase skills treat Postgres performance/schema/indexing/concurrency/connection behavior as specialist knowledge while keeping platform/Auth/Edge/Storage concerns separate. Current-product details are explicitly freshness-sensitive.

### Neon current skill corpus
Current Neon/Lakebase skills similarly separate database behavior from provider orchestration and recommend current official docs for evolving provider facts.

## Ownership analysis

### Software Development
Owns application architecture, repository implementation, ORM/data-access code, debugging, tests, and code review.

It should not need to carry deep planner/index/isolation/migration semantics in every coding task.

### Data Operations
Owns source authority, record identity, reconciliation, deduplication, deterministic transforms, spreadsheet/table staging, validation, and promotion of operational datasets.

It does not own DB planner behavior, transaction isolation, locks, connection modes, index design, or engine-specific migration mechanics.

### Cloudflare Platform
Owns D1/Hyperdrive/provider product selection, bindings, account resources, runtime integration, current limits, and Cloudflare-specific operational semantics.

Database Engineering owns D1/SQLite schema/query/transaction semantics. Provider and database owners should pair when both layers matter.

### Release Engineering
Owns production promotion, artifact/source provenance, rollout, rollback orchestration, and release evidence. Database Engineering supplies migration semantics and database recovery constraints.

### Quality Engineering
Owns independent acceptance/readiness evidence. Database Engineering determines what database behavior means; Quality Engineering independently verifies agreed behavior when warranted.

## Promotion decision

**PROMOTE** Database Engineering to a top-level faculty.

Reason: database semantics form an independently routable recurring layer across multiple DEDAL projects and engines. The layer includes:
- schema invariants and constraints;
- indexes/access paths and query-plan reasoning;
- transaction/isolation/locking correctness;
- migration/backfill/compatibility safety;
- connection/session/pooling behavior;
- engine-specific concurrency and recovery semantics.

This is meaningfully distinct from both application implementation and record/data reconciliation.

## Adaptation rules

- Keep the entrypoint compact; load schema/query or transaction/migration references only as needed.
- Do not turn Database Engineering into a vendor manual.
- Engine/provider/version-specific facts that can drift require current authoritative documentation when material.
- Query/performance claims require planner/runtime evidence where feasible.
- Schema rollback and data rollback are separate claims.
- Mutation authority remains task-scoped; database tools/MCP/CLI availability never grants write authority.

## Rejected patterns

- “Add an index to every filtered column.”
- “ORM schema compiles, therefore DB behavior is correct.”
- “Migration command succeeded, therefore production migration is safe.”
- “A down migration means data recovery is guaranteed.”
- applying PostgreSQL locking/isolation assumptions to SQLite/D1 or vice versa;
- promoting provider-specific CLI/API details into stable Core truth.

## Outcome boundary

This audit and routing contract justify architectural promotion. DEDAL-specific outcome improvement remains to be observed in ordinary project work and should be preserved as outcome evidence rather than assumed from upstream expertise.
