---
name: api-skills-delivery
description: >
  Generates delivery reports and upload specifications as downloadable Excel, PDF,
  and PowerPoint files for the content pipeline using Anthropic API Skills.
---

# API Skills Delivery Reports

Generate professional delivery artifacts (xlsx, pptx, pdf) using Anthropic managed API Skills.

## When to Invoke

- After a requirement is completed and content is published (delivery confirmation PDF)
- On request for an upload tracking dashboard (Excel)
- When `research-account-setup` completes platform configuration (setup guide PDF)
- Weekly for pipeline status decks (PowerPoint)

## Report Types

1. **Upload Tracking Dashboard (Excel)** -- upload queue, platform rate limits, weekly upload history with charts
2. **Delivery Confirmation (PDF)** -- published content details, generation metadata, upload metadata, next steps
3. **Platform Setup Guide (PDF)** -- API configuration, credential status, content specifications, verified capabilities
4. **Pipeline Status Deck (PowerPoint)** -- pipeline health table, throughput charts, issues and action items

See `references/report-formats.md` for detailed content schemas and field definitions for each report type.

## Workflow

1. Determine the report type from the request context or trigger event
2. Gather required data: query requirement files, platform status, upload history
3. Compose a structured prompt describing the report layout and data
4. Call the Anthropic API Skills endpoint with the appropriate skill type (`xlsx`, `pdf`, or `pptx`)
5. Save the generated file to `output/reports/`
6. Reference the report path in the requirement status update

## Output Directory

Save all generated reports to `output/reports/` using the naming convention:
`<report-type>-<requirement-id>-<YYYY-MM-DD>.<ext>`

## Cost Guidance

- Excel: ~2000-4000 output tokens
- PowerPoint: ~2000-4000 output tokens
- PDF: ~1000-2000 output tokens
- Batch multiple reports when possible to reduce overhead
