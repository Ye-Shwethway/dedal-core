# Quality Engineering Deep Audit — 2026-09-14

## Capability gap

DEDAL already has Software Development (implementation/debug/test), Interface Design (UX/UI direction), Release Engineering (artifact/deploy lifecycle), Security Engineering, and Automations. The uncovered concern is **independent product-quality verification**: acceptance truth, risk-based coverage, exploratory/E2E/regression strategy, failure evidence, and readiness verdicts.

## Sources reviewed

### First-party / authoritative
- Playwright current documentation: best practices, locators, auto-waiting, assertions, and accessibility testing. Reviewed 2026-09-14.
- Key durable patterns: test user-visible behavior; isolate tests; prefer user-facing locators; use auto-waiting/web-first assertions; automated accessibility scans are partial evidence, not complete accessibility proof.

### Community corpora used for pattern extraction
- `DwonnG/qa-agent-skills@c5dcf11d22bd40a55d4f7c30baa2f272b4dcf576` (MIT): test planning, test generation, merge/readiness guardrails, post-deploy comparison patterns.
- `petrkindlmann/qa-skills@b3bb61bd268b147476252c6ed5a0440c87b97441` (MIT): exploratory testing, agentic browser testing, reliability, explicit oracles, deterministic execution, and graduation of stable agentic flows into scripted tests.
- Additional community QA/Playwright repositories were sampled for corroboration only; no runtime or third-party scripts were installed.

## Adapt

1. **Independent verification ownership.** The implementer skill may write tests, but Quality Engineering owns the independent question of what evidence is sufficient to trust behavior.
2. **Acceptance before automation.** Recover explicit requirements and incumbent behavior, then convert them into observable claims before choosing tools.
3. **Risk-weighted coverage.** Prioritize critical journeys, state transitions, changed surfaces, irreversible effects, boundary inputs, and regression-prone areas instead of maximizing test count.
4. **Evidence layers.** Choose static/unit/component/integration/API/UI/visual/accessibility/exploratory evidence according to the claim; use the cheapest layer that proves it.
5. **Strong oracles.** Prefer user-visible/public-contract outcomes over implementation details.
6. **Failure classification.** Separate product defect, stale expectation, test defect, environment failure, flake, and insufficient evidence.
7. **Flake honesty.** Reruns are diagnostic, not proof; unresolved non-determinism remains a quality risk.
8. **Bounded evidence.** Failure traces/screenshots/logs are captured when useful and kept privacy-safe.
9. **Readiness verdicts.** READY / READY WITH KNOWN RISK / NOT READY / INCONCLUSIVE must expose scope, evidence, and residual risk.
10. **Execution surfaces remain separate.** Playwright, browser/computer use, mobile tooling, API clients, and accessibility scanners are tools/references rather than the faculty identity.

## Reject

- A Playwright-only top-level skill as the definition of QA.
- Test-count or code-coverage percentage as the primary quality objective.
- Blind retries until green.
- Pixel diffs without semantic interpretation.
- Automated accessibility scans presented as full accessibility certification.
- QA owning product requirements, code implementation, release promotion, or security policy.
- Heavy QA ceremony for trivial low-risk changes where targeted implementation tests already provide sufficient evidence.

## Ownership boundary

- **Software Development:** build/fix/refactor code; developer-facing test seams and targeted verification during implementation.
- **Quality Engineering:** acceptance truth, independent verification plan, exploratory/regression/E2E evidence, defect characterization, readiness recommendation.
- **Interface Design:** design direction and UX decisions; QA verifies behavior/visual/accessibility acceptance when requested.
- **Release Engineering:** source-to-artifact/deploy/rollback; consumes readiness evidence but owns promotion mechanics.
- **Security Engineering:** threat model and security policy; QA can execute agreed checks but does not redefine the security boundary.

## Promotion decision

**PROMOTE to active top-level faculty.** The capability is independently routable, recurring across DEDAL software projects, meaningfully distinct from implementation and release ownership, and supports the v0.19 cognitive-composition model without requiring a new runtime dependency.

Evidence boundary: this audit and routing contracts establish design/contract justification. Real-task outcome improvement remains to be observed on representative DEDAL projects.
