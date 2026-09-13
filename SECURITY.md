# Security Policy

`dedal-core` is intentionally public. Treat every committed byte as publicly readable forever.

## Allowed

- public architecture and design documentation;
- sanitized schemas and examples;
- reusable workflows and scripts;
- capability registries without credentials;
- tests and validation rules;
- public project metadata.

## Prohibited

Never commit:

- passwords, API keys, tokens, cookies, private keys, or credentials;
- raw ChatGPT memory exports or private conversation archives;
- private personal data or identity documents;
- confidential medical, patient, hospital, or employment data;
- secrets embedded in logs, screenshots, fixtures, archives, or generated artifacts;
- production `.env` files.

## Secret Handling

Use, in order of preference:

1. platform secret stores (for example GitHub Actions Secrets);
2. secured external services/backends;
3. local untracked environment files.

Commit only templates such as `.env.example` with fake values.

## Incident Response

If a secret or private value is accidentally committed:

1. revoke/rotate the exposed secret immediately;
2. remove it from the repository and history where practical;
3. assume the exposed value was copied;
4. document the incident without reproducing the secret;
5. add a guard that reduces recurrence.

Deleting a visible GitHub file does not make an exposed credential safe again; rotation is mandatory.

## Reporting

Security issues affecting this repository should be handled privately with the repository owner rather than by publishing sensitive exploit details in a public issue.
