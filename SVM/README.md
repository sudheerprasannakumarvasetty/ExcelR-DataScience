# SVM Analysis for Mushroom Edibility Prediction Assignment

### 1. Assignment Overview

This assignment involves building a machine learning model to accurately classify mushrooms as either **edible** or **poisonous** based on their physical characteristics. We utilize a Support Vector Machine (SVM) classifier, a powerful and effective algorithm for classification tasks. The entire analysis, from data exploration to model evaluation, is documented in the accompanying Jupyter Notebook (`Mushroom_SVM_Analysis.ipynb`).

### 2. Dataset

The dataset used is the **Mushroom Dataset**, a popular collection of hypothetical mushroom samples from the Audubon Society Field Guide. Each sample is described by 22 categorical features (e.g., cap shape, color, odor) and is classified as either edible or poisonous.

- **Source File:** `mushroom.csv`
- **Classes:** Edible, Poisonous
- **Features:** 22 categorical attributes

### 3. Assignment Workflow

The assignment follows a standard machine learning pipeline:

1.  **Exploratory Data Analysis (EDA):** We start by loading the data and exploring its structure, feature distributions, and correlations to gain initial insights.
2.  **Data Preprocessing:** Categorical features are converted into a numerical format using label encoding to make them suitable for the SVM model. The data is then split into training and testing sets.
3.  **Data Visualization:** We use various plots like histograms and heatmaps to visualize feature relationships and the class distribution.
4.  **SVM Implementation:** A basic SVM model with a linear kernel is implemented and trained on the preprocessed data.
5.  **Model Evaluation:** The model's performance is evaluated on the test set using key metrics like accuracy, precision, recall, and the F1-score. A confusion matrix is generated to visualize the results.
6.  **Hyperparameter Tuning:** We use `GridSearchCV` to experiment with different SVM kernels (`linear`, `rbf`, `poly`) and hyperparameters to find the optimal model configuration.
7.  **Comparison and Analysis:** The performance of different SVM kernels is compared, and a final analysis discusses the model's strengths, weaknesses, and practical implications.

### 4. How to Run This Assignment

To run the analysis yourself, please follow these steps:

1.  **Prerequisites:** Ensure you have Python and Jupyter Notebook (or JupyterLab) installed. You will also need the following libraries:
    - `pandas`
    - `numpy`
    - `matplotlib`
    - `seaborn`
    - `scikit-learn`

    You can install them using pip:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn jupyterlab
    ```

2.  **Download Files:** Download the assignment files to your local machine.

3.  **Place the Dataset:** Make sure the `mushroom.csv` file is in the same directory as the Jupyter Notebook.

4.  **Launch Jupyter:** Open your terminal, navigate to the assignment directory, and run:
    ```bash
    jupyter lab
    ```
    or
    ```bash
    jupyter notebook
    ```

5.  **Open and Run:** Open the `Mushroom_SVM_Analysis.ipynb` file and run the cells sequentially to reproduce the analysis.

### 5. Key Findings

- The SVM classifier, particularly with an **RBF kernel**, achieved **perfect accuracy (100%)** on the test set, demonstrating its effectiveness for this classification problem.
- The dataset is well-structured and the classes are highly separable, making it an ideal use case for SVMs.
- Hyperparameter tuning confirmed that a non-linear kernel (RBF) with an appropriate `C` value provides the best performance.

### 6. Technologies Used

- **Language:** Python 3
- **Libraries:**
    - **Data Manipulation:** Pandas
    - **Numerical Operations:** NumPy
    - **Data Visualization:** Matplotlib, Seaborn
    - **Machine Learning:** Scikit-learn
- **IDE:** Jupyter Notebook / JupyterLab

---
