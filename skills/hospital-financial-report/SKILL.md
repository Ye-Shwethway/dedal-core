---
name: hospital-financial-report
description: Reconcile monthly hospital cash flow from income forms and expense vouchers, maintain audited monthly history, repair report formulas, and compile approved values-only Excel reports. Use for Hospital Financial Report, hfr, $hfr, hospital cash-flow review, voucher reconciliation, financial month close, or historical financial analysis.
---

# Hospital Financial Report (hfr)

Read `references/workflow.md` before execution. Resolve the private hospital profile and current checkpoint from `/DEDAL/private-overlay/state/state-registry.json`; load only that workstream. Public Core contains portable procedure, never actual hospital transactions or identifiers. Read current Spreadsheets and Google Drive/Sheets skills for workbook operations; PDF skill for scanned vouchers. Use the connected source for current state, not an old attachment or cached result.

1. Resolve hospital, reporting month, exact workbook, batches and revision. Read live metadata, bounded inputs, formulas, validation and effective values. Never guess IDs, dates, amounts, currency, categories, counts or missing documents.
2. Extract source-grounded transactions. Retain source/page/line, original amount/currency, confirmed reporting amount, OPD/IPD allocation, exclusions and unresolved questions. Detect duplicates; repeated totals/conversion notes are not additional transactions.
3. Apply explicit private hospital rules. Ask about ambiguity; mark pending rather than entering estimates or invented zeros. Distinguish absent optional income from unreadable/unreceived evidence.
4. Reconcile normalized records with inputs and outputs. Keep formulas in the master; write source input fields. Test changes natively and independently sum amounts. Preserve surrounding layout/data.
5. Maintain append-only audit, immutable revision snapshots and resumable checkpoints in the hospital-owned financial system. Hidden helpers are allowed, not submission tabs. Store only operational configuration and owned-system references in the private overlay; never publish financial data.
6. Present questions and totals for Creator review. Bind approval to hospital, month and snapshot digest/revision. A material change invalidates approval. Approval alone does not authorize compilation.
7. Compile only on explicit Creator export instruction for that approved revision. Produce exactly four separate Excel files named by the profile. Export evaluated values without formulas, external links, COA or helpers. Preserve numeric amounts, date values and formatting; text-only means no live formulas, not converting all numbers to strings.
8. Run `scripts/verify_exports.py` on the four files. Inspect every rendered report and compare totals/representative cells with the approved snapshot. Archive files and hashes; return only verified outputs.
9. Recover from checkpoint plus actual readback before retrying. Amend a closed month with a new revision, reason, superseded-by links and fresh approval; never overwrite accepted history. Never silently carry closing balance into the next opening budget.

Use `scripts/validate_review.py` for supplied review records and export gates. Validators verify declarations/bytes, not user identity, source legibility or live service truth. Actual Creator instruction and connected readback remain required.
