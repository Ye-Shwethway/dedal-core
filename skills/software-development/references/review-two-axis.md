# Two-Axis Code Review

Review an exact change set against two independent questions.

## 1. Pin the comparison

Resolve the fixed point/merge base and inspect the exact diff plus relevant commit list. Do not review an imagined branch state.

## 2. Standards axis

Ask whether the change follows repository-local engineering rules, architecture, naming, security/privacy boundaries, and maintainability expectations. Project-local documented rules outrank generic heuristics.

Generic smell checks may include duplicated logic, speculative generality, shotgun surgery, unclear naming, leaky interfaces, unnecessary pass-through layers, and repeated conditional structures. Treat these as judgement calls unless the repository makes them hard rules.

## 3. Intent/spec axis

Ask separately whether the change actually implements the requested behavior:
- missing or partial requirements;
- behavior that is wrong despite looking complete;
- accidental scope creep;
- regressions or changed behavior that were not requested.

Use the originating issue/spec/accepted conversation/checkpoint when available. If no durable spec exists, state that limitation instead of inventing one.

## 4. Report separately

Do not let clean style hide wrong behavior, or correct behavior hide architectural violations. Keep Standards and Intent findings distinguishable even if the same reviewer performs both passes.

Independent workers may be useful when available, but conceptual independence matters more than parallelism.
