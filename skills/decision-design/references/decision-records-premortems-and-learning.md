# Decision Records, Premortems, and Learning

## Bounded premortem

For high-impact or fragile plans, assume the plan has failed and ask for a small number of plausible failure causes.

For each material cause, record:
- mechanism: how failure would happen;
- early signal: what would appear before full failure;
- mitigation: prevention or containment;
- owner/authority if coordination matters.

Use premortems to surface hidden concerns, not to produce exhaustive disaster catalogs.

## Lightweight decision record

Persist only durable decisions worth future context.

Recommended fields:
- decision / status;
- context and objective;
- serious alternatives considered;
- rationale / tradeoffs;
- reversibility class;
- confidence / material uncertainty at decision time;
- consequences;
- reevaluation trigger;
- evidence links where relevant.

Prefer short records. If a decision is later changed, supersede/link rather than rewriting the original rationale as if the earlier state never existed.

## Review decision quality separately from outcome

A good decision can have a bad outcome because of uncertainty; a poor decision can get lucky.

When reviewing:
1. reconstruct what was known and unknown at the time;
2. compare assumptions with what later happened;
3. identify surprises or missed signals;
4. distinguish process defects from unavoidable uncertainty;
5. capture one or two reusable changes if they matter.

Avoid hindsight bias: do not score the old decision using information that became available only afterward.

## Learning loop

`record -> execute -> observe -> compare with assumptions -> update rule/context if durable`

Do not create a new universal rule from one noisy outcome. Promote lessons when they recur, have strong causal evidence, or address a high-severity failure mode.