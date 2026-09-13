# Security Verification

Security claims require evidence matched to the control.

## Verification ladder

Prefer, in order where applicable:
1. static/configuration assertions — permissions, schemas, secret absence, dependency pins;
2. isolated negative tests — forbidden action is rejected;
3. integration tests — authz/trust boundaries hold across tool/service calls;
4. adversarial tests — realistic malicious content attempts to steer privileged behavior;
5. runtime monitoring/audit evidence — sensitive actions are attributable and observable.

## Adversarial test design

Test the system's boundaries, not only model compliance. Include cases where malicious instructions appear in:
- fetched web content;
- repository docs/issues;
- tool results;
- persistent context/memory candidates;
- dependency metadata;
- messages from lower-authority principals.

Measure whether the system protects assets and authority, not merely whether the model labels an input as malicious.

## Residual-risk language

Use precise claims:
- `control present` — mechanism exists;
- `control verified for case X` — evidence observed;
- `risk reduced` — attack requires additional conditions;
- `not proven` — evidence is incomplete.

Do not say `secure`, `safe`, or `prompt-injection-proof` from one classifier, one test suite, or one successful red-team run.
