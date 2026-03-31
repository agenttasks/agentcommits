---
name: generate-report
description: >
  Generate downloadable reports using Anthropic API Skills (xlsx, pptx, pdf).
  Use when users want to create experiment dashboards, content calendars,
  strategy decks, or requirement specification documents.
---

# Generate Report via API Skills

Generate professional documents from plugin data using Anthropic managed API Skills.

## Report Types

| Type | Default Format | Data Source |
|------|---------------|-------------|
| experiment | Excel (xlsx) | ab-experiment-measurement results |
| calendar | Excel (xlsx) | content-strategy weekly calendar |
| strategy | PowerPoint (pptx) | Aggregated weekly metrics |
| requirement | PDF | requirements-handoff specifications |

## Steps

1. Identify the report type and data source
2. Format the data into a clear prompt for the API Skill
3. Call `client.beta.messages.create()` with the appropriate skill:
   - `{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}` for Excel
   - `{"type": "anthropic", "skill_id": "pptx", "version": "latest"}` for PowerPoint
   - `{"type": "anthropic", "skill_id": "pdf", "version": "latest"}` for PDF
4. Include the `code_execution` tool in the request
5. Extract and download generated files

## API Pattern

```python
response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    container={"skills": [{"type": "anthropic", "skill_id": "<skill-id>", "version": "latest"}]},
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": "<report-prompt>"}],
    betas=["code-execution-2025-08-25", "files-api-2025-04-14", "skills-2025-10-02"],
)
```

See `references/report-templates.md` for specific prompt templates per report type.
