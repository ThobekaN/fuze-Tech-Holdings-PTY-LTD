import streamlit as st
import pandas as pd

# 🔄 AUTOMATED DATA LAYER INTEGRATION
from database import MOCK_TRANSIT_TELEMETRY

user_profile = st.session_state["user_data"]
active_id = user_profile["client_id"]

st.title("🚌 LEGACY TRANSIT TOKEN — B2B TransitTech Platform")
st.markdown(f"### *Multi-Tenant Transit Access Stream — Client Node: {active_id}*")
st.divider()

# Pull only the authenticated client's isolated transit data slice
client_transit_logs = MOCK_TRANSIT_TELEMETRY.get(active_id, [])
df_transit = pd.DataFrame(client_transit_logs)

simulate_screenshot_fraud = st.sidebar.button("🚨 Simulate Static Screenshot Fraud")

metric_col1, metric_col2 = st.columns(2)
with metric_col1:
    st.metric(label="📊 Total Access Scans", value=f"{len(df_transit)} Active Checks")
with metric_col2:
    if simulate_screenshot_fraud:
        st.metric(label="🛡️ Gate Perimeter Status", value="CONTAINMENT ACTIVE", delta="Static Capture Defeated", delta_color="inverse")
    else:
        st.metric(label="🛡️ Gate Perimeter Status", value="100% OPERATIONAL", delta="Tokens Rotating (30s)")

st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📋 Shuttle Gateway Access Logs & Token Telemetry")
    if simulate_screenshot_fraud and len(df_transit) > 0:
        new_scan = {"Scan_ID": "WITS-004", "Student_Number / Staff_ID": "2814103", "Transit_Route": "Amic -> WEC -> Wits Junction", "Card_State": "OUTSIDE_SYSTEM", "Token_Age_Sec": 245, "Gate_Action": "CRITICAL ERROR - EXPIRED TOKEN"}
        df_transit = pd.concat([df_transit, pd.DataFrame([new_scan])], ignore_index=True)
        st.error("🚨 CRITICAL ACCESS ALERT: Scan WITS-004 presented a static barcode token older than the 30-second rotation window! System flags screenshot fraud and locked the door.")
    st.dataframe(df_transit, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("🛡️ Automated Perimeter Protection Engine")
    for index, row in df_transit.iterrows():
        st.markdown(f"**🎫 Scan ID:** {row['Scan_ID']} | **👤 Identity:** {row['Student_Number / Staff_ID']}")
        if "APPROVED" in row['Gate_Action']:
            st.success(f"✅ Verified Entry. Status: **{row['Gate_Action']}**")
        elif "ANTI-PASSBACK" in row['Gate_Action']:
            st.warning(f"⚠️ Anti-Passback Violation. Status: **{row['Gate_Action']}**")
        else:
            st.error(f"❌ Access Denied. Status: **{row['Gate_Action']}**")
        st.divider()
