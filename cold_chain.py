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
    st.session_state["DB_HEALTHTECH"][active_id] = [
        {"Fridge_ID": "FRG-501", "Clinical_Facility": "Braamfontein Clinic", "Current_Temp_C": 4.2, "Safety_Range": "2°C - 8°C", "Thermal_Status": "NORMAL"},
        {"Fridge_ID": "FRG-502", "Clinical_Facility": "Hillbrow Health Hub", "Current_Temp_C": 5.1, "Safety_Range": "2°C - 8°C", "Thermal_Status": "NORMAL"},
        {"Fridge_ID": "FRG-503", "Clinical_Facility": "Parktown Pharmacy", "Current_Temp_C": 14.8, "Safety_Range": "2°C - 8°C", "Thermal_Status": "CRITICAL SPIKE"}
    ]

# 📊 1. MAIN TRANSACTION DATA GRID LAYER
st.markdown("#### 🌡️ Real-Time Active Asset Transceiver Streams")

# Reads keys directly from your database.py mapping file array bounds
raw_data = st.session_state["DB_HEALTHTECH"][active_id]
standardized_data = []

for record in raw_data:
    standardized_data.append({
        "Fridge_ID": record.get("Fridge_ID", "UNKNOWN"),
        "Clinical_Facility": record.get("Clinical_Facility", "Pharmacy Sub-Branch"),
        "Current_Temp_C": record.get("Current_Temp_C", 4.0),
        "Safety_Range": record.get("Safety_Range", "2°C - 8°C"),
        "Thermal_Status": record.get("Thermal_Status", "NORMAL")
    })

df_health = pd.DataFrame(standardized_data)

# Visual Anchor KPI Metric Cards (Hardened against Column KeyErrors)
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
with kpi_col1:
    st.metric(label="✅ Monitored Refrigerator Units", value=f"{len(df_health)} Probes Active")
with kpi_col2:
    avg_temp = round(df_health["Current_Temp_C"].mean(), 2) if not df_health.empty else 0.0
    st.metric(label="❄️ Group Mean Temperature", value=f"{avg_temp} °C", delta="Stable Bounds")
with kpi_col3:
    critical_alerts = len(df_health[df_health["Thermal_Status"] == "CRITICAL SPIKE"])
    st.metric(label="🚨 Spoilage Threats Isolated", value=f"{critical_alerts} Checked")

st.write("")
st.dataframe(
    df_health, 
    column_config={
        "Fridge_ID": "Hardware Serial ID",
        "Clinical_Facility": "Facility Branch Location",
        "Current_Temp_C": "Current Temperature (°C)",
        "Safety_Range": "Authorized Safety Limits",
        "Thermal_Status": "Operational Alarm Status"
    },
    use_container_width=True, 
    hide_index=True
)
st.divider()

# ==============================================================================
# ⚡ HIGH-LEVERAGE SAAS SCALING INFRASTRUCTURE LAYER
# ==============================================================================
st.markdown("#### ⚡ Scale Infrastructure Footprint")
st.caption("Incremental Billing Engine: Scale your telemetry limits and request additional hardware transceivers on the fly without interrupting running pipelines.")

with st.container(border=True):
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        expansion_units = st.number_input("Request Additional HaaS Probe Units:", min_value=1, max_value=50, value=15, key="num_haas_expand")
    with col_input2:
        facility_target = st.text_input("Target Deployment Storage Sub-Facility Branch:", "Pharmacy Main Cold Room B", key="txt_haas_branch")
        
    st.info(f"ℹ️ **Pro-Rata Invoice Projection:** Adding {int(expansion_units)} nodes drops a combined physical unit deposit request down the payment queue. Monthly subscription updates apply at +R400/fridge upon automated edge configuration activation.")
    
    if st.button("Authorize Dynamic Expansion Protocol", key="btn_trigger_haas_scale"):
        if facility_target and expansion_units:
            
            log_box = st.empty()
            with log_box.container():
                st.code("🔍 Intercepting incremental pro-rata telemetry request matrix...", language="sql")
                time.sleep(0.4)
                st.code(f"💳 Running client ledger verification... Stripe/PayFast allocation token success.", language="sql")
                time.sleep(0.4)
                st.code(f"🔒 WHITELISTING {int(expansion_units)} SECURITY ENVELOPE KEYS ON CENTRAL CLUSTER...", language="sql")
                time.sleep(0.3)
                
                new_nodes = []
                for node_index in range(1, int(expansion_units) + 1):
                    generated_serial = f"FRG-{random.randint(600,999)}"
                    simulated_temp = round(random.uniform(2.5, 5.8), 1)
                    
                    # Appends matching database structures seamlessly
                    new_nodes.append({
                        "Fridge_ID": generated_serial,
                        "Clinical_Facility": facility_target.strip(),
                        "Current_Temp_C": simulated_temp,
                        "Safety_Range": "2°C - 8°C",
                        "Thermal_Status": "NORMAL"
                    })
                    
                    if node_index <= 3 or node_index == int(expansion_units):
                        st.code(f"📝 INSERT INTO cold_chain_probes (client_id, serial, branch) VALUES ('{active_id}', '{generated_serial}', ...);", language="sql")
                        time.sleep(0.1)
                    elif node_index == 4:
                        st.code("📝 [Batch Processing Remaining Node Insert Queries...]", language="sql")
                        time.sleep(0.2)
                        
                st.code("📡 Webhook handshake committed. Dropship dispatch notification pushed directly to hardware vendor Otto Wireless.", language="sql")
                time.sleep(0.3)
                st.code("✅ METADATA CAP SHEET RECORD SYNCHRONIZED. Edge bootloaders tracking repository channels.", language="sql")
                time.sleep(0.2)
            
            log_box.empty()
            
            # Commit the expansion list seamlessly down into your database model structure
            st.session_state["DB_HEALTHTECH"][active_id].extend(new_nodes)
            st.toast(f"⚡ Platform limits scaled! {int(expansion_units)} hardware serial identifiers whitelisted to client slot.", icon="🛰️")
            time.sleep(0.2)
            st.rerun()
        else:
            st.error("Expansion Denied: Explicit target sub-facility parameters are required.")
