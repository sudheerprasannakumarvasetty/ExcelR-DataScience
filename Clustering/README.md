# Clustering Analysis K-Means, Hierarchical, and DBSCAN

## Overview
This project applies three clustering techniques **K-Means**, **Hierarchical Clustering**, and **DBSCAN** to the *EastWestAirlines* customer dataset to identify meaningful customer segments.  
The workflow includes data preprocessing, exploratory analysis, clustering implementation, visualization, and performance evaluation.

---

## Dataset
- **File:** `EastWestAirlines.xlsx`
- **Description:** Contains customer profile and travel activity features.
- **Goal:** Group customers into clusters for potential business insights.

---

## Methodology
1. **Preprocessing**
   - Removed irrelevant identifiers (`ID#`)
   - Filled missing values
   - Removed outliers using IQR method
   - Scaled features with `StandardScaler`

2. **Exploratory Analysis**
   - Descriptive statistics and correlation heatmap
   - Distribution and pair plots to detect patterns

3. **Clustering**
   - **K-Means:** Optimal K chosen via Elbow Method and Silhouette Score
   - **Hierarchical:** Ward linkage, dendrogram analysis
   - **DBSCAN:** Tuned `eps` and `min_samples` to identify clusters and noise

4. **Evaluation**
   - Internal metric: Silhouette Score
   - Cluster counts and interpretation of characteristics

---

## Tools & Libraries
- Python 3
- pandas, numpy
- matplotlib, seaborn
- scikit-learn, scipy

---

## Key Results
- **K-Means** achieved the highest silhouette score with clear cluster separation.
- **Hierarchical** produced similar segmentation but was more sensitive to outliers.
- **DBSCAN** effectively identified noise points and unusual customer patterns.

---

## Conclusion
Clustering revealed distinct customer groups that can support **targeted marketing** and **customer relationship strategies**. Scaling and parameter tuning significantly influenced cluster quality.