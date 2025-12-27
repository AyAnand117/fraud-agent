import pandas as pd
import joblib

MODEL_PATH = "models/fraud_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

def preprocess_transaction(transaction: dict):
    df = pd.DataFrame([transaction])

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Time features 
    df["transaction_hour"] = df["timestamp"].dt.hour
    df["transaction_day"] = df["timestamp"].dt.dayofweek

    # Fraud Features
    df["high_amount"] = (df["amount"]>1000).astype(int)
    df["foreign_transaction"] = (
        df["country"] != df["home_country"]).astype(int)

    FEATURES = ["amount", "transaction_hour", "transaction_day", "high_amount", "foreign_transaction"]

    return df[FEATURES]

# Add Validation functions

REQUIRED_FIELDS = {
    "amount": (int, float),
    "timestamp": str,
    "country": str,
    "home_country": str
    }

def validate_transaction(transaction: dict):
    for field, field_type in REQUIRED_FIELDS.items():
        if field not in transaction:
            raise ValueError(f"Missing required field:{field}")

        if not isinstance(transaction[field], field_type):
            raise TypeError(f"Invalid type for field: {field}")

    if transaction["amount"]<0:
            raise ValueError("Amount cannot be negative")


# Prediction function

def predict_fraud(transaction: dict):
    validate_transaction(transaction)

    model = load_model()
    X = preprocess_transaction(transaction)

    fraud_probability = model.predict_proba(X)[0][1]

    return {
        "fraud_probability": round(fraud_probability,3),
        "prediction": "Fraud" if fraud_probability >=0.85 else "NOT FRAUD"
        }


if __name__ == "__main__":
    sample_transaction = {
        "amount" : 2200,
        "timestamp": "2025-08-20T01:30:00",
        "country": "FR",
        "home_country":"US"
        }

    result = predict_fraud(sample_transaction)
    print(result)


