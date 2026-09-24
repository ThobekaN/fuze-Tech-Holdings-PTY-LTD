import streamlit as st
import pandas as pd
import random
import time

# 🔄 DATA INGESTION: Direct import from shared global schema database
from database import MOCK_HEALTH_TELEMETRY

# 🔗 SECURITY AT THE EDGE: Direct Data Ingestion Check
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔒 Unauthorized Session Scope: Explicit parent portal token authorization required.")
    st.stop()

user_profile = st.session_state["user_data"]
active_id = user_profile["client_id"]

st.title("🏥 LEGACY COLD CHAIN — B2B HealthTech Platform")
st.markdown(f"### *Multi-Tenant Pharmacy Thermal Control — Client Node: {active_id}*")
st.divider()

# Ensure the multi-tenant session data array is securely instantiated in memory
if active_id not in st.session_state["DB_HEALTHTECH"] or not st.session_state["DB_HEALTHTECH"][active_id]:
    # Dynamically pull the authenticated client's isolated health telemetry records from database.py
    st.session_state["DB_HEALTHTECH"][active_id] = MOCK_HEALTH_TELEMETRY.get(active_id, [])

# Read data straight from the running session memory dictionary cache slice
client_health_logs = st.session_state["DB_HEALTHTECH"][active_id]
df_health = pd.DataFrame(client_health_logs)

simulate_thermal_breach = st.sidebar.button("🚨 Simulate Critical Thermal Breach")

metric_col1, metric_col2 = st.columns(2)
with metric_col1:
    # Captures breach injection increments automatically
    total_fridges = len(df_health) + (1 if simulate_thermal_breach and len(df_health) > 0 else 0)
    st.metric(label="📊 Total Connected Nodes", value=f"{total_fridges} Units Active")
with metric_col2:
    if simulate_thermal_breach:
        st.metric(label="🛡️ Thermal Integrity Status", value="BREACH CONTAINMENT ACTIVE", delta="Spoilage Intercepted", delta_color="inverse")
    else:
        st.metric(label="🛡️ Thermal Integrity Status", value="100% SECURE", delta="Probes Syncing (60s)")

st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📋 Medication Storage Inventory Tracker & Telemetry")
    if simulate_thermal_breach and len(df_health) > 0:
        new_probe = {"Probe_ID": "PRB-504", "Clinical_Facility": "Emergency Inventory Vault", "Current_Temp_C": 14.8, "Safety_Range": "2°C - 8°C", "Thermal_Status": "CRITICAL SPIKE"}
        df_health = pd.concat([df_health, pd.DataFrame([new_fridge])], ignore_index=True)
        st.error("🚨 CRITICAL METRIC ALERT: Node FRG-504 logs an ambient environment of 14.8°C! System trajectory rules isolate localized cooling system trips to guard refrigerated inventory fractions.")
    st.dataframe(df_health, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("🛡️ Automated Perimeter Protection Engine")
    for index, row in df_health.iterrows():
        st.markdown(f"**🎫 Node ID:** {row['Probe_ID']} | **🏥 Facility:** {row['Clinical_Facility']}")
        if "NORMAL" in row['Thermal_Status']:
            st.success(f"✅ Safe Thermal Envelope. Status: **{row['Thermal_Status']} ({row['Current_Temp_C']}°C)**")
        else:
            st.error(f"❌ Thermal Excursion Detected. Status: **{row['Thermal_Status']} ({row['Current_Temp_C']}°C)**")
        st.divider()

st.divider()

# ==============================================================================
# ⚡ HIGH-LEVERAGE SAAS SCALING INFRASTRUCTURE LAYER (HEALTH TECH)
# ==============================================================================
st.markdown("#### ⚡ Scale Infrastructure Footprint")
st.caption("Incremental Billing Engine: Request additional hardware transceivers and scale telemetry thresholds instantly without taking down running loops.")

with st.container(border=True):
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        expansion_units = st.number_input("Request Additional HaaS Probe Units:", min_value=1, max_value=50, value=15, key="num_health_expand")
    with col_input2:
        facility_target = st.text_input("Target Deployment Storage Sub-Facility Branch:", "Pharmacy Main Cold Room B", key="txt_health_branch")
        
    st.info(f"ℹ️ **Pro-Rata Invoice Projection:** Adding {int(expansion_units)} nodes drops a combined physical unit deposit request down the payment queue. Monthly subscription updates apply at +R400/fridge upon automated edge configuration activation.")
    
    if st.button("Authorize Dynamic Expansion Protocol", key="btn_trigger_health_scale"):
        if facility_target and expansion_units:
            
            # LIVE ENTERPRISE HAAS DROPSHIP CONSOLE LOGS
            log_box = st.empty()
            with log_box.container():
                st.code("🔍 Intercepting incremental pro-rata telemetry request matrix...", language="sql")
                time.sleep(0.4)
                st.code(f"💳 Running client ledger verification... Stripe/PayFast allocation token success.", language="sql")
                time.sleep(0.4)
                st.code(f"🔒 WHITELISTING {int(expansion_units)} SECURITY ENVELOPE KEYS ON CENTRAL CLUSTER...", language="sql")
                time.sleep(0.3)
                
                new_probes = []
                for node_index in range(1, int(expansion_units) + 1):
                    generated_probe_id = f"PRB-{random.randint(600, 999)}"
                    simulated_temp = round(random.uniform(2.5, 5.8), 1)
                    
                    new_probes.append({
                        "Probe_ID": generated_fridge_id,
                        "Clinical_Facility": facility_target.strip(),
                        "Current_Temp_C": simulated_temp,
                        "Safety_Range": "2°C - 8°C",
                        "Thermal_Status": "NORMAL"
                    })
                    
                    if node_index <= 3 or node_index == int(expansion_units):
                        st.code(f"📝 INSERT INTO cold_chain_probes (client_id, serial, branch) VALUES ('{active_id}', '{generated_fridge_id}', ...);", language="sql")
                        time.sleep(0.1)
                    elif node_index == 4:
                        st.code("📝 [Batch Processing Remaining Node Insert Queries...]", language="sql")
                        time.sleep(0.2)
                        
                st.code("📡 Webhook handshake committed. Dropship dispatch notification pushed directly to hardware vendor Otto Wireless.", language="sql")
                time.sleep(0.3)
                st.code("✅ METADATA CAP SHEET RECORD SYNCHRONIZED. Edge bootloaders tracking repository channels.", language="sql")
                time.sleep(0.2)
            
            log_box.empty()
            
            # Commit the newly scaled list straight down into your active memory dictionary layer
            st.session_state["DB_HEALTHTECH"][active_id].extend(new_fridges)
            st.toast(f"⚡ Platform limits scaled! {int(expansion_units)} hardware serial identifiers whitelisted to client slot.", icon="🛰️")
            time.sleep(0.2)
            st.rerun()
        else:
            st.error("Expansion Denied: Explicit target sub-facility parameters are required.")
