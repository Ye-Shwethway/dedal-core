# Worker deployment and connector recovery

Use this reference for live Worker source inspection, source patches, deployment-path failures, connector aggregation, and recovery from ambiguous write outcomes.

## Authority and source identity

A Cloudflare Worker has several potentially different source representations:

1. repository source;
2. generated/build artifact;
3. currently deployed Worker content;
4. a sanitized/public reconstruction of deployed behavior.

Do not assume they are byte-identical. Before patching production, identify which representation is authoritative for the requested change.

If the live deployed Worker is ahead of the repository, do **not** upload the older repository file merely because it is easier to access. Read the deployed source or reconstruct the exact deployable artifact first, patch that state, and reconcile the repository separately.

Record version/hash/etag/deployment identity before mutation when available. After mutation, read back the deployed source or metadata and verify the intended marker/version rather than relying only on the upload response.

## Execution-surface ladder

Treat connectors, aggregators, MCP servers, direct APIs, CLIs, and dashboards as execution surfaces with different transport fidelity. A surface that can list or invoke resources is not automatically safe for binary/multipart/source uploads.

Prefer this order for routine authorized work:

1. use the connected native/direct Cloudflare surface when it faithfully supports the required request shape;
2. use an aggregation surface when its schemas and transport preserve the operation contract;
3. use direct API/CLI execution when a higher-level connector loses required request semantics;
4. ask for manual dashboard editing only after practical automated paths have been exhausted or when explicit human review is the purpose.

For mobile-constrained Creator workflows, manual source editing is especially a last resort.

Do not treat connector failure as proof the Cloudflare API or resource is broken. Localize the failure layer first: auth, schema discovery, request serialization, API validation, runtime behavior, or read-back.

## Transport fidelity

Worker source uploads may require exact content-type and multipart/module metadata semantics. Before a production write:

- inspect the current authoritative Cloudflare API contract when material;
- verify whether the execution surface supports raw bodies, multipart boundaries/files, and module metadata without rewriting them;
- distinguish service-worker syntax from ES-module Workers;
- prefer a content-only endpoint when only code should change so bindings/configuration are not unintentionally replaced.

If an aggregator serializes a request incorrectly, switch execution surface instead of repeatedly changing correct Worker code to satisfy the broken transport.

## Large source retrieval

A connector may successfully fetch a Worker while truncating or externalizing a large response for the model. Do not infer that the source itself is truncated.

Safer recovery options include:

- server-side extraction of version/hash/target markers;
- bounded chunk retrieval with offsets and an end-to-end hash check;
- an alternate first-party/direct connector that preserves raw response content;
- repository reconstruction only when repository state is proven equivalent to the live target.

Before patching reconstructed chunks, verify total length/hash and unique target occurrence where practical.

## Post-mutation ambiguity and retries

Some operations can commit upstream and fail during immediate verification because the upstream service is eventually consistent or the connector loses the success response.

When a mutation can have committed:

1. do **not** blindly retry;
2. read back the target state first;
3. if the desired state is present exactly once, treat the mutation as committed and continue;
4. if state is absent and the operation is proven retry-safe, retry within the bounded recovery policy;
5. if the outcome is unknown and retry may duplicate/destructively repeat work, report an outcome-unknown state and stop automatic retry.

For read-after-write verification on eventually consistent APIs, bounded retry is preferred to a single immediate read when the operation contract permits it. Keep the retry window small and explicit.

## Aggregated MCPs

An aggregation layer may expose an existing remote MCP without replacing the MCP's canonical schemas. Verify this rather than assuming it:

- compare discovered tool count/names against the remote MCP;
- inspect high-impact schemas and required intent fields;
- run read-only calls first;
- test a bounded idempotent mutation before relying on the aggregation path for broader writes;
- keep the remote MCP/Gateway as the source of tool semantics unless an explicit migration is intended.

OAuth dynamic client registration, callback allowlists, and provider authorization are separate layers. A registration failure does not imply the MCP tool surface itself is invalid.

## Completion evidence

For a production Worker code change, a strong completion claim normally needs:

- pre-change target identity/version;
- successful source upload/deployment response;
- post-change deployed metadata/source read-back;
- target health or bounded functional verification;
- explicit note of any repository/live-source divergence that remains.

A dashboard screenshot, connector success badge, or deploy HTTP 200 alone is weaker evidence.
