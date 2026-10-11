# MSA: Mandatory Generic-First Receipt Matching and Naming Gate

Status: Owner-approved workflow addendum, 2026-10-11. Scope: every relevant CMS receipt row BEFORE any Main Stock mutation. This extends `cms-batch-intake.md`, `cms-price-and-matching.md`, and `received-stock-operational-workflow.md`. Read this source through the canonical intake branch before matching or posting a receipt.

## Mandatory evidence sequence (no code-only or brand-only unmatched verdict)

1. Preserve transfer source verbatim in preflight: paper date, physical receipt month, source line, CMS code, CMS brand, quantity, original unit, unit price, expiry, and batch provenance. Do not apply quantity or post to production during preflight.
2. Look up the exact CMS code in the newest authoritative `CMS_Price_List_YYYYMM`, especially **Description (long description)**, **Brand Name**, Form, Type, Class and Price. Do not substitute Brand Name for the generic identity. Check previous catalogue versions if the current code is missing, deprecated, or reused.
3. Extract or derive candidate generic/active ingredient(s), clinically significant salt/combination, strength/concentration, route, formulation, size and pack/device specifications from the description. Record evidence and confidence; distinguish a supported generic from a guess.
4. Search the entire `Main Stock` for the **generic operational family**, not merely the CMS code or exact brand. Ignore only trailing expiry `(M/YYYY)` when comparing; inspect siblings, historical names, `Item_Mapping`, `Local_Code_Registry`, relevant prior batch/lot history. Similar names are never enough if chemistry/strength/formulation/spec differs.
5. If identity still ambiguous, perform bounded external research (manufacturer/regulator/formulary/pharmacopoeia authoritative sources when available); cite sources in review evidence. Never use external research to alter actual received quantity, source price, paper date, or expiry.
6. Classify each relevant row `EXISTING_SAME_EXPIRY_LOT`, `EXISTING_GENERIC_NEW_EXPIRY_LOT`, `EXISTING_GENERIC_DIFFERENT_BRAND_OR_CODE`, `NEW_GENERIC_CANDIDATE`, or `REVIEW/CONFLICT`. Code miss is not a new-item verdict. One generic may have legitimate brands and CMS codes; retain received lot-specific source identity.
7. Unit: use verified local operational unit, honoring Creator-confirmed preflight decisions; flag any count/pack conversion requiring approval. Preserve source units independently.
8. For multiple source rows belonging to the same generic, preserve source rows and group only compatible **same-expiry** lots when explicitly confirmed. Different expiry dates must remain separate. Check receipt idempotency prior to any future production write.

## Mandatory Main Stock naming for a subsequently approved intake

`<Verified local generic / operational name, strength/form/spec> (<CMS Brand Name>) (<M/YYYY expiry>)`

- Keep the established local **generic** identity at the beginning; align to staff's convention and do not replace it with the CMS brand.
- Append the actual verified **CMS Brand Name** in its own parentheses for this received lot; do not duplicate when generic and brand are truly the same or use meaningless extra parentheses without Owner review.
- Append a terminal `(M/YYYY)` **only** if expiry is nonblank; obtain from structured expiry and keep them synchronized. Blank expiry = omit suffix.
- Preserve product-defining parentheticals (strength, volume, manufacturer/spec etc.) without treating them as expiry metadata. For devices, use verified operational device identity in place of medicinal generic name.
- Do not silently rename or rewrite **existing historical** Main Stock rows: apply this format prospectively to newly approved receipt rows; existing same-lot additions retain local canonical family naming unless Owner separately authorizes normalization. Prevent duplicate families merely because older rows do not contain brand parentheses.
- For legacy products supplied without an identifiable brand (including handwritten voucher), record `Brand: Not established` in preflight and ask the Owner for naming before any NEW_ITEM creation; do not invent brand text.
- Example only, NOT a confirmed mapping: `Metoprolol succinate ER 25mg (Amperol XL) (4/2029)`. Active ingredient/formulation must be independently verified from catalogue/evidence.

## Preflight evidence and decision contract

For every matched intake row, record fields or linked evidence: source row/reference, latest catalogue version, CMS code, CMS brand, catalogue long description, generic resolved, formulation/strength/spec verification, existing local generic family and sibling rows, local unit, expiry-lot route, match confidence, evidence links, conflict/hold reason and Owner approval. Do not overwrite source columns.

- `SAFE` requires corroborating ingredient/generic + strength/form/spec evidence and compatible family; if catalogue absent or ambiguous, do not bluff.
- `REVIEW` for potential synonyms, brand/generic uncertainty, packaging conversion uncertainty or low-confidence research.
- `CONFLICT` for ingredient, salt, combination, strength/formulation or device-spec incompatibility, or recycled code.
- `NEW_GENERIC_CANDIDATE` requires full local-family search and explicit Owner naming/creation approval; it is not authorization to create.
- Existing price catalogue price is **identity evidence** only for this task; never alter receipt source price to fit catalogue.

## Posting hard stop

Preflight writes may store reconciliation evidence and decisions only. No production `Main Stock`, `Daily Usage`, `Fixed Assets`, `This Month Received`, or new-item creation until a separate, explicit final approval plus a fresh posting/idempotency checkpoint and all existing workbook contract guards. Expired physical receipts stay recorded, eventual Remark indicates expiry, no automatic disposal. Laboratory zero source prices remain numeric 0.00, never FOC. Date/receipt month follows actual physical receipt; preserve original source date.

## Acceptance test for this gate

Given a CMS brand with a code absent from Main Stock but a long Description naming an established generic, classify an existing generic family candidate, NOT auto-new item. Given a genuinely different active ingredient, strength or route, block the match. Given two expiry lots, preserve both. Given blank expiry equipment, emit no invented suffix. Given an expired receipt, preserve source, note in future Remark and do not dispose. Require all source preflight lines to reach an evidence-backed identity route/approved hold before requesting final posting approval.
