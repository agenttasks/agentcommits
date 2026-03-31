# Metrics and Scoring

Composite scoring formula, statistical test procedure, and report template for A/B experiment measurement. For individual metric definitions, formulas, and weights see `run-experiment/references/experiment-schemas.md` (Derived Metrics table).

## Composite score formula

```
composite = (completion_rate * 0.30)
          + (engagement_rate * 0.25)
          + (share_rate * 0.20)
          + (follower_conversion * 0.15)
          + (ctr * 0.10)
```

Compute one composite score per variant per platform. Average across platforms for overall comparison.

## Two-proportion z-test procedure

For each derived rate metric, compare Variant A rate (p_a) against Variant B rate (p_b):

1. Calculate pooled proportion: `p_pool = (x_a + x_b) / (n_a + n_b)`
2. Calculate standard error: `SE = sqrt(p_pool * (1 - p_pool) * (1/n_a + 1/n_b))`
3. Calculate z-statistic: `z = (p_a - p_b) / SE`
4. Determine p-value from z using the standard normal distribution (two-tailed)
5. Calculate Cohen's h: `h = 2 * arcsin(sqrt(p_a)) - 2 * arcsin(sqrt(p_b))`

### Decision criteria

- Minimum sample size: 200 views per variant
- Confidence level: 95% (critical z = 1.96)
- Significant if p < 0.05
- Report effect size interpretation: small (h ~ 0.2), medium (h ~ 0.5), large (h ~ 0.8)

## Weekly report template

```markdown
## Week {N} Experiment Report

### Hypothesis
{hypothesis}

### Variable Tested
{variable}: {variant_a_label} vs {variant_b_label}

### Results
| Platform | Variant A Score | Variant B Score | Winner | p-value | Effect Size |
|----------|----------------|----------------|--------|---------|-------------|

### Conclusion
{statistical interpretation}

### Action
{changes based on results}

### Next Experiment
{next hypothesis}
```
