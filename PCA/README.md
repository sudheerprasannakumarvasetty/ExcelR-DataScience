# PCA and Clustering Analysis on Wine Dataset

## Objective

This project demonstrates the application of **Principal Component Analysis (PCA)** for dimensionality reduction and evaluates its impact on clustering results. We compare clustering performance on both original and PCA-transformed data using K-Means clustering.

---

## Dataset

The dataset used in this analysis is `wine.csv`, which contains various chemical attributes of wine samples.  
Target column (if any) was not present, hence clustering was performed in an unsupervised manner.

---

## Project Workflow

### 🔹 Task 1: Exploratory Data Analysis (EDA)
- Loaded the dataset and explored basic statistics.
- Visualized feature distributions using histograms and box plots.
- Investigated feature correlations with a heatmap.

### 🔹 Task 2: Dimensionality Reduction with PCA
- Standardized the dataset using `StandardScaler`.
- Applied PCA to reduce the number of features.
- Used a **Scree plot** and **cumulative explained variance** to determine optimal components.
- Transformed the original dataset using the selected principal components.

### 🔹 Task 3: Clustering with Original Data
- Applied **K-Means clustering** on the original dataset.
- Visualized clusters using 2D PCA projection.
- Evaluated using **Silhouette Score** and **Davies–Bouldin Index**.

### 🔹 Task 4: Clustering with PCA-Reduced Data
- Re-applied K-Means on the PCA-transformed dataset.
- Visualized the clusters.
- Evaluated clustering performance.

### 🔹 Task 5: Comparison and Analysis
- Compared clustering results between original and PCA-transformed data.
- Analyzed the impact of dimensionality reduction on clustering performance.

### 🔹 Task 6: Conclusion and Insights
- Summarized key findings and differences observed.
- Provided practical recommendations on when to use PCA with clustering.

---

## Results Summary

| Metric                    | Original Data | PCA-Reduced Data |
|--------------------------|---------------|------------------|
| Silhouette Score         | 0.30648398324833453 | 1.315707552261773  |
| Davies-Bouldin Index     | 0.32292055407233017 | 1.2578453408449173 |

---

## Key Learnings

- PCA helps reduce dimensionality without losing significant information.
- Clustering on PCA-reduced data can improve performance and efficiency.
- Visualization becomes easier with PCA (especially in 2D).
- PCA may discard noise and redundant features, improving cluster separation.

---
