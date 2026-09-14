# Multi-Agent Delegation Authority Audit — 2026-09-14

## Scope

Gap-oriented audit for DEDAL's next hardening frontier: authority inheritance across delegation and handoff.

## Sources reviewed

- OpenAI current agent orchestration guidance: handoffs can transfer workflow execution between agents.
- Anthropic containment guidance: reduce autonomous blast radius by constraining what agents are able to do, not only by supervising behavior.
- OWASP agentic security guidance: confused-deputy and privilege-escalation risks require least-privilege entitlements and authorization checks tied to the acting user/principal.

No external runtime, package, or multi-agent framework was installed or executed.

## Classification

### ADAPT — authority attenuation

A child agent receives only the subset of parent authority required for its subtask. Delegation is not ambient privilege inheritance.

### ADAPT — handoff/control separation

Workflow control may move to another agent, but authority remains separately scoped and explicit.

### ADAPT — bounded re-delegation

Re-delegation requires explicit permission and cannot exceed the original authority chain.

### ADAPT — provenance return contract

Delegated work should return compact conclusions, evidence references, uncertainty, and blocked/escalated actions. Consequential claims remain candidate state pending appropriate verification.

### ADAPT — brokered capabilities over credential copying

Where the host permits, prefer scoped/brokered actions rather than handing child workers reusable ambient credentials.

### ALREADY COVERED

- smallest-sufficient topology;
- verified-state promotion;
- read-only verifier preference;
- task-scoped tool authority;
- high-impact confirmation and confused-deputy boundaries.

### REJECT AS DEFAULT

- automatically cloning all parent tools/credentials into every child;
- assuming a handoff transfers all authority;
- allowing child self-authorization when it encounters a blocked action;
- mandatory multi-agent decomposition for work one capable agent can perform efficiently.

## DEDAL decision

- New skill: **NO**.
- Security Engineering refinement: **YES**.
- Agent Engineering refinement: **YES**.
- Full multi-agent runtime: **NO**.
- Evidence level: design + executable contract validation only; representative outcome improvement not yet measured.
