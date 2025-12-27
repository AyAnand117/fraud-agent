import pandas as pd

# Load training data

X_train = pd.read_csv("data/processed/X_train.csv")
X_test = pd.read_csv("data/processed/X_test.csv")
y_train = pd.read_csv("data/processed/y_train.csv")
y_test = pd.read_csv("data/processed/y_test.csv")

print("Data loaded successfully")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

# ------------------------------
# Logistic Regression Model
# ------------------------------

from sklearn.linear_model import LogisticRegression

# Initialize the model
model = LogisticRegression(max_iter=1000, class_weight="balanced")

# Train the model 
model.fit(X_train, y_train.values.ravel())

print("Model training completed")

# Predict on test data
y_pred = model.predict(X_test)

print("Predictions Completed")

y_prob = model.predict_proba(X_test)[:,1]
print("Sample fraud probabilities:")
print(y_prob[:20])

# ------------------------------
# Model Evaluation
# ------------------------------

from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)


print("\n--- Model Evaluation ---")
print(f"Accuracy : {accuracy}")
print(f"Precision : {precision}")
print(f"Recall : {recall}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ------------------------------
# Interpret model features
# ------------------------------

feature_importance = pd.DataFrame({
    "feature": X_train.columns,
    "coefficient": model.coef_[0]
    }).sort_values(by="coefficient", ascending = False)

print("\nFeature Importance:")
print(feature_importance)

# Saving the trained model
import joblib
import os

# Create models folder
os.makedirs("models", exist_ok=True)

# Save trained model
joblib.dump(model, "models/fraud_model.pkl")

print("\nModel saved to models/fraud_model.pkl")





