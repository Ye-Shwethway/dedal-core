# LongHorizon-Harness Deep Audit — 2026-09-14

## Source

- Repository: `AMAP-ML/LongHorizon-Harness`
- Pinned revision: `a1dd930614972b92361c1b9cd6aac441a6db5a65`
- License: MIT
- Paper: `LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks` (arXiv:2608.01964, 2026-08-03)

No upstream package, script, or runtime was installed or executed during this audit.

## What is materially useful

### ADAPT — verified-state-only promotion

The strongest pattern is not the number of agents. The harness keeps execution claims separate from durable task state and advances state only after environment-grounded audit evidence. DEDAL should adopt the invariant:

> executor/model claims are candidate state; durable accepted state requires evidence appropriate to the claim.

This aligns with DEDAL's existing live-state-over-memory and truthful-completion rules while making the promotion boundary explicit.

### ADAPT — verifier authority separation

The upstream auditor is designed as a verifier rather than a repair worker. It detects workspace mutations during audit and can invalidate or downgrade the audit when the verifier changes the state it is judging. DEDAL should prefer read-only verification where the execution surface supports it and treat verifier-created evidence as suspect unless the workflow explicitly authorizes verifier mutation.

### ADAPT — compact verified carryover

The manager receives maintained task state plus selected auditor reports rather than raw historical trajectories. This is a strong long-horizon context pattern: carry forward compact verified facts, decisions, unresolved gaps, and references; retrieve raw traces only for diagnosis.

### ADAPT — completion is gated by audit state

A manager request to finish is not accepted unless prior audit evidence reports clean completion and contract alignment. DEDAL should preserve the same principle without requiring a dedicated auditor agent: completion claims should be gated by independent evidence when the environment provides an objective verifier/test/read-back path.

### ALREADY COVERED — resumable externalized state

DEDAL already externalizes accepted state, evidence, risks, next executable step, owner, and verified revision in executable checkpoints. The upstream round ledger reinforces this design but does not justify a new top-level skill.

### ALREADY COVERED — bounded role budgets and failure exits

DEDAL Agent Engineering already requires explicit retry/termination/escalation semantics and bounded loops. Upstream implementation details are useful evidence, not a new architecture requirement.

### REJECT AS DEFAULT — mandatory manager/executor/auditor multi-agent topology

The paper reports gains for its MEA topology on several benchmarks, but DEDAL should not generalize that into a universal three-agent requirement. Coordination cost, tool availability, and task verifiability vary. Prefer the smallest sufficient topology; use an independent verifier role only when it adds evidence unavailable from deterministic checks or read-back.

### REJECT — importing provider/runtime implementation

Do not vendor the upstream dashboard, adapters, process supervisor, workspace snapshot machinery, provider-specific CLI integration, or evaluation harness into Core. Those are product/runtime implementation choices rather than durable DEDAL operating principles.

## Evidence notes

The paper reports improvements across WeaveBench, Terminal-Bench 2.1, and OSWorld 2.0, including cross-model results. Treat these as upstream experimental evidence for the architecture, not as measured DEDAL gains.

The current source also contains explicit crash persistence, resumable round ledgers, verifier mutation detection, audit control headers, and completion guards. These implementation details support the adapted principles above.

## DEDAL decision

- New skill: **NO**
- Agent Engineering refinement: **YES**
- Knowledge/Memory refinement: **no separate change needed now**
- Project Bootstrap refinement: **no separate change needed now**
- Outcome claim: **contract/design refinement only; DEDAL real-task improvement not yet measured**
