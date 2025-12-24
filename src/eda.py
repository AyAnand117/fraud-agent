import pandas as pd

DATA_PATH ="data/raw/transactions.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully")
print("Shape of dataset:", df.shape)
print(df.head())

print("\n--- Column Info ---")
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Fraud Distribution ---")
print(df["is_fraud"].value_counts())

print("\n--- Amount Statistics ---")
print(df['amount'].describe())

TARGET = "is_fraud"

# ------------------------------
# Preprocessing Functions
# ------------------------------

def preprocess_dataframe(df):
    df = df.copy()

    # Convert timestamps to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Create time-based features
    df["transaction_hour"] = df["timestamp"].dt.hour
    df["transaction_day"] = df["timestamp"].dt.dayofweek

    return df


df = preprocess_dataframe(df)
print(df.head())

# ------------------------------
# Feature Engineering
# ------------------------------

def add_fraud_features(df):
    df = df.copy()

    # High Amount Flag
    df["high_amount"] = (df["amount"]>1000).astype(int)

    # Foreign Transaction flag
    df["foreign_transaction"] = (df["country"] != df["home_country"]).astype(int)

    return df

df = add_fraud_features(df)

print("\n--- After Feature Engineering ---")
print(df[[
    "amount",
    "high_amount",
    "foreign_transaction",
    "transaction_hour",
    "is_fraud"]].head())

# ------------------------------
# Save processd data
# ------------------------------
OUTPUT_PATH = "data/processed/transactions_processed.csv"
df.to_csv(OUTPUT_PATH, index=False)

print(f"\nProcessed dataset saved to {OUTPUT_PATH}")


# ------------------------------
# Feature Selection
# ------------------------------

FEATURES = [
    "amount",
    "transaction_hour",
    "transaction_day",
    "high_amount",
    "foreign_transaction"
    ]
TARGET ="is_fraud"
X = df[FEATURES]
y =df[TARGET]

print("\nSelected Features:")
print(X.head())

print("n\Target Variable:")
print(y.value_counts())

# ------------------------------

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test =train_test_split(
    X, y, test_size =0.2, 
    random_state=42, stratify =y
    )

print("\nTrain/Test SPlit:")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

# ------------------------------

X_train.to_csv("data/processed/X_train.csv", index=False)
X_test.to_csv("data/processed/X_test.csv", index=False)
y_train.to_csv("data/processed/y_train.csv", index=False)
y_test.to_csv("data/processed/y_test.csv", index=False)

print("\nTrain/Test Datasets saved in data/processed/")
