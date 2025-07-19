
# Estimation and Confidence Intervals — Durability Study of Print-Heads

## Project Overview

This project analyzes the **durability** of print-heads in a manufacturing setting where **destructive testing** limits the sample size. We estimate the population mean durability using **confidence intervals** based on both sample and known population standard deviations.

---

## Background

The manufacturer of PC print-heads conducted durability testing on a **sample of 15 print-heads**, measuring the number of characters printed before failure (in millions). The testing is destructive and costly, necessitating a statistical approach to estimate overall performance with confidence.

---

## Data

Durability values (in millions of characters before failure):

```
1.13, 1.55, 1.43, 0.92, 1.25, 1.36, 1.32, 0.85, 1.07,
1.48, 1.20, 1.33, 1.18, 1.22, 1.29
```

---

## Assignment Tasks

### 🔹 Task A: 99% Confidence Interval Using Sample Standard Deviation

- **Method Used**: *t-distribution*
- **Why t-distribution?**
  - Sample size < 30
  - Population standard deviation is unknown
- **Steps:**
  - Calculated sample mean and sample standard deviation
  - Found degrees of freedom (n-1)
  - Used `scipy.stats.t.interval()` to build the confidence interval
  - Interpretation: There is a 99% chance the true population mean lies within the constructed interval

### 🔹 Task B: 99% Confidence Interval Using Known Population Standard Deviation

- **Method Used**: *z-distribution*
- **Why z-distribution?**
  - Population standard deviation is known (σ = 0.2)
- **Steps:**
  - Calculated standard error using σ/√n
  - Used `scipy.stats.norm.interval()` to build the interval
  - Compared with the t-distribution-based interval

---

## Key Learnings

- **Confidence intervals** help estimate population parameters using sample data
- The **t-distribution** is appropriate for small samples with unknown σ
- The **z-distribution** is preferred when population σ is known
- Confidence intervals become **narrower** with lower variability or larger sample sizes

---

## Conclusion

Through this analysis, we built reliable statistical bounds to estimate the average durability of print-heads. Such techniques are crucial in industrial scenarios where **direct testing is limited**, but **data-driven decisions** are essential for quality control and process improvement.