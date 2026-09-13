# Validation and Promotion Gates

Validation should convert important business/data assumptions into observable checks.

## Contract dimensions

Check what matters for the workflow:
- required columns/fields;
- data types and parsing;
- allowed domains/status values;
- uniqueness and duplicate constraints;
- referential integrity / code lookup validity;
- date and numeric ranges;
- cross-field relationships;
- aggregate totals or count deltas;
- formula presence/patterns;
- source/version identity.

Not every workflow needs every dimension.

## Staging gate

Before staging is considered reviewable:
- ingestion scope is known;
- raw/source evidence is retained or reproducibly addressable;
- deterministic transforms completed;
- obvious validation failures are surfaced;
- unresolved exceptions are not silently dropped.

## Promotion gate

Before production promotion, verify:
1. intended target/version;
2. expected record-count delta or explained differences;
3. blocking validation results;
4. unresolved material exceptions;
5. duplicate/merge impact;
6. formula/derived-field integrity where applicable;
7. rollback/snapshot path for consequential mutations;
8. required human/Creator authority.

A successful write or import receipt is not sufficient promotion evidence.

## Post-promotion verification

Read back the authoritative target. Re-run the highest-value invariants against the promoted state rather than assuming staging and production are identical.

Keep warnings distinct from blockers. A workflow that treats every anomaly as fatal becomes unusable; a workflow that treats every anomaly as informational becomes unsafe.
