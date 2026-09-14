# Test Strategy and Oracles

## Start from claims, not test types

Translate the requested product behavior into observable claims. For each claim record the risk if wrong, the cheapest trustworthy evidence layer, and what would count as failure.

Use layers deliberately:

- static/contract checks for schemas, invariants, and build-time rules;
- unit/component checks for isolated logic and stable seams;
- integration/API checks for boundaries between components/services;
- UI/E2E checks for critical user-visible workflows;
- visual/accessibility checks for presentation and inclusive interaction claims;
- exploratory testing for unknown failure modes and interaction sequences.

Do not duplicate the same weak assertion across many layers.

## Risk-weighted coverage

Prioritize:

1. critical user journeys and irreversible/data-loss paths;
2. changed code and adjacent regression surfaces;
3. state transitions, retries, concurrency, persistence, and boundary inputs;
4. platform/device/browser differences that materially affect behavior;
5. historically flaky or failure-prone areas.

Coverage percentage and test count are secondary signals. They do not prove important behavior is covered.

## Strong oracles

Prefer assertions on:

- user-visible state;
- public API response and side effects;
- durable data/state invariants;
- explicit contracts and acceptance criteria;
- stable accessibility semantics;
- source-to-artifact/runtime identity when the quality claim depends on the exact build.

Avoid CSS/XPath/layout structure, private implementation details, internal call counts, or transient timing as the primary oracle unless the requirement itself is about those details.

## Isolation and repeatability

Tests should not silently depend on order, shared mutable state, stale sessions, uncontrolled clocks, or external services when a bounded substitute is practical. When an external dependency is material to the claim, test it explicitly rather than mocking away what must be proven.

For UI automation, prefer user-facing locators and auto-waiting/web-first assertions. Stable test IDs are acceptable when they represent an explicit testing contract.

## Regression design

For a confirmed defect:

1. preserve the smallest reproduction;
2. identify the owning behavior contract;
3. add the cheapest durable regression seam that would have failed before the fix;
4. avoid overfitting the test to the implementation of the fix;
5. keep the original failure evidence linked when useful.
