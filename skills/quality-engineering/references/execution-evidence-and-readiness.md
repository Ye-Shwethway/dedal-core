# Execution Evidence and Readiness

## Exploratory and automated execution

Use deterministic scripted checks when the behavior and oracle are stable. Use exploratory or agentic checks when the purpose is to discover unknown interaction failures or when the interface is changing quickly. Agentic exploration still needs a bounded goal, seeded/controlled state where practical, step limits, and an explicit success/failure oracle.

For browser E2E work, inspect existing config and test conventions first. Prefer user-facing locators, isolated contexts, web-first assertions, and boundary mocking that does not mock the behavior under test.

## Failure evidence

When a check fails, classify before fixing:

- product defect;
- stale/wrong expectation;
- test implementation defect;
- environmental/infrastructure failure;
- flaky/non-deterministic behavior;
- insufficient evidence.

Capture the smallest useful evidence: failing assertion, reproduction steps, relevant logs, screenshot/trace/video when diagnostic, environment/version identity, and affected behavior. Avoid full dumps or secret-bearing artifacts when a smaller excerpt proves the issue.

## Flake policy

A rerun may diagnose non-determinism but does not erase the first failure. Record whether the failure is reproducible, environment-specific, race/timing-sensitive, or unresolved. Quarantine only with explicit ownership and follow-up; never turn repeated reruns into a readiness signal.

## Visual verification

Use stable viewport/device, deterministic data, controlled fonts/assets where practical, and an intentional baseline. Distinguish expected intentional design changes from unexplained regressions. Pixel diffs need human/product interpretation when semantics are unclear.

## Accessibility verification

Automated scans can catch machine-detectable issues, but passing axe/ARIA checks does not prove full accessibility. When the claim matters, include keyboard/focus behavior, semantics, text alternatives, contrast, zoom/responsiveness, and manual/inclusive assessment appropriate to scope.

## Readiness verdict

Use a concise verdict such as:

- **READY** — requested critical claims verified; no material unexplained defects in scope.
- **READY WITH KNOWN RISK** — evidence is adequate for the decision, with explicit bounded residual risks.
- **NOT READY** — critical defect, missing critical evidence, or unresolved flake blocks confidence.
- **INCONCLUSIVE** — environment/tooling/evidence cannot support a trustworthy verdict.

A verdict must state what was tested, what was not, exact defects/risks, and the evidence basis. Quality Engineering recommends readiness; Release Engineering or the Creator owns promotion decisions.
