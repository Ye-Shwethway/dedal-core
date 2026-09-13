# Agentic Loops

## Core loop

A minimal agent loop is:

`observe state -> model chooses next action -> deterministic execution -> append result -> repeat or exit`

The harness must own loop state and termination. Do not leave “keep going until done” as the only control mechanism for consequential work.

## Exit contract

Define exits that fit the workflow:
- verified success / final structured output;
- no further tool action required;
- explicit blocked / unsupported state;
- retry budget exhausted;
- repeated non-progress;
- authority boundary reached;
- human escalation required;
- cost/time/turn budget reached.

## Feedback-driven refinement

Iterative refinement is useful when a later pass receives information capable of changing the result. Useful signals include:
- tests or compiler/runtime output;
- environment/tool feedback;
- validator/schema failure;
- external evaluator or rubric;
- source/evidence contradiction;
- explicit Creator feedback.

Patterns such as Self-Refine and Reflexion show that linguistic feedback can improve subsequent attempts, but DEDAL does not assume reflection is inherently corrective.

## Reflection rule

Use critique/reflection only when:
1. the task is important enough to justify another pass;
2. there is a concrete criterion or new signal;
3. the next attempt can take a meaningfully different action.

Stop when critique becomes repetitive, speculative, or unsupported by new evidence.

## Retry discipline

Classify failures before retrying:
- transient/runtime -> bounded retry may help;
- invalid input/schema -> change the call;
- wrong strategy -> re-plan with failure evidence;
- missing authority/data -> escalate or retrieve;
- capability absence -> stop truthfully.

Never spin on an unchanged failing action.

## Checkpoints

For long loops, externalize compact state at meaningful boundaries: current objective, completed evidence, accepted decisions, failures, remaining tasks, and next action. A checkpoint should let a fresh session continue without replaying the entire trajectory.
