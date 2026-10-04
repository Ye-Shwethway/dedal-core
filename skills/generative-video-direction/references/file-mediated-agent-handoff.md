# File-Mediated Agent Handoff

## When to use
Use a file-mediated handoff when DEDAL prepares canonical source states but a separate specialist agent owns generative-video execution. The shared workspace is a transport/control surface; the canonical continuity truth remains the production manifest.

## Handoff contract

Before sending `images_ready`, require:
- all listed source assets exist and are individually reviewable;
- the production manifest version is current;
- adjacent frame pairs are classified `reachable | needs_bridge | intentional_cut`;
- identity, physical, prop/load, pairwise reachability, and video-readiness checks pass;
- the message names the exact manifest version and requests acknowledgement when needed.

The downstream agent may return `image_request`, `feedback`, `video_complete`, `ack`, or `status`. Pair-specific feedback is preferred over prose-only feedback because it permits narrow bridge insertion.

## Manifest pinning
Never generate from a handoff whose manifest version differs from the current production manifest. Request a resync instead.

## Closed-loop repair
A downstream `needs_bridges` verdict should identify `{from_frame, to_frame, issue, requested_action}`. Return that pair to Visual Narrative Production, add only the necessary intermediate anchors, bump the manifest version, revalidate the affected neighborhood, and emit a new handoff.

## Polling asymmetry
Do not claim background polling unless an actual runtime/automation performs it. A bridge may be asymmetric: the specialist agent can poll its inbox while DEDAL reads its inbound folder on activation or through a real scheduled mechanism.

## Provider boundary
The file bridge does not define provider syntax. Generative Video Direction still compiles the canonical source sequence to the freshly verified provider control surface after the handoff is consumed.
