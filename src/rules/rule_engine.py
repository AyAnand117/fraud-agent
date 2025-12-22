class FraudRuleEngine:
    def __init__(self):
        self.rules = {
            "HIGH_AMOUNT": self.high_amount,
            "ODD_HOUR": self.odd_hour,
            "FOREIGN_COUNTRY": self.foreign_country
        }

    def evaluate(self, transaction):
        triggered_rules = []
        risk_score = 0.0

        for rule_name, rule_func in self.rules.items():
            if rule_func(transaction):
                triggered_rules.append(rule_name)
                risk_score += 0.3

        risk_score = min(risk_score, 1.0)

        return {
            "is_fraud": risk_score >= 0.6,
            "risk_score": round(risk_score, 2),
            "triggered_rules": triggered_rules
        }

    def high_amount(self, transaction):
        return transaction["amount"] > 1000

    def odd_hour(self, transaction):
        hour = transaction["timestamp"].hour
        return hour < 5 or hour > 23

    def foreign_country(self, transaction):
        return transaction["country"] != transaction["home_country"]
