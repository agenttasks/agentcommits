---
name: run-experiment
description: >
  Create and manage A/B experiments for social media content optimization.
  Use when users want to design experiments, deploy variants, analyze results,
  or generate weekly experiment reports with statistical rigor.
---

# Run A/B Experiment

Design, deploy, track, and analyze week-based A/B experiments for content optimization.

## Actions

- **create** — Design a new experiment with hypothesis, variable, and variants
- **status** — Check current experiment progress and metrics
- **analyze** — Run statistical analysis on completed experiment data
- **report** — Generate a weekly experiment report

## Steps

1. Use the `ab-experiment-measurement` skill to design or analyze the experiment
2. Validate experiment design against the experiment schema (see `references/experiment-schemas.md`)
3. Deploy variants according to the weekly schedule
4. Collect metrics from platform analytics
5. Analyze results with two-proportion z-test for statistical significance
6. Generate a weekly report with conclusions and next actions

## Arguments

- Action: create, status, analyze, report
- Experiment ID (for status/analyze/report) or variable name (for create)
