---
name: ab-experiment-measurement
description: |
  Designs and measures week-based A/B experiments for social media content,
  computing composite performance scores and statistical significance.
allowed-tools: Read, Write, Bash, Grep
---

# A/B Experiment Measurement

## Experiment design

Define each experiment to test exactly ONE variable (hook type, duration, style, posting time, CTA type, or audio). Assign two variants: A (control) and B (treatment).

Follow the weekly schedule:
- Mon/Wed: deploy Variant A
- Tue/Thu: deploy Variant B
- Fri: collect and analyze results
- Sat: generate report and plan next week

## Metric collection

Collect per-platform raw metrics: views, completions, likes, comments, shares, new followers, link clicks. Derive rates from these (see `references/metrics-and-scoring.md` for formulas and weights).

## Composite scoring

Calculate the weighted composite score for each variant. Refer to `references/metrics-and-scoring.md` for the full weight table and formula.

## Statistical analysis

Run a two-proportion z-test comparing variant rates. Require a minimum of 200 views per variant before analysis. Use 95% confidence (z = 1.96). Report p-value and effect size (Cohen's h). Declare significance only when p < 0.05.

See `references/metrics-and-scoring.md` for the z-test procedure.

## Reporting

Generate a weekly report containing:
1. Hypothesis and variable tested
2. Per-platform results table (variant scores, winner, p-value, effect size)
3. Statistical interpretation and conclusion
4. Recommended action based on results
5. Next experiment hypothesis

## Experiment backlog

Maintain a prioritized queue of experiments. Suggested order:
1. Hook type optimization
2. Optimal video duration
3. Posting time optimization
4. Visual style testing
5. CTA effectiveness
6. Platform-specific optimization

Validate all experiment definitions against the schema in `run-experiment/references/experiment-schemas.md`.
