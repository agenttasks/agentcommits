---
name: generate-report
description: Generates formatted marketing data science reports with standardized layouts, sections, and visualizations.
---

# Generate Report

## When to use

Activate when a user asks to create, draft, or format a marketing report. This skill covers report structure, content organization, and presentation -- not the API call mechanics (see `api-skills-reports` for that).

## Report creation flow

1. Determine the report purpose: executive summary, deep-dive analysis, recurring dashboard narrative, or ad-hoc investigation.
2. Select the appropriate template from `references/report-templates.md`.
3. Populate each section with the relevant data, metrics, and narrative.
4. Apply formatting conventions (headings, tables, chart placeholders, callout boxes).
5. Include an executive summary at the top with key findings and recommended actions.

## Content guidelines

- Lead every report with a one-paragraph executive summary stating the key takeaway.
- Use plain language for metrics explanations; avoid jargon without defining it first.
- Include period-over-period comparisons (WoW, MoM, YoY) where applicable.
- Flag statistically significant changes with confidence intervals when available.
- End with a "Recommended Actions" section containing 2-5 concrete next steps.

## Formatting rules

- Use H2 headings for major sections, H3 for subsections.
- Present KPIs in a summary table at the top of each section.
- Mark positive trends with "up" indicators and negative trends with "down" indicators.
- Round percentages to one decimal place; round currency to whole numbers.
- Use consistent date formats (YYYY-MM-DD) throughout.

## Visualization placeholders

When the output format supports charts, include placeholders specifying:
- Chart type (bar, line, pie, heatmap).
- Axes and data series.
- Title and subtitle text.

## Cross-references

- For report templates and section structures, see `references/report-templates.md`.
- For API-based report file generation, see the `api-skills-reports` skill.
