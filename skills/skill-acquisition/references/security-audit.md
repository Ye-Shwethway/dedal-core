# External Skill Security Audit

Treat every third-party skill as untrusted input until reviewed. Inspection does not require execution.

## Review layers

### 1. Instruction boundary

Read `SKILL.md` and references for:

- attempts to override system/platform/project authority;
- vague or over-broad triggers;
- self-promotion into core instructions or memory;
- automatic state-changing actions without clear user intent;
- instructions to conceal behavior, disable safeguards, or misreport outcomes.

### 2. Data boundary

Flag access to:

- credentials, `.env`, SSH/GPG stores, cookies, tokens, browser profiles, private memory, unrelated user files;
- private conversations or project content beyond the task scope;
- external transmission of user/project data not necessary for the stated purpose;
- durable retention without minimization and an explicit need.

### 3. Execution boundary

Inventory every script and command. Flag:

- `sudo`/root or persistence mechanisms;
- package-manager lifecycle scripts or unpinned dependencies;
- downloaded-and-executed remote code;
- shell obfuscation, encoded payloads, dynamic eval, or unexplained binaries;
- writes outside the intended workspace;
- destructive commands without a reversible/approved gate;
- network calls to domains unrelated to the declared function.

### 4. Supply-chain boundary

Check publisher/repository identity, version/revision, license, maintenance, dependency provenance, security reports, and known malicious-copy/typosquat risk.

Registry malware/static scans are useful signals, not authority. A package can be malware-clean while still having dangerous agentic behavior, privacy retention, broad triggers, or excessive permissions.

## Decision classes

- **reject** — malicious, opaque, incompatible authority model, unacceptable privacy/credential behavior, or unresolvable licensing risk;
- **idea-only** — useful concept but code/instructions should not be imported;
- **adapt** — useful and sufficiently understood, but DEDAL rewrite is safer/better;
- **exact-import candidate** — rare; license, provenance, runtime, scripts, permissions, and tests are all understood and exact reuse is justified.

## Default DEDAL stance

Do not install third-party skills into a privileged runtime merely to evaluate them. Prefer static inspection and an independently written DEDAL adaptation. If later evaluation genuinely requires execution, use the least-privileged isolated environment available and verify outputs before promotion.