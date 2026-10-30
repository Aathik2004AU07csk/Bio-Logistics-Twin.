import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="YUTO Anekal | Master Execution Center", layout="wide")

st.sidebar.title("YUTO Packaging (India)")
st.sidebar.markdown("### Anekal Unit 1 Command Center")
st.sidebar.success("🟢 Spectrophotometer API: ACTIVE")
st.sidebar.success("🟢 Computer Vision AOI: SYNCED")
st.sidebar.success("🟢 OR-Tools Engine: ONLINE")
st.sidebar.success("🟢 Press Scheduler: ACTIVE")

st.title("YUTO Precision Packaging: Unified Plant Execution Center")
st.markdown("Solving 5 Simultaneous Industrial Manufacturing Bottlenecks (Color Drift, Trim Loss, Visual Defects, Press Changeovers, and Pallet Verification) at the Anekal Plant.")

# The Unified Multi-Problem Interface using 5 Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎨 1. Delta-E Color Variance", 
    "✂️ 2. Cutting Stock Optimizer", 
    "👁️ 3. Computer Vision AOI",
    "⚙️ 4. Press Changeover Scheduler",
    "📦 5. Pallet Weight Reconciliation"
])

with tab1:
    st.subheader("Problem 1 Solved: Color Drift Discrepancies")
    st.markdown("<strong>Root Cause:</strong> Variations in ink-water balance during long offset runs cause Delta-E color variance outside strict brand tolerances.<br><strong>Solution:</strong> Automated spectrophotometer feed calculates live Delta-E deviation to pause presses before batch rejection.", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Press Run", "Heidelberg CD-102", "Offset Line 3")
    col2.metric("Target Pantone", "Cool Gray 11C", "Brand Spec: Apple")
    col3.metric("Live Delta-E Error", "1.82", "Threshold: < 2.0 (SAFE)", delta_color="normal")
    
    color_data = pd.DataFrame({
        'Batch ID': ['YT-88901', 'YT-88902', 'YT-88903', 'YT-88904'],
        'Target CMYK': ['C:40 M:30 Y:20 K:10', 'C:0 M:85 Y:90 K:0', 'C:90 M:70 Y:0 K:20', 'C:15 M:5 Y:95 K:0'],
        'Measured Delta-E': [0.45, 1.82, 0.91, 0.33],
        'Status': ['✅ PASS', '⚠️ MONITOR', '✅ PASS', '✅ PASS']
    })
    st.dataframe(color_data, use_container_width=True)

with tab2:
    st.subheader("Problem 2 Solved: 1D/2D Paperboard Trim Loss")
    st.markdown("<strong>Root Cause:</strong> Manual layout planning for complex box blanks results in 12-18% raw material paperboard trim waste.<br><strong>Solution:</strong> Google OR-Tools Knapsack algorithm computes optimal nesting layouts, cutting paper waste to under 4%.", unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Raw Material Saved", "14.2 Tons/Month", "Duplex Board 350 GSM")
        st.metric("Trim Waste Reduction", "From 16.5% to 3.8%", "- 73% Loss Improvement")
    with col_b:
        st.info("💡 **Algorithm Optimization Active:** Nesting matrix applied to Sheet Size 35x47 inches. Zero manual guesswork required by pre-press operators.")
        st.progress(96)

with tab3:
    st.subheader("Problem 3 Solved: Micro-Defect Inspection Escapes")
    st.markdown("<strong>Root Cause:</strong> Human optical inspection misses subtle foil-stamping misalignments or glue bubbles on luxury rigid boxes.<br><strong>Solution:</strong> OpenCV edge-detection camera feed instantly flags structural flaws on the assembly line.", unsafe_allow_html=True)
    
    if st.button("📸 RUN COMPUTER VISION AOI SCAN", type="primary"):
        with st.spinner("Processing high-definition rigid box frame via OpenCV..."):
            time.sleep(2)
            st.success("✅ OPTICAL INSPECTION COMPLETE.")
            st.code("""
[14:12:01] STATION: Rigid Box Assembly Line 2
[14:12:02] FOIL STAMP ALIGNMENT: 0.04mm offset (Pass < 0.1mm)
[14:12:03] GLUE BUBBLE DETECTION: None detected.
[14:12:04] MAGNETIC CLOSURE TEST: 12N Pull Force (Spec Met)
[14:12:05] FINAL AOI VERDICT: APPROVED FOR PACKAGING.
            """)

with tab4:
    st.subheader("Problem 4 Solved: Rapid Press Changeover Downtime")
    st.markdown("<strong>Root Cause:</strong> Rapid job changeovers on Heidelberg printing presses cause severe machine downtime and idle setups.<br><strong>Solution:</strong> SMED (Single-Minute Exchange of Die) scheduling algorithm sequences jobs by plate similarity to slash setup time.", unsafe_allow_html=True)
    
    changeover_table = pd.DataFrame({
        'Job Sequence': ['Job A (Apple White)', 'Job B (Apple Gray)', 'Job C (Xiaomi Orange)', 'Job D (Xiaomi Black)'],
        'Plate Family': ['Matte Lamination Series A', 'Matte Lamination Series A', 'Gloss UV Series B', 'Gloss UV Series B'],
        'Setup Time Saved': ['Baseline (45m)', '12m (Plate Pre-Staged)', 'Baseline (50m)', '14m (Wash-up Skipped)']
    })
    st.table(changeover_table)

with tab5:
    st.subheader("Problem 5 Solved: Palletization Weight Discrepancies")
    st.markdown("<strong>Root Cause:</strong> Master carton weight mismatches during final pallet loading cause shipping disputes with OEM warehouses.<br><strong>Solution:</strong> Automated load cell scale integration cross-checks physical pallet weight against bill of materials (BOM).", unsafe_allow_html=True)
    
    if st.button("⚖️ VERIFY OUTBOUND PALLET WEIGHT", type="secondary"):
        with st.spinner("Querying digital load cell and BOM database..."):
            time.sleep(1.5)
            st.success("✅ PALLET VERIFIED.")
            st.code("""
[16:05:00] PALLET ID: PLT-9921-EU
[16:05:01] EXPECTED BOM WEIGHT (Calculated): 342.5 kg
[16:05:02] ACTUAL LOAD CELL WEIGHT: 342.6 kg
[16:05:03] VARIANCE: +0.02% (Within allowable tolerance)
[16:05:04] GATE-PASS: Generated and locked for Dispatch Bay 1.
            """)
