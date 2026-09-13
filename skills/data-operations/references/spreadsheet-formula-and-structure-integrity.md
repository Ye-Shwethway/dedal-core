# Spreadsheet Formula and Structure Integrity

Spreadsheets mix data, logic, presentation, and controls in one artifact. Treat them separately during inspection.

## Formula audit

When formulas matter:
- distinguish formulas from cached/calculated values;
- compare formula patterns across structural siblings;
- inspect absolute/relative/mixed references where copying is involved;
- detect `#REF!`, `#VALUE!`, `#DIV/0!`, `#N/A`, `#NAME?`, and other error states;
- look for formulas replaced by hard-coded values inside otherwise calculated regions;
- verify ranges include newly inserted rows/columns;
- consider calculation mode and volatile/external dependencies before trusting displayed values.

An inconsistent formula may be intentional. Flag the difference and determine intent rather than blindly normalizing it.

## Structural behavior

Potentially behavior-bearing workbook features include:
- hidden rows/columns/sheets;
- tables and calculated columns;
- named ranges;
- data validation rules;
- protected/locked cells;
- filters and sort state;
- merged cells;
- external workbook links;
- macros/scripts/queries;
- pivot/query refresh dependencies.

Formatting alone is usually presentation, but formatting may also encode review state or warnings in operational workflows. Preserve it when the owning workflow gives it semantic meaning.

## Safe editing

For consequential workbook changes:
1. identify editable input zones vs derived/protected logic;
2. capture formula/structure baseline for affected areas;
3. edit the smallest necessary scope;
4. recalculate or reopen with a compatible engine when required;
5. compare formulas, values, validations, and structural counts after edit;
6. preserve a rollback copy when risk warrants it.
