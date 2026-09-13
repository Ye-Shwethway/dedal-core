# Adaptation Notes — Project Bootstrap

DEDAL Project Bootstrap is a provider-agnostic context-adaptation workflow.

## Primary influences reviewed 2026-09-14

- AGENTS.md open format and repository snapshot `agentsmd/agents.md` @ `d001185d792eb6402a58e4cbef1c228b309ec25d`.
- Current GitHub Copilot repository/custom-instruction guidance: repository-wide instructions, path-specific instructions, and nearest scoped `AGENTS.md` precedence where supported.
- DEDAL's existing fresh-chat bootstrap, multi-session delivery, Harness v1, and repository source-of-truth rules.

## Adopted

- predictable agent-facing instruction entrypoints;
- scoped/local instructions rather than one global mega-prompt;
- project instructions should include setup/build/test conventions useful to execution;
- compact context maps and progressive disclosure;
- explicit separation of stable rules from volatile checkpoint state;
- live source verification before relying on remembered project state.

## Rejected / generalized

- dependence on a single vendor's filename or precedence behavior as universal;
- generating repository instructions by copying the entire README/docs tree;
- treating agent instructions as authoritative evidence that code/runtime actually behaves as described;
- storing transient session detail in permanent root instructions.

Platform-specific instruction precedence must be verified against current tool documentation when it affects execution.
