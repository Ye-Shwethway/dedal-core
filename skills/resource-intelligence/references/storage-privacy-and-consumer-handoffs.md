# Storage, privacy, and consumer handoffs

## Public/private split

Public Core may define generic schemas, lifecycle states, source/evidence classes, delta semantics, privacy rules, and sanitized examples.

Private overlay owns actual tracked targets and user/project-specific intelligence: profiles, watchlists, catalogue rows, subjective preferences, selections/rejections, private source IDs, private performance outcomes, and learned weights.

Suggested private shape:

```text
/DEDAL/private-overlay/resource-intelligence/
  profiles/
  catalog/
  events/
  indexes/
  checkpoints/
```

Use existing DEDAL State Contract artifact roles:
- profile/catalog current state: canonical pointers;
- discovery/change runs: immutable evidence;
- attention queues/search indexes: derived indexes;
- bounded refresh history: rolling logs when appropriate.

Do not create `latest`, `final`, `(1)`, or duplicate canonical catalogues.

## Consumer handoff

Provide only the fields necessary for the next owner:

`resource_id | canonical_identity | relevant profile fit | current delta | evidence refs | uncertainty/conflicts | opportunity/lead | last_verified`

The consumer owns its domain gates. Resource Intelligence must not silently convert a discovery lead into approval to publish, buy, deploy, cite, prescribe, or otherwise act.

## Retention and retirement

Retire resources when they are explicitly rejected, permanently unavailable, outside profile scope, or superseded by a canonical identity. Preserve history sufficient to avoid rediscovery loops. A retired record may be reactivated only with new evidence or a changed profile.

## Retained proof and scoped decisions

Save real proof images under the canonical private workstream alongside a stable evidence index. Preserve file identity/version history, source attribution, asset hash and resource/opportunity scope. Keep private images, subjects, Creator ratings and rejection reasons out of public Core/Git. Handoffs include the current scoped review, exact proof identity, screening basis and unresolved requirements; consumers must not infer acceptance from tracked lifecycle or fit rank. Report preview-only evidence as unsaved until retention succeeds. Preserve rejection even when source access fails; do not claim the rejected preview was archived.
