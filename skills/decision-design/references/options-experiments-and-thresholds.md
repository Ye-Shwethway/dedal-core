# Options, Experiments, and Commit Thresholds

## Preserve options deliberately

Under meaningful uncertainty, prefer actions that create information while preserving future choices when their cost is reasonable.

An option-preserving step is useful when it:
- is materially cheaper/safer than full commitment;
- tests a decision-relevant assumption;
- does not create hidden lock-in larger than the uncertainty it resolves;
- has a clear observation point and exit.

Examples include prototypes, spikes, staged rollout, sandbox trials, temporary adapters, reversible configuration, and small representative tests.

## Experiment contract

Before running a decision experiment, state:
1. uncertainty being tested;
2. candidate action;
3. bounded cost/time/resources;
4. observable evidence;
5. what outcome favors which decision;
6. stop condition;
7. what remains untested.

Do not call implementation work an experiment if there is no explicit learning question.

## Critical decision path

Separate the full dependency tree from the few upstream decisions/unknowns that actually block progress.

Prefer resolving blockers in order of:
- downstream dependency count;
- consequence if wrong;
- uncertainty;
- cheapness of evidence;
- time criticality.

Do not spend cycles polishing downstream options while a parent assumption is unresolved.

## Commit / continue / stop / revisit

### Commit
Commit when the preferred option satisfies required constraints and remaining uncertainty is acceptable relative to reversibility/downside.

### Continue exploring
Continue only when the next evidence has plausible decision value greater than its cost/delay.

### Stop
Stop analysis when:
- the same option remains preferred across plausible uncertainty ranges;
- next evidence is unlikely to change action;
- delay cost exceeds expected information value;
- the Creator accepts the known residual risk.

### Revisit
A deferred or accepted decision should name a trigger where practical, such as:
- scale/users exceed a threshold;
- observed error/failure rate changes;
- a dependency/API/policy changes;
- cost or latency exceeds a bound;
- new evidence contradicts a key assumption;
- a planned date/release milestone arrives.

Avoid vague "revisit later" notes with no trigger.