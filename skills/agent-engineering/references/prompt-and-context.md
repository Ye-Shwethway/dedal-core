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

## Progressive disclosure

Keep durable, widely applicable rules close to the agent. Load specialized detail only when the current task requires it. Prefer stable identifiers, file paths, source links, query handles, or other references that let the agent retrieve supporting context just in time.

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

## Context lifecycle

As a run grows:
- preserve goal, accepted decisions, constraints, and evidence identity;
- discard or summarize redundant chatter and superseded observations;
- retain errors or failed attempts only when they affect the next decision;
- prefer factual state artifacts over narrative summaries when exactness matters;
- re-fetch live state when freshness can change the answer.

## Prompt optimization

Do not optimize wording by intuition alone when the workflow matters. Maintain a task set and metric/rubric, compare variants, and keep the version that improves the complete system without unacceptable regressions.

Prompt or few-shot optimization systems such as DSPy demonstrate a general principle: **instructions/examples should be treated as tunable program parameters when a reliable metric exists**, not as sacred prose.

## Anti-patterns

- giant system prompts containing every known rule;
- duplicating the same guidance in multiple layers;
- hiding critical authority rules in retrieved optional context;
- treating context-window size as permission to include low-value material;
- preserving stale tool results when live state is authoritative;
- prompt tweaks without an eval or observed failure they are intended to fix.
