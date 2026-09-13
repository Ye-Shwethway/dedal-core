# Decision / Planning Intelligence v2 Capability Audit — 2026-09-14

## Gap

DEDAL Decision Design v1 already handled process sizing and dependency-aware decision frontiers, but it did not explicitly govern reversibility, uncertainty, option value, commit/stop thresholds, premortems, or post-decision learning.

## Evidence reviewed

- Amazon 2015 shareholder letter: distinguishes consequential one-way-door decisions from reversible two-way-door decisions; warns against applying heavyweight process to reversible choices.
- NASA Decision Analysis and Risk-Informed Decision Making guidance: objectives, alternatives, uncertainty/risk analysis, deliberation, selection, and continuous risk management.
- Gary Klein, HBR 2007, "Performing a Project Premortem": prospective failure analysis to surface concerns before execution.
- Martin Fowler, 2026 Architecture Decision Record guidance: short records containing context, decision, alternatives, consequences, confidence, and reevaluation triggers.
- Atlassian decision review guidance: review how decisions were made and guard against hindsight bias.
- Existing `mattpocock/skills` source @ `3cca18b368ae95cdbdebbff572ccafa662551015`, MIT, remains the original adaptation source for dependency/frontier mechanics.

## Synthesis

Upgrade existing `decision-design`; do not create a duplicate top-level planning skill.

New durable model:
`decision weight = reversibility/downside/uncertainty/blast radius`

Operational loop:
`frame -> classify facts/assumptions/values/constraints -> weight decision -> map dependencies -> reduce high-value uncertainty -> compare alternatives -> commit/experiment/defer/stop -> record/review when durable`

## Adapt

- one-way vs two-way door heuristic;
- NASA-style objectives/alternatives/uncertainty/risk-aware selection;
- option-preserving bounded experiments;
- explicit commit/continue/stop/revisit thresholds;
- bounded premortem for consequential fragile plans;
- concise decision records with confidence and reevaluation triggers;
- post-decision review that separates process quality from outcome luck.

## Reject / constrain

- fake numerical precision without evidence;
- heavyweight decision matrices for routine reversible work;
- premortem ritual for every task;
- endless research toward impossible certainty;
- outcome-only retrospectives;
- skill multiplication where an existing independently routable skill already owns the domain.

## Security / execution

No external package, script, or executable was installed or run for this adaptation. Public sources were inspected as evidence only.