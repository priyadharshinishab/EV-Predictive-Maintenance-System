import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv(r"ev_data.csv")

# Features
X = df[["voltage", "temperature", "current", "cycles"]]

# Dummy labels (for demo)
y_failure = (df["temperature"] > 45).astype(int)

# Train models
failure_model = RandomForestClassifier()
failure_model.fit(X, y_failure)

anomaly_model = IsolationForest()
anomaly_model.fit(X)

health_model = LinearRegression()
health_model.fit(df[["voltage", "temperature", "cycles"]], df["temperature"])

# Save models
joblib.dump(failure_model, "failure_model.pkl")
joblib.dump(anomaly_model, "anomaly_model.pkl")
joblib.dump(health_model, "health_model.pkl")

print("✅ Models saved successfully!")
