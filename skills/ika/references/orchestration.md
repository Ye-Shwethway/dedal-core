# IKA Orchestration Contract

## Goal

Use only as much decomposition as the task benefits from while preserving authority, evidence, validation, and serialized canonical writes.

## Capability handshake

Before orchestration, determine what the current runtime actually supports:

- independent native workers/tasks;
- safe parallel tool calls without independent workers;
- single-agent sequential execution;
- no suitable execution surface.

Never infer worker availability from product branding and never claim subagents ran unless they actually did.

## Default policy

`auto` behavior is implicit: small bounded work stays single-agent; larger source-heavy create/refresh/audit work may decompose when independent work can materially shorten the critical path or add useful independent verification.

Prefer the fewest useful workers/roles. More parallelism is not automatically better.

## Safe decomposition

Useful logical roles include source inventory, knowledge extraction, conflict analysis, refresh analysis, candidate assembly, audit review, publication, and verification. These are semantic boundaries, not a requirement to spawn one worker for each role.

Worker/tool results remain advisory until DEDAL reconciles them against authority and acceptance criteria.

## Mutation discipline

Parallelize read-only independent work when safe. Serialize writes to the canonical archive and dependent manifest/registry state. After a verified canonical write, optional mirrors may update independently if provider semantics allow it.

Fail fast on blocking authority conflicts, secret/sensitivity risk, schema failures, or incomplete required evidence.

## Reporting

When orchestration materially affects execution, report the real backend used and any important fallback. Do not invent timings or speed multipliers.
