
# Logistic Regression - Titanic Survival Prediction (Assignment)

This assignment involves building a **Logistic Regression** model to predict survival of passengers aboard the Titanic, based on provided features. The task also includes deploying the model using **Streamlit** for basic user interaction.

---

## Dataset Used

- `Titanic_train.csv` – used for training and evaluation
- `Titanic_test.csv` – optional for further testing or experiments

---

## Objectives

- Explore and preprocess the Titanic dataset
- Train a Logistic Regression model using scikit-learn
- Evaluate model performance using classification metrics
- Deploy the trained model using Streamlit (locally)

---

## Assignment Steps

### 1. Data Exploration
- Checked for missing values, data types, and summary statistics
- Visualized relationships using seaborn/matplotlib

### 2. Preprocessing
- Filled missing values in `Age` and `Embarked`
- Converted categorical variables (`Sex`, `Embarked`) to numeric
- Dropped unused columns like `Name`, `Cabin`, `Ticket`

### 3. Model Building
- Used Logistic Regression from scikit-learn
- Trained the model on an 80/20 split of the dataset

### 4. Evaluation
- Evaluated using: Accuracy, Precision, Recall, F1-score, ROC-AUC
- Plotted the ROC curve

### 5. Streamlit App (Deployment)
- Created a simple app using Streamlit
- User can enter input values and receive prediction
- App loads the trained model from `logistic_model.pkl`

---

## How to Run the Streamlit App

### Prerequisites
- Python 3.8 or higher

### Required Libraries  
You need to manually create a `requirements.txt` file with the following:

```text
streamlit
scikit-learn
pandas
numpy
matplotlib
seaborn
joblib
```

### Steps to Run
1. Open terminal in the project folder
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

## Sample Input for Testing

| Feature   | Value   |
|-----------|---------|
| Pclass    | 1       |
| Sex       | female  |
| Age       | 29      |
| SibSp     | 0       |
| Parch     | 0       |
| Fare      | 100     |
| Embarked  | C       |

**Expected Prediction:** Survived (high probability)

---

## Key Concepts (Interview Q&A)

**1. What is the difference between precision and recall?**  
- Precision = TP / (TP + FP): How many predicted positives were correct  
- Recall = TP / (TP + FN): How many actual positives were identified  
> Precision = accuracy of positive predictions  
> Recall = coverage of actual positives

**2. What is cross-validation?**  
- Technique to test model stability by training/testing on multiple data splits (e.g., k-fold)
- Reduces overfitting and gives reliable performance estimates
