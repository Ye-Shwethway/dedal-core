# Visual Verification

Visual completion requires rendered evidence when the available tools and project make rendering practical.

## Bounded pass

1. Build/run the strongest available target.
2. Inspect the relevant device classes or viewport widths in one batched pass when possible.
3. Check the requested path plus material states: loading/error/empty/focus/hover/touch as applicable.
4. Record concrete defects rather than vague impressions.
5. Fix the material defects in one coherent batch.
6. Re-check once to confirm the fixes.

A second iterative polish loop is not automatic. Continue only when the confirmation pass reveals a new material defect or the Creator requests another refinement.

## Evidence hierarchy

Prefer, as available:
- rendered browser/app observation;
- screenshots or visual-regression captures tied to the current build;
- accessibility/runtime diagnostics;
- exact code/diff inspection when rendering is unavailable.

Never report visual verification if only source code was inspected.

## Comparison discipline

For redesigns, compare against the intended new direction and product requirements, not merely the old screenshot. For refinements, compare against incumbent identity and scope so improvement does not silently become redesign.

## Durable direction

If a finished implementation establishes reusable visual rules, propose recording the resulting tokens/components/direction in the owning project. Derive durable documentation from what actually shipped, not from abandoned mock intentions.
