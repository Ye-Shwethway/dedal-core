# Memory model, scopes, and ownership

## Memory is layered state

DEDAL should not treat all remembered information as one undifferentiated pool. Separate:

- active working context;
- episodic workflow trace;
- durable project knowledge;
- user-global working preferences;
- external authoritative state.

The practical question is not only `should this be remembered?` but also `who owns it, at what scope, for how long, with what evidence, and how should it be retrieved?`

## Scope classes

### Task-local
Temporary assumptions, intermediate calculations, scratch plans, one-off tool results. Discard after the task unless a concrete durable lesson emerges.

### Project-local
Accepted architecture, product decisions, build/release state, canonical references, known constraints, checkpoints. Prefer project-owned artifacts/repos/archives over global memory.

### User-global
Stable cross-project preferences and working conventions that genuinely generalize. Keep this narrow; project-specific facts should not leak upward merely because they recur.

### External-authoritative
Live services, repositories, databases, current files, primary sources, device/system state. Memory can point to these systems but should not replace them.

## Ownership rules

1. Assign one canonical owner whenever practical.
2. Mirrors and summaries are derived views, not co-equal masters.
3. Store version/revision identifiers when a fact depends on a particular snapshot.
4. When the owner is live and queryable, re-read it for material current-state decisions rather than trusting memory.
5. Public Core may define the schema/contract but not absorb private payloads.

## Promotion ladder

A useful default promotion path is:

`observation -> candidate note -> verified project fact/decision -> compact durable record -> optional broader preference/policy only if scope truly generalizes`

Promotion should consider:
- utility across future tasks;
- evidence and confidence;
- stability/freshness profile;
- sensitivity/privacy;
- scope leakage risk;
- whether a stronger canonical owner already exists.

Repeated exposure alone is not sufficient evidence. A generated summary can amplify a mistake just as easily as a truth.

## Demotion and retirement

Durable memory should also move downward when appropriate:
- `current -> stale` when freshness expires;
- `current -> superseded` when a newer authoritative state replaces it;
- `verified -> disputed` when credible conflicting evidence appears;
- `durable -> archival` when operational relevance drops;
- `retained -> deleted/forgotten` when policy/user governance requires removal in the actual owning system.

A memory architecture that only adds state and never retires it will eventually become a context-pollution system.
