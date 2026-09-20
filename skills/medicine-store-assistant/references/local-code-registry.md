# Local Code Registry Contract

Use this reference when a stable local item identity has no usable CMS-issued code, when assigning a local fallback Serial Code, or when replacing that fallback with a later authoritative CMS code.

## Purpose

A local fallback code gives an unresolved-but-stable local item identity a durable operational identifier for audit, history, joins, reconciliation, and later CMS mapping. It is **not** a CMS code and must never be treated as catalogue evidence.

## Identity semantics

A local code identifies one stable local item identity, not one spreadsheet row and not one expiry lot.

- Ignore only a clearly terminal expiry suffix when deciding whether multiple rows are the same local identity.
- Preserve meaningful differences in drug/product, strength, formulation, route, size, device specification, brand/manufacturer clues, and other operational identity.
- Same identity across multiple legitimate lots/rows reuses the same local code.
- Different identities must never share one local code.
- If identity is materially ambiguous, do not issue or propagate a code until the ambiguity is resolved.

## Issuance

Use the configured local namespace, such as a fixed prefix plus zero-padded monotonic number.

Before issuing a new code:

1. read the local-code registry,
2. normalize the candidate local identity under the normal MSA identity rules,
3. check same-family/sibling rows for an existing local or authoritative CMS code,
4. reuse an existing local code only for the same proven identity,
5. otherwise allocate the next never-before-issued local number.

Do not fill numeric gaps and do not recycle retired/replaced codes.

> **One local code = one local identity for life. A code may appear on several legitimate lots of that identity, but it is never reassigned to another identity.**

## Registry

Keep a dedicated support registry when local fallback codes are in use. At minimum retain Local Code, Local Item Identity, Status, later CMS Code/Name when known, Assigned Date, Replaced/Retired Date, provenance, and Notes when useful.

Useful statuses include `ACTIVE_LOCAL`, `REPLACED_BY_CMS`, `RETIRED`, and `REVIEW`.

The registry is durable mapping/audit evidence, not a replacement for live stock truth.

## CMS replacement

When authoritative evidence later proves a CMS identity:

1. verify the CMS code together with clinically/operationally meaningful identity evidence,
2. checkpoint before the live identity mutation,
3. replace the live operational Serial Code with the authoritative CMS code where appropriate,
4. update dependent CMS fields only when independently supported,
5. preserve `local code -> CMS code` lineage in the registry,
6. mark the local code `REPLACED_BY_CMS` rather than deleting it,
7. never issue that local code to another identity,
8. read back and audit the replacement.

Do not rewrite closed historical snapshots solely to replace an old local code with a newer CMS code.

## CMS-field boundary

A local fallback code does not prove CMS catalogue identity, CMS Name, CMS Price, or current catalogue inclusion. Do not populate or infer those fields merely because a local code was assigned.

## Checkpoint, marking, and audit

Initial assignment and later CMS replacement are operational identity mutations.

- Create and verify the normal pre-mutation restore checkpoint.
- Read current rows and registry state before writes.
- Mark directly written and verified live Serial Code cells under the normal visual-marking protocol.
- Record one coherent grouped audit entry when the operation spans many rows.
- Read the affected live rows, registry entries, and audit evidence back before reporting success.

## Invariant

> **Local codes stabilize unresolved local identity; CMS codes replace them only when authoritative evidence arrives, while the local-code lineage remains permanently auditable.**
