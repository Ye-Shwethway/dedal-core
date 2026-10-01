# Visual Narrative Production outcome evaluation v1

## Purpose

Measure whether the workflow reduces Creator rework across scene types. The string-presence contract validator proves only that instructions exist. It does not prove an agent activates them or that the pixels improve.

## Comparison setup

- Compare the previous skill version and candidate skill on the same scene briefs, character/place references, image tool, model/surface, number of allowed calls, and delivery destination. Run versions in independent contexts when possible; do not leak diagnoses or expected fixes into the candidate prompt.
- Include three or more distinct scene classes: one recurring character moving through a space; one person interacting with an object under load/contact; one performance/recovery or emotional-state transition. Add a two-character spatial scene before generalizing beyond single-character work.
- Example held-out briefs (replace with equivalent private cases when available): a technician crosses a workshop toward a workbench from a side camera; a worker pulls a heavy crate onto a shelf with visible hand contact; a runner cools down after a hard interval while retaining composed athletic posture; two people pass a folder across a table without swapping screen positions. Define their actual references and shot counts before either run.
- Freeze shot count and acceptance rubric before generation. Keep the Creator's visual judgment separate from deterministic delivery/plan checks.

## Evidence per run

Record scene card and reference roles; actual pixel inputs and supported controls; generated candidate count; each rendered image; per-image QA finding; corrections and reason; accepted shots/roles; individual asset links and destination read-back. Keep private character assets outside public Core.

## Measures

1. **First-pass usable rate:** shots passing role, identity, continuity, and contact gates before Creator correction / planned shots.
2. **Escaped material defects:** objectively detectable failures shown to Creator as choices / delivered choices. Target zero; record the actual count.
3. **Correction burden:** additional renders and Creator correction turns per accepted shot.
4. **Sequence coverage:** distinct beat information and plausible adjacent state transitions, judged with a fixed rubric.
5. **Reference and delivery integrity:** required pixel inputs actually bound; requested individual assets readable at the stated destination.

Classify QA as pass, usable-with-debt, or fail with a one-sentence pixel-grounded reason. Use human review for taste and character fidelity; do not replace it with an uncalibrated vision score. Report per-case results and variation, including failures. A static PASS or one accepted scene is not a demonstrated lower-model or general performance gain.
