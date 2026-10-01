# Viewer Comment Engagement

Use this reference when reading, replying to, editing, or moderating public viewer comments on a Creator-owned YouTube channel.

## Decision ladder

1. **Read the full thread first.** Include existing channel replies and later viewer follow-ups so the response does not answer stale context.
2. **Classify the interaction.** Use one of: `positive_low_risk`, `neutral_factual`, `sensitive_or_contested`, `abuse_or_spam`.
3. **Choose the least consequential action.** A reply is preferred over moderation when the viewer is merely disagreeing. No action is valid when a reply would add heat without value.
4. **Match autonomy to risk.** Low-risk social engagement can be autonomous; sensitive or materially escalatory replies require Creator review. Destructive moderation always uses the appropriate explicit authority gate.
5. **Verify factual claims.** For time-sensitive or externally verifiable claims, use the appropriate Research path before posting. Keep uncertainty visible.
6. **Write in channel voice, not debate voice.** Friendly, concise, and non-defensive is the default. Do not treat a reasonable skeptical question as hostility.
7. **Read back the write.** When the API exposes the resulting comment, confirm exact text/parent/thread state after reply or edit.

## Tone rules

- Acknowledge reasonable questions before correcting or qualifying them.
- Prefer `documented fact + uncertainty boundary` over advocacy for or against the viewer's premise.
- Avoid sarcasm, dogpiling, moralizing, or implying expertise the channel does not have.
- Do not convert fan enthusiasm into factual certainty about a public figure's private life, health, medication, drug use, motives, or conduct.
- If a public figure has made a relevant documented statement, attribute it explicitly and do not extend it beyond what was said.
- If the thread becomes argumentative or sensitive after an initially safe reply, reclassify the thread before any further response.

## Moderation boundary

Moderation is not a tone-control tool. Do not reject, delete, hide, or ban merely because a comment is skeptical, critical, or disagrees with the channel. Use moderation only under the applicable channel policy and authority, and preserve explicit destructive-intent gates for irreversible or user-impacting actions.

## Learning boundary

Portable engagement rules belong in public Core. Channel-specific voice, recurring audience patterns, private moderation preferences, and exact comment examples belong in private operational state rather than the public repository.

## Execution routing and reply closure

For Creator-owned channel review/comment workflows, engagement is an execution task, not merely a reporting task. When straightforward low-risk comments are discovered and the Creator's standing workflow authorizes autonomous replies, complete the reply attempt during the same run rather than reporting them as pending merely because one execution surface failed.

Use this bounded route ladder:

1. **Fresh thread read on the authoritative channel.** Discover current thread state from live YouTube before composing a reply. Never start a reply pass from remembered parent IDs alone.
2. **Deduplicate before mutation.** Inspect existing channel replies and follow-ups. If an earlier insert was accepted but visibility is uncertain, read back first; never blind-resend.
3. **Primary write path.** Prefer the dedicated direct DEDAL YouTube MCP comment-reply action.
4. **Direct diagnostic fallback.** If the dedicated wrapper fails before a provider outcome is known, test the bounded generic YouTube Data API route when available to distinguish wrapper failure from provider/backend failure.
5. **Independent execution fallback.** If the direct custom-MCP path is unavailable, test verified Composio YouTube surfaces. Treat Composio custom-MCP passthrough and Composio native YouTube as separate routes with separate auth/transport state. Failure on one is not evidence that the other failed.
6. **Runtime independence.** DEDAL Runtime/Python Canary health can help isolate infrastructure state, but Runtime is sidecar/assist only. Do not make comment execution depend on Runtime when direct MCP or Composio remains usable.
7. **Single mutation, then verification.** Once any route returns an accepted YouTube comment object/reply ID, stop failover writes. Read back the parent/thread. A totalReplyCount increment is useful propagation evidence; embedded replies may lag or be a subset, so absence there alone is not a failed write.
8. **Outcome vocabulary.** Report separately: sent_verified_visible, sent_accepted_pending_readback, not_sent_execution_blocked, not_sent_provider_rejected, and held_for_creator_decision. Never collapse these into generic failed.
9. **Finish the authorized low-risk queue.** A channel-review run is not complete while discovered positive_low_risk or verified neutral_factual comments remain unreplied solely because the first route failed and an independent verified route is still available.
10. **No destructive fallback.** Failover never expands authority into delete/hide/ban/reject actions.

For multilingual comments, reply in the commenter's language when meaning is clear and keep the established channel voice concise. Emoji-only friendly reactions may receive a lightweight matching acknowledgement. Questions about titles, cast, music, or episode identity may be answered autonomously only from verified content facts; do not invent details.

## Review-run completeness gate

Before closing a combined analytics + comment-engagement review:

- enumerate the authenticated channel's live uploads first and build the recent cohort dynamically;
- include every newly published upload plus the current comparison cohort; resolve title, video ID, and publish time before analytics;
- report public counters for every cohort item and compare only against a clearly identified prior verified snapshot;
- distinguish Analytics states: observed nonzero, observed zero, unavailable/not processed, suppressed/incomplete, and execution error;
- scan top-level comments and follow-up replies across the full cohort, not only breakout videos;
- execute authorized straightforward replies through the route ladder above and read back when available;
- surface ambiguous/sensitive items with exact comment, translation when needed, and proposed response rather than auto-posting;
- verify the newest live upload is present, no discovered recent upload was silently omitted, and Short/long-form variants with different IDs remain separate.

A report is part of task completion: do not describe the run as successful if execution occurred but the Creator-facing summary was not delivered.
