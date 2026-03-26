import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras import Input
from sklearn.preprocessing import MinMaxScaler

# Load data
df = pd.read_csv("ev_data.csv")

# Select features
features = df[["voltage", "temperature", "current", "cycles"]]

# Normalize data
scaler = MinMaxScaler()
scaled = scaler.fit_transform(features)

# Create sequences for LSTM
def create_sequences(data, seq_length=10):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length][1])  # Predict temperature trend
    return np.array(X), np.array(y)

X, y = create_sequences(scaled)

# Build LSTM model (FIXED)
model = Sequential([
    Input(shape=(X.shape[1], X.shape[2])),
    LSTM(50, return_sequences=True),
    LSTM(50),
    Dense(1)
])

# Compile model
model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(X, y, epochs=5, batch_size=16)

# Save model (new format)
model.save("lstm_model.keras")

print("✅ LSTM model trained and saved successfully!")
