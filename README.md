# Group Assignment 1 - Classification: COVID-19 Text Classification Project

This project classifies COVID-19 research papers into five predefined topics (A–E) using classical machine learning models and different text representations.

## ✅ What’s Done

* **Two input types evaluated:**
  * `clean_abstract`
  * `full_text` (title + abstract)

* **Text preprocessing and vectorization:**
  * TF-IDF (unigram and bigram)
  * CountVectorizer (BoW)

* **Models trained and compared:**
  * Logistic Regression
  * Logistic Regression (GridSearchCV)
  * Naive Bayes
  * Random Forest

* **Feature types tested:**
  * TF-IDF
  * TF-IDF + N-gram (1,2)
  * All models run for both input types

* **Evaluation metrics:**
  * Accuracy
  * Macro F1 Score
  * 10-fold cross-validation (macro F1 mean ± std)
  * Confusion Matrix visualized for every model

## 📊 Results Summary

A total of **14 experiments** (7 model variants × 2 input types) were conducted.

| Input Type | Model                               | Accuracy | Macro F1 | CV F1 Mean | CV F1 Std |
| ---------- | ----------------------------------- | -------- | -------- | ---------- | --------- |
| Abstract   | TF-IDF + Logistic Regression        | 0.830    | 0.829    | 0.8049     | 0.0346    |
| Abstract   | TF-IDF N-gram + Naive Bayes         | 0.830    | 0.823    | 0.7588     | 0.0283    |
| Abstract   | BoW + Naive Bayes                   | 0.825    | 0.823    | 0.7639     | 0.0485    |
| Abstract   | TF-IDF N-gram + Logistic Regression | 0.855    | 0.851    | 0.8016     | 0.0284    |
| Abstract   | TF-IDF + LR (GridSearchCV)          | 0.850    | 0.847    | 0.8032     | 0.0381    |
| Abstract   | TF-IDF + Random Forest              | 0.865    | 0.862    | 0.8036     | 0.0356    |
| Abstract   | TF-IDF Ngram + Random Forest        | 0.850    | 0.848    | 0.8047     | 0.0466    |
| Full Text  | TF-IDF + Logistic Regression        | 0.855    | 0.854    | 0.8163     | 0.0352    |
| Full Text  | TF-IDF N-gram + Naive Bayes         | 0.840    | 0.833    | 0.7746     | 0.0217    |
| Full Text  | BoW + Naive Bayes                   | 0.820    | 0.818    | 0.7821     | 0.0409    |
| Full Text  | TF-IDF N-gram + Logistic Regression | 0.865    | 0.862    | 0.8186     | 0.0294    |
| Full Text  | TF-IDF + LR (GridSearchCV)          | 0.865    | 0.860    | 0.8213     | 0.0370    |
| Full Text  | TF-IDF + Random Forest              | 0.860    | 0.859    | 0.8184     | 0.0395    |
| Full Text  | TF-IDF Ngram + Random Forest        | 0.865    | 0.864    | 0.8131     | 0.0418    |

---

✅ **Best performing model**:

> `TF-IDF Ngram + Random Forest` on **Full Text**, with
> **Accuracy = 0.865**, **Macro F1 = 0.864**, **CV F1 Mean = 0.8131**

## 📁 Output

* Confusion matrix plot for each model
* Final comparison chart: Accuracy vs Macro F1 across all 14 runs
* Table of scores saved in notebook variable `summary_df`

## ▶️ How to Run

1. Make sure the following CSVs are in the root directory:
   - `covid19_preprocessed_dataset.csv`
   - `covid19_combined_text_dataset.csv`

2. Open `NLP_COVID19_dual_input_comparison.ipynb`

3. Run all cells.

All results, metrics, confusion matrices, and comparison plots will be generated at the end.



# Group Assignment 2 - Clustering: COVID-19 Topic Discovery Project

This project explores unsupervised topic discovery for COVID-19 research abstracts using multiple embedding methods and clustering algorithms.

## ✅ What’s Done

- **Text embedding methods:**
  - TF-IDF
  - Doc2Vec
  - sBERT

- **Clustering algorithms applied:**
  - KMeans
  - Hierarchical Clustering

- **Evaluation metrics:**
  - Silhouette Score
  - Cohen's Kappa (vs. true labels)

- **Cluster interpretation techniques:**
  - Keyword frequency & bar charts
  - WordCloud visualization
  - Named Entity Recognition (NER)
  - TF-IDF heatmaps (Correct vs Misclassified samples)

## 📊 Results Summary

A selection of clustering combinations were tested.

| Model                | Kappa   | Silhouette |
|---------------------|---------|------------|
| sBERT + Spectral     | 0.1325  | 0.0817     |
| sBERT + KMeans       | 0.0375  | 0.0876     |
| Doc2Vec + KMeans     | -0.0638 | 0.0495     |
| Doc2Vec + Spectral   | 0.0125  | 0.0331     |
| w2v + EM             | -0.1463 | 0.1019     |
| BoW + EM             | 0.2900  | N/A        |

**Best performing (alignment to labels):**  
**sBERT + Spectral**, with Kappa = 0.1325  
(though all models show weak alignment, as expected in unsupervised clustering)


## 📁 Output

- Cluster distribution plots
- Top keywords and WordCloud for each cluster
- Named Entity analysis per cluster
- TF-IDF heatmaps: misclassified vs correct clusters

## ▶️ How to Run

1. Make sure the following CSV is in the root directory:
   - `covid19_preprocessed_dataset.csv`

2. Open `NLP_COVID19_dual_input_comparison.ipynb`

3. Run all cells. All metrics, cluster interpretations, and plots will be generated.

