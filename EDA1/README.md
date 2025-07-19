# Exploratory Data Analysis on Cardiographic Dataset

## Objective

This project focuses on performing Exploratory Data Analysis (EDA) on the `cardiographic.csv` dataset to uncover meaningful patterns, identify anomalies, and understand the structure and characteristics of the data. The analysis aims to support further modeling or decision-making related to fetal health monitoring.

---

## Dataset Description

The dataset comprises several physiological parameters related to fetal health. Below are the key features and their assumed interpretations:

| Feature | Description |
|---------|-------------|
| `LB` | Baseline Fetal Heart Rate (FHR) |
| `AC` | Accelerations in FHR |
| `FM` | Fetal Movements |
| `UC` | Uterine Contractions |
| `DL` | Decelerations Late |
| `DS` | Decelerations Short |
| `DP` | Decelerations Prolonged |
| `ASTV` | Abnormal Short-Term Variability (%) |
| `MSTV` | Mean Short-Term Variability |
| `ALTV` | Abnormal Long-Term Variability (%) |
| `MLTV` | Mean Long-Term Variability |

---

## Tasks Performed

### 1. Data Cleaning & Preparation
- Loaded dataset using pandas.
- Checked and handled missing values.
- Converted incorrect data types to appropriate formats.
- Identified and treated outliers where necessary.

### 2. Statistical Summary
- Generated descriptive statistics including mean, median, standard deviation, and IQR.
- Highlighted anomalies and interesting observations in the dataset.

### 3. Data Visualization
- Plotted histograms and boxplots for understanding distribution.
- Used bar charts and pie charts for categorical analysis.
- Explored relationships via scatter plots and correlation heatmaps.
- Applied advanced plots like pair plots and violin plots for deeper insight.

### 4. Pattern Recognition & Insights
- Analyzed correlation between variables to uncover dependencies.
- Derived initial patterns and trends from variable relationships.

### 5. Conclusion
- Summarized key findings from the data.
- Offered potential implications and suggestions for further investigation.

---

## Deliverables

- **[EDA1.ipynb]**: Contains all code, visualizations, and explanatory commentary.
- Summary Report: A brief overview of insights, patterns, and suggestions derived from the analysis.

---

## Sample Visuals

> Below are examples of visualizations included in the notebook:

- Distribution Plots (Histogram, Boxplot)
- Correlation Heatmap
- Pair Plots
- Violin Plots

---

## Key Insights

- Several features show strong correlation with fetal heart rate variability.
- Outlier presence in acceleration and contraction variables was noted.
- Visual patterns support medical intuition regarding fetal health indicators.

---
