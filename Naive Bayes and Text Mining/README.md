# Text Classification & Sentiment Analysis on Blog Posts using Naive Bayes

## Overview

This project involves analyzing a dataset of blog posts to:
1. Classify them into categories using a Naive Bayes classifier.
2. Perform sentiment analysis to understand the tone (positive, negative, neutral) of each blog.

It combines text preprocessing, feature extraction (TF-IDF), machine learning (Naive Bayes), and sentiment analysis (VADER) to give meaningful insights from raw text data.

---

## Dataset

- File: `blogs.csv`
- Columns:
  - `Data`: The content of the blog post.
  - `Labels`: The category it belongs to (e.g., Tech, Sports, Lifestyle, etc.)

---

## Tasks Performed

### 1. Data Exploration & Preprocessing
- Loaded and explored the structure and class distribution.
- Cleaned and tokenized the text:
  - Lowercased all text
  - Removed punctuation, stopwords, and extra whitespaces
  - Lemmatized words for uniformity
- Converted text to numerical format using TF-IDF Vectorizer

### 2. Naive Bayes Text Classification
- Split dataset into training and testing (80/20 split, stratified by category)
- Used Multinomial Naive Bayes for classification
- Evaluated using:
  - Accuracy, Precision, Recall, F1-Score
  - Confusion Matrix

### 3. Sentiment Analysis
- Applied VADER sentiment analysis
- Categorized each post as:
  - Positive (compound > 0.05)
  - Negative (compound < -0.05)
  - Neutral (in between)
- Visualized:
  - Pie chart of overall sentiment
  - Bar chart of sentiment distribution per category

### 4. Evaluation & Insights
- Classification Report showed model performance
- Confusion matrix showed misclassifications
- Top TF-IDF words per category displayed for interpretability
- Sentiment trends observed per category

---

## Results

| Metric       | Score (approx.) |
|--------------|-----------------|
| Accuracy     | ~85%            |
| Precision    | High across most categories |
| Sentiment    | Mostly neutral or positive |
| Insights     | "Tech" had neutral tones, "Lifestyle" showed positive sentiment |

---

## Key Libraries Used

- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `nltk` (for tokenization, stopwords, lemmatization)
- `sklearn` (TF-IDF, Naive Bayes, evaluation)
- `nltk.sentiment.vader` (VADER sentiment analysis)

---

## Conclusion

This project demonstrates practical NLP techniques for working with unstructured text:
- Naive Bayes is effective for multi-class classification with TF-IDF features.
- VADER provides valuable sentiment analysis for understanding tone and mood.
- Visualizations make it easy to interpret trends and classifier behavior.

---

## Future Improvements

- Use advanced models like Logistic Regression, SVM, or Transformers for better accuracy.
- Apply topic modeling (LDA) to explore themes within blog content.
- Expand sentiment analysis using deep learning (e.g., BERT sentiment classifiers).
