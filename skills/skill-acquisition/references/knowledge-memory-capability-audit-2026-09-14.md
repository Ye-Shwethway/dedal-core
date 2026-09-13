# Knowledge / Memory Architecture capability audit — 2026-09-14

## Capability gap

DEDAL already had strong project archive (`$ika`), project bootstrap, agent context, and state-boundary contracts, but no single generic architecture answered all of:
- what kinds of memory/state exist;
- who owns each state class;
- project-local vs global scope;
- promotion/demotion rules;
- freshness and contradiction handling;
- retrieval/compaction policy;
- memory poisoning and deletion governance.

## Current-source findings

### OpenAI — memory synthesis
OpenAI's 2026 `Dreaming` memory work frames long-horizon memory quality around freshness, continuity, relevance, correctness, and scalability. Durable memory must be synthesized rather than treated as an ever-growing transcript.

### Anthropic — context engineering
Anthropic separates the finite active context window from the wider universe of possible information. Their long-horizon guidance uses compaction and structured note-taking outside the context window, then selectively reloads useful state.

### MemGPT / Letta
MemGPT (arXiv:2310.08560) models limited context using hierarchical/virtual memory concepts. Letta's current architecture exposes persisted memory blocks and message-buffer/state distinctions. This supports the conceptual separation of persistent memory from active message context, without requiring DEDAL to adopt Letta as a runtime.

Pinned Letta repository snapshot:
- repo: `letta-ai/letta`
- commit: `5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a`
- license: Apache-2.0
- inspected: 2026-09-14

### Existing DEDAL contracts
`$ika` already established evidence-linked project records, bounded retrieval, stable history, and archive authority. `kernel/STATE_BOUNDARY.md` established that public Core must not become a private-memory database. The new capability generalizes these principles across all state layers rather than duplicating archive operations.

## DEDAL synthesis

Adopt:
- memory != context;
- explicit state classes and scopes;
- one canonical owner where practical;
- provenance/freshness envelope scaled to consequence;
- deliberate promotion/demotion;
- contradiction as a first-class state;
- bounded retrieval and compaction;
- checkpoint-as-executable-state;
- poisoning resistance;
- deletion/forgetting governed by the real owner;
- downstream behavior as the evaluation target.

Reject:
- retain-everything defaults;
- one universal memory store;
- automatic promotion from repeated/model-generated content;
- semantic/vector retrieval as a mandatory dependency;
- universal TTLs;
- raw private state in public Core;
- hidden chain-of-thought persistence;
- claims that a model can delete platform-owned memory merely by saying it forgot.

## Boundary with `$ika`

Keep `$ika` independently routable for concrete project archive create/load/refresh/audit/impact workflows. `knowledge-memory` provides the generic architecture governing state scope, ownership, freshness, retrieval, conflict handling, compaction, and governance. Pair them when both are needed.

## Security note

Memory is an attack surface: poisoned retrieved text, stale mirrors, generated summaries, and inferred state can influence future decisions if promoted carelessly. Security Engineering remains the primary threat-model skill; Knowledge/Memory Architecture defines the state and promotion controls that reduce that risk.

## Runtime decision

No third-party memory system was installed. DEDAL Core remains runtime-neutral and may use Files, repos, databases, platform memory, connected services, or future stores according to actual authority and sensitivity.
