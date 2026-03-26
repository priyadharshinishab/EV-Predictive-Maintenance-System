import joblib
import numpy as np

# Load models
clf = joblib.load(r"C:\Users\priya\EV Predictive Maintenance System\model.pkl")
anomaly_model = joblib.load(r"C:\Users\priya\EV Predictive Maintenance System\anomaly.pkl")
health_model = joblib.load(r"C:\Users\priya\EV Predictive Maintenance System\health.pkl")

def predict_failure(voltage, temperature, current, cycles):
    data = np.array([[voltage, temperature, current, cycles]])
    return clf.predict(data)[0]

def detect_anomaly(voltage, temperature, current, cycles):
    data = np.array([[voltage, temperature, current, cycles]])
    return anomaly_model.predict(data)[0]

def predict_health(voltage, temperature, cycles):
    data = np.array([[voltage, temperature, cycles]])
    return health_model.predict(data)[0]