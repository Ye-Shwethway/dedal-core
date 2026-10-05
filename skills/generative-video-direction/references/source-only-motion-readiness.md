# Source-Only Motion Readiness

Use when DEDAL prepares source images for an external video executor, or no video execution surface is available. Load Visual Narrative Production's `references/source-production-design.md` for the shared physical/source planning method. Never silently follow the general 'generate takes' lifecycle beyond the available capability.

## Scope and readiness

Declare `source_only`. DEDAL owns temporal design, source-image requirements, pair diagnosis, and truthful handoff. The external executor owns video jobs/takes and their moving-result QA. A source-ready label means accepted images and a defensible plan exist; it does not mean motion succeeded, a provider was tested, or a collaborator acknowledged receipt.

When actual pixels are absent, output a **planned** source plan with QA pending. When images exist, inspect them and bind exact accepted asset versions before readiness. Separate `planned`, `source_ready`, `sent`, `acknowledged`, and `video_verified` using the project's existing protocol. Do not change protocol message/status names locally; map these distinctions to its documented fields and evidence.

## Pair ledger

`motion-shot-spec.schema.json` offers optional `source_only_plan` with planning stage, pixel-QA state and typed pairs. Source-ready/sent/acknowledged declarations structurally require passed pixel QA and no unresolved pair decision; actual pixels, acceptance and communication evidence are still required separately. A valid self-declared object does not prove readiness or ACK. Existing project protocols remain authoritative.

For every intended adjacency record:

| Field | Required decision |
| --- | --- |
| Pair | Ordered accepted A/B IDs and versions; shared scene/beat IDs |
| Relation | continuous motion, deliberate cut, hold, or loop |
| Mechanism | Specific action events from observed A to observed B; contact/support and possession changes |
| Timing | Estimated action/settling time and assumptions; fit to intended segment duration |
| Motion | Subject/object path, direction, rotation, start/end velocity or settle state |
| Camera | Locked family, feasible continuous move, or explicit cut; world-to-screen effect |
| Risk | Missing evidence, occlusion, topology/view burden, contradictory states, known debt |
| Decision | ready, needs_bridge, split, cut, repair_source, or unresolved; smallest responsible change |

Reason from **observed source states**, not their planned captions. State why a pair is reachable; 'small delta', 'natural transition', and a pass checkbox alone are insufficient. Estimate duration without pretending to know an exact universal biomechanical threshold. If a duration is missing, state a provisional timing assumption and avoid execution-ready provider claims.

## Choose the remedy

- **Add a bridge** when an intermediate contact/possession/phase state is missing within one continuous action.
- **Split** when distinct actions exceed the segment's timing/control burden.
- **Use an explicit cut** when continuity is editorially unnecessary; document elapsed action and exit/entry state. A cut does not excuse a contradicting object count or load.
- **Repair source** when an endpoint already has impossible grip, geometry, identity, or wrong phase. More bridges cannot repair an invalid endpoint.
- **Hold/loop** only when purpose and boundary state/velocity support it. Matching poses alone do not guarantee a seamless loop.
- **Leave unresolved** when required source facts or material provider controls remain unknown.

A contact event can be visible in a generated segment between source anchors; it need not receive a still for every millisecond. Add anchors according to risk and evidence, avoiding both blind interpolation and unnecessary frame inflation.

## Provider handoff

Keep a provider-neutral plan usable even if the executor has not selected a model. Verify the exact provider/model/mode and material image roles, number/order, duration/aspect constraints, first/last/extension behavior, and input format before compiling an execution-ready request. An image reference mode does not necessarily enforce an endpoint, and a source keyframe is not necessarily an input accepted by that mode.

Compile concise action/camera timing from the neutral plan; appearance lives primarily in the input image for I2V. Preserve shared boundary anchors when the verified mode supports adjacent first/last segments. Start-only mode leaves the desired end state less constrained: mark that risk and require moving-result QA from the executor. If controls are unknown, provide requirements and questions, not invented supported parameters or submitted-job claims.

## Closure and feedback

Handoff accepted asset order/version, pair ledger, source QA, explicit cuts/holds, timing assumptions, capability evidence or unknowns, known debt, and a narrow feedback request keyed by pair/asset. Use the existing set-scoped messages; do not contact a collaborator unless the Creator authorized that communication.

When feedback arrives, distinguish a source defect from interpolation, provider controls, camera design, and editorial assembly. Repair only the owning layer, revalidate affected neighbors, revise the manifest, and reissue only the affected scope under the existing protocol. Keep an accepted package closed until actual pair-specific evidence warrants reopening it.
