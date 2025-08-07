# Adult Income Prediction - Data Preprocessing & Feature Engineering

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg)](https://jupyter.org/)

> A comprehensive data science project demonstrating advanced preprocessing, feature engineering, and selection techniques on the Adult Income dataset to predict whether an individual's income exceeds $50K per year.

## Overview

This project showcases a complete machine learning pipeline focused on data preparation techniques essential for building robust predictive models. The workflow demonstrates practical skills in exploratory data analysis, preprocessing, feature engineering, and selection methods using the classic Adult Income dataset.

### Key Learning Objectives
- Master data exploration and cleaning techniques
- Implement various encoding strategies for categorical variables
- Apply feature scaling and transformation methods
- Create meaningful engineered features
- Utilize advanced feature selection techniques

## Dataset

| Attribute | Details |
|-----------|---------|
| **Name** | Adult Income Dataset |
| **Source** | UCI Machine Learning Repository |
| **Records** | ~32,561 instances |
| **Features** | 15 attributes |
| **Target** | Binary classification (>50K, <=50K) |
| **Year** | 1994 Census Database |

### Features Overview
- **Demographic**: age, sex, race
- **Education**: education level, education-num
- **Employment**: workclass, occupation, hours-per-week
- **Financial**: capital-gain, capital-loss
- **Geographic**: native-country
- **Social**: marital-status, relationship

## ✨ Features

- **Comprehensive Data Exploration** - In-depth analysis of data structure and quality
- **Smart Missing Value Handling** - Mean/mode imputation strategies
- **Multiple Scaling Techniques** - StandardScaler and MinMaxScaler implementation
- **Advanced Encoding Methods** - One-hot and label encoding for categorical variables
- **Feature Engineering** - Creation of meaningful derived features
- **Feature Transformation** - Log transformation for skewed distributions
- **Intelligent Feature Selection** - Isolation Forest and Predictive Power Score analysis
- **Comparative Analysis** - PPS vs Correlation matrix insights

## Project Structure

```
adult-income-prediction/
├── data/
│   ├── adult.csv
│   └── processed/
├── notebooks/
│   └── EDA2.ipynb
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   └── utils.py
├── results/
│   ├── visualizations/
│   └── reports/
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

### Prerequisites
- Python 3.7+
- Jupyter Notebook

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/adult-income-prediction.git
   cd adult-income-prediction
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn ppscore
```

## Usage

1. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open the main notebook**
   Navigate to `notebooks/EDA2.ipynb`

3. **Run the analysis**
   Execute cells sequentially to reproduce the complete analysis

### Quick Demo
```python
# Load and preprocess data
from src.preprocessing import load_and_clean_data
from src.feature_engineering import create_features

data = load_and_clean_data('data/adult.csv')
engineered_data = create_features(data)
```

## Methodology

### 1. Data Exploration & Preprocessing
- **Data Quality Assessment**: Missing values, data types, distributions
- **Missing Value Treatment**: 
  - Numerical: Mean imputation
  - Categorical: Mode imputation
- **Feature Scaling**:
  - **StandardScaler**: Z-score normalization (μ=0, σ=1)
  - **MinMaxScaler**: Range normalization [0,1]

### 2. Encoding Strategies
- **One-Hot Encoding**: Low cardinality categoricals (<5 unique values)
  - Applied to: `sex`, `income`
  - Preserves categorical nature, increases dimensionality
- **Label Encoding**: High cardinality categoricals (≥5 unique values)
  - Applied to: `occupation`, `education`
  - Memory efficient, potential ordinality bias

### 3. Feature Engineering
- **Binned Features**: 
  ```python
  hours_per_week_category = ['Part-time', 'Full-time', 'Over-time']
  ```
- **Composite Features**:
  ```python
  capital_gain_loss = capital_gain - capital_loss
  ```
- **Log Transformation**: Applied to highly skewed `capital_gain` (skewness: 11.95)

### 4. Feature Selection
- **Outlier Detection**: Isolation Forest algorithm
- **Predictive Power Score (PPS)**: Non-linear relationship detection
- **Comparative Analysis**: PPS vs Pearson correlation insights

## Results

### Key Insights
- Successfully reduced data skewness through log transformation
- Identified non-linear relationships missed by correlation analysis
- Created meaningful engineered features improving predictive potential
- Achieved clean dataset ready for ML model training

### Performance Metrics
- **Data Quality**: 100% completeness after preprocessing
- **Feature Reduction**: Optimal feature subset identified via PPS
- **Outlier Removal**: ~5% outliers detected and handled
