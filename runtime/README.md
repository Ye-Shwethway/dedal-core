# DEDAL Runtime Contracts

This directory contains deterministic contracts intended for host/harness integration.

## GitHub mutation guard

`github_mutation_guard.py` enforces a locked repository mutation mode against `github-mutation-policy.json`.

A host adapter should:

1. create one `MutationGuard` when the work unit locks `direct-single-file` or `atomic-multi-file`;
2. call `check(tool, is_mutation=True)` immediately before every GitHub mutation;
3. execute the provider mutation only when the guard accepts it;
4. call `record_success(tool, is_mutation=True)` only after the provider reports that mutation succeeded;
5. retain the same guard instance until the work unit completes, is abandoned, or is explicitly reconciled after authoritative state drift.

Unknown mutation tools fail closed when presented as mutations.

### Enforcement boundary

This code is enforceable inside a host, proxy, MCP/plugin adapter, or other tool dispatcher that routes mutations through it. The public DEDAL Core repository cannot intercept native provider tools by itself. Until a host integrates the guard, the repository has executable contract validation but not platform-level interception.
