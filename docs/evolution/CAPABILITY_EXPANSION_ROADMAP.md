# Capability Expansion Roadmap

_Date established: 2026-09-14_

This roadmap records the next eight high-value generic capability areas for DEDAL Core. Order reflects expected cross-project value, risk reduction, and current gaps. It is a plan, not a promise that every area must become a separate top-level skill; later evidence may justify merge/adapt/reject decisions.

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

## Wave 2

4. **Data / Spreadsheet / Operational Workflow Engineering — active**
   - schema inference and data contracts;
   - reconciliation, duplicate/anomaly handling;
   - staging -> review -> production promotion;
   - formulas, deterministic transforms, audit trails;
   - spreadsheet/database interoperability and provenance.

5. **Writing / Editorial Engineering — active**
   - audience/intent fidelity;
   - fact/expression separation;
   - structural editing and compression/expansion;
   - voice and terminology consistency;
   - multilingual fidelity/localization;
   - publication QA and optional editorial lint.

6. **Visual Direction / Image Production — active**
   - canonical identity/trait locks;
   - per-dimension reference hierarchy;
   - shot/set planning and composition;
   - style/character continuity;
   - targeted edits;
   - drift detection and rendered visual QA.

7. **Decision / Planning Intelligence v2 — active (merged into Decision Design)**
   - uncertainty and option value;
   - reversible vs irreversible decisions;
   - dependency/critical-path thinking;
   - commit/continue/stop/revisit thresholds;
   - bounded premortems;
   - decision records and post-decision learning.

8. **Knowledge / Memory Architecture — planned next**
   - episodic vs durable state;
   - provenance and contradiction resolution;
   - freshness/staleness;
   - project-local vs global knowledge;
   - retrieval/compaction;
   - poisoning resistance and memory governance.

## Promotion rule

For every area:
`gap -> current evidence/corpus -> boundary with existing skills -> DEDAL-native synthesis -> contract/eval -> real-task outcome evidence -> promote/merge/revise/reject`

Prefer improving an existing skill when the domain is not independently routable. Avoid skill multiplication for prestige or ecosystem fashion.