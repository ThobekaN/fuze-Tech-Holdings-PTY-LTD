import streamlit as st
import pandas as pd

# 🔄 DATA LAYER INTEGRATION LOOP
from database import MOCK_GRID_TELEMETRY

# Pull the globally verified tenant token straight from session memory
user_profile = st.session_state["user_data"]
active_id = user_profile["client_id"]

st.title("⚡ LEGACY UTILITY LABS — B2B GridTech Platform")
st.markdown(f"### *Multi-Tenant Grid Isolation Stream — Client Node: {active_id}*")
st.divider()

# 🚨 DATA ISOLATION QUERY: Pull only the current client's data matrix records
client_meters = MOCK_GRID_TELEMETRY.get(active_id, [])
df_meter = pd.DataFrame(client_meters)

simulate_bypass = st.sidebar.button("🚨 Simulate Smart Meter Bypassing")

met_col1, met_col2 = st.columns(2)
with met_col1:
    st.metric(label="📊 Active Utility Nodes", value=f"{len(df_meter)} Smart Meters")
with met_col2:
    if simulate_bypass:
        st.metric(label="🚨 Revenue Protection Status", value="FRAUD INTERCEPTED", delta="-45A Diverted Load", delta_color="inverse")
    else:
        st.metric(label="🚨 Revenue Protection Status", value="100% INTACT", delta="Zero Leakage")

st.divider()
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("📋 Core Utility Grid Registry & Telemetry Logs")
    if simulate_bypass and len(df_meter) > 0:
        df_meter.loc[len(df_meter)-1, "Metered_Usage_kW"] = 0.0
        df_meter.loc[len(df_meter)-1, "Substation_Line_Current_Amps"] = 65.2
        df_meter.loc[len(df_meter)-1, "System_Status"] = "CRITICAL FRAUD BYPASS"
        st.error(f"🚨 REVENUE EXPOSURE ALERT: Meter {df_meter.loc[len(df_meter)-1, 'Meter_ID']} registers 0.0kW consumption while local line transformer experiences massive active current loads!")
    st.dataframe(df_meter, use_container_width=True, hide_index=True)

with col_r:
    st.subheader("🛡️ Automated Revenue Protection Engine")
    for index, row in df_meter.iterrows():
        st.markdown(f"**🏢 Facility Account:** {row['Property_Fund']} | **Node:** {row['Meter_ID']}")
        if "NORMAL" in row['System_Status']:
            st.success(f"✅ Verified Operational. Status: **{row['System_Status']}**")
        else:
            st.error(f"❌ Structural Failure Alert. Status: **{row['System_Status']}**")
        st.divider()
