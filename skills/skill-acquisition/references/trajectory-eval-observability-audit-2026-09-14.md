# Trajectory Eval & Observability Audit — 2026-09-14

## Sources

- OpenAI Agents SDK tracing docs, reviewed 2026-09-14: traces are end-to-end workflows composed of typed spans for agents, generations, function calls, guardrails, handoffs, and custom events.
- `harness/harness-evals` pinned at `dc742e28cee08e1db95b65afce49fbdf9ae3ab5c`; Apache-2.0 license verified. The project separates task/output metrics from tool correctness, tool-argument checks, trajectory consistency, and baseline regression.
- `nderman/agent-harness` pinned at `c0253dd6b0e9ada5e8bf45bded9c89f6c730daaa`. Used as a community design reference for strict typed-seam record/replay, event-sourced traces, deterministic trajectory assertions, and live drift canaries.

No third-party runtime or package was installed or executed during this audit.

## ADAPT

### Trace and eval are different layers

A trace answers what happened. An eval answers whether the observed path and outcome satisfy the contract. DEDAL should not confuse more telemetry with stronger evidence.

### Privacy-minimal typed trajectory

For Core-level evidence, keep structured event metadata rather than raw prompt/response transcripts. Useful types are context reads, tool calls/results, guardrails, retries, state transitions, verification, and handoffs. Raw content belongs in task-owned sources only when needed and authorized.

### Deterministic trajectory assertions first

Prefer structural assertions for objective behaviors: required/forbidden actions, tool ordering, argument boundaries, retry limits, verification after mutation, and evidence-linked state promotion. Use model/human judges only for semantic dimensions that cannot be reduced safely to deterministic checks.

### Failure-to-regression promotion

A real observed failure should be converted into the smallest reproducible regression case that protects the violated invariant. Do not preserve private conversations merely to create a regression fixture.

### Replay only at a stable seam

Record/replay can be valuable when a provider/model client or tool-dispatch seam is controllable. Strict fingerprints should fail on changed prompt/tool/request contracts. Replay is not evidence that the live provider has not drifted; live canaries remain a separate concern.

## ALREADY COVERED

- DEDAL already distinguishes contract validation from real-task outcome validation.
- GitHub mutation guard tests already demonstrate deterministic positive/negative tool-path assertions.
- Executable checkpoints already externalize accepted state and evidence.

## REJECT AS DEFAULT

- Full raw prompt/response capture in DEDAL Core.
- Persisting chain-of-thought or private scratchpads for observability.
- Building a telemetry backend, dashboard, or OpenTelemetry pipeline before a real operational need exists.
- LLM-judge-only evaluation for behavior that can be checked deterministically.
- Treating offline replay as proof against live-model drift.

## DEDAL decision

- New skill: **NO**
- Agent Engineering refinement: **YES**
- Add executable trajectory contract: **YES**
- Full observability platform: **NO**
- Outcome claim: **contract/design validation only until representative real trajectories are scored**
