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

## Keep external

- credentials, API keys, cookies, session data;
- raw private memory or personal account exports;
- patient-identifying or confidential hospital data;
- private documents unless intentionally sanitized for publication;
- exact private infrastructure secrets;
- transient runtime state better owned by a live service/database.

## State ownership rule

Store exact state in the system best suited to own it. GitHub owns versioned code/docs; Library/Drive own durable files; project repos own project truth; databases/backends own structured private state; connected services own their live account state.

DEDAL Core may index or describe those systems, but should not duplicate sensitive state merely for convenience.
