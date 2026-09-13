# Record Identity and Reconciliation

## Start with identity

Before deduplication, merging, lookup, or reconciliation, define what makes two records the same real-world entity or event.

Possible identity evidence:
- stable unique ID;
- trusted external code;
- composite key such as `(item, batch, expiry)` or `(patient, date, encounter)` when domain-authorized;
- constrained entity match using multiple supporting fields.

A display name alone is rarely a safe identity key.

## Normalize for comparison

Normalization may include trimming whitespace, canonical case, normalized dates/units, punctuation cleanup, type coercion, or domain-approved aliases. Preserve raw values when provenance matters.

Keep these concepts distinct:
- raw value;
- normalized comparison value;
- canonical accepted value.

## Match classes

Classify candidate outcomes explicitly:
- **exact** — stable key or trusted exact composite match;
- **mapped** — approved reference/alias mapping;
- **probable** — multiple fields strongly support identity but review may still matter;
- **ambiguous** — multiple candidates or material conflict;
- **unmatched** — no supported candidate.

Never collapse ambiguous/unmatched into exact merely for completeness.

## Iterative reconciliation

For large or messy datasets:
1. resolve exact/high-confidence groups first;
2. remove them from the unresolved set;
3. refine rules for the remainder;
4. inspect exceptions and collisions;
5. record accepted mappings where reuse is safe;
6. rerun validation after merges or canonicalization.

## Merge safety

Before merging duplicates, verify fields that must agree and decide field-level authority where they differ. Preserve meaningful lineage: which source rows contributed, what was chosen, and why.
