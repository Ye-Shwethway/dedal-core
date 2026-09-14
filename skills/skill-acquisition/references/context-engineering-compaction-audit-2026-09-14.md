# Context Engineering / Compaction Deep Audit — 2026-09-14

## Sources reviewed

- Anthropic, `Effective context engineering for AI agents` (2025-09-29).
- Anthropic, `Scaling Managed Agents: Decoupling the brain from the hands` (2026-04-08).
- OpenAI, `Introducing the Agents API` (2026-09-10 public beta context-management direction).
- OpenAI, `From model to agent: Equipping the Responses API with a computer environment` (native compaction discussion).
- `langchain-ai/context_engineering`, pinned at `c1a78c1d7f466f68924624f280fd3c0b9742fd29`.
- Letta public context/memory architecture material for tiered in-context vs external memory patterns.

No external package, notebook, runtime, or script was installed or executed for this audit.

## Main finding

The strongest shared pattern is that context engineering is not one summarization step. It is a lifecycle with distinct operators:

- **write** important state outside the active window;
- **select** only what the next decision needs;
- **compress** redundant history while preserving decision-critical anchors;
- **isolate** deep or unrelated work so it does not pollute the main context.

This maps cleanly onto DEDAL's existing Agent Engineering and Knowledge/Memory layers; it does not justify a new top-level skill.

## ADAPT — reference-first, just-in-time retrieval

Prefer stable references/identifiers plus compact working facts over copying large source bodies into durable context. Retrieve the source only when needed. Exact IDs/scopes should beat broad semantic recall when available.

For volatile live state, relevance alone is insufficient: selection must also consider authority and freshness. A compacted or remembered repo/service fact must be refreshed when staleness could alter the next action.

## ADAPT — compaction with recoverability

Compaction is a lossy optimization and must not silently become a new source of truth. Preserve:

- active goal and hard constraints;
- accepted decisions;
- unresolved risks/blockers;
- evidence/source identity;
- next executable step;
- pointers to live state that may require re-verification.

When canonical source material still exists, keep a recovery reference. Prefer clearing old raw tool results before compressing authority boundaries or accepted decisions.

## ADAPT — explicit isolation return contract

Isolation is useful for research breadth, specialist work, or tool-heavy exploration, but the child context should return compact conclusions, uncertainty, evidence, and references rather than dumping its whole transcript into the parent context.

Multi-agent isolation remains optional. It should be chosen only when it reduces pollution or enables useful independent work.

## ALREADY COVERED

DEDAL already has:

- live-state-over-memory precedence;
- progressive disclosure and smallest-sufficient skill loading;
- executable checkpoints;
- verified-state promotion;
- bounded retrieval and provenance-aware memory architecture;
- compact long-horizon carryover.

The new value is making context operators and compaction safety executable rather than merely descriptive.

## REJECT AS DEFAULT

- Loading all potentially relevant files/tools into context because the window is large.
- Treating semantic similarity as sufficient retrieval ranking when authority/freshness differ.
- Irreversible prose compaction that drops source identity.
- Automatic sub-agent fan-out solely to gain fresh context windows.
- Vendor-specific memory filesystems or managed-agent runtimes as a Core dependency.

## DEDAL decision

- New skill: **NO**
- Agent Engineering refinement: **YES**
- Knowledge/Memory architectural rewrite: **NO; existing ownership is sufficient**
- Executable context contract: **YES**
- Outcome claim: **contract validation only; real-task gains remain unmeasured**
