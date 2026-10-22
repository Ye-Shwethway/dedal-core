# MSA October 2026 Intake — Lessons and Posting Contract

Status: owner-directed workflow refinement based on completed October 2026 intake, 12 October 2026. Preserve all earlier MSA references and skills; this document is a narrow **batch-intake precedence addendum**, not a replacement for unrelated review/highlight workflows.

## Case evidence
Keep hospital transaction counts, quantities, row mappings and workbook identifiers in the current private operational evidence, never public Core. Use live source totals for each task.

## 1. Source OCR/transcription: high-reliability gate
1. Inspect every source image manually at adequate resolution; treat OCR as a suggestion, not authority. Read CMS code, *literal printed brand/name*, quantity, unit, **expiry**, unit price, transfer, and original line number independently. Never silently rewrite paper wording to match the catalogue.
2. Use **two independent expiry passes**: (a) direct visual paper reading and (b) separate reading without copying first-pass transcription. Diff both against final preflight row; any mismatch becomes a structured hold until checked against image or user correction.
3. Parse `DD/MM/YYYY` as **day-first**. Convert month-year vouchers without inventing a day in source evidence. Normalize comparison to **month/year**; preserve exact source text/date in provenance. Validate calendar dates; never infer expiry from adjacent lines, the Main Stock expiry, brand or catalogue.
4. Owner-edited *live preflight* becomes latest authoritative input after explicit owner approval. **Refresh the entire live range immediately before production**; old chat memory, old screenshots, and earlier extracted numbers never overwrite owner corrections.
5. Add a source-row digest/checkpoint and freeze source columns before posting. If any identity, quantity or expiry changes after routing, re-evaluate *all* same-family lot candidates and planned route, not just the previously referenced row.

## 2. Product-family and lot matching
- Resolve full generic/active composition + strength + form/concentration + unit/specification + expiry M/YYYY against **all Main Stock rows**, confirmed mappings, and local-code records. CMS code/brand alone is insufficient. Never decide `EXISTING` merely because a remembered reference is compatible.
- Same operational identity, same expiry M/YYYY, compatible unit and presentation => existing lot; **aggregate multiple physical source lines exactly once**, preserve original source lines and grouped ledger.
- Same operational family with different expiry M/YYYY => new sibling *adjacent to the family*. Distinct concentration/packaging may also require a separate sibling even when generic strength is the same; note differences explicitly (e.g. acetylcysteine Asist vs Ateran).
- Truly new family => verified local generic/strength/form name with brand and terminal `(M/YYYY)` if known; do not falsely label a brand typo as a different drug. Same family with two expiry lots => two rows.
- Equipment with no expiry: blank permitted; NEVER manufacture a date or expiry suffix.
- Current-source/owner decisions override historical preflight matching suggestions. Recompute downstream row indices after row insertion; use stable receipt ID + source preflight row + code/family/expiry for final mapping; do not trust stale Main Stock row numbers.

## 3. Safe production posting
1. Check owner approval, idempotency, available formula ranges, current monthly received stock, existing markers, and exact workbook schema. Copy *whole workbook* to a named **pre-posting checkpoint** before write.
2. One receipts dataset is the **single receipt source of truth**. Mutate `Main Stock.Received Stock`; do not manually duplicate `This Month Received` or formula-derived Daily Usage inputs. Insert structural rows in both Main Stock and Daily Usage, in a consistent order. Insert new sibling rows high-to-low against the same captured baseline or recompute live references each mutation.
3. New rows: populate verified No., Items, optional Expiry Date, Unit, Remaining Stock=0, Received Stock, Reorder Level (actual new receipt quantity unless stronger owner rule), factor, verified CMS Price if available, Remark where operationally necessary, stable Serial Code and CS Name. Copy/rebuild per-row formulas for M/N; preserve array-formula anchors for derived columns and paired Daily Usage references. Correct **expiry number format** `mmm-yyyy` on inserted rows; serial values such as `47177` are formatting defects, not acceptable display.
4. After insertion renumber No. sequentially in both sheets, read back EVERY receipt row, verify full non-formula required fields, optional exemptions (expiry when unspecified, remarks, verified FOC/unknown cost), names, local unit, lot month/year, code/CS name, quantity, formula presence, and derived results. Check all current source lines mapped once and group totals matched to the reviewed receipt; validate row-by-row Main Stock/Daily Usage alignment and `This Month Received` total and no `#REF!` or other formula errors.
5. Source quantities entered in expired lots must remain in receipt inventory, and operational Remark gets `Received expired; Expiry: DD-MM-YYYY` where applicable. No automatic discard. FOC is a *dispensing policy*; it does not mean paper's purchasing price is numerically zero. Lab's authoritative numeric 0.00 remains zero without FOC relabel.
6. Commit posted status only AFTER readback; `Applied?=YES` only if ledger maps source to actual production lot. A partial write must be reported as partial, never full close. Retain checkpoint and append audit transaction with totals/exceptions.

## 4. Visual marks and clean operational tables (owner preference, batch receipts)
- **Owner-specified exception to existing cell-only `visual-marking.md`: for *verified batch-receipt rows in Main Stock*, apply light green `#D9EAD3` to the **entire data row A:U**. Do not use this rule for unrelated ordinary edits; yellow/red should not be painted across all fields for one local anomaly.
- Do not put diagnostic cell notes/comments or yellow exception fills in Main Stock/Daily Usage/This Month Received. Put ALL diagnostic reasons, source references, status, follow-up and marker provenance in a **hidden helper review ledger** and/or `Audit_Log`; user-facing Main Stock stays clean. Preserve genuine operational Remark values (such as `Received expired` and FOC) while removing only diagnostic annotation.
- Pre-intake scan and owner choice to clear/preserve previous MSA markers remains mandatory. Clearing markings must preserve cell values, formula, borders, validation and unrelated format.
- All green row coloring and readbacks must occur after structural posting to avoid painting wrong rows after insertion. The previous October error was green on only Received Stock and comments displaying black corner indicators; both violated owner presentation expectation.
- Existing cell-only protocol is *superseded for batch receipt green full-row marking and diagnostic annotation*. Keep the earlier protocol for non-batch work until formally reconciled.

## 5. Public Health double-ledger receipt routing
- Public Health voucher items must be posted once to medicine store inventory AND separately as receipts to the dedicated Public Health monthly report, with different ledger semantics. Never sum them as two independent hospital receipt events.
- Locate the hospital + month-specific Public Health workbook; verify its `Monthly Stock Report` headers, opening balances, existing lot/batch rows, formulas and report period. Historical opening, balances and batch names are immutable without evidence-backed corrections.
- **Batch Name unknown => always create a NEW REPORT ROW**, even when item and expiry match an old row. Source new row: Opening Stock=0, Incoming=receipt quantity, Outgoing/Lost=blank unless supported, Balance=receipt quantity, expiration from verified source (M/YYYY); `Batch Name` blank; Remark `batch name pending verification; separate receipt, do not merge`.
- Only after actual batch-name evidence and owner approval consider merging same batch; verify item, formulation, unit, expiry, batch code, prior receipts and reported balances. If batch differs, retain separate rows. Preserve donor blank rather than guessing.
- Create the required distinct rows and reconcile current source quantities without altering historical opening or old lots. Audit linkage should record preflight source voucher/row and report workbook/row.

## 6. Regression checks (run at next intake)
- Owner corrects expiry but old planned action remains => automatically detect and regenerate action (not silent original route).
- Same code, same lot appears in 2 source lines => one stock row receives summed quantity, no duplicate.
- Same generic brand changes or concentration differs => correct sibling/new item and explicit evidence.
- Paper shows 1/6/2028 => 1 June, not 6 January. Voucher `10/2028` => month-year only, never guessed paper day.
- New row expiry formats as Excel serial => fail presentation validation and repair formatting.
- Row insert shifts Main Stock but not Daily Usage or array formula range => BLOCK close.
- Missing arbitrary required non-formula fields => BLOCK close; policy-authorized blank expiry or FOC cost => documented permitted exception.
- Yellow/red reason exists only as cell note, not hidden ledger => BLOCK close.
- Batch receipt green only on `G` rather than entire Main Stock A:U => fail presentation validation.
- New Public Health receipt has unknown batch but same expiry as existing row => still create new report row, hold merge pending verification.
- Close only when every source line posted, exactly once, with two-ledger reconciliation and totals; report precise outstanding issues without inventing zeros.

## Integration
The stock-mutation supply-intake profile loads this addendum; Public Health reporting is conditional on voucher scope. Preserve unrelated MSA workflows.
