# Forecasting Exchange Rates using Time Series Analysis

## Overview

This project applies ARIMA and Exponential Smoothing techniques to forecast USD to AUD exchange rates based on historical data. The analysis provides a comprehensive comparison of different time series forecasting models to identify the best-performing approach for exchange rate prediction.

## Dataset

**Source:** `exchange_rate.csv`

**Columns:**
- `Date`: Date of observation
- `USD_AUD`: Exchange rate (USD to Australian Dollar)

## Project Structure

### Part 1: Data Preparation and Exploration
- Load and parse the dataset, set the date as the index
- Visualize the time series to inspect trends, seasonality, and anomalies
- Handle missing values and outliers
- Perform seasonal decomposition for trend/seasonality analysis

### Part 2: ARIMA Model Building
- Perform stationarity check using the ADF test
- Use ACF and PACF plots for initial parameter estimation
- Perform grid search for optimal (p, d, q) parameters based on AIC
- Fit the ARIMA model and perform residual diagnostics
- Forecast future exchange rates and compare with actual values

### Part 3: Exponential Smoothing Model Building
- Evaluate Simple Exponential Smoothing (SES), Holt's Linear Trend, and Holt-Winters models
- Select seasonal periods based on data frequency
- Fit and forecast using each model
- Compare forecasted values with actual data

### Part 4: Model Evaluation and Comparison
- Compute MAE, RMSE, and MAPE for all models
- Compare results visually and numerically
- Identify the best-performing model

## Installation

Install the required dependencies before running the project:

```bash
pip install pandas numpy matplotlib statsmodels scikit-learn
```

## Usage

1. **Setup**: Place `exchange_rate.csv` in the project directory

2. **Run Analysis**: Open and run `time_with_explanations.ipynb` in Jupyter Notebook or JupyterLab

3. **Review Results**: Examine the generated plots and printed evaluation metrics

## Files

- `time_with_explanations.ipynb` - Main analysis notebook
- `exchange_rate.csv` - Historical exchange rate data
- `forecast_evaluation_metrics.csv` - Model performance metrics (generated)

## Key Features

- **Complete Workflow**: From data loading to forecasting and evaluation
- **Multiple Models**: Both ARIMA and Exponential Smoothing approaches tested
- **Comprehensive Evaluation**: Visual and numerical comparison of model performance
- **Best Model Selection**: Identification of optimal forecasting method based on RMSE

## Deliverables

- **Notebook**: `time_with_explanations.ipynb` with complete analysis
- **Metrics**: `forecast_evaluation_metrics.csv` with model comparison results
- **Visualizations**: 
  - Time series trends and patterns
  - Seasonal decomposition plots
  - Residual diagnostics
  - Forecast comparison charts

## Results

The project provides insights into:
- Historical exchange rate patterns and trends
- Comparative performance of different forecasting models
- Best-performing model identification based on evaluation metrics
- Future exchange rate predictions with confidence intervals
