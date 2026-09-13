# Capability Expansion Roadmap

_Date established: 2026-09-14_

This roadmap records eight high-value generic capability areas for DEDAL Core. Order reflects expected cross-project value, risk reduction, and observed gaps. The initial eight-area campaign is now implemented; future work should consolidate, evaluate, merge, or revise rather than automatically create more skills.

## Wave 1 — active

1. **Security Engineering**
   - trust/authority boundaries;
   - prompt/goal hijacking and indirect injection;
   - tool authorization and least privilege;
   - secrets/identity/privilege;
   - memory/context poisoning;
   - third-party skill/dependency/supply-chain risk;
   - red-team and security verification.

2. **Project Bootstrap / Context Adapter**
   - unfamiliar repo/project onboarding;
   - instruction hierarchy and scoped `AGENTS.md`-style guidance;
   - compact project context maps;
   - setup/build/test/run discovery;
   - architecture/source-of-truth mapping;
   - continuity/current-state compression;
   - stale-context/drift control.

3. **Release / Deployment Engineering**
   - version/release units;
   - reproducible-enough builds;
   - artifact identity/provenance/signing/attestations;
   - CI/CD and credential boundaries;
   - staged promotion/canary/track handling;
   - runtime verification;
   - rollback and migration safety.

## Wave 2 — active

4. **Data / Spreadsheet / Operational Workflow Engineering**
   - schema inference and data contracts;
   - reconciliation, duplicate/anomaly handling;
   - staging -> review -> production promotion;
   - formulas, deterministic transforms, audit trails;
   - spreadsheet/database interoperability and provenance.

5. **Writing / Editorial Engineering**
   - audience/intent fidelity;
   - fact/expression separation;
   - structural editing and compression/expansion;
   - voice and terminology consistency;
   - multilingual fidelity/localization;
   - publication QA and optional editorial lint.

6. **Visual Direction / Image Production**
   - canonical identity/trait locks;
   - per-dimension reference hierarchy;
   - shot/set planning and composition;
   - style/character continuity;
   - targeted edits;
   - drift detection and rendered visual QA.

7. **Decision / Planning Intelligence v2 — merged into Decision Design**
   - uncertainty and option value;
   - reversible vs irreversible decisions;
   - dependency/critical-path thinking;
   - commit/continue/stop/revisit thresholds;
   - bounded premortems;
   - decision records and post-decision learning.

8. **Knowledge / Memory Architecture**
   - memory vs active context separation;
   - episodic vs durable project vs user-global state;
   - canonical ownership and scope isolation;
   - provenance, freshness, contradiction resolution;
   - retrieval and compaction;
   - poisoning resistance, retention, deletion, and governance.

## Campaign status

All eight planned areas are active as of DEDAL Core v0.17.0. This closes the initial capability-expansion build campaign.

The next phase is **consolidation and outcome validation**:
- exercise skills naturally on real work;
- capture regressions and overlap;
- merge/remove rules that add ceremony without measured value;
- strengthen runtime enforcement where prose contracts are insufficient;
- evaluate context/memory quality across real multi-session workflows;
- avoid expanding skill count merely because another public pattern exists.

## Promotion rule

For any future capability area:
`gap -> current evidence/corpus -> boundary with existing skills -> DEDAL-native synthesis -> contract/eval -> real-task outcome evidence -> promote/merge/revise/reject`

Prefer improving an existing skill when the domain is not independently routable. Avoid skill multiplication for prestige or ecosystem fashion.
