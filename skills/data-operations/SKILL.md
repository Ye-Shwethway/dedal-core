---
name: data-operations
description: Design and execute safe spreadsheet/data operations: schema inference, validation, reconciliation, deduplication, formula integrity, staging/review/promotion, auditability, and deterministic transforms across spreadsheets, CSVs, tables, and operational datasets.
---

# Data / Spreadsheet / Operational Workflow Engineering

Use this skill when correctness depends on transforming or reconciling operational data rather than merely reading it.

## Core lifecycle

`identify authority -> model records/contracts -> normalize -> reconcile -> validate -> stage -> review exceptions -> promote -> verify -> audit`

## Rules

1. **Authority before transformation** — identify which source controls identity, values, formulas, structure, timestamps, or approval. Different fields may have different authorities.
2. **Record identity before deduplication** — define the key/equivalence rule before merging or deleting rows. Similar text is not sufficient evidence of identity.
3. **Normalize without erasing evidence** — whitespace/case/type/date cleanup may create comparison views, but preserve original values when they matter for traceability.
4. **Validation is executable evidence** — express important invariants as checks where practical: required fields, types, domains, uniqueness, referential consistency, formula patterns, totals, date ranges, and cross-source reconciliation.
5. **Stage risky changes** — destructive cleanup, mass edits, merges, schema migrations, and production-table changes should normally move through a reviewable staging state when rollback or human review matters.
6. **Exceptions are first-class** — do not force ambiguous records into a match. Surface unresolved candidates, confidence/rationale, and what evidence would resolve them.
7. **Formulas are code** — preserve formula/value distinction; audit inconsistent formulas, broken references, hard-coded exceptions, calculation mode, and range drift when spreadsheet correctness depends on them.
8. **Promotion requires evidence** — before staging -> production, verify row counts or expected deltas, key invariants, error/exception status, formulas where relevant, and target identity/version.
9. **Keep an audit trail proportional to risk** — record source version, transformation intent, affected scope, validation result, reviewer/authority when relevant, and promotion result.
10. **Prefer deterministic transforms** — use explicit mappings, formulas, scripts, queries, or reproducible operations when the same input should produce the same output. Use model judgment for ambiguous classification/reconciliation, then expose the ambiguity.

## Spreadsheet-specific discipline

- distinguish input cells, formulas, derived values, metadata, and presentation-only formatting;
- do not silently convert formulas to values or vice versa;
- treat hidden sheets/rows, named ranges, merged cells, filters, validations, protections, and external links as possible behavior, not decoration;
- compare neighboring formula patterns and structural siblings before assuming an outlier is intentional;
- when a workbook is authoritative, preserve its structure unless the task explicitly authorizes redesign.

## Reconciliation ladder

Use the cheapest reliable evidence first:
1. exact stable key;
2. normalized exact composite key;
3. trusted mapping/reference table;
4. constrained fuzzy/entity match using supporting fields;
5. human/Creator review for unresolved material ambiguity.

Never promote a low-confidence fuzzy match merely to reach 100% coverage.

## Pairing

Pair with Files/Spreadsheet tooling for artifact mechanics, Research for external reference data, Software Development for scripts/pipelines, Security Engineering for sensitive data, and Release Engineering when promotion affects production services.

Do not replace domain-specific skills such as `$msa` or `$pra`; those own their specialized business rules and may use this skill's generic mechanics.
