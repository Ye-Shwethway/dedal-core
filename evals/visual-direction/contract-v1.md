# Visual Direction Contract v1

## Required behaviors

### VD-01 Reference authority
Given multiple references with different roles, the workflow identifies which reference controls identity, body/shape, grooming, wardrobe/props, composition, style, and environment as needed. It does not silently average conflicting references.

### VD-02 Canonical locks
Recurring subjects have explicit invariant traits and allowed variation. A new output does not become canonical merely because it is newer or prettier.

### VD-03 Shot/set planning
Multi-image work defines shared series constraints and shot-level variation before generation. Individual-image deliverables are not collapsed into a split-screen/contact sheet unless requested.

### VD-04 Edit locality
For a local defect in an otherwise accepted image, targeted edit/correction is preferred over unnecessary full regeneration when the tool supports it.

### VD-05 Rendered visual verification
The actual image output is inspected before any claim that identity, composition, text, anatomy, or style requirements are satisfied.

### VD-06 Drift taxonomy
Failures are classified at least as identity, age/grooming, anatomy/proportion, pose/action, wardrobe/prop, composition/camera, environment, style/grade, text/detail, or edit-spillover when applicable.

### VD-07 Bounded iteration
A correction pass is driven by an observed defect, explicit Creator request, or exploratory goal. Endless prompt accumulation without new evidence is a regression.

### VD-08 Acceptance authority
Automated similarity/reward metrics are advisory only. Canonical acceptance requires human/Creator judgement or an explicit project acceptance rule.

## Regression failures
- style reference silently changes subject identity;
- rejected/experimental image becomes a canonical anchor;
- prompt-only inspection is reported as visual verification;
- unrelated accepted content changes during a local edit without being surfaced;
- recurring identity drift is treated only as a prompt-length problem;
- output series changes age/body/grooming/era unintentionally;
- automated score overrides obvious visual mismatch;
- reference roles are unclear and the system pretends they are not.

## Evaluation posture
Contract validation proves the workflow is encoded. Real-task outcome validation requires representative generation/edit sessions with actual outputs and Creator acceptance signals.