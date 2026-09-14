# Prompt and Context Engineering

## Principle

Prompt engineering is one component of context engineering. The model's effective input includes instructions, tool definitions, retrieved evidence, state, prior events, examples, and output contracts.

Optimize for **high-signal context per token**, not maximum context volume.

## Instruction contract

A strong instruction set normally establishes:
- objective and success criteria;
- scope and non-goals;
- authority / risk boundaries;
- available actions and when to use them;
- expected outputs or schemas where precision matters;
- important edge cases and failure behavior.

Use direct language at the right altitude: neither brittle pseudo-code for every possibility nor vague slogans that assume hidden shared context.

## Four context operators

Treat context management as four separable operations rather than one generic "memory" action:

1. **write** — persist state outside the active window when it must survive turns/sessions;
2. **select** — load the smallest relevant subset for the next decision;
3. **compress** — reduce token volume while preserving decision-critical anchors and recoverability;
4. **isolate** — keep unrelated/deep work out of the main working context and return only the evidence needed upstream.

Choose the smallest operator that solves the actual problem. Do not invoke persistence, compaction, or sub-agent isolation merely because a long context window exists.

## Progressive disclosure and reference-first retrieval

Keep durable, widely applicable rules close to the agent. Load specialized detail only when the current task requires it. Prefer stable identifiers, file paths, source links, query handles, commit SHAs, or other references that let the agent retrieve supporting context just in time.

When full source material is recoverable, keep the **reference plus a compact working fact** rather than duplicating the whole source in durable context. Re-fetch the source when exact wording, freshness, or changed state matters.

Do not pre-load large bodies of documentation merely because they could become relevant.

## Separate context classes

When the runtime permits, distinguish:
1. **durable policy/instructions** — stable behavior and boundaries;
2. **task state** — current goal, plan, unresolved decisions, budgets;
3. **evidence** — retrieved files, web sources, API results;
4. **interaction history** — messages and prior actions;
5. **tool affordances** — tool descriptions and schemas;
6. **examples** — only where they materially improve the target behavior.

This makes compaction, retrieval, provenance, and debugging easier.

## Compaction safety contract

Compaction is a lossy optimization, not a source-of-truth operation.

A safe compacted state preserves, when present:
- active goal and hard constraints;
- accepted decisions and their owning scope;
- unresolved risks / blockers;
- evidence identity or provenance needed to re-open the source;
- next executable step;
- live-state pointers whose freshness may require re-verification.

Do not irreversibly replace canonical external state with a prose summary. A compacted item should remain recoverable through a source/reference when the underlying material still exists.

Prefer deleting or summarizing old raw tool output before compressing accepted decisions or authority boundaries. If a fact is volatile, compaction must not turn it into a timeless claim.

## Freshness-aware selection

Selection should consider **relevance + authority + freshness**, not semantic similarity alone.

- Stable policy/preferences may be reused when their owner has not changed.
- Live repository/service/version/status facts should be refreshed when staleness could change the next action.
- A remembered or compacted fact never outranks a contradictory live authoritative source.
- If an exact identifier is known, prefer scoped retrieval by that identifier over broad semantic search.

## Isolation

Use isolated context only when separation has a concrete benefit: independent research breadth, large tool-heavy exploration, sensitive scope separation, or specialist work that would pollute the main context.

The isolated worker should return compact evidence, conclusions, unresolved uncertainty, and references. Do not automatically import its full transcript into the parent context.

## Context lifecycle

As a run grows:
- preserve goal, accepted decisions, constraints, and evidence identity;
- discard or summarize redundant chatter and superseded observations;
- retain errors or failed attempts only when they affect the next decision or belong in regression evidence;
- prefer factual state artifacts over narrative summaries when exactness matters;
- re-fetch live state when freshness can change the answer;
- keep recent/raw material available outside the active context when future recovery is plausible.

## Prompt optimization

Do not optimize wording by intuition alone when the workflow matters. Maintain a task set and metric/rubric, compare variants, and keep the version that improves the complete system without unacceptable regressions.

Prompt or few-shot optimization systems such as DSPy demonstrate a general principle: **instructions/examples should be treated as tunable program parameters when a reliable metric exists**, not as sacred prose.

## Anti-patterns

- giant system prompts containing every known rule;
- duplicating the same guidance in multiple layers;
- hiding critical authority rules in retrieved optional context;
- treating context-window size as permission to include low-value material;
- preserving stale tool results when live state is authoritative;
- irreversible compaction with no source/reference path when recoverability matters;
- semantic retrieval that ignores authority or freshness;
- importing full sub-agent/tool transcripts when a compact evidence handoff is enough;
- prompt tweaks without an eval or observed failure they are intended to fix.
