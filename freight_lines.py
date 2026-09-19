import streamlit as st
import pandas as pd

# 🔄 DATA LAYER INTEGRATION LOOP
from database import MOCK_FLEET_TELEMETRY

# Pull the globally verified tenant token straight from session memory
user_profile = st.session_state["user_data"]
active_id = user_profile["client_id"]

st.title("🚚 LEGACY FREIGHT LINES — B2B LogTech Platform")
st.markdown(f"### *Multi-Tenant Telematics Isolation Stream — Client Node: {active_id}*")
st.divider()

# 🚨 DATA ISOLATION QUERY: Pull only the current client's data matrix records
client_fleet = MOCK_FLEET_TELEMETRY.get(active_id, [])
df_fleet = pd.DataFrame(client_fleet)

simulate_theft = st.sidebar.button("🚨 Simulate Fuel Theft Anomaly")

m_col1, m_col2 = st.columns(2)
with m_col1:
    st.metric(label="📊 Monitored Fleet Size", value=f"{len(df_fleet)} Heavy Vehicles")
with m_col2:
    if simulate_theft:
        st.metric(label="🛡️ System Security Profile", value="CRITICAL ALERT", delta="-45L Sudden Siphon", delta_color="inverse")
    else:
        st.metric(label="🛡️ System Security Profile", value="SECURE", delta="All Probes Normal")

st.divider()
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("📋 Isolated Client Fleet Log Registry")
    if simulate_theft and len(df_fleet) > 0:
        df_fleet.loc[0, "Fuel_Liters"] = df_fleet.loc[0, "Fuel_Liters"] - 45.0
        df_fleet.loc[0, "Speed_KMH"] = 0.0
        st.error(f"🚨 CRITICAL TELEMETRY EXPOSURE: Sudden slope drop detected on Vehicle {df_fleet.loc[0, 'Truck_ID']} while stationary! Alarm fired.")
    st.dataframe(df_fleet, use_container_width=True, hide_index=True)

with col_r:
    st.subheader("🚧 Automated Border Compliance Status")
    for index, row in df_fleet.iterrows():
        st.markdown(f"**🆔 Vehicle ID:** {row['Truck_ID']} | **👤 Operator:** {row['Driver']}")
        if row['BURS_Clearance'] == "PROCEED TO BORDER":
            st.success(f"✅ BURS Clearance Approved. Status: **{row['BURS_Clearance']}**")
        else:
            st.warning(f"⚠️ BURS Clearance Blocked. Status: **{row['BURS_Clearance']}**")
        st.divider()
