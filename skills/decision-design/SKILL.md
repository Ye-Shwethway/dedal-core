---
name: decision-design
description: Stress-test plans, architectures, product decisions, and high-impact choices using process sizing, dependency frontiers, reversibility, uncertainty, option value, commit/stop thresholds, and decision learning. Use deliberately, not for routine fully specified work.
---

# Decision Design v2

Use when the Creator wants a plan or idea challenged before action, or when a material decision has unresolved branches, meaningful uncertainty, or costly consequences.

## 1. Size the process

Use the lightest process that safely fits the work:
- **Spike** — resolve one important unknown cheaply; default output is evidence/recommendation, not production commitment.
- **Bounded** — well-scoped change to an existing flow; inspect context, resolve material uncertainty, proceed without ceremony.
- **Architectural** — new subsystem/project/shared-interface or high-impact direction; map dependencies, alternatives, risks, and durable consequences.

Upgrade the process when hidden complexity appears. Do not downgrade simply to avoid necessary reasoning.

## 2. Weight the decision

Process weight should rise with:
`irreversibility × downside × uncertainty × blast radius`

Classify the choice:
- **two-way / reversible** — cheap rollback or substitution exists; prefer fast decisions, bounded experiments, and preserved options;
- **partially reversible** — rollback exists but has migration, user, data, cost, or coordination friction;
- **one-way / effectively irreversible** — reversal is impossible or unacceptably costly; require stronger evidence, consultation, and explicit acceptance.

Do not use a heavy one-way-door process for every reversible choice. Do not treat a high-downside irreversible choice like a casual experiment.

## 3. Separate facts, uncertainties, and owner choices

Before asking the Creator for factual information that can be inspected from repositories, files, tools, or public research, retrieve it.

Distinguish:
- **known facts** — evidence-backed;
- **assumptions** — believed but not verified;
- **uncertainties** — materially outcome-sensitive unknowns;
- **preferences/values** — Creator authority;
- **constraints** — hard boundaries unless explicitly changed.

Ask the Creator only for decisions that genuinely express goals, risk tolerance, canon, product behavior, irreversible direction, or other owner authority.

## 4. Resolve the decision frontier

Model dependencies between decisions. A question belongs to the current **frontier** only when prerequisites are settled or can be verified now.

Do not ask downstream questions whose answers depend on unresolved upstream choices. Identify the critical decision path: the smallest set of upstream choices/unknowns blocking meaningful progress.

## 5. Preserve option value under uncertainty

When uncertainty is high and a cheap reversible experiment can materially reduce it, prefer the experiment over premature commitment.

A useful experiment has:
- a specific uncertainty it targets;
- a bounded cost/time/resource budget;
- an observable outcome;
- a decision it will change;
- a stop condition.

Do not run experiments that cannot affect the decision. Do not postpone commitment indefinitely merely because more information is theoretically possible.

## 6. Use explicit commit / stop / revisit thresholds

Before substantial exploration, define what would be enough to:
- **commit** — evidence/risk is sufficient to choose;
- **continue** — next evidence has positive expected decision value;
- **stop** — additional analysis is unlikely to change the choice enough to justify cost;
- **revisit later** — name the trigger: new evidence, scale threshold, failure mode, dependency change, or date/event.

Thresholds may be qualitative when numeric precision would be fake.

## 7. Stress-test high-impact plans

For consequential or fragile plans, use a bounded premortem: assume the plan failed and identify a small number of plausible causes, early warning signals, and mitigations.

Do not premortem routine work by default. Avoid exhaustive catastrophe lists.

## 8. Work in rounds

For substantial design sessions:
1. Frame objectives, constraints, authority, and decision weight.
2. Map unresolved branches and critical dependencies.
3. Resolve retrievable facts and high-value uncertainties.
4. Compare viable alternatives against the same criteria.
5. Recommend the current best action and state confidence/remaining uncertainty.
6. Commit, experiment, defer with trigger, or stop.
7. Persist durable decisions when worthy.

## 9. Decision records and learning

For durable decisions, record only what future work needs:
- context/objective;
- decision and serious alternatives;
- rationale/tradeoffs;
- confidence/uncertainty at decision time;
- consequences;
- reevaluation trigger.

Do not rewrite history when the decision changes; supersede/link the old record where the project convention supports it.

Post-decision review should judge **decision quality using information available at the time**, not only outcome quality. Capture surprises, wrong assumptions, and process changes worth reusing without hindsight theater.

## Anti-ceremony rule

If the task is already sufficiently specified and reversible, act. Decision Design exists to reduce consequential uncertainty and coordination cost, not to turn normal work into an interview.

## Completion

Summarize settled decisions, meaningful rejected alternatives, remaining assumptions/risks, reversibility, next executable step, and any revisit trigger. Propose a durable spec/ADR/checkpoint update only when the decision is worth preserving.