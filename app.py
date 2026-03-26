import streamlit as st
import pandas as pd
from utils import predict_failure, detect_anomaly, predict_health

st.set_page_config(page_title="EV AI Dashboard", layout="wide")

st.title("🚗 EV Predictive Maintenance System")

# Input Section
st.sidebar.header("Input Parameters")

voltage = st.sidebar.slider("Voltage", 40.0, 60.0, 48.0)
temperature = st.sidebar.slider("Temperature", 20.0, 60.0, 35.0)
current = st.sidebar.slider("Current", 0.0, 20.0, 10.0)
cycles = st.sidebar.slider("Charge Cycles", 100, 1000, 500)

# Predictions
failure = predict_failure(voltage, temperature, current, cycles)
anomaly = detect_anomaly(voltage, temperature, current, cycles)
health = predict_health(voltage, temperature, cycles)

# Display Results
st.subheader("🔍 Results")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Battery Health (%)", f"{health:.2f}")

with col2:
    st.metric("Failure Risk", "YES" if failure == 1 else "NO")

with col3:
    st.metric("Anomaly Status", "Anomaly" if anomaly == -1 else "Normal")

# Load dataset
df = pd.read_csv("ev_data.csv")

st.subheader("📊 Data Visualization")

st.line_chart(df["temperature"])
st.line_chart(df["voltage"])

st.subheader("📋 Sample Data")
st.dataframe(df.head())