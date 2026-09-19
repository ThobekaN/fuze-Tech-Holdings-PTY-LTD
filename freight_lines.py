import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Custom Title Header for Multi-Page Rendering
st.title("🚚 LEGACY FREIGHT LINES — B2B LogTech Platform")
st.markdown("### *Fuze Tech Holdings Innovation: Real-Time SADC Logistics Management*")
st.divider()

# 2. Database Simulation (Handles variable fleet sizes dynamically)
@st.cache_data
def load_initial_fleet_data():
    return {
        "Truck_ID": ["LFL-001", "LFL-002", "LFL-003", "LFL-004"],
        "Client_Company": ["Super Group Logistics", "Imperial Transport", "Value Logistics", "Cargo Carriers"],
        "Route": ["JHB -> Gaborone", "JHB -> Windhoek", "JHB -> Lobatse", "JHB -> Gaborone"],
        "Speed_KMH": [0.0, 80.0, 0.0, 70.0],
        "Fuel_Liters": [280.5, 300.0, 195.0, 420.8],
        "BURS_Clearance": ["PROCEED TO BORDER", "HOLD AT STAGING", "HOLD AT STAGING", "PROCEED TO BORDER"]
    }

fleet_data = load_initial_fleet_data()
df = pd.DataFrame(fleet_data)

# 3. Simulation Controls in Sidebar
st.sidebar.subheader("🕹️ Telematics Simulation")
simulate_theft = st.sidebar.button("🚨 Simulate Fuel Theft Event (LFL-001)")

# 4. Top-Level Metrics Panel (Dynamically calculates based on fleet size)
metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric(label="📊 Active Managed Fleet", value=f"{len(df)} Heavy Vehicles", delta="B2B SaaS Model")
with metric_col2:
    cleared_trucks = len(df[df["BURS_Clearance"] == "PROCEED TO BORDER"])
    st.metric(label="🛂 BURS Border Cleared", value=f"{cleared_trucks} / {len(df)} Trucks", delta="Automated Validation")
with metric_col3:
    if simulate_theft:
        st.metric(label="🛡️ System Security Status", value="ALERT", delta="-45L Sudden Drop!", delta_color="inverse")
    else:
        st.metric(label="🛡️ System Security Status", value="SECURE", delta="All Probes Normal")

st.divider()

# 5. Dashboard Grid (Explicit 2-Column Layout Definition)
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📋 Active Fleet Registry & Telematics Status")
    
    # Logic for siphoning anomaly detection (The core Python block)
    if simulate_theft:
        df.loc[df["Truck_ID"] == "LFL-001", "Fuel_Liters"] = 235.5
        df.loc[df["Truck_ID"] == "LFL-001", "Speed_KMH"] = 0
        st.error("🚨 CRITICAL TELEMETRY ALERT: Sudden fuel volume drop detected on LFL-001 while stationary! System flags unauthorized siphoning hazard.")
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("🚧 Automated Border Compliance Engine")
    st.info("ℹ️ Ensuring strict alignment with the 2026 BURS Pre-Border Electronic Mandate.")
    
    for index, row in df.iterrows():
        st.markdown(f"**🆔 Vehicle ID:** {row['Truck_ID']} | **💼 Client:** {row['Client_Company']}")
        if row['BURS_Clearance'] == "PROCEED TO BORDER":
            st.success(f"✅ BURS Clearance Approved. Status: **{row['BURS_Clearance']}**\n\n*Permitted to approach Skilpadsnek Boom.*")
        else:
            st.warning(f"⚠️ BURS Clearance Blocked. Status: **{row['BURS_Clearance']}**\n\n*Action Required: Keep vehicle stationary at Zeerust Staging Area.*")
        st.divider()

st.caption(f"🕒 System timestamp synced: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} SAST | Developed by Thobeka Asanda Ngcobo.")
