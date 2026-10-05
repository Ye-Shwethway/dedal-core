# Core 0.39.0 refinement operations

The direct `/DEDAL/core` tree remains the boot authority. These additions improve deterministic verification and recovery without introducing an external Runtime or silently expanding tool permissions.

## Loading and readiness

Run `python scripts/context_plan.py --profile PROFILE_ID --phase execute` against a current materialized tree. It verifies full release integrity and returns only the selected profile's full-read paths, machine-verified dependencies, gates and observable bytes. Read every `read_full` instruction body completely. Machine verification checks large inventories and schemas; it is never evidence that the model read their full contents. Do not dump complete inventories merely to prove integrity.

Receipt v6 adds `read_class`: `boot`, `discovery`, `hydration`, or `reused`. Boot/discovery can precede semantic routing. Hydration must follow route review; reused current reads require a reason and activation timestamp after both the read and route. Receipts are task/release bound. Cross-chat caches are not implemented. Refresh volatile private state from its owner before a side effect.

Seven operation profiles cover Core, character sequences, Orison, stock changes, report exports, publishing writes and deployments. Lexical signals are candidates; Burmese paraphrases, quoted terms, negation and multiple operations still require semantic review. Resolve multi-profile work into sequential task-bound phase receipts and recompose at material subgoal changes. Never union unrelated preconditions blindly.

## Evidence

`evidence_mode: coverage` with a null bundle digest is explicitly a declaration. In `local_artifacts` mode pass `--evidence-bundle EVENTS.json --artifact-root ROOT`. The bundle binds task/release and contains one event for every source/gate reference. Source events bind path, complete artifact, byte count, observed metadata, full-read flag and SHA-256. Source verification proves matching local bytes; it cannot prove tool origin or the model's understanding.

Gate events use typed methods. The verifier reruns allowlisted pure commands for `validator_green`, inspects the recorded rollback plan for `rollback_path_recorded`, and compares the current checkpoint for `checkpoint_updated`. Other domain properties, live readback, visual review and Creator acceptance remain explicitly unresolved by the local verifier. An existing picture or a self-authored approval JSON cannot establish an accepted outcome. Use actual authoritative tools and reviewer evidence through governing instructions; no authenticated host event adapter is claimed.

## Interrupted publication

Prepare a frozen candidate outside canonical Core. Run `scripts/publication.py prepare` with baseline, candidate and actual Library metadata, and persist its private journal before writes. Supply a fresh snapshot keyed by relative path, each value containing `library_file_id`, observed `version_id` and a digest computed from complete downloaded bytes. Snapshot creation must reject duplicate canonical paths. Resolve destination folders for new files; never invent IDs.

Use `request --stage source`, save the emitted request, and pass its `uploads` to the current Library helper. Record every per-item outcome with `record`, persist the journal, and obtain fresh metadata/bytes. Only then request the manifest stage, repeat readback, and request the pointer. A failed `record` exits nonzero; inspect that exit before any dependent action. `bytes_complete` is not acceptance: run full inventory readback, essential checks and checkpoint closure.

After interruption use `reconcile` from fresh bytes. Already-correct replacements are skipped, unfinished writes use current version guards, and third-party drift or identity changes stop as conflicts. Unknown-success creates are not repeated: resolve their exact unique identity, validate intended bytes, and use `adopt --path EXACT_PATH` to record that observed identity before reconciling. For rollback use `--direction rollback`; restore prior source bytes then manifest then pointer. Requests also list newly created nodes requiring archival outside canonical Core by their observed identity. Archive through Library management and refresh the snapshot before advancing; the upload helper does not silently delete them. No duplicate active root is created.

Sequential Library writes are not atomic. During update integrity may fail and boot must remain blocked. The journal provides the recovery route, not continuous availability or an always-running background recovery process.

## Measurement and evaluation

Byte budgets are observable; host token count and cost remain null when not supplied. Budget overruns require a concrete correctness reason and do not authorize skipping instruction bodies. Context plans measure selected full-content bytes plus compact plan payload separately from local machine-file bytes.

Run the controlled comparison suite at worthy checkpoints. Freeze baseline, candidate, cases and graders outside candidate execution, and record their hashes. Deterministic state/oracles test routing, safe publication/retry, artifact acceptance and handoff contracts. These are controlled outcomes, not fresh model-driven image production or a measurement of general intelligence. Record first-attempt pass, repeated trials and local latency honestly; report model tokens/cost/corrections as unavailable. Visual quality and live scheduled-service reliability require separately authorized real workloads and actual rendered/readback evidence.
