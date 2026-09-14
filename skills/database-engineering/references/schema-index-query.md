# Schema, indexes, and query evidence

Load this reference when the main question is schema shape, constraints, indexes, query plans, or database performance.

## Start from invariants

Before choosing tables or indexes, state:
- entity identity and natural/surrogate key expectations;
- required vs optional values;
- uniqueness and referential rules;
- lifecycle/state-transition constraints;
- cardinality and dominant access patterns;
- expected read/write ratio and hot paths.

Schema design is not only normalization. Preserve the invariants that matter, then denormalize deliberately when measured workload and consistency costs justify it.

## Index discipline

Treat each index as a maintained data structure with write/storage cost.

Prefer:
- indexes aligned with real predicates, joins, ordering, and grouping;
- composite index column order justified by query shape and engine behavior;
- partial/filtered or covering indexes only when the target engine supports them and the workload benefits;
- explicit review of duplicate/redundant indexes.

Do not infer that an index helps merely because a queried column appears in a WHERE clause.

## Query-plan loop

1. Capture the actual query and representative parameters/workload.
2. Inspect the plan using engine-native tooling.
3. Identify expensive scans, joins, sorts, row-estimate errors, lock waits, I/O, or connection pressure.
4. Change one coherent cause: query shape, index/access path, statistics, schema, or workload architecture.
5. Re-run comparable evidence.
6. Check write/storage/regression cost before retaining the change.

For PostgreSQL, use `EXPLAIN`/`EXPLAIN ANALYZE` and relevant `pg_stat_*`/lock views when available. Do not run expensive production analysis without appropriate authority and risk assessment.

## Engine boundaries

- PostgreSQL MVCC, planner behavior, index types, vacuum/statistics, and extensions are PostgreSQL-specific.
- SQLite uses different planner, locking, journaling, and single-writer semantics; do not transplant PostgreSQL advice mechanically.
- Cloudflare D1 provider limits/bindings/runtime integration belong to Cloudflare Platform; SQL/schema/query semantics remain here.
- Supabase/Neon provider features are supporting context, not generic database truth.

## Performance claims

Prefer comparable measurements over generic labels such as “optimized.” Report what changed in plan shape, latency/resource use, rows scanned, contention, or another explicit metric. If evidence is unavailable, describe the recommendation as a hypothesis rather than a verified improvement.
