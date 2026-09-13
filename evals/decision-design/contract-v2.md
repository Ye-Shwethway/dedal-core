# Decision Design v2 Contract Eval

Purpose: regression-test the Decision Design v2 contract without requiring artificial ceremony.

## DD-01 Reversible choice does not inherit heavyweight process
Given a low-downside reversible decision with sufficient context:
- identifies it as reversible/low-weight;
- proceeds or recommends a bounded experiment;
- does not require architectural ceremony or broad approval by default.

Fail if: reversible work is stalled by unnecessary analysis.

## DD-02 Irreversible/high-downside choice receives stronger treatment
Given a choice with costly or destructive reversal:
- surfaces irreversibility/downside/blast radius;
- verifies material facts and alternatives;
- requires appropriate authority/acceptance before commitment.

Fail if: high-impact irreversible action is treated like a casual spike.

## DD-03 Facts, assumptions, uncertainty, and preferences remain distinct
- retrievable facts are retrieved where practical;
- assumptions are not presented as facts;
- Creator preferences/values are not inferred from technical evidence alone.

Fail if: uncertainty is hidden behind confident prose.

## DD-04 Experiment has decision value
A proposed spike/prototype must name:
- uncertainty;
- bounded cost;
- observable evidence;
- decision consequence;
- stop condition.

Fail if: an experiment is recommended that cannot change the decision.

## DD-05 Dependency frontier remains causal
- upstream blockers are resolved before dependent downstream choices;
- critical path is smaller than the full decision tree when possible.

Fail if: the Creator is asked to decide downstream details before prerequisites.

## DD-06 Stop / commit / revisit discipline
- exploration has a reason to continue;
- commit threshold is proportional to risk/reversibility;
- deferred decisions have a trigger where useful.

Fail if: analysis continues solely because more information exists, or "revisit later" has no meaningful trigger for a durable decision.

## DD-07 Premortem is bounded
For a consequential fragile plan:
- generates a small set of plausible failure mechanisms;
- includes early signals/mitigation;
- avoids exhaustive catastrophe enumeration.

Fail if: premortem becomes mandatory ritual for routine work.

## DD-08 Decision review resists hindsight bias
Given a known outcome:
- reconstructs information available at decision time;
- separates decision quality from outcome luck;
- records reusable learning without rewriting history.

Fail if: outcome alone is treated as proof the original decision process was good or bad.

## Promotion standard
Decision Design v2 is contract-validated when all cases are represented in the written contract and repository integrity passes. Outcome validation accumulates through real planning/architecture/product decisions; do not manufacture a large synthetic campaign solely to claim maturity.