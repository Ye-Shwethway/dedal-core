# Runtime Configuration

Keep workflow rules public and runtime authority private.

## Normal Chat or Work

1. Load this repository's canonical `SKILL.md` and required references.
2. Use an explicitly connected Google Drive/Google Sheets capability.
3. When the Owner has designated the Google workbook as the primary working system, treat that exact authorized Google Sheet as the canonical operational source. Legacy Excel files are reference/migration/import evidence only unless the Owner explicitly designates a newer external dataset as authoritative for a specific reconciliation.
4. Resolve the workbook from an exact user-provided URL, protected runtime configuration, or authorized Drive discovery.
5. Confirm the workbook title, required sheet names, headers, and target ranges before writing.
6. If the connector cannot read or write the target, stop. Repository access is not spreadsheet authorization.

## GitHub Actions or bot runtime

Use protected secrets or workload identity. Suggested configuration names are:

- `MSA_SPREADSHEET_ID`
- `GOOGLE_SERVICE_ACCOUNT_JSON` or a short-lived Google workload credential
- provider-specific model credentials only when OCR or ambiguous matching requires a model

Never place secret values, live data exports, or operational source images in the repository, workflow logs, test fixtures, issues, or pull requests. Grant the runtime access only to the intended workbook and minimum required APIs.

## Startup checks

Before an operational run:

1. Resolve exactly one authorized workbook.
2. Verify the expected sheets and production headers from live data.
3. Perform a bounded read before any write.
4. Default to dry-run when the runtime cannot establish identity, target range, or write authority.
5. Require idempotency and read-back verification for automated or retried writes.
