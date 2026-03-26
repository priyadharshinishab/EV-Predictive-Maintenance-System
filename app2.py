import streamlit as st
import pandas as pd

from lstm_utils import (
    predict_failure,
    detect_anomaly,
    predict_health,
    predict_temperature_trend
)

from alerts import send_alert

st.set_page_config(page_title="EV AI Dashboard", layout="wide")

st.title("🚗 EV Predictive Maintenance System")

# Sidebar
st.sidebar.header("Input Parameters")

voltage = st.sidebar.slider("Voltage", 40.0, 60.0, 48.0)
temperature = st.sidebar.slider("Temperature", 20.0, 60.0, 35.0)
current = st.sidebar.slider("Current", 0.0, 20.0, 10.0)
cycles = st.sidebar.slider("Charge Cycles", 100, 1000, 500)

# Predictions
failure = predict_failure(voltage, temperature, current, cycles)
anomaly = detect_anomaly(voltage, temperature, current, cycles)
health = predict_health(voltage, temperature, cycles)
trend = predict_temperature_trend(voltage, temperature, current, cycles)

# Display
st.subheader("🔍 Results")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Battery Health (%)", f"{health:.2f}")
col2.metric("Failure Risk", "YES" if failure == 1 else "NO")
col3.metric("Anomaly", "Anomaly" if anomaly == -1 else "Normal")
col4.metric("Temp Trend", f"{trend:.2f}")

# DEBUG (REMOVE LATER)
st.write("Failure:", failure)
st.write("Anomaly:", anomaly)

# 🚨 ALERT SYSTEM (FINAL FIX)
if st.button("🚨 Check & Send Alert"):

    if failure == 1 or anomaly == -1 or temperature > 45:

        alert_msg = f"""
        🚨 ALERT!

        Voltage: {voltage}
        Temperature: {temperature}
        Current: {current}
        Cycles: {cycles}

        ⚠️ Risk Detected!
        """

        send_alert(alert_msg)
        st.error("🚨 Alert Sent!")

    else:
        st.success("✅ System Normal")

# Visualization
df = pd.read_csv("ev_data.csv")

st.subheader("📊 Data")
st.line_chart(df["temperature"])
st.line_chart(df["voltage"])
st.dataframe(df.head())
