
# Hypothesis Testing & Chi-Square Test — Statistical Analysis in Business Scenarios

## Overview

This project demonstrates the use of **Hypothesis Testing** and **Chi-Square Test for Independence** to evaluate business decisions and customer behavior in two case studies:

- Association between **Device Type** and **Customer Satisfaction** using the Chi-Square test.
- Evaluation of **Operating Costs** using one-sample hypothesis testing.

---

## Case Study 1: Chi-Square Test of Independence

### Objective:
Determine if there's a significant association between the type of smart home device purchased (Smart Thermostat vs Smart Light) and customer satisfaction level.

### Data:
A contingency table summarizing customer satisfaction:

| Satisfaction Level   | Smart Thermostat | Smart Light | Total |
|----------------------|------------------|-------------|--------|
| Very Satisfied       | 50               | 70          | 120    |
| Satisfied            | 80               | 100         | 180    |
| Neutral              | 60               | 90          | 150    |
| Unsatisfied          | 30               | 50          | 80     |
| Very Unsatisfied     | 20               | 50          | 70     |
| **Total**            | 240              | 360         | 600    |

### Tasks:
1. **Hypotheses:**
   - H₀: Device type and satisfaction level are independent
   - H₁: Device type and satisfaction level are associated

2. **Chi-Square Statistic:**
    Computed using observed and expected frequencies.

3. **Degrees of Freedom (df):**
   \[
   df = (rows - 1) 	imes (columns - 1) = 4
   \]

4. **Critical Value:**
    Found from the Chi-Square distribution table at α = 0.05

5. **Conclusion:**
    Based on comparison between calculated value and critical value

---

## Case Study 2: Hypothesis Testing on Operating Costs

### Objective:
Verify restaurant owners' claim that actual weekly operating costs are higher than predicted by the model:

\[
W = 1000 + 5X
\]

Given:
- Sample mean cost: 3050
- X (units/week): μ = 600, σ = 25
- Sample size (n): 25

### Tasks:
1. **Hypotheses:**
   - H₀: Mean weekly cost = model prediction (Rs. 4000)
   - H₁: Mean weekly cost > model prediction

2. **Theoretical Mean:**
   \[
   \mu = 1000 + 5 	imes 600 = 4000
   \]

3. **Standard Error:**
   \[
   \sigma = 5 	imes 25 = 125, SE = rac{125}{\sqrt{25}} = 25
   \]

4. **Test Statistic (Z):**
   \[
   Z = rac{3050 - 4000}{25} = -38
   \]

5. **Decision:**
    Compare with critical z-value at α = 0.05

6. **Conclusion:**
    Final verdict on whether to reject H₀ and accept the claim

---

## Summary

- The **Chi-Square test** assessed whether device type and satisfaction are related — a key insight for marketing strategy.
- The **Hypothesis test** helped validate claims about operational cost inflation, supporting business decision-making through data.

---
