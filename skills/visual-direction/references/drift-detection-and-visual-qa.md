# Drift Detection and Visual QA

## Drift taxonomy
Review failures by class rather than saying only “looks wrong”:
- identity/facial drift;
- age/grooming drift;
- anatomy/proportion drift;
- pose/action mismatch;
- wardrobe/prop drift;
- composition/camera drift;
- environment continuity drift;
- style/medium/grade drift;
- text/logo/detail corruption;
- edit spillover: unrelated content changed.

## Visual QA pass
1. Inspect the rendered output itself.
2. Compare against the authoritative reference(s) for each relevant dimension.
3. Mark invariant violations before aesthetic polish.
4. Check composition and requested action.
5. Check anatomy, object relationships, text/details, and obvious generation artifacts.
6. Check series continuity when applicable.
7. Decide: accept, accept-with-note, targeted revise, or reject/regenerate.

## Revision discipline
Use the narrowest corrective instruction that addresses the defect. Preserve accepted aspects explicitly. If a correction repeatedly causes a new regression elsewhere, reconsider the reference/control strategy rather than endlessly adding prompt clauses.

## Bounded iteration
Normally use one generation, one structured visual review, one coherent correction pass, and one focused re-check. Continue when a material defect remains, the Creator requests alternatives, or the task is explicitly exploratory.

## Metrics
Automated perceptual/similarity/reward scores can help compare large batches, but they are proxies. They can miss identity subtleties, story intent, anatomy defects, or aesthetic mismatch. Treat them as triage evidence, never canonical acceptance authority.

## Acceptance record
For recurring subjects/series, record:
- accepted output identifier;
- which reference roles it satisfies;
- newly approved durable traits/direction, if any;
- known tolerated deviations;
- whether it supersedes or merely supplements earlier anchors.