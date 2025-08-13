# Titanic Survival Prediction using LightGBM & XGBoost

## Objective

The objective of this project is to compare the performance of LightGBM
and XGBoost algorithms using the Titanic dataset.

## Dataset

The Titanic dataset contains passenger details such as age, sex, class,
and survival status. Two CSV files are used: - `Titanic_train.csv`:
Training data with survival labels. - `Titanic_test.csv`: Testing data
without labels.

## Steps Followed

### 1. Exploratory Data Analysis (EDA)

-   Loaded the dataset using pandas.
-   Checked for missing values.
-   Plotted histograms and box plots for data distributions.
-   Visualized relationships between features and survival using scatter
    and bar plots.

### 2. Data Preprocessing

-   Imputed missing values for numerical and categorical columns.
-   Encoded categorical variables using Label Encoding.
-   Applied further preprocessing to prepare data for ML models.

### 3. Model Building

-   Split data into training and testing sets.
-   Selected evaluation metrics: Accuracy, Precision, Recall, and
    F1-score.
-   Built predictive models using:
    -   **LightGBM**
    -   **XGBoost**
-   Performed hyperparameter tuning and cross-validation.

### 4. Comparative Analysis

-   Compared performance metrics of LightGBM and XGBoost.
-   Visualized accuracy scores for both models.
-   Observed strengths and weaknesses:
    -   LightGBM was faster to train.
    -   XGBoost achieved slightly better precision in our case.

## Results Summary

-   Both models performed well on the Titanic dataset.
-   LightGBM is suitable for faster training with large datasets.
-   XGBoost is slightly better when precision is more important.

## Requirements

Install required libraries:

``` bash
pip install pandas numpy matplotlib seaborn scikit-learn lightgbm xgboost
```
