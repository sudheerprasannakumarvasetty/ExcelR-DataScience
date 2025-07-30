# K-Nearest Neighbors Classification on Zoo Dataset

## Overview

This project applies the **K-Nearest Neighbors (KNN)** algorithm to classify animals in the **Zoo dataset** based on various characteristics such as presence of hair, feathers, number of legs, ability to fly, and more. It includes end-to-end steps from data analysis to model training, evaluation, and visualization.

---

## Dataset

- **File:** `Zoo.csv`
- **Source:** UCI Machine Learning Repository
- **Features:** 16 binary features + 1 numeric (`legs`)
- **Target:** `type` (animal class, encoded from 1 to 7)

---

## Objectives

1. Understand and explore the Zoo dataset
2. Preprocess the data (handle outliers, check for missing values)
3. Split the dataset using 80/20 stratified train-test split
4. Train a KNN classifier for animal type prediction
5. Evaluate model performance using various metrics
6. Visualize decision boundaries using two key features

---

## Tasks Performed

### 1. Data Exploration
- Loaded dataset and displayed head, shape, and info
- Plotted:
  - Count plot of animal types
  - Heatmap of correlation matrix
  - Boxplot for feature distribution

### 2. Data Preprocessing
- Confirmed there are no missing values
- Detected outliers using boxplots (not removed, which is valid here)

### 3. Feature Selection and Splitting
- Selected `X` (all columns except `animal name` and `type`)
- Target `y` is the `type`
- Performed stratified train-test split (80/20)

### 4. KNN Classification
- Used `KNeighborsClassifier` from sklearn
- Tried different `K` values from 1 to 15
- Chose best `K=5` based on accuracy

### 5. Evaluation Metrics
- Calculated:
  - **Accuracy**
  - **Precision**
  - **Recall**
  - **F1-Score**
- Plotted confusion matrix and classification report

### 6. Decision Boundary Visualization
- Selected only two features (`milk` and `feathers`)
- Plotted decision regions using `contourf`
- Points plotted using `seaborn.scatterplot` to visualize true class

---

## Results Summary

| Metric       | Score (approx.) |
|--------------|-----------------|
| Accuracy     | ~95%            |
| Best K       | 5               |
| Distance     | Euclidean (p=2) |
| Visualization | Done in 2D with selected features |

- Model performed well across all classes with high accuracy and balanced classification metrics.

---

## Libraries Used

- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `sklearn` (KNN, model selection, metrics)
- `warnings`, `collections`, `scipy`

---

## Conclusion

- **KNN** is an effective non-parametric classifier for categorical animal classification.
- The model showed strong performance with minimal preprocessing.
- Visualizing decision boundaries helps in interpreting the model's logic in 2D space.

---

## Future Improvements

- Use GridSearchCV to automate hyperparameter tuning
- Try other distance metrics (Manhattan, Minkowski)
- Apply feature scaling (e.g., MinMaxScaler) and compare results
- Experiment with PCA to reduce dimensionality before plotting

---
