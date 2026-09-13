# Adaptation Notes

`decision-design` is a DEDAL-native decision/planning skill. v1 was influenced by Matt Pocock's public `grilling` / `grill-me` skill pattern; v2 keeps that dependency-frontier model and adds risk/uncertainty/reversibility/learning discipline.

## Source lineage

Original source repository: `mattpocock/skills`
Inspected source commit/tree: `3cca18b368ae95cdbdebbff572ccafa662551015`
Source license: MIT (Copyright 2026 Matt Pocock)
Adapted: 2026-09-14

Additional v2 evidence reviewed:
- Amazon 2015 shareholder letter: one-way vs two-way door decisions; reversible decisions should not inherit heavyweight irreversible-decision process.
- NASA Decision Analysis / Risk-Informed Decision Making guidance: objectives, alternatives, uncertainty/risk analysis, deliberation, and selection.
- Gary Klein, "Performing a Project Premortem" (HBR, 2007): prospective failure analysis for consequential plans.
- Martin Fowler, "Architecture Decision Record" (2026): short durable records with context, rationale, consequences, confidence, and reevaluation triggers.
- Atlassian decision-review guidance: review decision process and avoid hindsight-only judgment.

## Retained from v1

- process sizing (Spike / Bounded / Architectural);
- dependency-aware decision tree/frontier;
- separating retrievable facts from owner decisions;
- iterative rounds;
- anti-ceremony for routine, sufficiently specified work.

## Added in v2

- reversibility / downside / uncertainty / blast-radius weighting;
- explicit facts vs assumptions vs uncertainties vs values vs constraints;
- critical decision path;
- option-preserving experiments with decision-linked stop conditions;
- commit / continue / stop / revisit thresholds;
- bounded premortem for high-impact plans;
- confidence and reevaluation triggers in durable decision records;
- post-decision learning that distinguishes decision quality from outcome luck.

## Rejected as universal doctrine

- numeric scoring when precision is not evidence-backed;
- premortems for every routine task;
- heavyweight consensus for reversible decisions;
- endless research in pursuit of certainty;
- outcome-only judgments that rewrite what was knowable at decision time.

This package is a rewritten DEDAL contract, not a verbatim copy of any source.