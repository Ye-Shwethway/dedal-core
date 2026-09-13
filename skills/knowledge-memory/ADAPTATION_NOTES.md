# Adaptation Notes — Knowledge / Memory Architecture

This capability is a DEDAL-native synthesis, not a direct port of one framework.

## Primary influences reviewed on 2026-09-14

- OpenAI, **Dreaming: Better memory for a more helpful ChatGPT** (2026-06-04): memory synthesis must optimize freshness, continuity, relevance, correctness, and scalability over long horizons.
- Anthropic, **Effective context engineering for AI agents** (2025-09-29): context is finite; compaction and structured note-taking help long-horizon agents; memory outside the context window should be selectively brought back in.
- Anthropic, **Effective harnesses for long-running agents** (2025-11-26): session resets require clear persistent artifacts/checkpoints to preserve progress.
- MemGPT, **Towards LLMs as Operating Systems** (arXiv:2310.08560): hierarchical memory/context tiers and virtual context management as a conceptual model.
- `letta-ai/letta` @ `5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a`, Apache-2.0: explicit persisted memory blocks, attachment/detachment, and state outside the immediate message buffer.
- Existing DEDAL `$ika`, Project Bootstrap, Agent Engineering, Security Engineering, and `kernel/STATE_BOUNDARY.md` contracts.

## Retained ideas

- memory and active context are distinct;
- long-horizon systems need persistent structured state outside the prompt window;
- memory should be tiered/scoped rather than treated as one transcript;
- retrieval should be selective and context-budget aware;
- freshness/correctness matter as much as retention;
- persistent state should be inspectable and resumable;
- untrusted or inferred content must not silently become trusted durable memory.

## DEDAL-specific changes

- added explicit ownership and public-Core/private-state boundaries;
- separated working context, episodic trace, project-local durable knowledge, user-global preferences, and external-authoritative state;
- made promotion/demotion, contradiction handling, freshness classes, and deletion governance explicit;
- preserved `$ika` as the specialized archive workflow rather than replacing it;
- avoided framework-specific runtime APIs, vector-store assumptions, or mandatory autonomous self-editing memory;
- prohibited hidden chain-of-thought as a required memory artifact.

## Rejected as universal rules

- retaining every interaction;
- semantic/vector retrieval as a mandatory dependency;
- one global memory store for all projects and privacy classes;
- automatic self-promotion of generated summaries/inferences;
- fixed TTLs for all knowledge;
- memory volume as a quality metric;
- framework lock-in to Letta/MemGPT or any other memory runtime.

No third-party memory framework, package, model, or executable was installed or run for this adaptation.
