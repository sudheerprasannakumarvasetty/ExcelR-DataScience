
# Multiple Linear Regression — Toyota Corolla Price Prediction

## Project Overview

This project applies **Multiple Linear Regression (MLR)** to predict the price of a used Toyota Corolla based on various attributes. The analysis includes preprocessing, feature engineering, model building, evaluation, and the application of regularization techniques.

---

## Dataset Description

The dataset contains the following variables:

| Feature          | Description                                  |
|------------------|----------------------------------------------|
| Age              | Age in years                                 |
| KM               | Accumulated kilometers on the odometer       |
| FuelType         | Type of fuel (Petrol, Diesel, CNG)           |
| HP               | Horse Power                                  |
| Automatic        | Transmission Type (1 = Automatic, 0 = Manual)|
| CC               | Cylinder Volume (in cc)                      |
| Doors            | Number of doors                              |
| Weight           | Car weight (in kilograms)                    |
| Quarterly_Tax    | Tax paid quarterly                           |
| Price            | Selling price in Euros (Target variable)     |

---

## Tasks Performed

### 1. Exploratory Data Analysis (EDA)

- Summarized dataset with statistical descriptions
- Visualized relationships using:
  - Pairplots
  - Correlation heatmaps
  - Boxplots and histograms
- Encoded categorical features
- Handled missing or inconsistent values (if any)

### 2. Data Splitting

- Split dataset into **80% training** and **20% testing**
- Used `train_test_split` from `sklearn`

### 3. Model Building

Built and compared **3 different regression models**:
- **Model 1**: Full model using all variables
- **Model 2**: Reduced model after removing less significant variables
- **Model 3**: Model with transformed variables and interaction terms

Interpreted model coefficients and their influence on price.

### 4. Model Evaluation

- Evaluated using:
  - R² (coefficient of determination)
  - RMSE (Root Mean Squared Error)
  - MAE (Mean Absolute Error)
- Performed residual analysis and multicollinearity checks

### 5. Regularization Techniques

- Applied **Lasso** and **Ridge Regression**
- Compared results with baseline models
- Selected optimal alpha using cross-validation

---

## Interview Questions

### 🔹 What is Normalization & Standardization?

- **Normalization** scales data to a range [0, 1]
- **Standardization** centers data to have mean 0 and std deviation 1
- Helps ML models converge faster and interpret coefficients more effectively

### 🔹 Techniques to Address Multicollinearity:

- **Variance Inflation Factor (VIF)**
- **Removing correlated predictors**
- **Using PCA (Principal Component Analysis)**
- **Regularization methods like Ridge**

## Conclusion

This analysis demonstrates a complete end-to-end regression pipeline for predicting car prices using multiple predictors. By applying regularization and performing model diagnostics, we achieved robust insights into the factors that influence used car pricing.