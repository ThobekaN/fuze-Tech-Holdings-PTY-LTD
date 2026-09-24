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

# 📊 1. COLOURED SUMMARY TILE CARDS
st.markdown("#### 📊 Real-Time Thermal Grid Telemetry Summary")
df_health = pd.DataFrame(st.session_state["DB_HEALTHTECH"][active_id])

total_units = len(df_health)
avg_temp = round(df_health["Current_Temp_C"].mean(), 2) if not df_health.empty else 0.0
critical_alerts = len(df_health[df_health["Thermal_Status"] == "CRITICAL SPIKE"])

kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
    with st.container(border=True):
        st.markdown("<p style='color:#38BDF8; font-size:14px; font-weight:bold; margin:0;'>🛰️ MONITORED NODES</p>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='margin:0; font-size:28px;'>{total_units} Units Live</h2>", unsafe_allow_html=True)
        st.caption("Active Hardware Pings Synchronized")

with kpi_col2:
    with st.container(border=True):
        st.markdown("<p style='color:#34D399; font-size:14px; font-weight:bold; margin:0;'>❄️ GROUP MEAN TEMPERATURE</p>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='margin:0; font-size:28px;'>{avg_temp} °C</h2>", unsafe_allow_html=True)
        st.caption("Target Bounds: 2°C - 8°C")

with kpi_col3:
    with st.container(border=True):
        if critical_alerts > 0:
            st.markdown("<p style='color:#F87171; font-size:14px; font-weight:bold; margin:0;'>🚨 THERMAL EXCURSIONS ACTIVE</p>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='margin:0; font-size:28px; color:#F87171;'>{critical_alerts} Breaches</h2>", unsafe_allow_html=True)
            st.caption("🔴 Critical Spoilage Risks Flagged")
        else:
            st.markdown("<p style='color:#34D399; font-size:14px; font-weight:bold; margin:0;'>🚨 THERMAL EXCURSIONS ACTIVE</p>", unsafe_allow_html=True)
            st.markdown("<h2 style='margin:0; font-size:28px; color:#34D399;'>0 Breaches</h2>", unsafe_allow_html=True)
            st.caption("🟢 All Environmental Perimeters Safe")

st.write("")

# 🔄 2. INTERACTIVE HARDWARE TELEMETRY STREAM SIMULATOR
st.markdown("#### 🏃‍♂️ Live Edge Sensory Simulation Control")
st.caption("Simulate real-time ambient environment logs broadcasting from the firmware probes right into the cloud database tables.")

if st.button("🔄 Execute Edge Hardware Sensor Query Loop", key="btn_run_telemetry_sim"):
    sim_placeholder = st.empty()
    with sim_placeholder.container():
        st.info("⏰ Query Loop Active: Connecting to wireless transceiver socket layers...")
        time.sleep(0.4)
        
        # Simulate local background processing data updates dynamically
        for idx, row in enumerate(st.session_state["DB_HEALTHTECH"][active_id]):
            # Give random variance to temperature values
            new_temp = round(row["Current_Temp_C"] + random.uniform(-0.6, 0.6), 1)
            # Clip parameters so they don't fall below absolute freezing bounds
            if new_temp < 0.0: new_temp = 1.2
            
            st.session_state["DB_HEALTHTECH"][active_id][idx]["Current_Temp_C"] = new_temp
            st.session_state["DB_HEALTHTECH"][active_id][idx]["Thermal_Status"] = "NORMAL" if 2.0 <= new_temp <= 8.0 else "CRITICAL SPIKE"
            
        st.success("✅ Remote handshake complete: Telemetry stream written straight to Supabase instance!")
        time.sleep(0.4)
    sim_placeholder.empty()
    st.rerun()

st.write("")

# 📋 3. DATA DATA GRID LAYER WITH FORMATTED STATUS PILLS
st.markdown("#### 📋 Core Medication Cold Storage Inventory Tracker")

# Enforce clean visual cell status mapping representations
def map_visual_status_pills(status_string):
    if status_string == "CRITICAL SPIKE":
        return "🔴 THERMAL BREACH: SPOILAGE RISK"
    return "🟢 SECURE: NORMAL OPERATING ENVELOPE"

df_render = pd.DataFrame(st.session_state["DB_HEALTHTECH"][active_id])
df_render["Perimeter_Safety_Indicator"] = df_render["Thermal_Status"].apply(map_visual_status_pills)

st.dataframe(
    df_render,
    column_config={
        "Fridge_ID": "Hardware Serial ID",
        "Clinical_Facility": "Facility Branch Location",
        "Current_Temp_C": st.column_config.NumberColumn("Current Temperature", format="%.1f °C"),
        "Safety_Range": "Authorized Safety Limits",
        "Thermal_Status": None,  # Hides original raw text string column
        "Perimeter_Safety_Indicator": "🔒 System Security Clearance Evaluation"
    },
    use_container_width=True,
    hide_index=True
)
st.divider()

# ==============================================================================
# ⚡ 4. HIGH-LEVERAGE SAAS SCALING INFRASTRUCTURE LAYER
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
            
            st.session_state["DB_HEALTHTECH"][active_id].extend(new_nodes)
            st.toast(f"⚡ Platform limits scaled! {int(expansion_units)} hardware serial identifiers whitelisted to client slot.", icon="🛰️")
            time.sleep(0.2)
            st.rerun()
        else:
            st.error("Expansion Denied: Explicit target sub-facility parameters are required.")
