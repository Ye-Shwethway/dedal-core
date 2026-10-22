# Public Health Monthly Receipt Reporting (MSA)

Owner-approved operational workflow addition, 12 October 2026. Supplementary to `october-2026-intake-lessons-and-posting-contract.md` and canonical `received-stock-operational-workflow.md`.

## Scope
When a hospital store intake includes a Public Health voucher, the medicine store and the Public Health monthly stock report are **two destinations for one physical receipt**. Post and audit each explicitly; do not double count receipt globally.

## Required identification
1. Use the authoritative, owner-reviewed incoming voucher row, physical receipt month, item identity, local unit, quantity and exact expiry month/year. Preserve original voucher date and blank CMS code.
2. Find the particular hospital and monthly report; do not accidentally use a prior month report, archived checkpoint, another hospital workbook, or the ordinary Medicine Store Cloud tab.
3. Read report header/schema, existing lot rows, empty prepared rows, opening balances, formula cells, expiry formats, batch names and known batch history.
4. Source batch name is **unknown until verified from packaging/issue documentation**. Expiry M/YYYY is NOT batch identity; matching expiry never grants merge permission.

## New receipt with unverified batch
- Always append/occupy a fresh prepared row for each distinct incoming item/lot.
- Keep original rows and preceding month's opening stock untouched.
- Populate item/description and operational unit, Opening=0, Incoming=source quantity, Balance=quantity. Outgoing/Lost/Actual physical count/Discrepancy stay blank unless independently verified; batch name stays blank; donor remains blank unless evidence identifies donor.
- Set verified expiry with same month/year as source and format consistently `mmm-yy` as the report convention. Retain report's date convention and row numbering.
- Write human-readable Remark indicating October receipt, voucher provenance, `Batch name pending verification — keep separate; do not merge`.
- Preflight idempotency: do not append a second copy if identical voucher item/expiry/quantity and a pending-row entry already exists.
- Read back every populated source-target field and total against voucher. Save an audit record without placing debug cell notes in human-facing report.

## When batch becomes known
Compare historical candidate with exact batch, generic/formulation, unit, expiry and original stock movement. Merge only after owner verifies same physical batch and explicitly requests it. Preserve a reconciliation trace and do not erase or double count historical incoming/outgoing quantities; if not same, keep separate rows.

## Private case evidence
Hospital names, report identifiers, row mappings and actual receipt quantities belong in the current private operational evidence. This public procedure defines no fixed transaction totals.
