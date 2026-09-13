# Testing and Seams

Use when designing regression tests, integration tests, or test-first implementation.

## Test the behavior boundary

Prefer tests at a stable **seam**: a public or project-recognized interface where externally meaningful behavior can be observed without coupling to implementation details.

Good tests survive internal refactors when behavior is unchanged.

Avoid:
- private-method/internal-collaborator coupling unless the project explicitly treats that surface as contractual;
- tautological expected values derived by the same logic as the implementation;
- snapshots or mocks that can pass while user-visible behavior is wrong;
- inventing many new seams purely to make tests easy.

## Vertical slices

When TDD is appropriate, prefer one behavior at a time:

`red -> minimal green -> next behavior`

Do not write a large horizontal batch of imagined tests before implementation feedback exists. Use each passing slice to inform the next.

## Seam choice

Prefer an existing high-level seam that exercises the real behavior. Add a new seam only when it improves architecture for a genuine reason, not solely to satisfy a test harness.

If no correct seam can reproduce a bug, record that architectural limitation rather than adding a misleading shallow test.

## TDD is a mode, not a religion

Use red-before-green when the user requests TDD, when a regression can be cleanly captured, or when it materially reduces risk. For tiny mechanical changes or environments where execution is unavailable, use the strongest practical verification instead.
