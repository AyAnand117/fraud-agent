from datetime import datetime
from rules.rule_engine import FraudRuleEngine

engine = FraudRuleEngine()

sample_transaction = {
    "transaction_id": "TXN001",
    "user_id": "USER123",
    "amount": 1500,
    "timestamp": datetime.now(),
    "merchant": "Online Store",
    "country": "FR",
    "home_country": "US"
}

result = engine.evaluate(sample_transaction)
print(result)
