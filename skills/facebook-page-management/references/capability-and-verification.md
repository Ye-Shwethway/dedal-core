# Capability and Verification

## Capability state model

Track Facebook Page capabilities as separate evidence states:

- **exposed** — A tool/action is listed by the execution surface;
- **authorized** — current scopes/tasks indicate the account/Page should be permitted;
- **read-verified** — the operation returned current authoritative Page state;
- **write-verified** — a bounded mutation completed and remote read-back confirmed the intended state;
- **degraded** — the tool is exposed but current reads/writes are stale, policy-blocked, or otherwise unreliable.

Do not collapse these states into a single "supported" claim.

## Identity and authority

- Resolve managed Pages from the authenticated identity before mutation.
- Preserve Page IDs and composite post IDs only in runtime/private state, never public examples tied to a real account.
- Check current Page tasks/roles when an administrative or publishing mutation fails with an authority-style error.
- Distinguish a user access token from a Page access context. Provider APIs may require Page-scoped authorization even when the user token has the correct grants.

## Mutation evidence

For consequential writes use:

`resolve Page -> read baseline -> explicit intent -> narrow mutation -> read-back -> cleanup/rollback when planned -> report exact state`

When a mutation fails:

`exact tool/provider error -> classify auth vs policy vs media/input vs transient -> minimal correction -> at most one evidence-supported retry`

Never retry a destructive or externally communicative mutation merely because the first response was ambiguous.

## Public/private separation

Public Core may store:

- general Page-operation workflows;
- generic permission/task names;
- provider-agnostic verification patterns;
- sanitized failure classes and live-gate lessons.

Private state must hold:

- real Page/account IDs and aliases;
- Page-specific voice, niche, content calendar, audience strategy, moderation policy, or messaging persona;
- private analytics and message content;
- tokens, cookies, auth artifacts, app secrets, webhook secrets, or business identifiers.
