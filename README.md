# README - COVID-19 Text Classification Project

This notebook classifies COVID-19 research papers into 5 topics (A–E) using machine learning.

## ✅ What’s Done

* Used two types of input:

  * `clean_abstract`
  * `full_text` (title + abstract)

* Text cleaned and vectorized with TF-IDF

* Trained Logistic Regression models on both versions

* Evaluated using Accuracy, F1, and 10-fold CV

* Saved models + confusion matrix plotted

## 📊 Results

| Input              | Accuracy | F1 Score |
| ------------------ | -------- | -------- |
| Abstract only      | 0.795    | 0.794    |
| Full text (better) | 0.825    | 0.823    |

## 📁 Output Files

* `model_TF-IDF+Abstract.pkl`
* `model_TF-IDF+Full_Text.pkl`

## ▶️ How to Run

Just open the notebook and run all cells.
Final results + plots will be shown at the end.
