import streamlit as st
import pandas as pd

# 🔄 DATA LAYER INTEGRATION LOOP
from database import MOCK_HEALTH_TELEMETRY

user_profile = st.session_state["user_data"]
active_id = user_profile["client_id"]

st.title("🏥 LEGACY COLD CHAIN — B2B HealthTech Platform")
st.markdown(f"### *Multi-Tenant Thermal Monitoring Stream — Client Node: {active_id}*")
st.divider()

client_fridge_logs = MOCK_HEALTH_TELEMETRY.get(active_id, [])
df_health = pd.DataFrame(client_fridge_logs)

simulate_generator_failure = st.sidebar.button("🚨 Simulate Load-Shedding Power Trip")

metric_col1, metric_col2 = st.columns(2)
with metric_col1:
    st.metric(label="📊 Tracked Refrigeration Units", value=f"{len(df_health)} Active Nodes")
with metric_col2:
    if simulate_generator_failure:
        st.metric(label="🌡️ Medical Inventory Security", value="CRITICAL SPOIL RISK", delta="+6.2°C Derivative Trajectory", delta_color="inverse")
    else:
        st.metric(label="🌡️ Medical Inventory Security", value="ALL NODES SAFE", delta="Thermal Trajectory Stable")

st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📋 Core Clinical Thermal Logs & Sensor Streams")
    if simulate_generator_failure and len(df_health) > 0:
        df_health.loc[0, "Current_Temp_C"] = 12.4
        df_health.loc[0, "Thermal_Status"] = "EMERGENCY ALERT"
        st.error(f"🚨 THERMAL TRAJECTORY FAILURE: Node {df_health.loc[0, 'Fridge_ID']} at {df_health.loc[0, 'Clinical_Facility']} has experienced a sharp temperature surge. Internal script is initiating emergency backup transfer protocols.")
    st.dataframe(df_health, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("🛡️ Proactive Asset Salvage & Dispatch Routine")
    st.info("ℹ️ Continuous mathematical evaluation of clinical thermal zones to shield life-saving stock.")
    for index, row in df_health.iterrows():
        st.markdown(f"**🏢 Facility:** {row['Clinical_Facility']} | **Fridge:** {row['Fridge_ID']}")
        if "NORMAL" in row['Thermal_Status']:
            st.success(f"✅ Temperature Verified. Status: **{row['Thermal_Status']}** ({row['Current_Temp_C']}°C)")
        else:
            st.error(f"❌ Thermal Exposure Flagged. Status: **{row['Thermal_Status']}** ({row['Current_Temp_C']}°C)")
        st.divider()
