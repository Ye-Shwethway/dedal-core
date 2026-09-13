# Debugging Loop

Use for hard bugs, regressions, flaky behavior, and performance failures.

## Core rule

Prefer a **tight, red-capable feedback loop** before committing to a theory. The loop should exercise the user's actual symptom and be as deterministic, fast, and repeatable as the environment allows.

Possible loops include a failing test, CLI/HTTP repro, fixture replay, headless UI script, differential old-vs-new run, property/fuzz loop, or automated bisection.

## Workflow

1. **Define the symptom** precisely. Redact secrets from logs/artifacts.
2. **Build or identify the feedback loop.** Run it at least once when execution is available.
3. **Reproduce and minimize.** Remove nonessential inputs/steps while preserving the failure.
4. **Rank falsifiable hypotheses.** Prefer a small set whose predictions can distinguish causes.
5. **Probe one variable at a time.** Instrument boundaries that discriminate hypotheses; avoid noisy log-everything debugging.
6. **Fix the root cause.** Turn the minimized repro into a regression test when a meaningful seam exists.
7. **Re-run the original scenario.** A narrow regression test alone is not enough if the real path can still fail.
8. **Clean up.** Remove temporary instrumentation/harnesses and record the actual cause at a durable checkpoint when useful.

## When reproduction is unavailable

Do not fabricate certainty or stall unnecessarily. State what cannot be reproduced, inspect the strongest available evidence, prefer reversible diagnostic changes, and identify what observation would confirm/refute the leading hypotheses.

## Performance branch

Measure before changing code. Establish a baseline and compare after each meaningful change. Prefer profilers, query plans, timings, or controlled differential runs over speculative logging.
