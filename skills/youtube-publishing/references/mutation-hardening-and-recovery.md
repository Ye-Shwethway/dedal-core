# Mutation Hardening and Recovery

This reference captures production lessons from live YouTube mutation work. It is a policy/evidence layer, not a substitute for current provider documentation.

## Replace-style media

Treat replacement as a transaction when vendor-native update semantics are absent, ambiguous, or empirically unreliable:

1. verify exact owner/resource identity;
2. read the current resource when possible;
3. require a DEDAL-managed recoverable baseline before destructive replacement;
4. delete the old resource only when the baseline is sufficient;
5. insert/apply the replacement once;
6. read back provider state;
7. persist the new managed baseline only after verification;
8. if insert/apply fails, attempt rollback from the previous managed source;
9. report truthful partial state if rollback also fails.

Playlist hero images follow this model. Live testing showed that `playlistImages.update` could fail with vendor-side `unexpectedPart` behavior around resumable media while delete + insert was deterministic when managed state existed. `IMAGE_TYPE_ALREADY_EXISTS` on a second hero insert further supports explicit replacement rather than blind insertion.

## Banner sources

Channel branding readback can expose a display-oriented Google URL that is not directly reusable as an upload source. Preserve a full-resolution/recoverable banner source. A valid 16:9 source meeting current YouTube size/type limits must be verified at execution time; historical requirements are not a permanent contract.

## Mutation without readable prior state

When a provider exposes set/unset but no reliable get/list for the current value:

- do not infer that the prior state is empty;
- do not perform a test set followed by unset as a “restore” strategy;
- mark unmanaged state as fail-closed;
- permit removal only when DEDAL has evidence the resource is DEDAL-managed, or when the Creator explicitly authorizes destructive handling of unmanaged state.

Current YouTube watermark management falls into this category.

## Stage-aware diagnostics

Use the narrowest diagnostic chain:

`dedicated MCP -> bounded Gateway -> D1 audit -> vendor error -> minimal patch -> one bounded retry -> readback`

Recommended audit fields:
- action and outcome;
- profile/resource identifiers needed for attribution;
- stage (`context`, `media`, `upload`, `branding_lookup`, `apply`, or another bounded stage);
- internal error code;
- vendor HTTP/status, reason, message, location, and location type;
- bounded vendor error JSON;
- resumable session/sub-stage identifiers that are safe to retain.

Never persist OAuth access/refresh tokens, bearer secrets, cookies, PKCE verifiers, raw authorization codes, or unbounded response bodies.

## Verification maturity

Distinguish:
- **exposed**: tool/schema exists;
- **contract-validated**: guard/eval exists;
- **live-gated**: representative real mutation plus readback/restoration evidence exists;
- **managed-safe**: replacement/removal also has sufficient baseline/rollback semantics.

Do not promote a capability from one level to another by implication.
