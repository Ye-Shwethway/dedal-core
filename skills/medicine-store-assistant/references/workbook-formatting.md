# Workbook Formatting Defaults

Use this reference as the global presentation baseline for Medicine Store Assistant spreadsheet tables. It governs presentation only; it never changes operational truth, formulas, values, identity/matching decisions, sort order, approval state, or historical meaning.

## Authority and scope

Apply formatting in this order:

1. explicit Owner instruction for the current task;
2. an authoritative form/template or an already-approved sheet-specific visual contract;
3. semantic state/alert styling from `visual-marking.md` and task-specific references;
4. this global workbook-formatting baseline.

Use this baseline for human-facing MSA tables that are created, populated, appended, extended, materially rewritten, or explicitly normalized. Hidden/helper/app-internal sheets are not blanket-restyled unless the task explicitly includes them.

## Table boundary baseline

For every human-facing table, apply **all borders** to the actual table range by default.

- Border color: black.
- Border style: thin / normal solid line.
- Apply outer borders and every internal horizontal and vertical cell boundary.
- Include header rows and all populated data rows/columns.
- Blank cells structurally inside a defined table region keep the table border.
- When a table is extended later, extend the same border treatment to the new cells.
- Do not format the entire worksheet grid merely because a table exists; target the actual used rectangle or explicitly defined table region.
- Stronger black separators may be used for deliberate section/family boundaries, multi-block archives, or subtotal/section breaks.

Prefer a precise border-only API request such as `updateBorders` when available so existing fills and other cell formats are not rewritten.

## Header baseline

For ordinary single-row table headers, default to:

- bold text;
- horizontal center alignment;
- vertical middle alignment;
- wrap enabled so labels remain readable;
- the existing/approved header fill and font color preserved when a deliberate style already exists.

**Do not treat a transparent/white background with default black font as the desired generic header style merely because it is the current state.** If no deliberate/approved header style is established, use the workbook-standard MSA header: **dark teal fill (`#155F82`) with white bold text**, centered/middle/wrapped. This is the fallback for ordinary human-facing tables and review/history tables. Reuse a different nearby approved header exemplar only when that tab clearly belongs to a distinct intentional visual family.

Before changing header formatting, classify the current header as either (a) deliberate approved style, (b) special/template style, or (c) unstyled/default. Only category (c) receives the standard dark-teal/white fallback.

For formatting APIs, keep border and header-style mutations separate when practical. Use `updateBorders` for borders. When writing header style, use a precise field mask that explicitly preserves or intentionally sets background fill and font color; never rely on a partial generic formatting helper that may reset either property.

For multi-row/grouped headers, preserve the established hierarchy, merged/group labels, section colors, and stronger separators. Do not flatten a grouped header into a single-row style.

## Title rows and section labels

If a table has a separate title row above its column headers:

- preserve approved merges and title-band styling;
- keep the title readable and visually distinct from the data header;
- do not convert a title row into ordinary data styling.

Section labels and archive boundary rows may use stronger borders/fills when an approved sheet-specific contract requires them.

## Freeze panes and scrolling

For long human-facing tables, keep the header row frozen by default.

- Single-row header table: normally freeze 1 row.
- Approved two-level/grouped header table: normally freeze 2 rows.
- Preserve an existing intentional frozen-column arrangement.
- Do not change an already-correct freeze layout merely for consistency.

## Body-cell readability

Preserve the established body style unless readability is materially poor.

- Keep vertical alignment consistent within a table.
- Use wrapping for long narrative/text fields when needed to avoid unreadable clipping.
- Do not force wrapping on every compact numeric/code column if the current layout is already readable.
- Preserve intentional left/center/right alignment conventions. New compact identifiers, dates, statuses, and quantities may use centered alignment when that matches the surrounding workbook; narrative/item/remark text may remain left-aligned.
- Avoid merged cells inside ordinary data bodies. Merges are acceptable for approved titles, grouped headers, form layouts, or section labels.

## Number and date formats

Treat number/date formats as data-presentation semantics, not decoration.

- Preserve an established column format during formatting-only work.
- Keep one logical column internally consistent when creating/extending a table.
- Do not change numeric precision, sign display, currency/price semantics, or date granularity unless the task or existing contract requires it.
- Preserve special formats such as signed `+/-` price changes, `mmm-yyyy` expiry display, FOC/text pricing states, and other approved domain formats.

## Semantic colors and conditional formatting

Formatting cleanup must preserve meaning-bearing styles.

Do not erase or replace:

- green/yellow/red operational markers from `visual-marking.md`;
- expiry/review/priority fills;
- conditional formatting such as price increase/decrease colors;
- section/header colors that encode an approved workbook structure.

For dynamic conditions, prefer conditional formatting over manually painting repeated body cells when the logic is rule-based.

## Filters, banding, and decorative styling

Filters, banded rows, and other convenience styling are optional, not universal defaults.

- Preserve an existing useful basic filter/table filter.
- Add a filter only when it clearly improves a flat review table and does not conflict with forms, grouped headers, calculated layouts, or the user's workflow.
- Do not add decorative banding, gradients, heavy themes, or dashboard-like styling merely for appearance.
- Do not make one tab visually inconsistent with the workbook without a task-specific reason.

## Column widths and row heights

Do not blanket-autofit an established workbook.

- Preserve intentional widths/heights.
- Resize only columns/rows that are materially clipped or unreadable after an edit, and only as narrowly as necessary.
- Long descriptions may receive more width or wrap when needed; compact numeric/code columns should remain compact where practical.

## Template and special-layout precedence

A canonical form/template or explicitly approved sheet-specific style overrides this baseline where its design is intentional.

Examples include:

- `Master Data` grouped archive styling and month-boundary rows;
- form/request sheets with signature or merged layout regions;
- review sheets with approved priority/decision colors;
- title bands and multi-row headers.

The global rule fills gaps; it does not erase purposeful visual hierarchy.

## Existing versus touched tables

This is the default for MSA work going forward.

- When creating or materially rewriting a table, make the affected table compliant.
- When appending/extending a compliant table, extend its formatting consistently.
- Do not mass-restyle unrelated historical or hidden/internal areas merely because this rule exists.
- An explicit workbook-formatting cleanup request authorizes normalization of the selected existing human-facing tables.

## Verification

After formatting changes, verify representative cells from each relevant class: title/header, ordinary body, highlighted/conditional cell, table edge, and any special section boundary.

Confirm that:

1. all intended table boundaries use thin solid black borders unless a stronger approved separator applies;
2. header readability rules are satisfied without overwriting approved fills/font colors;
3. semantic fills/font colors and conditional rules remain intact;
4. formulas, values, validation, hyperlinks/chips, number/date formats, and table meaning were not changed;
5. freeze/header structure remains correct;
6. no unrelated hidden/helper/app-internal sheet was restyled outside scope.

Treat this reference as the default MSA workbook-formatting contract unless the Owner or an authoritative template explicitly overrides it.
