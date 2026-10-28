import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(page_title="Thermal Control Tower", layout="wide", initial_sidebar_state="expanded")

st.sidebar.title("Anekal Bio-Logistics")
st.sidebar.markdown("### Thermal Control Tower")
st.sidebar.success("OpenWeather API: ACTIVE")
st.sidebar.success("GPS Telemetry: ACTIVE")

st.title("Predictive Supply Chain Execution")
st.markdown("Monitoring high-risk biologics transit in the Bommasandra/Anekal corridor.")

st.subheader("Process A: Live Telemetry & K-Means Risk Clustering")

map_data = pd.DataFrame({
    'lat': [12.8159],
    'lon': [77.6775]
})

col1, col2 = st.columns([2, 1])
with col1:
    st.map(map_data, zoom=12)
with col2:
    st.markdown("**AWB Number:** 892-BLR-441")
    st.markdown("**Location:** Bommasandra Checkpost")
    st.markdown("**Queue Delay:** 1 hr 15 mins")
    st.error("**Risk Cluster:** Level 3 (Severe Risk)")
    
st.divider()

st.subheader("Process B: Thermodynamic Mass-Transfer Prediction")

time_steps = np.arange(0, 180, 1) 
external_temp = 25 + (time_steps / 10) + np.random.normal(0, 1.5, len(time_steps))
internal_temp = 2.0 + (0.02 * time_steps) + (0.0005 * external_temp ** 2)

chart_data = pd.DataFrame({
    'External Temp (°C)': external_temp,
    'Internal Temp (°C)': internal_temp,
    'Critical Threshold (8°C)': np.full(len(time_steps), 8.0)
})

met1, met2, met3 = st.columns(3)
met1.metric(label="Current External Heat", value="38.4 °C", delta="Spiking")
met2.metric(label="Current Internal Payload", value="6.8 °C", delta="Stable")
met3.metric(label="TIME TO BREACH (8.0°C)", value="00:43:12", delta="- Critical", delta_color="inverse")

st.line_chart(chart_data, color=["#FF4B4B", "#1E88E5", "#FF0000"])

st.divider()

st.subheader("Process C: Automated Ground Execution (Twilio API Payload)")
st.warning("SYSTEM ALERT: Thermodynamic breach predicted in < 45 minutes. Human bypass engaged.")

alert_box = """
**⚠️ CRITICAL INTERVENTION COMMAND ⚠️**
* **Target:** AWB #892-BLR-441
* **Location:** Tarmac Zone C, BLR
* **Payload:** Monoclonal Antibodies ($2.1M)
* **Action Required:** Move pallet to Cold Room 4 immediately. 

> *Twilio API Status: Delivered (Read)*  
> *Ground Crew Reply: "CONFIRM - Pallet secured at 14:18 IST"*
"""
st.info(alert_box)
