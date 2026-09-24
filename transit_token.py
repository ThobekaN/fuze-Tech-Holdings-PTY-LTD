import streamlit as st
import pandas as pd
import random 
import time

# 🔄 AUTOMATED DATA LAYER INTEGRATION
from database import MOCK_TRANSIT_TELEMETRY

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔒 Unauthorized Session Scope: Explicit parent portal token authorization required.")
    st.stop()

user_profile = st.session_state["user_data"]
active_id = user_profile["client_id"]

st.title("🚌 LEGACY TRANSIT TOKEN — B2B TransitTech Platform")
st.markdown(f"### *Multi-Tenant Transit Access Stream — Client Node: {active_id}*")
st.divider()

if active_id not in st.session_state["DB_TRANSITTECH"] or not st.session_state["DB_TRANSITTECH"][active_id]:
    st.session_state["DB_TRANSITTECH"][active_id] = MOCK_TRANSIT_TELEMETRY.get(active_id, [])

# Pull only the authenticated client's isolated transit data slice
client_transit_logs = st.session_state["DB_TRANSITTECH"][active_id]
df_transit = pd.DataFrame(client_transit_logs)

simulate_screenshot_fraud = st.sidebar.button("🚨 Simulate Static Screenshot Fraud")

metric_col1, metric_col2 = st.columns(2)
with metric_col1:
    total_scans = len(df_transit) + (1 if simulate_screenshot_fraud and len(df_transit) > 0 else 0)
    st.metric(label="📊 Total Access Scans", value=f"{total_scans} Active Checks")
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
        if "WITS" in "Scan_ID":
            new_scan = {"Scan_ID": "WITS-004", "Student_Number / Staff_ID": "2814103", "Transit_Route": "Amic -> WEC -> Wits Junction", "Card_State": "OUTSIDE_SYSTEM", "Token_Age_Sec": 245, "Gate_Action": "CRITICAL ERROR - EXPIRED TOKEN"}
            df_transit = pd.concat([df_transit, pd.DataFrame([new_scan])], ignore_index=True)
            st.error("🚨 CRITICAL ACCESS ALERT: Scan WITS-004 presented a static barcode token older than the 30-second rotation window! System flags screenshot fraud and locked the door.")
        elif "UJ" in "Scan_id":
            new_scan =  {"Scan_ID": "UJ-003", "Student_Number / Staff_ID": "4852713", "Transit_Route": "APK -> SWC", "Card_State": "IN_TRANSIT", "Token_Age_Sec": 56, "Gate_Action": "CRITICAL ERROR - EXPIRED TOKEN"}
            df_transit = pd.concat([df_transit, pd.DataFrame([new_scan])], ignore_index=True)
            st.error("🚨 CRITICAL ACCESS ALERT: Scan UJ-003 presented a static barcode token older than the 30-second rotation window! System flags screenshot fraud and locked the door.")
        else:
            new_scan =  {"Scan_ID": "UKZN-703", "Student_Number / Staff_ID": "345162", "Transit_Route": "Makhabane Bus Stop -> Joosub Hall", "Card_State": "IN_TRANSIT", "Token_Age_Sec": 73, "Gate_Action": "CRITICAL ERROR - EXPIRED TOKEN"}
            df_transit = pd.concat([df_transit, pd.DataFrame([new_scan])], ignore_index=True)
            st.error("🚨 CRITICAL ACCESS ALERT: Scan UKZN-703 presented a static barcode token older than the 30-second rotation window! System flags screenshot fraud and locked the door.")
    st.dataframe(df_transit, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("🛡️ Automated Perimeter Protection Engine")
    df_normal = df_transit[df_transit["Gate_Action"] == "ACCESS APPROVED"]
    df_problem = df_transit[df_transit["Gate_Action"] != "ACCESS APPROVED"]

    with st.expander(f"🟢 Stable Infrastructure Envelopes ({len(df_normal)} Nodes)", expanded=True):
        if not df_normal.empty:
            for index, row in df_normal.iterrows():
                st.markdown(f"**🎫 Scan ID:** {row['Scan_ID']} | **👤 Identity:** {row['Student_Number / Staff_ID']}")
                st.success(f"✅ Verified Entry. Status: **{row['Gate_Action']} ({row['Card_State']})**")
        else:
            st.caption("No nodes currently tracking inside baseline gate fields")

    with st.expander(f"🔴 Isolated System Critcal Anomalies ({len(df_problem)} Nodes)", expanded=True):
        if not df_problem.empty:
            for index, row in df_problem.iterrows():
                st.markdown(f"**🎫 Scan ID:** {row['Scan_ID']} | **👤 Identity:** {row['Student_Number / Staff_ID']}")
                if "ANTI-PASSBACK" in row['Gate_Action']:
                    st.warning(f"⚠️ Anti-Passback Violation. Status: **{row['Gate_Action']} ({row['Card_State']})**")
                else:
                    st.error(f"❌ Access Denied. Status: **{row['Gate_Action']} ({"ALREADY " + row['Card_State']})**")
        else:
            st.caption("All operational perimeters clear. Zero excursions active")
