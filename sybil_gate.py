import streamlit as st
import pandas as pd

# 🔄 DATA LAYER INTEGRATION LOOP
from database import MOCK_CYBER_TELEMETRY

# Pull verification tokens out of active session state memory
user_profile = st.session_state["user_data"]
active_id = user_profile["client_id"]

st.title("🛡️ LEGACY SYBIL GATE — B2B CyberTech Platform")
st.markdown(f"### *Multi-Tenant Fraud Isolation Stream — Client Node: {active_id}*")
st.divider()

# 🚨 DATA ISOLATION QUERY: Pull only the current client's data matrix records
client_fraud_logs = MOCK_CYBER_TELEMETRY.get(active_id, [])
df_cyber = pd.DataFrame(client_fraud_logs)

simulate_mass_abuse = st.sidebar.button("🚨 Simulate Multi-Accounting Sybil Attack")

metric_col1, metric_col2 = st.columns(2)
with metric_col1:
    st.metric(label="📊 Total Scanned Checkouts", value=f"{len(df_cyber)} API Requests")
with metric_col2:
    if simulate_mass_abuse:
        st.metric(label="🛡️ Platform Margin Protection", value="R12,400 Saved", delta="+R4,800 Intercepted", delta_color="normal")
    else:
        st.metric(label="🛡️ Platform Margin Protection", value="R7,600 Saved", delta="Monitoring Webhooks")

st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📋 Live Promo API Gateway & Telemetry Logs")
    if simulate_mass_abuse and len(df_cyber) > 0:
        # Append a new spoof row to simulate a multi-accounting clone farm
        new_row = {"Transaction_ID": "TXN-904", "User_Alias": "promo_hunter_za", "Claimed_Email": "asanda.n@gmail.com", "Device_Hardware_Fingerprint": "HW-UUID-4401", "Promo_Code": "FIRST100", "Evaluation_Status": "CRITICAL PROMO ABUSE ALERT"}
        df_cyber = pd.concat([df_cyber, pd.DataFrame([new_row])], ignore_index=True)
        st.error("🚨 CRITICAL ANTI-FRAUD ALERT: Transaction TXN-904 claims a unique first-time promo under user promo_hunter_za, but the hardware fingerprint matches HW-UUID-4401. System flags device cloning multi-accounting attack!")
    st.dataframe(df_cyber, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("🛡️ Automated Promotion Protection Engine")
    st.info("ℹ️ Cross-referencing hardware fingerprints and location metrics to seal corporate marketing links.")
    for index, row in df_cyber.iterrows():
        st.markdown(f"**🔑 Transaction:** {row['Transaction_ID']} | **📧 Input:** {row['Claimed_Email']}")
        if "APPROVED" in row['Evaluation_Status']:
            st.success(f"✅ Verified Unique User. Status: **{row['Evaluation_Status']}**")
        elif "COORD" in row['Evaluation_Status']:
            st.warning(f"⚠️ Address Clustering Risk. Status: **{row['Evaluation_Status']}**")
        else:
            st.error(f"❌ Hardware Duplication Blocked. Status: **{row['Evaluation_Status']}**")
        st.divider()
