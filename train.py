import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.linear_model import LinearRegression
import joblib

# Generate synthetic EV data
np.random.seed(42)

data = pd.DataFrame({
    "voltage": np.random.normal(48, 2, 500),
    "temperature": np.random.normal(35, 5, 500),
    "current": np.random.normal(10, 3, 500),
    "cycles": np.random.randint(100, 1000, 500)
})

# Failure condition
data["failure"] = (data["temperature"] > 45).astype(int)

# Health score
data["health"] = 100 - (data["cycles"] * 0.05 + data["temperature"] * 0.2)

# Save dataset
data.to_csv("ev_data.csv", index=False)

# Features
X = data[["voltage", "temperature", "current", "cycles"]]
y = data["failure"]

# Train classification model
clf = RandomForestClassifier()
clf.fit(X, y)

# Train anomaly model
anomaly_model = IsolationForest()
anomaly_model.fit(X)

# Train regression model
reg = LinearRegression()
reg.fit(X[["voltage", "temperature", "cycles"]], data["health"])

# Save models
joblib.dump(clf, "model.pkl")
joblib.dump(anomaly_model, "anomaly.pkl")
joblib.dump(reg, "health.pkl")

print("Models trained and saved successfully!")