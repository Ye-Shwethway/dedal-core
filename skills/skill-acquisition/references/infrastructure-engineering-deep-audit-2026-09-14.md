# Infrastructure / IaC Deep Audit — 2026-09-14

## Question

Does infrastructure lifecycle work deserve a distinct top-level owner, or is Terraform/Packer-style guidance sufficiently covered by Software Development, Release Engineering, Security Engineering, Cloudflare Platform, and Reliability Engineering?

## Sources

- HashiCorp `agent-skills` pinned at `c2d65dfe492f74d360d35b859b88932222470bd8` (official first-party corpus; current catalog reviewed 2026-09-14).
- HashiCorp Terraform current official documentation for `plan`, `apply`, state/drift and refresh-only workflows, reviewed 2026-09-14.
- OpenTofu current official CLI documentation for plan/apply semantics, reviewed 2026-09-14.

## High-signal findings

HashiCorp maintains a lifecycle-governed skills catalog with active Terraform and Packer skills covering provider configuration/resources/testing, module refactoring, imports/search, policy, stacks, style, acceptance tests, machine-image builders and registry workflows. This supports progressive specialist knowledge rather than a single frozen vendor manual.

Terraform's core lifecycle is not ordinary application implementation. It reconciles declared configuration, tracked state, and live provider reality; plan produces a proposal, while apply performs side effects. Drift, refresh-only/state reconciliation, imports, resource moves, provider upgrades and replacements create correctness and recovery concerns distinct from software code review.

A successful infrastructure apply is also not equivalent to a software release or a healthy service. Release Engineering owns source/artifact/application promotion, while Reliability Engineering owns live service health. Infrastructure Engineering supplies the resource-lifecycle layer between those domains.

## Ownership decision

**PROMOTE Infrastructure Engineering as a top-level DEDAL faculty.**

It owns:
- desired configuration / IaC state / live resource reconciliation;
- plan/apply semantics and destructive-change review;
- imports, moves, refactors and drift reconciliation;
- module/provider lifecycle reasoning;
- infrastructure state/backend safety and partial-apply recovery reasoning;
- machine-image lifecycle reasoning where infrastructure semantics dominate.

It does not own:
- application implementation (`software-development`);
- application artifact promotion (`release-engineering`);
- live service health/incidents (`reliability-engineering`);
- provider-specific product architecture such as Cloudflare topology (`cloudflare-platform`);
- database engine semantics (`database-engineering`);
- security authority/policy (`security-engineering`);
- independent product acceptance (`quality-engineering`).

## Durable adaptations

1. Treat configuration, state, and live provider reality as distinct evidence views.
2. A speculative plan is not an applied change; a successful apply is not service-health proof.
3. Review replace/destroy actions explicitly when they may cause persistence, identity or downtime effects.
4. Drift is classified before reconciliation; live/manual changes may be authoritative or accidental.
5. Prefer supported import/move/refactor mechanisms over direct state surgery.
6. State/backend operations are elevated and may expose sensitive information.
7. `auto-approve` removes interaction, not authority.
8. Provider/tool/version specifics remain live-doc-sensitive.

## Why not a Terraform skill

DEDAL should not bind the faculty identity to Terraform. Terraform, OpenTofu, Packer and future declarative provisioning tools are execution/reference technologies. The durable ownership layer is infrastructure lifecycle and reconciliation semantics.

## Promotion evidence boundary

This audit plus routing contracts establishes architecture and contract justification, not measurable real-project outcome gains. Outcome validation should now happen naturally during ordinary infrastructure/VPS/Cloudflare/multi-provider work.

## Campaign conclusion

After this promotion, the current skill-expansion wave has no remaining immediate top-level candidate with comparable evidence. Mobile is reference-pack-approved; observability is absorbed under Reliability Engineering; Postgres practices are under Database Engineering; browser/computer control remains an execution surface; healthcare/clinical informatics remains a later/high-bar bounded audit area. The next phase should be ordinary-work outcome validation rather than continued expansion for its own sake.
