# Tool Authority and Least-Privilege Audit — 2026-09-14

## Capability gap

DEDAL already documented trust boundaries, least privilege, read/write separation, high-impact confirmation, and confused-deputy risk. The missing layer was an executable contract separating a tool's technical availability from task-scoped action authority.

## Sources reviewed

- OWASP AI Agent Security Cheat Sheet — least-privilege tool sets, per-tool permission scoping, explicit authorization for sensitive operations, high-impact validation, bounded propagation.
- OWASP MCP Security Cheat Sheet — MCP tool/schema poisoning, confused-deputy risk, excessive OAuth scopes, tool-definition drift/rug pulls, per-server credentials, schema integrity and approval.
- OWASP MCP Tool Poisoning — untrusted tool responses must not be able to reach privileged actions merely through model instruction-following; restrictions belong at the execution boundary.
- OWASP Prompt Injection Prevention / GenAI guidance — validate proposed tool calls against user/session permissions; privileged actions require stronger controls; authorization must not depend solely on model output.

No third-party package, scanner, MCP server, or runtime was installed or executed for this audit.

## ADAPT

1. **Availability is not authorization.** Installed/connected/discoverable/callable tools do not automatically belong to the current task's authority envelope.
2. **Task-scoped grants.** Bind consequential authority to tool, mode, resource scope, task intent, accepted authority source, and confirmation state where required.
3. **No privilege inheritance across modes.** Read does not imply write/delete/send/deploy/external-effect authority.
4. **No authority from untrusted content.** Web/file/email/tool/model/MCP content may inform action but cannot create its own permission.
5. **Intent and resource confinement.** A valid tool grant for one intent/resource cannot silently broaden because intermediate content requests expansion.
6. **High-impact confirmation.** Destructive, externally visible, or credential-bearing actions require the stronger gate appropriate to impact.
7. **MCP definition drift as re-authorization signal.** Where host support exists, pin or verify approved tool/schema identity; material drift invalidates prior trust until reviewed.
8. **Deterministic boundary preferred.** Authorization belongs in host/tool/service enforcement where possible; prompts are not access-control systems.

## ALREADY COVERED

- Creator authority and explicit approval boundaries.
- trust-boundary mapping and confused-deputy reasoning.
- least privilege and read/write separation as design principles.
- mutation verification and evidence-linked durable state.
- privacy-minimal trajectory logging.

## REJECT AS DEFAULT

- universal human confirmation for every read-only action;
- mandatory multi-agent privilege separation for low-risk tasks;
- trusting MCP/tool descriptions because the server is connected;
- wildcard permissions for convenience;
- model-generated risk scores as the sole authorization control;
- importing a full external authorization framework into Core without a controllable host execution seam.

## DEDAL decision

New top-level skill: **NO**.
Primary owner: **security-engineering**.
Pair with agent-engineering when the control must be embedded in a harness/runtime and with provider/domain skills for concrete service permissions.

## Evidence boundary

This audit plus executable cases establish design/contract validation only. The public Core cannot intercept every native provider/tool call, so real runtime enforcement depends on the host/service exposing an enforceable dispatch or ACL seam. Do not claim universal tool blocking from this repository contract alone.
