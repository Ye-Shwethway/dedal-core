---
name: quality-engineering
description: Independently evaluate whether software behavior is trustworthy through acceptance criteria, risk-based test design, exploratory and automated verification, regression analysis, defect evidence, and readiness verdicts. Use when the task is about proving quality rather than implementing the product or shipping it.
---

# Quality Engineering

Own the question: **what evidence is needed to trust this product behavior?**

Quality Engineering is an independent verification faculty. It does not replace implementation, interface design, security review, or release engineering.

## Workflow

1. **Define acceptance truth** — recover the user goal, explicit requirements, incumbent behavior, platform constraints, and known risks. Convert ambiguity into testable expectations without inventing product requirements.
2. **Model risk** — prioritize critical user journeys, failure impact, changed surfaces, data/state transitions, boundary conditions, and regression exposure. Do not test everything equally.
3. **Choose evidence layers** — use the cheapest layer that can prove the claim: static/contract, unit/component, integration/API, UI/E2E, visual, accessibility, exploratory, or production-like smoke evidence.
4. **Design strong oracles** — assert user-visible outcomes, stable contracts, data/state invariants, or externally observable effects. Avoid implementation-detail assertions that can pass while the product is broken.
5. **Execute independently** — inspect existing tests first, then run or author the smallest useful verification set. Keep tests isolated and reproducible where practical; separate environment failure, test failure, and product defect.
6. **Investigate failures** — reproduce, minimize, classify severity/scope, capture bounded evidence, and distinguish deterministic defect from flake, stale expectation, test bug, or environment issue.
7. **Assess regression and readiness** — report covered claims, uncovered risks, known defects, confidence limits, and a readiness verdict appropriate to the requested decision.
8. **Preserve durable QA evidence** — when valuable, record regression tests, acceptance artifacts, failure evidence, or repeatable checks in the owning project.

## Core rules

- Test behavior users or dependent systems can actually observe whenever possible.
- Prefer risk-weighted coverage over raw test count or coverage percentage.
- A passing test only proves its oracle and environment, not general correctness.
- A flaky test is a reliability defect in the verification system; do not normalize repeated reruns as proof.
- Automated accessibility checks are useful but do not substitute for manual/inclusive accessibility assessment when that claim matters.
- Visual diffs need stable baselines and explicit tolerances; pixel change alone is not automatically a defect.
- Exploratory and agentic testing must still use explicit goals, bounded scope, and a success/failure oracle.
- Keep screenshots, traces, videos, logs, and dumps bounded and privacy-safe; capture failure evidence rather than indiscriminate telemetry.
- Do not claim readiness when critical paths are unverified or material defects remain unexplained.

## Pairing boundaries

- `software-development` implements/fixes code and owns developer-facing test seams during implementation.
- `interface-design` owns UX/UI direction and design-quality decisions; Quality Engineering verifies resulting behavior/accessibility/visual acceptance when requested.
- `release-engineering` owns artifact provenance, deployment, rollout, and rollback; Quality Engineering supplies readiness evidence, not promotion authority.
- `security-engineering` owns threat/adversarial security reasoning; Quality Engineering may execute agreed security checks but does not redefine security policy.
- Browser/computer/Playwright/mobile/API tools are execution surfaces, not QA ownership.

## Progressive references

- `references/test-strategy-and-oracles.md` — risk modeling, test layers, acceptance criteria, oracles, isolation, and regression design.
- `references/execution-evidence-and-readiness.md` — exploratory/E2E execution, failure evidence, flake handling, accessibility/visual checks, and readiness verdicts.

Load tool/framework-specific guidance only when that execution surface is actually used.
