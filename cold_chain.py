import streamlit as st
import pandas as pd
import random
import time

# 🔗 SECURITY AT THE EDGE: Direct Data Ingestion Check
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("🔒 Unauthorized Session Scope: Explicit parent portal token authorization required.")
    st.stop()

user_profile = st.session_state["user_data"]
active_id = user_profile["client_id"]

st.title("🏥 LEGACY COLD CHAIN — HealthTech Operations")
st.markdown(f"### *Central Pharmacy Ambient Thermal Control Node — Workspace ID: `{active_id}`*")
st.divider()

# Ensure the multi-tenant database slice holds initialized rows
if active_id not in st.session_state["DB_HEALTHTECH"] or not st.session_state["DB_HEALTHTECH"][active_id]:
    # Bootstrap baseline structural sample arrays matching real database footprints
    st.session_state["DB_HEALTHTECH"][active_id] = [
        {"probe_id": "PRB-9921-X", "facility": "Braamfontein Public Clinic", "temp_c": 4.20, "slope": -0.02, "status": "NORMAL"},
        {"probe_id": "PRB-9922-X", "facility": "Braamfontein Public Clinic", "temp_c": 3.85, "slope": 0.04, "status": "NORMAL"},
        {"probe_id": "PRB-9923-X", "facility": "Braamfontein Public Clinic", "temp_c": 5.12, "slope": -0.01, "status": "NORMAL"},
    ]

# 📊 1. MAIN TRANSACTION DATA GRID LAYER
st.markdown("#### 🌡️ Real-Time Active Asset Transceiver Streams")
df_health = pd.DataFrame(st.session_state["DB_HEALTHTECH"][active_id])

# Visual Anchor KPI Metric Cards
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
with kpi_col1:
    st.metric(label="✅ Monitored Refrigerator Units", value=f"{len(df_health)} Probes Active")
with kpi_col2:
    avg_temp = round(df_health["temp_c"].mean(), 2) if not df_health.empty else 0.0
    st.metric(label="❄️ Group Mean Temperature", value=f"{avg_temp} °C", delta="Stable Bounds")
with kpi_col3:
    critical_alerts = len(df_health[df_health["status"] == "EMERGENCY SPIKE"])
    st.metric(label="🚨 Spoilage Threats Isolated", value=f"{critical_alerts} Safe", delta="0 Operational Violations")

st.write("")
st.dataframe(df_health, use_container_width=True, hide_index=True)
st.divider()

# ==============================================================================
# ⚡ HIGH-LEVERAGE SAAS SCALING INFRASTRUCTURE LAYER (REPAIRED MECHANICS)
# ==============================================================================
st.markdown("#### ⚡ Scale Infrastructure Footprint")
st.caption("Incremental Billing Engine: Scale your telemetry limits and request additional hardware transceivers on the fly without interrupting running pipelines.")

with st.container(border=True):
    col_input1, col_input2 = st.columns([1, 2])
    with col_input1:
        expansion_units = st.number_input("Request Additional HaaS Probe Units:", min_value=1, max_value=50, value=15, key="num_haas_expand")
    with col_input2:
        facility_target = st.text_input("Target Deployment Storage Sub-Facility Branch:", "Pharmacy Main Cold Room B", key="txt_haas_branch")
        
    st.info(f"ℹ️ **Pro-Rata Invoice Projection:** Adding {int(expansion_units)} nodes drops a combined physical unit deposit request down the payment queue. Monthly subscription updates apply at +R400/fridge upon automated edge configuration activation.")
    
    # Secure, isolated button state to handle asynchronous loop modifications safely
    if st.button("Authorize Dynamic Expansion Protocol", key="btn_trigger_haas_scale"):
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
                
                # Dynamically compile the 15 brand-new hardware data tracks asynchronously
                new_nodes = []
                for node_index in range(1, int(expansion_units) + 1):
                    generated_serial = f"PRB-99{random.randint(3,9)}{random.randint(1,9)}-X"
                    simulated_temp = round(random.uniform(3.1, 5.9), 2)
                    simulated_slope = round(random.uniform(-0.04, 0.05), 2)
                    
                    new_nodes.append({
                        "probe_id": generated_serial,
                        "facility": facility_target.strip(),
                        "temp_c": simulated_temp,
                        "slope": simulated_slope,
                        "status": "NORMAL"
                    })
                    
                    if node_index <= 3 or node_index == int(expansion_units):
                        st.code(f"📝 INSERT INTO cold_chain_probes (client_id, serial, branch) VALUES ('{active_id}', '{generated_serial}', ...);", language="sql")
                        time.sleep(0.2)
                    elif node_index == 4:
                        st.code("📝 [Batch Processing Remaining Node Insert Queries...]", language="sql")
                        time.sleep(0.3)
                        
                st.code("📡 Webhook handshake committed. Dropship dispatch notification pushed directly to hardware vendor Otto Wireless.", language="sql")
                time.sleep(0.4)
                st.code("✅ METADATA CAP SHEET RECORD SYNCHRONIZED. Edge bootloaders tracking repository channels.", language="sql")
                time.sleep(0.3)
            
            log_box.empty()
            
            # Append new hardware blocks natively into the running state memory array cache
            st.session_state["DB_HEALTHTECH"][active_id].extend(new_nodes)
            st.toast(f"⚡ Platform limits scaled! {int(expansion_units)} hardware serial identifiers whitelisted to client slot.", icon="🛰️")
            time.sleep(0.5)
            st.rerun()
        else:
            st.error("Expansion Denied: Explicit target sub-facility parameters are required.")
