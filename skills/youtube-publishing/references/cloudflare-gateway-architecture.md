# Cloudflare gateway architecture

Cloudflare owns OAuth, exact channel identity, encrypted token custody, job state,
resumable-session initiation, and remote verification. The VPS owns source retrieval
and direct byte transfer.

Worker Secrets cannot be dynamically created by OAuth callbacks. Per-channel refresh
tokens therefore use AES-256-GCM ciphertext in a dedicated D1 credential table; the
32-byte KEK is a Worker Secret. Alias + channel ID are authenticated as additional
data, preventing ciphertext substitution between profiles.

A profile begins disabled with a pre-registered channel ID. OAuth must return exactly
one `channels.list(mine=true)` identity matching it. Credential rows repeat alias and
channel ID; jobs snapshot channel ID; every upload mutation repeats identity
verification.

The runner gets an encrypted-at-rest resumable session URI, not a Google token. It
recovers from interruption through YouTube's confirmed byte offset. An expired or
ambiguous session is not automatically replaced because a lost completion response
could otherwise create a duplicate.
