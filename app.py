import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Thermal Control Tower", layout="wide", initial_sidebar_state="expanded")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Anekal Bio-Logistics")
st.sidebar.markdown("### Thermal Control Tower")
st.sidebar.divider()
page = st.sidebar.radio("Navigation Menu", [
    "1. Live Fleet Tracking (Process A)", 
    "2. Thermodynamic Twin (Process B)", 
    "3. Intervention System (Process C)"
])
st.sidebar.divider()
st.sidebar.success("🟢 OpenWeather API: ACTIVE")
st.sidebar.success("🟢 GPS Telemetry: ACTIVE")
st.sidebar.success("🟢 Twilio Webhook: READY")

# --- PAGE 1: LIVE FLEET TRACKING ---
if page == "1. Live Fleet Tracking (Process A)":
    st.title("Live Telemetry & K-Means Risk Clustering")
    st.markdown("Real-time monitoring of high-risk biologics transit in the Bommasandra/Anekal corridor.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Live GPS Fleet Map**")
        # Simulating multiple trucks near Bommasandra and BLR airport
        map_data = pd.DataFrame({
            'lat': [12.8159, 12.8350, 13.1989],
            'lon': [77.6775, 77.6550, 77.7068]
        })
        st.map(map_data, zoom=10)
        
    with col2:
        st.markdown("**Active Fleet Status**")
        st.error("**AWB: 892-BLR-441** | Loc: Bommasandra | Risk: LEVEL 3")
        st.warning("**AWB: 332-BLR-110** | Loc: Electronic City | Risk: LEVEL 2")
        st.success("**AWB: 994-BLR-775** | Loc: BLR Tarmac | Risk: LEVEL 1")
        
        st.divider()
        st.markdown("**K-Means Clustering Metrics**")
        st.metric(label="Current Queue Delay", value="1 hr 15 mins", delta="15 mins above average", delta_color="inverse")
        st.metric(label="Ambient Heat", value="38.4 °C")

# --- PAGE 2: THERMODYNAMIC DIGITAL TWIN ---
elif page == "2. Thermodynamic Twin (Process B)":
    st.title("Thermodynamic Mass-Transfer Prediction")
    st.markdown("Simulating Fourier's Law of Heat Conduction based on live packaging R-values.")
    
    # Interactive Slider for the prototype demonstration
    st.markdown("### 🎛️ Interactive Prototype Controls")
    spike_temp = st.slider("Simulate Tarmac Ambient Temperature (°C)", min_value=25.0, max_value=45.0, value=38.4, step=0.5)
    
    # Mathematical simulation based on the slider input
    time_steps = np.arange(0, 180, 1) 
    base_external = 25 + (time_steps / 20) 
    # Injecting the user's selected spike temperature into the algorithm
    external_temp = np.where(time_steps > 90, spike_temp + np.random.normal(0, 1.0, len(time_steps)), base_external)
    
    # Calculating internal temperature rise
    internal_temp = 2.0 + (0.015 * time_steps) + (0.0004 * external_temp ** 2)
    
    chart_data = pd.DataFrame({
        'External Temp (°C)': external_temp,
        'Internal Temp (°C)': internal_temp,
        'Critical Threshold (8°C)': np.full(len(time_steps), 8.0)
    })
    
    # Calculate dynamic time to breach
    breach_index = np.argmax(internal_temp >= 8.0)
    if breach_index > 0:
        minutes_to_breach = 180 - breach_index
        time_str = f"00:{minutes_to_breach}:12"
        alert_status = "- Critical"
    else:
        time_str = "SAFE"
        alert_status = "Stable"
    
    met1, met2, met3 = st.columns(3)
    met1.metric(label="External Heat", value=f"{spike_temp} °C")
    met2.metric(label="Internal Payload", value=f"{internal_temp[-1]:.1f} °C")
    
    if time_str != "SAFE":
        met3.metric(label="TIME TO BREACH (8.0°C)", value=time_str, delta=alert_status, delta_color="inverse")
    else:
        met3.metric(label="TIME TO BREACH (8.0°C)", value=time_str, delta="Secured", delta_color="normal")
        
    st.line_chart(chart_data, color=["#FF4B4B", "#1E88E5", "#FF0000"])

# --- PAGE 3: INTERVENTION SYSTEM ---
elif page == "3. Intervention System (Process C)":
    st.title("Automated Ground Execution (Twilio API)")
    st.markdown("Bypassing human dispatch to prevent thermodynamic failure.")
    
    st.warning("⚠️ SYSTEM ALERT: Thermodynamic breach predicted in < 45 minutes for AWB #892-BLR-441.")
    
    # Interactive Button to simulate API firing
    if st.button("🚨 TRIGGER EMERGENCY PROTOCOL (Send WhatsApp Command)", use_container_width=True):
        with st.spinner("Connecting to Twilio Webhook..."):
            time.sleep(2) # Simulating network delay
            st.success("API Payload Delivered Successfully to Ground Crew via WhatsApp.")
            
            alert_box = f"""
            **⚠️ CRITICAL INTERVENTION COMMAND ⚠️**
            * **Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}
            * **Target:** AWB #892-BLR-441
            * **Location:** Tarmac Zone C, BLR
            * **Payload:** Monoclonal Antibodies ($2.1M)
            * **Action Required:** Move pallet to Cold Room 4 immediately. 
            
            ---
            **📱 Ground Crew Automated Response:**
            > *✓ Status: Read (14:17 IST)*  
            > *✓ Reply: "CONFIRM - Pallet secured at 14:18 IST"*
            """
            st.info(alert_box)
    else:
        st.info("System is standing by. Click the button above to simulate the automated API execution.")
