---
name: dedal-knowledge-archive
description: Create, load, refresh, audit, and inspect durable evidence-linked project knowledge. Invoke with $ika or knowledge-archive tasks.
---

# DEDAL Knowledge Archive ($ika)

Use durable project archives when a task needs exact project continuity beyond chat memory. Model memory is orientation, not the database. Live project state and primary sources remain authoritative.

## Start here

1. Identify the project and requested operation: `create`, `load`, `refresh`, `audit`, or `impact`.
2. Resolve the archive's actual canonical repository/location before reading or writing.
3. Load only the task-specific reference needed:
   - archive structure and authority -> `references/archive-contract.md`
   - bounded loading/retrieval -> `references/retrieval-contract.md`
   - relationships/change impact -> `references/relationships-and-impact.md`
   - complex execution/orchestration -> `references/orchestration.md`
4. Verify current execution surfaces; never assume native workers, Drive, Library, or a particular plugin is available.
5. Keep canonical mutations serialized and verify writes by read-back.

## Operations

- **Create**: inventory necessary sources, rank authority, extract atomic evidence-linked knowledge, validate, publish to the archive's canonical store, then mirror only where approved.
- **Load**: read manifest/current context first, then retrieve the smallest sufficient bounded package for the current task.
- **Refresh**: compare current evidence with archived records, preserve stable IDs/history, mark superseded/disputed material rather than erasing it, validate, publish, read back.
- **Audit**: inspect schema, evidence closure, authority, freshness, sensitivity, conflicts, registry/manifest consistency, and mirror status.
- **Impact**: report direct one-hop records/projects that should be reviewed after a known change. Impact results are advisory and never mutate linked records automatically.

## Authority and state

Use this default ordering when evidence conflicts:

1. live project / primary source;
2. explicit current Creator instruction;
3. authoritative project artifacts;
4. canonical archive records;
5. derived context/mirrors;
6. model memory/inference.

Material knowledge should distinguish states such as `verified`, `inferred`, `proposed`, `disputed`, `deprecated`, and `unknown`.

## Public-core / private-state boundary

DEDAL Core is public. Do not copy private archives, project records, confidential registry contents, credentials, health data, or other sensitive state into this skill directory.

This skill defines the public operating contract. Actual archives may remain in private repositories, Drive, Library, databases, or other approved stores. The archive manifest determines ownership and canonical location.

## Runtime-neutral execution

Skills describe how to work; current tools/plugins/MCP/sandbox/Actions provide execution. Prefer the smallest useful execution graph. Parallelize read-only independent work when the runtime genuinely supports it; serialize canonical writes. Never claim workers were spawned unless independent workers actually ran.

## Creator authority

Do not promote archive-derived learning into DEDAL Kernel/Core rules merely because a pattern appears useful. Durable behavior changes require the normal DEDAL improvement process and Creator authority where the change is high-impact or explicitly gated.

## Non-goals

No model-weight training, no silent private-state publication, no multi-master archive, no unbounded recursive graph traversal, no automatic mutation of related records from impact analysis, and no assumption that legacy IANEO experimental chambers are part of ordinary archive operations.

## Legacy provenance

This skill is a DEDAL-native adaptation of the earlier private IANEO Knowledge Archive work. See `ADAPTATION_NOTES.md`. It intentionally preserves proven archive mechanics while removing IANEO-specific identity and runtime assumptions.
