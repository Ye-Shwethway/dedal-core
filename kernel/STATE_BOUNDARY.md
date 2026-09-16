# State Boundary

DEDAL Core is public, version-controlled operational architecture. It is not the storage location for raw private memory or sensitive operational data.

## Allowed in DEDAL Core

- public operating rules and architecture;
- reusable skills and workflows;
- sanitized schemas/examples;
- capability and routing registries;
- evaluation rules and non-sensitive regression fixtures;
- provenance metadata that does not expose secrets;
- continuity checkpoints that describe architecture without private payloads.

## Private operational overlay

A host may maintain a Library-only private operational overlay outside this repository for durable Creator/project context that improves cross-chat execution without making that context public. Appropriate overlay material includes project/channel identifiers, stable aliases, niche/domain notes, non-secret resource IDs, verified workflow lessons, and private continuity checkpoints.

The overlay is not a secret manager. Credentials, OAuth tokens, API keys, cookies, passwords, private keys, and equivalent authentication material remain outside both Core and the overlay.

The overlay is subordinate to authoritative live state: connected services own current account/resource state, and GitHub owns repository history and code identity. Stale overlay facts must be refreshed or marked stale after contradictory read-back.

## Keep external

- credentials, API keys, cookies, session data;
- raw private memory or personal account exports;
- patient-identifying or confidential hospital data;
- private documents unless intentionally sanitized for publication;
- exact private infrastructure secrets;
- transient runtime state better owned by a live service/database.

## State ownership rule

Store exact state in the system best suited to own it. GitHub owns versioned code/docs; Library/Drive own durable files; project repos own project truth; databases/backends own structured private state; connected services own their live account state.

DEDAL Core may index or describe those systems, but should not duplicate sensitive state merely for convenience. Library-only operational overlays may retain non-secret private context, but they must remain physically and transactionally outside public Git synchronization.
