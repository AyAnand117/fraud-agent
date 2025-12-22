import random
import uuid
from datetime import datetime, timedelta
import csv
import os

COUNTRIES = ["US", "UK", "FR", "DE", "IN"]
MERCHANTS = ["Amazon", "Walmart", "Target", "Ebay", "AliExpress"]

def generate_transaction(is_fraud=False):
    home_country = random.choice(COUNTRIES)

    if is_fraud:
        amount = random.uniform(1000, 5000)
        country = random.choice([c for c in COUNTRIES if c != home_country])
        hour = random.choice([0, 1, 2, 3, 4, 23])
    else:
        amount = random.uniform(5, 300)
        country = home_country
        hour = random.randint(8, 21)

    timestamp = datetime.now() - timedelta(
        days=random.randint(0, 30),
        hours=hour
    )

    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": f"user_{random.randint(1, 200)}",
        "amount": round(amount, 2),
        "timestamp": timestamp.isoformat(),
        "merchant": random.choice(MERCHANTS),
        "country": country,
        "home_country": home_country,
        "is_fraud": int(is_fraud)
    }

def generate_dataset(n_rows=5000, fraud_ratio=0.05):
    data = []
    for _ in range(n_rows):
        is_fraud = random.random() < fraud_ratio
        data.append(generate_transaction(is_fraud))
    return data

def save_to_csv(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    dataset = generate_dataset()
    save_to_csv(dataset, "data/raw/transactions.csv")
    print("Synthetic dataset generated at data/raw/transactions.csv")





