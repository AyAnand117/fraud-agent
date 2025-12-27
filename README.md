# Fraud Detection System (Rule-Based + Machine Learning)

## Overview
This project is an end-to-end fraud detection system built using Python.  
It starts with a rule-based fraud engine, progresses through synthetic data generation and exploratory data analysis (EDA), and evolves into a machine learning–based fraud prediction pipeline. The project is designed to mirror real-world fraud detection workflows used in financial systems.

The system is being actively extended toward API-based deployment using FastAPI.

---

## Project Structure

```

fraud-agent/
├── src/
│ ├── rules/
│ │ └── engine.py
│ ├── data_generator.py
│ ├── eda.py
│ ├── train_model.py
│ └── prediction_pipeline.py
├── api/
│ ├── init.py
│ └── main.py
├── data/
│ ├── raw/
│ │ └── transactions.csv
│ └── processed/
│ ├── transactions_processed.csv
│ ├── X_train.csv
│ ├── X_test.csv
│ ├── y_train.csv
│ └── y_test.csv
├── models/
│ └── logistic_regression.pkl
├── README.md
└── .gitignore

```

---

## Features Implemented

### 1. Rule-Based Fraud Engine
- Detects fraud using explainable rules such as:
  - High transaction amount
  - Foreign country usage
  - Unusual transaction timing
- Outputs a risk score and triggered rules
- Serves as a baseline fraud detection approach

---

### 2. Synthetic Data Generation
- Generates realistic transaction data due to lack of real-world datasets
- Includes both fraudulent and non-fraudulent transactions
- Simulates real-world fraud characteristics such as:
  - Class imbalance
  - Noisy and overlapping patterns
- Output saved as CSV for downstream use

---

### 3. Exploratory Data Analysis (EDA)
- Loaded and analyzed transaction data
- Checked data types, missing values, and fraud distribution
- Identified important fraud-related features
- Observed strong class imbalance (fraud is rare)

---

### 4. Feature Engineering & Preprocessing
- Converted timestamps into time-based features
- Engineered fraud-relevant indicators
- Avoided data leakage by removing label-derived features
- Saved clean, processed datasets for ML training

---

### 5. Machine Learning Model
- Trained a Logistic Regression model for fraud classification
- Handled class imbalance using `class_weight="balanced"`
- Evaluated model using:
  - Precision
  - Recall
  - Accuracy
  - ROC-AUC
- Identified and fixed data leakage issues during experimentation

---

### 6. Fraud Prediction Pipeline
- Built a reusable prediction pipeline that:
  - Validates input data
  - Applies preprocessing and feature engineering
  - Loads trained ML model
  - Outputs fraud probability and prediction
- Designed to be production-ready and API-safe

---

### 7. FastAPI Preparation
- Created API folder structure
- Implemented FastAPI app skeleton
- Added `/predict` endpoint placeholder
- Ready for full ML integration in next iteration

---

## Assumptions
- Synthetic data is used due to lack of publicly available fraud datasets
- Fraud patterns are partially rule-driven for learning purposes
- Probability thresholding is used for fraud classification
- The system is designed for educational and portfolio demonstration

---

## Key Learnings
- Importance of avoiding data leakage in ML
- Handling class imbalance in fraud detection
- Why accuracy alone is misleading for fraud problems
- Difference between rule-based and ML-based systems
- How to design ML pipelines for production use

---

## Next Steps
- Integrate ML pipeline into FastAPI `/predict` endpoint
- Add Pydantic request/response schemas
- Compare rule-based vs ML system performance
- Add transaction velocity–based fraud features
- Deploy API locally and test using HTTP requests

---

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI (in progress)
- Git & GitHub
- Visual Studio 2022
