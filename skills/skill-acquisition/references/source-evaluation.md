# Skill Source Evaluation

Use this before adopting ideas or files from an external skill.

## Minimum record

For every serious candidate, capture:

- source repository/registry and exact path;
- inspected revision, version, or retrieval date;
- author/publisher identity when available;
- license and whether reuse/adaptation is permitted;
- intended runtime/client and required tools;
- scripts, dependencies, network access, credentials, filesystem scope, and external services;
- maintenance/activity signals;
- tests/evals/examples present;
- useful patterns;
- DEDAL conflicts or assumptions that must be removed;
- disposition: reject, idea-only, adapt, or exact-import candidate.

## Quality dimensions

Evaluate qualitatively rather than pretending a single numeric score proves quality.

### Relevance
Does it solve a recurring DEDAL problem better than the current skill?

### Trigger precision
Is the description narrow enough to activate correctly? Penalize broad rules that force invocation on unrelated tasks.

### Progressive disclosure
Does the entrypoint stay focused while deeper references/scripts load only when needed?

### Workflow quality
Look for explicit phases, preconditions, failure paths, rollback, verification, and completion criteria.

### Evidence discipline
Prefer skills that distinguish observed facts from assumptions and require fresh evidence for completion claims.

### Portability
Separate durable workflow logic from one product's tool names, worker model, file paths, or UI.

### Maintainability
Prefer clear structure, small composable references, schemas/tests where useful, changelog/history, and recent maintenance.

### License/provenance
Unknown or incompatible licensing blocks copying. Ideas may still inspire an independently written workflow when legally appropriate, but do not reproduce protected expression.

### Security/privacy
Apply `security-audit.md`; registry reputation or scanner badges never bypass this review.

## Source preference

When equivalent patterns exist, prefer standards and first-party examples over community forks, then mature maintained projects over anonymous or thin packages. Community skills remain valuable for novel ideas and failure modes.