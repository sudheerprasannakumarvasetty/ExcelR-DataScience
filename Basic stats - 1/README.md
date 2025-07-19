# Basic Statistics, Descriptive Analytics & Data Preprocessing on Sales & Discounts Dataset
### Introduction
This project focuses on performing descriptive analytics, visual data exploration, and essential data preprocessing tasks on a Sales & Discounts dataset. It serves as a foundational step in preparing data for more complex analytical or machine learning applications.

## Descriptive Analytics for Numerical Columns
### Objectives:
- Compute key statistical metrics: mean, median, mode, standard deviation

- Understand the central tendency and variability of numerical features

### Steps:
- Loaded dataset using pandas

- Identified numerical columns

- Used describe() and manual computation (e.g., mean(), median(), mode(), std())

- Brief inferences were drawn for each variable

## Data Visualization
### Histograms:
- Plotted histograms using matplotlib & seaborn

- Analyzed skewness and distribution shapes

- Identified potential outliers

### Boxplots:
- Created boxplots for numerical variables

- Highlighted IQR and extreme values

- Used to support outlier detection and distribution interpretation

### Bar Charts (Categorical Data):
- Identified categorical columns

- Used value_counts() and plotted bar charts

- Analyzed distribution of categories and dominance patterns

## Standardization of Numerical Variables
### Objective: ### 
To scale features using z-score normalization:

z = x − μ / σ ​
 
### Highlights:
- Performed standardization using sklearn.preprocessing.StandardScaler

- Compared distributions before and after scaling

- Verified zero mean and unit variance post-scaling

## Categorical Data Encoding
### Objective:
Transform categorical features into machine-readable format using one-hot encoding

### Approach:
Applied pandas.get_dummies() to convert categorical columns into binary features

Showcased the transformed dataframe with new dummy variables

## Conclusion
- Basic descriptive statistics provided insights into data quality and distribution

- Visualizations enhanced understanding of patterns, outliers, and imbalances

- Standardization ensured scale uniformity for ML compatibility

- One-hot encoding prepared categorical variables for modeling