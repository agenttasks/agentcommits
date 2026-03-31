---
name: generate-report
description: |
  Generate downloadable reports (Excel, PowerPoint, PDF) using Anthropic API Skills.
  Creates experiment dashboards, content calendars, strategy decks, and requirement specs.
allowed-tools: Read, Write, Bash, Grep, Glob
---

# Generate Report via API Skills

Generates professional documents from plugin data using Anthropic managed Skills.

## Usage

Arguments:
- `$1`: Report type - `experiment`, `calendar`, `strategy`, `requirement`
- `$2`: Format - `xlsx`, `pptx`, `pdf` (default depends on report type)
- `$3`: Additional context (experiment ID, week number, requirement ID)

## Steps

1. Load the relevant data (experiment results, calendar, requirement)
2. Use `api-skills-reports` skill to select the right API Skill
3. Generate the document via `generate_with_skill()`
4. Download the file to `output/reports/`
5. Log generation to session telemetry

## Report Type Defaults

| Report Type | Default Format | Data Source |
|------------|---------------|-------------|
| `experiment` | xlsx | ab-experiment-measurement |
| `calendar` | xlsx | content-strategy |
| `strategy` | pptx | Weekly aggregated metrics |
| `requirement` | pdf | requirements-handoff |

## Examples

```
/marketing-data-science:generate-report experiment xlsx EXP-001
/marketing-data-science:generate-report calendar
/marketing-data-science:generate-report strategy pptx
/marketing-data-science:generate-report requirement pdf REQ-2026-03-31-001
```
