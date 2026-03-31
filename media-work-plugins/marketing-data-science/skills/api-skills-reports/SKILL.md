---
name: api-skills-reports
description: Generates downloadable report files by calling Anthropic API Skills endpoints for marketing data science workflows.
---

# API Skills Reports

## When to use

Activate when a user requests a downloadable report (xlsx, csv, or pdf) from marketing data. This skill handles the API interaction pattern for report generation.

## Report generation flow

1. Identify the report type requested (campaign performance, audience segmentation, A/B test results, attribution, etc.).
2. Gather required parameters: date range, campaign IDs, metric filters, and output format.
3. Call the Anthropic API Skills endpoint to generate the report. See `references/api-patterns.md` for endpoint details and request structure.
4. Return the download link or file content to the user.

## Supported output formats

- **xlsx** -- preferred for tabular data with multiple sheets (e.g., summary + detail tabs).
- **csv** -- use for single-table exports or pipeline ingestion.
- **pdf** -- use for formatted narrative reports with charts.

## Parameter handling

- Default date range to the last 30 days when the user does not specify one.
- Validate campaign IDs against known campaigns before making the API call.
- Apply metric filters (impressions, clicks, conversions, spend) as requested.

## Error handling

- If the API returns a rate limit error, inform the user and suggest retrying after a short wait.
- If required parameters are missing, ask the user for clarification rather than guessing.
- If the requested report type is not supported, list the available report types.

## Cross-references

- For report layout templates and formatting conventions, see the `generate-report` skill and its `references/report-templates.md`.
- For detailed API request/response patterns, see `references/api-patterns.md`.
