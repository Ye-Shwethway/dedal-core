# Media, Scheduling, and Messaging

## Media publishing

Treat media transport and Page authorization as separate failure domains.

- A direct image/video URL must be retrievable by Facebook without private authentication.
- Redirecting, expiring, blocked, unsupported, or non-direct URLs may fail even when Page permissions are correct.
- If the execution surface supports managed file upload/staging, prefer it after a URL-fetch failure rather than changing Page permissions blindly.
- Verify the resulting Page-scoped post object or scheduled queue item after media creation.

## Scheduling

- Use a future provider-accepted timestamp and keep the object unpublished until the scheduled time.
- Read the scheduled queue after create/reschedule and confirm `is_published`/scheduled time when those fields are exposed.
- A draft/unpublished object and a scheduled object are not always returned by the same listing endpoint; direct post read-back may still be authoritative.
- Publishing a queued post immediately is a public mutation and requires explicit intent distinct from merely creating or inspecting the queue.

## Messenger

Messenger may depend on more than broad Page ownership: current messaging permission, Page access context, provider/app state, platform policy windows, and fresh conversation visibility can all matter.

Operational rules:

- read current thread state first;
- require visible fresh inbound activity before using a normal response window;
- derive the recipient from Page conversation metadata;
- do not use policy tags as a workaround for stale or missing conversation state;
- if the provider reports an expired/out-of-window state despite a claimed fresh user message, mark the messaging surface degraded and investigate connection/app/provider behavior before further sends;
- old conversation history being readable does not prove current inbound synchronization is healthy.
