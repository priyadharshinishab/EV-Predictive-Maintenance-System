import numpy as np
import joblib
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Load models
clf = joblib.load("model.pkl")
anomaly_model = joblib.load("anomaly.pkl")
health_model = joblib.load("health.pkl")
lstm_model = load_model("lstm_model.keras")

# Load scaler (recreate same way as training)
df = pd.read_csv("ev_data.csv")
features = df[["voltage", "temperature", "current", "cycles"]]

scaler = MinMaxScaler()
scaled = scaler.fit_transform(features)

# ----------- ML Predictions -----------

def predict_failure(voltage, temperature, current, cycles):
    data = np.array([[voltage, temperature, current, cycles]])
    return clf.predict(data)[0]

def detect_anomaly(voltage, temperature, current, cycles):
    data = np.array([[voltage, temperature, current, cycles]])
    return anomaly_model.predict(data)[0]

def predict_health(voltage, temperature, cycles):
    data = np.array([[voltage, temperature, cycles]])
    return health_model.predict(data)[0]

# ----------- LSTM Prediction -----------

def predict_temperature_trend(voltage, temperature, current, cycles):
    input_data = np.array([[voltage, temperature, current, cycles]])
    scaled_input = scaler.transform(input_data)

    # Repeat to form sequence (fake sequence for demo)
    sequence = np.repeat(scaled_input, 10, axis=0)
    sequence = sequence.reshape(1, 10, 4)

    prediction = lstm_model.predict(sequence)
    return prediction[0][0]