# MSA October Intake Routing Addendum — 2026-10-12

Applies to **all hospital medicine-store batch intake tasks**, especially CMS + Lab + Public Health vouchers. This is additive and preserves existing MSA skill references.

Mandatory reading path BEFORE the preflight/posting branch:
1. `references/generic-first-intake-reconciliation-2026-10-11.md`
2. `references/october-2026-intake-lessons-and-posting-contract.md`
3. `references/public-health-monthly-receipt-reporting.md` when Public Health stock is involved
4. Existing `references/cms-batch-intake.md`, `references/received-stock-operational-workflow.md`, `references/visual-marking.md`, `references/operational-sheet-compatibility.md`, `references/workbook-formatting.md` and related contracts.

Precedence clarification: on **verified Main Stock batch receipts only**, owner-confirmed **full-row A:U green** after posting/readback supersedes earlier cell-only green guidance. Keep diagnostic yellow/red reasons and cell notes out of visible operational tabs; store them in hidden review/helper audit. Operational Remarks containing real stock facts are allowed. These exceptions do **not** alter the warning/conflict semantics or unrelated workflows.

A Public Health voucher creates two destination ledger postings for the same physical receipt (not two distinct receipts). Unverified batch name means separate monthly-report row, blank batch, preserved old lots; merge only on owner-approved confirmed batch identity. Anti-TB FOC dispensing permits a blank CMS price, distinct from a verified source price of numeric zero.

Readback hard gates: mandatory fields except documented exemptions, month/year lot, idempotency, paired Main Stock/Daily Usage structural alignment, formula anchors and errors, source-total reconciliation, stable source-to-target ledger and checkpoint. Details and test cases reside in the linked references.

**Integration:** stock-mutation supply-intake routing loads this addendum and its posting rules. Public Health reporting is loaded only when that voucher is present.
