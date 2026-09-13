# Adaptation Notes — Security Engineering

DEDAL Security Engineering is a provider-agnostic synthesis, not a verbatim import.

## Primary influences reviewed 2026-09-14

- OWASP GenAI Security Project / Agentic Security Initiative and current Top 10 work. Repository snapshot: `OWASP/www-project-top-10-for-large-language-model-applications` @ `99f4395589bdbd120ae961f9cd179e79d7f9b27f`.
- OpenAI, `Designing AI agents to resist prompt injection` (2026-03-11): prompt injection should be addressed by constraining impact, not filtering alone.
- OpenAI, `A practical guide to building agents`: risk-rate tools using write access, reversibility, account permissions and impact; layer guardrails.
- Anthropic, `Trustworthy agents in practice` (2026-04-09): autonomy raises governance, prompt-injection and unintended-action risk.
- OWASP 2026 material on memory/context poisoning and agentic risk categories.

## Adopted

- explicit trust/authority boundaries;
- least privilege and blast-radius reduction;
- prompt/goal hijacking as a systems problem rather than prompt wording alone;
- memory/context persistence as an attack surface;
- realistic adversarial verification;
- separation of useful external evidence from action authority.

## Rejected / generalized

- vendor-specific product controls as universal requirements;
- security-through-classifier-only designs;
- universal confirmation for every write regardless of impact;
- treating a security checklist or Top 10 taxonomy as proof of safety;
- execution of third-party security tooling merely to inspect methodology.

Security guidance that depends on current platform/runtime behavior must be refreshed from authoritative sources before high-impact implementation.
