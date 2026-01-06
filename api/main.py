from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class TransactionInput(BaseModel):
    amount : float
    timestamp : str
    country : str
    home_country : str

app = FastAPI(
    title = "Fraud Detection API",
    description = "ML-based fraud detection with rule explanations",
    version = "1.0"
    )

from src.prediction_pipeline import predict_fraud
from src.rules.rule_engine import FraudRuleEngine

@app.post("/predict")
def predict(transaction: TransactionInput):

    # Convert Pydantic model to dict
    txn_dict = transaction.dict()

    # ML prediction
    ml_result = predict_fraud(txn_dict)

    # Rule-Based Explanation
    rule_engine = FraudRuleEngine()
    rule_result = rule_engine.evaluate({
        "amount": txn_dict["amount"],
        "timestamp": __import__("datetime").datetime.fromisoformat(txn_dict["timestamp"]),
        "country": txn_dict["country"],
        "home_country": txn_dict["home_country"]
        })
    
    return {
        "fraud_probability": ml_result["fraud_probability"],
        "prediction": ml_result["prediction"],
        "rule_based_flags": rule_result["triggered_rules"],
        "rule_risk_score": rule_result["risk_score"]
        }

@app.get("/")
def health():
    return{"status":"Fraud Detection API running"}



