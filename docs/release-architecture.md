# Release architecture

The deterministic `state/release-manifest.json` owns release version and the complete source digest map. `VERSION` and `state/active-release.json` are checked projections for tooling and activation; the pointer binds the exact manifest bytes. Do not add global release stamps to contracts or inventory. Contracts retain independent `schema_version` values; the skill catalogue's revision is independent. Checkpoints use `recorded_core_version` as provenance and change only when accepted decisions/state change. Supporting historical labels do not define current identity.

Ordinary skill/reference publication changes only intended sources, changelog, VERSION and manifest/pointer; `core-files.json` changes only for inventory changes. A release-only bump must leave boot, kernel, routing, profiles, response, budgets and checkpoints byte-identical. All loaded sources remain digest-verified against the active release. The manifest remains one compact complete map; component manifests are unnecessary at this scale.

## Publication audit

`scripts/publication_audit.py` accepts exact previous/candidate manifest bytes, a private release-bound baseline and a complete current canonical metadata map. The adapter must consume every inventory page, reject duplicate paths and retain file identity, concrete revision, file id and modification timestamp. A successful upload acknowledgement is not byte verification.

For unchanged source digests, reuse is permitted only when the prior full audit is at most seven days old, its release digest matches the exact prior manifest, and file identity and concrete Library revision match. Null/unknown revisions require fresh byte readback. Changed/new files and the manifest always require byte readback. The planner cannot infer reliable content revisions from file ids, timestamps or sizes alone. Baselines and tool observations are trusted adapter evidence, not authenticated host events.

Architecture/kernel/index/validator/script/schema changes automatically require full source readback. Explicit audits, unavailable/expired baselines also require full readback. Incremental releases carry forward `full_audit_at`; they never reset the full-audit clock. Complete metadata must be refreshed before and after byte reads and again after activation; identity/revision/file-id/timestamp drift fails closed. This detects observed races, not all possible concurrent writes: Library supplies no remote lock or atomic snapshot. Stop if concurrent activity is known. Unknown transport outcomes require normal publication reconciliation.

Publish sources, verify them, publish the manifest, certify source audit, then activate the pointer last. `publication.py` schema-2 journals require a candidate-bound complete source audit before emitting a forward pointer request. Read back final pointer bytes and refresh complete metadata; `publication_audit.close` yields `verified` evidence bound to the accepted manifest. Persist that evidence as the next private baseline only after essential/full CI and continuity reconciliation. A cached or incremental audit must never be reported as a fresh full-tree byte readback.

Keep local full inventory/structural validation and CI regression checks for releases; these are inexpensive relative to remote transfer. This migration retains full CI rather than implementing a speculative test-dependency graph. Full canonical byte audits are a separate explicit operation and are required whenever the planner indicates full mode.

## Recovery and measurement

Preserve Library identities and concrete version guards. Existing source → manifest → pointer rollback remains; the frozen 0.41.1 tree and public parent commit retain prior architecture. Do not delete/recreate canonical nodes to obtain revisions. Save journals before mutation and after outcomes; reconcile actual owner bytes before replay.

Measure changed source count, byte read count, reused count, unknown-revision count and actual elapsed transfer time. The regression suite verifies bounded read selection and release-only fanout, not host interception, remote atomicity, boot speed or real-work latency. A null-heavy adapter can limit transfer savings even though version fanout is removed.
