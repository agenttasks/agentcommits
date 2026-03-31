---
name: run-experiment
description: |
  Orchestrates the lifecycle of week-based A/B experiments for social media
  content optimization, from design through analysis and reporting.
---

# Run Experiment

## Actions

Accept one of the following actions:

- **create** -- Design a new experiment with hypothesis, variable, and two variants.
- **status** -- Check progress and current metrics for a running experiment.
- **analyze** -- Run statistical analysis on a completed experiment.
- **report** -- Generate a weekly experiment report with conclusions.

## Workflow

1. Validate the experiment definition against the schema in `references/experiment-schemas.md`.
2. Use the `ab-experiment-measurement` skill for metric computation and statistical analysis.
3. Deploy variants following the weekly schedule (Mon/Wed = A, Tue/Thu = B).
4. Collect platform analytics after each deployment day.
5. Run a two-proportion z-test once minimum sample sizes are met (200 views per variant).
6. Generate the weekly report with per-platform results, conclusion, and next-step recommendation.

## Arguments

- **action**: one of create, status, analyze, report
- **experiment_id**: required for status, analyze, report
- **variable**: required for create (hook_type, duration, style, posting_time, cta_type, audio)
