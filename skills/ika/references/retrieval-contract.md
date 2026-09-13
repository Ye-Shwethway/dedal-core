# Retrieval Contract

## Goal

Load the smallest sufficient archive context for the current task instead of dumping full project history into the active context.

## Baseline

For a known archive, read `manifest.json` and `current-context.md` first, then inspect deeper families only when the task requires them.

## Selection order

Prefer deterministic, inspectable selection:

1. exact stable record IDs;
2. explicit project/family/task cues;
3. normalized lexical overlap;
4. current state/status and freshness cues;
5. evidence closure from selected knowledge to its cited sources;
6. bounded broader fallback when narrow signals are insufficient.

Do not claim semantic/vector retrieval unless the actual runtime uses it.

## Bounds

Keep explicit limits for facts, decisions, sources, open questions, history, relationships, and evidence closure. If relevant evidence is omitted because of a bound, report truncation rather than pretending the package is complete.

Prefer selected records/sections over copying whole archive files into the active context.

## Diagnostics

A useful retrieval result should make clear:

- canonical revision used;
- retrieval mode;
- families considered and selected;
- selected/skipped counts when practical;
- why records were included;
- fallback reason if broad retrieval was necessary;
- evidence completeness/truncation;
- unresolved access gaps.

## Freshness rule

A concise `current-context.md` is a navigation surface, not proof that all underlying facts remain current. For claims whose correctness materially matters, verify the live/primary source when available.
