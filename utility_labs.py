import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Custom Title Header for Multi-Page Rendering
st.title("⚡ LEGACY UTILITY LABS — B2B GridTech Platform")
st.markdown("### *Fuze Tech Holdings Innovation: Real-Time Prepaid Meter Bypassing Detection*")
st.divider()

# 2. Database Simulation (Handles multi-tenant utility tracking dynamically)
@st.cache_data
def load_smart_meter_data():
    return {
        "Meter_ID": ["MTR-801", "MTR-802", "MTR-803", "MTR-804"],
        "Property_Fund": ["Growthpoint Braamfontein", "Redefine Parktown", "City Property CBD", "Wits Student Housing"],
        "Metered_Usage_kW": [4.2, 0.8, 0.0, 1.5],
        "Substation_Line_Current_Amps": [18.5, 4.1, 45.2, 6.8],
        "System_Status": ["NORMAL", "NORMAL", "SUSPECTED BYPASS", "NORMAL"]
    }

meter_data = load_smart_meter_data()
df = pd.DataFrame(meter_data)

# 3. Simulation Controls in Sidebar Workspace
st.sidebar.subheader("🕹️ Grid Telematics Simulation")
simulate_bypass = st.sidebar.button("🚨 Simulate Meter Bypassing Event (MTR-804)")

# 4. Top-Level Operational Metrics Panel
metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric(label="📊 Total Monitored Nodes", value=f"{len(df)} Smart Meters", delta="Fuze Tech Group Core")
with metric_col2:
    bypassed_meters = len(df[df["System_Status"] == "SUSPECTED BYPASS"])
    st.metric(label="🚨 Active Fraud Alerts", value=f"{bypassed_meters} Critical", delta="Real-Time Detection", delta_color="inverse")
with metric_col3:
    if simulate_bypass:
        st.metric(label="🛡️ Grid Integrity Index", value="91.4% - CRITICAL", delta="-8.6% Grid Leakage", delta_color="inverse")
    else:
        st.metric(label="🛡️ Grid Integrity Index", value="100% SECURE", delta="Zero Leakage Detected")

st.divider()

# 5. Dashboard Grid (Explicit 2-Column Split)
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📋 Core Utility Grid Registry & Telemetry Logs")
    
    # Anomaly Engine Logic (Cross-references meter recording vs line current)
    if simulate_bypass:
        df.loc[df["Meter_ID"] == "MTR-804", "Metered_Usage_kW"] = 0.0
        df.loc[df["Meter_ID"] == "MTR-804", "Substation_Line_Current_Amps"] = 62.8
        df.loc[df["Meter_ID"] == "MTR-804", "System_Status"] = "CRITICAL BYPASS DETECTED"
        st.error("🚨 CRITICAL UTILITY ALERT: Smart Meter MTR-804 reports 0.0 kW usage, but secondary line transformer registers 62.8 Amps entering the property! System flags active prepaid meter bypass.")
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("🛡️ Automated Revenue Protection Engine")
    st.info("ℹ️ Cross-examining data telemetry variables to protect municipal and landlord cash flows.")
    
    for index, row in df.iterrows():
        st.markdown(f"**🏢 Node ID:** {row['Meter_ID']} | **💼 Landlord Account:** {row['Property_Fund']}")
        if "NORMAL" in row['System_Status']:
            st.success(f"✅ Verified Secure. Status: **{row['System_Status']}**\n\n*Meter telemetry balances with grid consumption metrics.*")
        else:
            st.warning(f"⚠️ Revenue Exposure. Status: **{row['System_Status']}**\n\n*Action Required: Dispatch field audit team to isolate bridged physical wiring.*")
        st.divider()

st.caption(f"🕒 System timestamp synced: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} SAST | Developed by Thobeka Asanda Ngcobo.")
