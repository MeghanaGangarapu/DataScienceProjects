# Beyond Correlation: A Practical Guide to Causal Inference and A/B Testing


## 1. Introduction: Why Causal Inference Matters
"Correlation doesn’t imply causation." It’s a phrase we often hear, yet in data science and product decision-making, the distinction is critical. While correlation helps us spot patterns, only causal inference lets us make confident decisions about interventions: Should we ship this feature? Did our campaign actually drive conversions?

Understanding causality empowers organizations to make smarter, evidence-based decisions that go beyond surface-level insights.

---

## 2. Correlation ≠ Causation
Two variables moving together doesn’t mean one causes the other. There could be a third factor driving both, or the relationship might be purely coincidental.

Example: Ice cream sales and drowning deaths both increase during summer. Summer is the confounder here, not a causal link between ice cream and drowning.

To identify true causal relationships, we need rigorous methods like randomized controlled trials (A/B testing) and careful statistical reasoning.
- `Ice cream sales vs. drowning`
- `Cheese consumption vs. bedsheet entanglement deaths`

> These relationships are **spurious** — driven by hidden or confounding variables.
---

### 3. Key Terminology
| Term          | Definition                                       | Example                      |
| ------------- | ------------------------------------------------ | ---------------------------- |
| Treatment     | The intervention you're testing                  | Showing a discount offer     |
| Control group | The group that doesn't receive the treatment     | No offer shown               |
| Confounder    | A variable that affects both treatment & outcome | User location                |
| Randomization | Assigning treatment by chance                    | A/B testing users randomly   |
| Causal Effect | Difference in outcome due to treatment           | +5% conversions due to offer |

---
## Designing a Causal Experiment: Online A/B Testing
Randomized controlled experiments are the gold standard for measuring causal effects in a product or marketing setting.

#### Key Design Elements
- Randomization Unit: Usually a user or session.
- Target Population: Define user segments (e.g., by geography or device).
- Sample Size: Larger sizes yield more precise estimates.
- Experiment Duration: Run at least a full week to account for weekday effects.

#### Best Practices

- Persistent Assignment: Ensure the same user always sees the same variant.
- Guardrails: Define metrics that shouldn’t worsen (e.g., error rates, revenue).
- Segment Analysis: Look for subgroup-specific effects.
 ---

## Interpreting Results

## Statistical Significance
- Indicates the likelihood that the observed effect is not due to chance.
- Measured by p-value; typically, p < 0.05 is considered significant.

## Practical Significance
- Even if statistically significant, is the effect size worth acting on?
- Your team may decide that a lift under 2% is too small to justify launch costs.

## Confidence Intervals
Confidence intervals express the uncertainty around an estimate.
Example: A 6% observed lift with 95% CI of [2.1%, 9.9%] is statistically and practically significant.
CI containing 0: Not statistically significant, effect could be due to chance.

## When Results Are Unclear
Wide CI: Increase sample size.
CI crosses zero: No reliable inference.
Low lift: Evaluate implementation cost vs. potential gain.

---

##  Decision Framework: Ship or Scrap?

| **Observed Result**                                       | **Recommended Action**                | **Why?**                                                                 |
|-----------------------------------------------------------|----------------------------------------|--------------------------------------------------------------------------|
| ✅ Statistically & practically significant                | 🚀 Ship                               | Effect is real *and* valuable — proceed with rollout.                    |
| ✅ Stat. significant, ❌ not practically significant       | ⚖️ Reassess cost-benefit              | It's real, but too small to justify cost — may not be worth shipping.   |
| ❌ Not statistically significant                          | 🔁 Rerun with larger sample           | Data is inconclusive — need more power (sample size) to detect effect.  |
| ✅ Practically significant, ❌ not statistically significant| 🔍 Rerun with more power              | Effect seems valuable, but data is noisy — more evidence needed.        |
| ⚠️ CI crosses practical threshold                         | 🧪 Increase precision & rerun         | Can't confidently say if it’s meaningful — results are ambiguous.       |


 ---
## Common Biases & Effects
- **Novelty Effect**: Users try new feature initially
- **Primacy Effect**: Users take time to adopt
- **Simpson’s Paradox**: Segments may contradict aggregate

    > Use time plots to detect novelty/primacy effects.


## Guardrails & Tradeoffs
- **Guardrail metrics** : Shouldn’t change (e.g., error rate, revenue per user)
- **Tradeoff: Engagement** ↑ but revenue ↓? → Do a cost-benefit analysis.

    > Launch only if expected gain > implementation and maintenance cost.

# Optional Tools:
- Bayesian A/B Testing
- Uplift Modeling
- Sequential Testing

## Beyond A/B: Observational Causal Inference
When RCTs (randomized controlled trials) aren't feasible (e.g., for pricing changes or geographic rollouts), use these methods:

- Propensity Score Matching (PSM)
- Difference-in-Differences (DiD)
- Instrumental Variables (IV)
- Causal Forests / Double Machine Learning

# Case Study: Creative Effectiveness A/B Test
- **Goal**: Compare performance of two TV ads on engagement
- **Unit**: Two demographically similar markets
- **Metrics**: Site visits, search volume, conversions

```
Market A: 1M impressions, 10k visits → 10/1000
Market B: 800k impressions, 12k visits → 15/1000
```

Use t-test or Mann-Whitney U test based on metric distribution. Normalize by impressions to compare

### Why not household-level split?
Though it avoids geographic bias, household-level assignment introduces other variabilities:
    Different income levels → different responses
    Heavy vs. light watchers → different exposures
    hannel preference bias

# Summary
- Causal inference guides action, not just observation
- A/B tests reveal real effects, not random noise
- Statistical ≠ Practical Significance
- Confidence intervals provide nuance
- Run experiments mindfully and interpret results critically

