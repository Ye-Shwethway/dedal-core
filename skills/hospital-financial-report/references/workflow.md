# Monthly workflow and durable records

## Lifecycle
Use collecting -> needs_clarification -> reconciled -> approved -> export_requested -> exported -> closed. Reopen through a new immutable revision. Record approval and export request separately, both bound to hospital, month and snapshot SHA256. Capture actual Creator instruction reference, observed time and scope. Never manufacture evidence or treat a successful validator as permission.

Before master writes, checkpoint operation ID, target identities/ranges, before values/formulas, intended changes, source proof, prior revision and next step. Afterward compare actual cells and append outcome/readback. On uncertain success inspect before retrying; never replay expenses blindly.

## Durable records in the hospital-owned system
Use stable hospital+YYYY-MM keys. Keep snapshots independent of later master changes.
- Transactions: stable ID, document ID/hash/page/line, original date, approved correction/reason, original currency/amount, confirmed reporting currency/amount, cash category, OPD/IPD, exact COA code/name, inclusion status and question.
- Audit: unique event/operation ID, month/revision, actor/instruction reference, UTC timestamp, before/after, reason, proof, outcome/readback. Append corrections. Audit hashes detect changed bytes; they do not authenticate people.
- Snapshot: hospital/month/revision, inputs, formulas, evaluated typed values, normalized ledger, exclusions, reconciliation, source references/hashes and capture time. Hash canonical JSON; bind approval to that hash. Mark inherited workbook data unverified until source coverage is checked.
- Checkpoint: state, revision/hash, received/missing batches, questions, completed operations, write debt, approval, export request, archive references, verification and next step.
- Month index: immutable revision references, lifecycle, active accepted revision, superseded-by, archived source/ledger/master snapshot and four final file hashes.

Keep financial rows and snapshots in the owned hospital workbook/Drive archive. Put operational rules and owning-system references in the private overlay. Never put real financial data/source IDs in public Core.

## Workbook
Resolve live sheet IDs/ranges every run. Preserve four submission tabs, exclude COA/helpers from final files. One month input drives dates/headers; one opening input drives budgets. Cashier feeds Income; Income category/date totals and Expense categories feed Head Office. Independently reconcile category sums with totals. Errors, duplicate/unknown account mapping, out-of-period entries and missing source coverage block approval.

Code-only lookup requires a unique COA code. For duplicates require the exact approved category, not the first match. Insert extra voucher rows above signatures and inherit formulas/formatting; verify actual new-row formulas as well as SUM coverage.

Distinguish cash, credit, FOC, patient counts, deferred-family billing and other-income notes. Apply profile allocation; exclude staff change exchanges. Retain deferred-family provenance to avoid double counting. If a total other-income note lacks a split, preserve its total and ask only when a split is needed; never invent categories or counts.

Use only the converted reporting amount written on the voucher or explicitly supplied by Creator. Preserve originals. Never invent exchange rates. Repeated totals/converted notes corroborate one amount; they are not extra lines.

## Approval and export
Opening + included cash income - included expenses = closing. Test month ends, leap years, optional categories and formula changes natively. Reject unresolved or unconfirmed included entries.

After approval, explicit export instruction authorizes only the approved snapshot. Re-read current master and compare normalized digest; changes require a new review. Each final file contains exactly one visible report sheet, typed values, preserved formatting/print area, no formulas/helper tabs/external links/error cells or formula-bearing defined names. Verify contents against approved snapshot and retain four-file hashes. Preserve formula-bearing master separately.

Analyze historical months from the month index's accepted revision, not today's master or drafts unless requested. State revision/status and comparable currency/category scope. Never merge superseded and amended revisions or infer missing months.
