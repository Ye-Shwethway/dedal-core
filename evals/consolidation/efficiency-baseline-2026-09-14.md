# Efficiency Baseline — 2026-09-14

## Scope

Preliminary consolidation baseline using only evidence already observed in DEDAL Core work. This is not yet a full outcome-validation result.

## 1. Repository mutation efficiency — OBSERVED NUMERIC

Historical GH-01 smoke run 001 used a coherent multi-file task but produced two avoidable intermediate direct-write commits before a rebuilt final atomic commit. That is three repository commits for one intended milestone.

Recent v0.16 and v0.17 milestones each completed as one atomic fast-forward commit from the prior HEAD with intended file sets only.

Comparable repository-write amplification:
- early failed pattern: 3 commits / 1 intended milestone;
- current clean pattern: 1 commit / 1 intended milestone;
- reduction in commit amplification: 66.7%.

Caveat: v0.15 exposed a renewed two-direct-write regression before final reconciliation. Therefore this gain is demonstrated but not runtime-enforced or permanently solved.

## 2. CI verification discipline — QUALITATIVE OBSERVED

GH-02 demonstrated one bounded commit-scoped registration lookup, capture of the exact run ID, then run/job-specific polling until completed/success. Queued or in-progress state was not reported as success.

This is cleaner than repeated broad workflow listing, but no comparable pre-Harness broad-poll count exists, so no percentage is claimed.

## 3. Context-selection efficiency — STRUCTURAL PROXY

Current Master Index exposes 19 active skill entrypoints. The routing contract explicitly selects the smallest matching set and loads references only on demand.

Six representative routing simulations:
- repository mutation + CI: GitHub (+ Agent Engineering only when harness behavior is primary) -> 1–2;
- current evidence research: Research -> 1;
- medicine-store reconciliation: $msa + Data Operations -> 2;
- UI implementation: Interface Design + Software Development -> 2;
- identity-sensitive image work: Visual Direction -> 1;
- release/deployment: Release Engineering + Software Development -> 2.

Using the conservative upper choices above gives 10 selected entrypoints across six tasks, average 1.67/task versus 19 if every skill were loaded. This is a 91.2% reduction in entrypoint-count load as an architectural proxy.

This is NOT a measured 91.2% token, latency, or cost reduction because skill files vary in size and references are loaded progressively.

## 4. Research evidence efficiency — PARTIAL POSITIVE EVIDENCE

RS-02 is PASS: consequential claims were supported using scoped multi-source evidence without broad context dumping. RS-01 remains PARTIAL because a real stale-secondary/current-primary conflict has not yet occurred.

Conclusion: evidence selection appears better disciplined, but freshness-conflict handling lacks representative outcome evidence.

## 5. Recovery efficiency — QUALITATIVE OBSERVED

When mutation regressions occurred, current harness behavior preserved live authority, avoided force/history rewrite, rebuilt from current HEAD, and verified final state. This reduces destructive recovery risk, though the regressions themselves still create avoidable work.

## 6. Data, visual, decision, memory, bootstrap, release skills — NEEDS OUTCOME EVIDENCE

These capabilities now have contracts/evals and strong design rationale, but their net efficiency versus simpler/no-skill workflows has not yet been measured on enough comparable real tasks. Do not assign synthetic percentages.

## Preliminary conclusion

DEDAL has strong evidence of improved operational discipline and context routing, with measurable repository-transaction gains and a large structural reduction in unnecessary skill loading. The biggest unresolved efficiency risk is not missing guidance; it is that documentation-level mutation/tool rules are not runtime-enforced, as the v0.15 regression showed.

Current status: **meaningfully more efficient in several observed dimensions, but not yet globally quantified or fully outcome-validated.**