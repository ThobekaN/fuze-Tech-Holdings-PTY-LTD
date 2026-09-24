import streamlit as st
import pandas as pd

# 🔄 DATA LAYER INTEGRATION LOOP
from database import MOCK_FLEET_TELEMETRY

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔒 Unauthorized Session Scope: Explicit parent portal token authorization required.")
    st.stop()

# Pull the globally verified tenant token straight from session memory
user_profile = st.session_state["user_data"]
active_id = user_profile["client_id"]

st.title("🚚 LEGACY FREIGHT LINES — B2B LogTech Platform")
st.markdown(f"### *Multi-Tenant Telematics Isolation Stream — Client Node: {active_id}*")
st.divider()

# 🚨 DATA ISOLATION QUERY: Pull only the current client's data matrix records
client_fleet = st.session_state["DB_LOGTECH"][active_id]
df_log = pd.DataFrame(client_fleet)

simulate_theft = st.sidebar.button("🚨 Simulate Fuel Theft Anomaly")

m_col1, m_col2 = st.columns(2)
with m_col1:
    total_fleets = len(df_log) + (1 if simulate_theft and len(df_log) > 0 else 0)
    st.metric(label="📊 Monitored Fleet Size", value=f"{total_fleets} Heavy Vehicles")
with m_col2:
    if simulate_theft:
        st.metric(label="🛡️ System Security Profile", value="CRITICAL ALERT", delta="-45L Sudden Siphon", delta_color="inverse")
    else:
        st.metric(label="🛡️ System Security Profile", value="SECURE", delta="All Probes Normal")

st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📋 Isolated Client Fleet Log Registry")
    if simulate_theft and len(df_log) > 0:
        df_log.loc[0, "Fuel_Litres"] = df_log.loc[0, "Fuel_Litres"] - 45.0
        df_log.loc[0, "Speed_KMH"] = 0.0
        st.error(f"🚨 CRITICAL TELEMETRY EXPOSURE: Sudden slope drop detected on Vehicle {df_log.loc[0, 'Truck_ID']} while stationary! Alarm fired.")
    st.dataframe(df_log, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("🚧 Automated Border Compliance Status") 
    fuel_check = df_log.loc[0, "Fuel_Litres"] == df_log.loc[0, "Fuel_Litres"] - 45.0
    speed_check = df_log.loc[0, "Speed_KMH"] == 0.0
    df_problem = df_log[df_log["Fuel_Litres"] == (df_log.loc[0, "Fuel_Litres"] - 45.0)]
    df_normal = df_log[df_log["Fuel_Litres"] != (df_log.loc[0, "Fuel_Litres"] - 45.0)]
 

    with st.expander(f"🟢 Stable Infrastructure Envelopes ({len(df_normal)} Nodes)", expanded=True):
        if not df_normal.empty:
            for index, row in df_normal.iterrows():
                st.markdown(f"**🆔 Vehicle ID:** {row['Truck_ID']} | **👤 Operator:** {row['Driver']}")
                if row['BURS_Clearance'] == "PROCEED TO BORDER":
                    st.success(f"✅ BURS Clearance Approved. Status: **{row['BURS_Clearance']}**")
                elif "HOLD AT STAGING" in row['BURS_Clearance']:
                   st.warning(f"⚠️ BURS Clearance Blocked. Status: **{row['BURS_Clearance']}**")
        else:
            st.caption("No nodes currently tracking inside baseline gate")

    with st.expander(f"🔴 Isolated System Critcal Anomalies ({len(df_normal)} Nodes)", expanded=True):
       if not df_problem.empty:
           for index, row in df_problem.iterrows():
               st.markdown(f"**🆔 Vehicle ID:** {row['Truck_ID']} | **👤 Operator:** {row['Driver']}")
               if fuel_check and speed_check:
                   if row['BURS_Clearance'] == "PROCEED TO BORDER":
                       st.error("❌ Critical Telemetry Exposure. ✅ BURS Clearance Approved. Status: **{row['BURS_Clearance']}**")

                   else:
                       st.error("❌ Critical Telemetry Exposure. ⚠️ BURS Clearance Blocked. Status: **{row['BURS_Clearance']}**")
        else:
            st.caption("All operational perimeters clear. Zero excursions active")
