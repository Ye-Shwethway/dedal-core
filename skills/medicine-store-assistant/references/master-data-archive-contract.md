# Master Data Historical Snapshot Archive Contract

Use this reference whenever `$msa` creates, appends, verifies, repairs, or reasons from a collective closed-month `Master Data` archive.

## Role boundary

`Master Data` is a **closed-month historical snapshot ledger**. It is not a live operating surface and must not participate in current-stock calculations, live synchronization, receipt routing, Daily Usage entry, or current-cycle reorder mutation.

Current operational truth remains in the verified live operational sheets and source evidence. `Master Data` becomes authoritative only for the historical closed-month values that were deliberately snapshotted and verified at close.

Do not treat `Master Data` as a fifth compatibility-locked operational sheet.

## Values-only snapshot rule

Archive a closed month as frozen values/text, not live formulas.

- Copy the verified displayed/result values required by the archive projection.
- Do not copy formulas, array formulas, cross-sheet references, volatile functions, or helper logic into the closed-month archive.
- A formula-derived live value becomes a static historical value when archived.
- Historical snapshots must not change later because `TODAY()`, current stock, a renamed sheet, a deleted staging tab, or another live dependency changes.
- Do not copy transient operational/review marker colors as historical truth unless a specific archival contract explicitly requires them.

## Existing collective archive wins

When an established collective month archive already exists and remains usable, append to it rather than creating a second incompatible history system.

Preserve the established human-readable grouping of month identity plus the selected monthly source blocks. The archive projection may intentionally omit redundant derived columns when the same historical meaning is already represented elsewhere in the same month block.

Do not infer that every live operational column must be duplicated one-for-one in the archive. Maintain an explicit projection map from live headers to archive headers.

## Schema evolution

The archive may evolve as the live workbook gains useful fields.

- Map by verified header meaning, not remembered column index.
- Add a new archive field when it has durable historical value and does not create ambiguous duplication.
- Older months may remain blank for fields that did not exist or were not reliably available at the time.
- Backfill old months only from authoritative historical evidence. Never invent a value from current state.
- When replacing an old archive sub-schema with a newer one, migrate only fields with clear semantic equivalence; leave incompatible or unavailable fields blank, verify the migration, then remove the obsolete duplicate block if authorized.

## Month key and duplicate guard

Use the established month identity fields as the closed-month key, normally including hospital/facility, department/scope, month, and year when those dimensions exist.

Before appending:

1. inspect the existing archive,
2. confirm the intended closed month is not already present as a complete block,
3. distinguish a complete duplicate from a partial/corrupt block,
4. fail closed on ambiguity instead of appending a second copy.

A proven archive defect may be repaired only as an explicit historical amendment with checkpoint, read-back, and audit evidence. Do not silently rewrite a closed month.

## Month boundary row

When the established archive uses a dedicated end-of-month sentinel/boundary row, preserve exactly one boundary after each closed-month block.

Treat the sentinel as archive structure, not ordinary inventory data. It must not be deleted by operational cleanup or recolored/reused as a normal row. Exact wording and presentation are workbook-specific and belong in private/local configuration when necessary.

## Month-close ordering

The normal sequence is:

`inspect -> checkpoint -> freeze closing fingerprint -> append values-only Master Data snapshot -> append/verify month boundary -> verify archive -> recompute cleanup -> paired operational cleanup -> prepare next month -> verify formulas/alignment -> refresh derived history -> audit/readback`

The archive step must finish successfully before destructive cleanup/reset that would erase closed-month evidence.

## Closing fingerprint and verification

Before archive append, capture enough closing-state evidence to verify the snapshot, such as:

- month identity,
- source row coverage,
- representative item/lot identities,
- usage totals and closing balances,
- received-stock totals/coverage,
- Final Reorder row/quantity evidence when applicable,
- expiry-review coverage when applicable.

After append, read the archived block back and compare it with the closing fingerprint. Verify representative beginning/middle/end rows and any rows whose evidence would be lost by cleanup.

Do not proceed to cleanup when archive verification fails.

## Historical evidence and reorder reasoning

`Master Data` may be the primary human-readable closed-month ledger while hidden analytical/history sheets remain derived support state.

Do not count the same month twice merely because both `Master Data` and a derived history sheet contain it. When a helper history table is regenerated from `Master Data`, treat the helper as a cache/analysis projection, not an independent additional month of evidence.

Archived Final Reorder decisions remain a distinct human-decision evidence class inside the historical snapshot; they do not become current reorder authority.

## Desktop/external Excel gate

The mere existence of a legacy desktop workbook does not automatically block Google-side month close.

Use the external-sync/staging gate only when there is known newer or otherwise authoritative desktop/external evidence that has not yet been reconciled and is required by the Owner's workflow.

If the relevant historical Excel archive has already been migrated and verified in the canonical historical ledger, that migrated history alone is not a reason to freeze production or create staging tabs.

## Audit

Record a grouped month-close/archive operation with enough information to recover and verify the close, including the closed month, archive destination/range or identifier, archived coverage, cleanup result, checkpoint ID, and verification result.

Do not create per-cell audit noise for a single coherent archive append unless a narrower rule requires it.

## Invariant

> **Live sheets operate the current month. `Master Data` freezes verified closed-month history. The archive never drives live state merely because it contains older copies of operational values.**
