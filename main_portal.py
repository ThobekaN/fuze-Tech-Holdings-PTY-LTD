import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

# 🔄 GLOBAL DATA LAYER IMPORT
import database

# 1. Global Framework Page Configurations
st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

@st.cache_data(ttl=600)  # Caches the mock schemas in RAM for 10 minutes to stop reload lag
def get_cached_clients():
    return database.MOCK_CLIENTS_DB.copy()

@st.cache_data(ttl=600)
def get_cached_logtech():
    return database.MOCK_FLEET_TELEMETRY.copy()

@st.cache_data(ttl=600)
def get_cached_gridtech():
    return database.MOCK_GRID_TELEMETRY.copy()

@st.cache_data(ttl=600)
def get_cached_cybertech():
    return database.MOCK_CYBER_TELEMETRY.copy()

@st.cache_data(ttl=600)
def get_cached_transittech():
    return database.MOCK_TRANSIT_TELEMETRY.copy()

@st.cache_data(ttl=600)
def get_cached_healthtech():
    return database.MOCK_HEALTH_TELEMETRY.copy()

# 2. 🔐 STATE ENGINE ARCHITECTURE (Initializes data records inside active browser memory)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "user_data" not in st.session_state:
    st.session_state["user_data"] = None

if "DB_CLIENTS" not in st.session_state:
    st.session_state["DB_CLIENTS"] = get_cached_clients()
if "DB_LOGTECH" not in st.session_state:
    st.session_state["DB_LOGTECH"] = get_cached_logtech()
if "DB_GRIDTECH" not in st.session_state:
    st.session_state["DB_GRIDTECH"] = get_cached_gridtech()
if "DB_CYBERTECH" not in st.session_state:
    st.session_state["DB_CYBERTECH"] = get_cached_cybertech()
if "DB_TRANSITTECH" not in st.session_state:
    st.session_state["DB_TRANSITTECH"] = get_cached_transittech()
if "DB_HEALTHTECH" not in st.session_state:
    st.session_state["DB_HEALTHTECH"] = get_cached_healthtech()

def handle_logout():
    st.session_state["authenticated"] = False
    st.session_state["user_data"] = None
    st.rerun()

# 3. --- VIEW 1: EXECUTIVE HOME DIRECTORY PANEL RENDER FUNCTION ---
def render_home_portal():
    user_profile = st.session_state["user_data"]
    active_id = user_profile["client_id"]

    st.title("🛡️ FUZE TECH HOLDINGS — Gateway Portal")
    st.markdown("### *Central Infrastructure Control Center — Multi-Tenant Operating Hub*")
    st.divider()
    
    # Session Status Validation Alert Bar
    if any([user_profile["is_logtech_active"], user_profile["is_gridtech_active"], user_profile.get("is_cybertech_active", False), user_profile.get("is_transittech_active", False), user_profile.get("is_healthtech_active", False)]):
        st.success(f"🔓 **Active Database Session Token Verified.** Custom permission matrix mapped to: **{user_profile['account_name']}**.")
    else:
        st.error(f"🔒 **Limited Execution Mode:** Account `{active_id}` carries no active product tier licenses. All analytics sidebar routes are dynamically hidden.")
    
    # Portfolio Infrastructure Overview Data Metrics Block
        # 📊 Real-Time Monitored Infrastructure Footprint (Updated 5-Vertical Overview)
    st.markdown("#### 📊 Real-Time Monitored Infrastructure Footprint")
    
    # Split the screen into 5 equal columns to display all systems simultaneously
    kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)
    
    with kpi_col1:
        truck_count = len(st.session_state["DB_LOGTECH"].get(active_id, []))
        st.metric(label="🚚 Connected Fleets", value=f"{truck_count} Trucks Active" if user_profile["is_logtech_active"] else "0 Trucks Connected")
        
    with kpi_col2:
        meter_count = len(st.session_state["DB_GRIDTECH"].get(active_id, []))
        st.metric(label="⚡ Monitored Grid Nodes", value=f"{meter_count} Smart Meters" if user_profile["is_gridtech_active"] else "0 Smart Meters Connected")
        
    with kpi_col3:
        # Check if the specific client data row occupies a slot inside the CyberTech table
        cyber_count = len(st.session_state["DB_CYBERTECH"].get(active_id, []))
        st.metric(label="🛡️ Vetted API Checkouts", value=f"{cyber_count} Scanned" if user_profile.get("is_cybertech_active", False) else "0 Scanned")
        
    with kpi_col4:
        transit_count = len(st.session_state["DB_TRANSITTECH"].get(active_id, []))
        st.metric(label="🚌 Fleet Scanners", value=f"{transit_count} Busses Active" if user_profile.get("is_transittech_active", False) else "0 Busses Active")
    with kpi_col5:
        health_count = len(st.session_state["DB_HEALTHTECH"].get(active_id, []))
        st.metric(label="🏥 Refrigeration Nodes", value=f"{health_count} Units Tracked" if user_profile.get("is_healthtech_active", False) else "0 Units Tracked")

        
    st.divider()
    
    # 🚀 SUPABASE AUTOMATED API HANDSHAKE TILES
    st.markdown("#### 🏢 Unified Platform Ecosystem & Subscription Status")
    st.info("💡 *Live Demo Instructions:* Click an unsubscribed free trial module below. Paste the secure tracking provider API token from the hint box to simulate a real-world Supabase JSON fetch and write loop.")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # 🚚 1. LOGTECH AUTOMATED API ONBOARDING CARD (SUPABASE DEMO)
        with st.container(border=True):
            st.markdown("##### 🚚 Legacy Freight Lines (LogTech)")
            st.markdown("*Automated 2026 BURS custom clearance checks and real-time fuel-siphoning derivative analysis.*")
            if user_profile["is_logtech_active"]:
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Initialize LogTech Asset Node Integration"):
                    st.markdown("### 💳 Select Your Billing Alignment Model")

                    commercial_model = st.radio(
                        "Choose Onboarding Tier:",
                        [
                            "🎁 30-Day Free Trial (Onboard up to 5 trucks at R0.00)",
                            "💎 Direct Premium Enterprise Suite (Immediate Full Fleet Scale)"
                        ],
                        key="model_logTech"
                    )
                    st.divider()
                    if "30-Day" in commercial_model:
                        st.warning("⚠️ **Subscription Policy Notice:** Your account will automatically transition into a standard paid contract at R1,500/truck per month upon completion of the 30-day validation sprint, unless you manually submit a cancellation prompt through your profile management panel prior to expiration.")
                    else:
                        st.info("ℹ️ **Billing Policy Notice:** Immediate corporate invoicing loops will initialize at a flat R1,500 per managed logistics node per month.")

                    st.divider()
                    st.markdown("### 📡 API Token Gateway Handshake")
                    st.caption("Presentation Hint: Paste `cartrack_oauth2_token_881` into the field below.")
                    input_log_token = st.text_input("Enter Telematics Provider Read-Token ID", key="tk_logtech")
                    
                    if st.button("Establish API Loop Link", key="btn_connect_logtech"):
                        if input_log_token in database.REMOTE_TRACKING_SERVERS_JSON:
                            
                            # LIVE SUPABASE LOG CONSOLE ANIMATION
                            log_placeholder = st.empty()
                            with log_placeholder.container():
                                st.code("🔍 Resolving cross_border telematics fleet gateway address...", language="sql")
                                time.sleep(0.3)
                                if "30-Day" in commercial_model:
                                    st.code("📝 REGISTERING AUTO-RENEWAL MANDATE IN BILLING ENGINE...", language="sql")
                                    time.sleep(0.2)
                                st.code("⚡ CONNECTING TO SUPABASE POSTGRES CLUSTER...", language="sql")
                                time.sleep(0.2)
                                st.code(f"📝 INSERT INTO vehicles (client_id, registration, driver, route) VALUES ('{active_id}', ...);", language="sql")
                                time.sleep(0.2)
                                st.code("✅ TRANSACTION COMMITTED. Supabase cache tables synchronized.", language="sql")
                                time.sleep(0.2)
                            
                            log_placeholder.empty() 
                            
                            st.session_state["DB_LOGTECH"][active_id] = database.REMOTE_TRACKING_SERVERS_JSON[input_log_token]
                            st.session_state["user_data"]["is_logtech_active"] = True
                            for record in st.session_state["DB_CLIENTS"]:
                                if record["client_id"] == active_id:
                                    record["is_logtech_active"] = True
                                    break
                        else:
                            st.error("Connection Failed: Invalid or unauthorized API token string footprint.")
        st.write("") 
        
        # 🚌 4. TRANSITTECH TILES
        with st.container(border=True):
            st.markdown("##### 🚌 Legacy Transit Token (TransitTech)")
            st.markdown("*Eliminating card-sharing and screenshot forgery via database anti-passback lpgic and 30-second rotating cryptography tokens.*")
            if user_profile.get("is_transittech_active", False):
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Intialize TransitTech Security SDK"):
                    st.markdown("### 💳 Select Your Billing Alignment Model")
                    commercial_model = st.radio(
                        "Choose Onboarding Tier:",
                        [
                            "🎁 30-Day Free Trial (Provision up to a single transit routes at R0.00)",
                            "💎 Direct Premium Enterprise Suite (Immediate Global Campus Scale)"
                        ],
                        key="model_transitTech"
                    )
                    st.divider()
                    if "30-Day" in commercial_model:
                        st.warning("⚠️ **Subscription Policy Notice:** Your account will automatically transition into a paid contract at R800/bus per month upon completion of the 30-day trial, unless a cancellation prompt is manually submitted.")
                    else:
                        st.info("ℹ️ **Billing Policy Notice:** Corporate invoicing cycles will initialize immediately at a flat R800 per active operational transit node per month.")
                        
                    st.divider() 
                    st.markdown("### 📡 API Gateway Handshake")
                    st.caption("Presentation Hint: Type `wits_campus_transit_loop_key` into the field below.")
                    input_token = st.text_input("Enter Institutional Access Key ID", key="tk_transit")
                    
                    if st.button("Establish Campus Network API Link", key="btn_confirm_transit"):
                        if input_token == "wits_campus_transit_loop_key":
                            log_placeholder = st.empty()
                            with log_placeholder.container():
                                st.code("🔍 Routing campus mainframe server gateway parameters...", language="sql")
                                time.sleep(0.3)
                                if "30-Day" in commercial_model:
                                    st.code("📝 REGISTERING AUTO-RENEWAL MANDATE IN BILLING ENGINE...", language="sql")
                                    time.sleep(0.2)
                                st.code("📡 INTERFACING CONTROLLER: transit_gate_controller.py compiled at edge hardware...", language="python")
                                time.sleep(0.2)
                                st.code("📝 payload = {'client_institution_id': '" + active_id + "', 'vehicle_node_id': 'TERM-BUS-04'}", language="python")
                                time.sleep(0.2)
                                st.code("⚡ CONNECTING TO SUPABASE POSTGRES CLUSTER...", language="sql")
                                time.sleep(0.2)
                                st.code(f"📝 ALTER TABLE transit_scans ENABLE ROW LEVEL SECURITY;", language="sql")
                                time.sleep(0.2)
                                st.code("✅ TRANSACTION COMMITTED. Transit perimeter handshake established.", language="sql")
                                    
                            log_placeholder.empty()
             
                        st.session_state["DB_TRANSITTECH"][active_id] = database.MOCK_TRANSIT_TELEMETRY.get("CLIENT-442", [])
                        st.session_state["user_data"]["is_transittech_active"] = True
                        for record in st.session_state["DB_CLIENTS"]:
                            record["is_transittech_active"] = True
                            break
                    else:
                        st.error("Connection Failed: Remote institutional gateway endpoint rejected configuration.")

    with col2:
        # ⚡ 2. GRIDTECH AUTOMATED API ONBOARDING CARD (SUPABASE DEMO)
        with st.container(border=True):
            st.markdown("##### ⚡ Legacy Utility Labs (GridTech)")
            st.markdown("*Active prepaid meter fraud isolation by matching consumer usages directly against clip-on secondary line current transformers.*")
            if user_profile["is_gridtech_active"]:
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Initialize GridTech Substation Integration"):
                    st.markdown("### 💳 Select Your Billing Alignment Model")

                    commercial_model = st.radio(
                        "Choose Onboarding Tier:",
                        [
                            "🎁 30-Day Free Trial (Mount up to 10 smart meters at R0.00)", 
                            "💎 Direct Premium Enterprise Suite (Full Estate Infrastructure Portfolio)"
                        ],
                        key="model_gridTech"
                    )

                    st.divider()

                    if "30-Day" in commercial_model:
                        st.warning("⚠️ **Subscription Policy Notice:** Your account will automatically transition into a paid contract at R150/meter per month upon completion of the 30-day trial, unless a cancellation prompt is manually submitted.")
                    else:
                        st.info("ℹ️ **Billing Policy Notice:** Corporate invoicing cycles will initialize immediately at a flat R150 per micro property node per month.")

                    st.divider()

                    st.markdown("### 📡 API Token Gateway Handshake")
                    st.caption("Presentation Hint: Paste `city_power_grid_key_442` into the field below.")
                    input_grid_token = st.text_input("Enter Smart Grid API Key", key="tk_grid")
                    
                    if st.button("Establish Grid Handshake Link", key="btn_connect_gridtech"):
                        if input_grid_token in database.REMOTE_MUNICIPAL_GRID_JSON:
                            
                            # LIVE SUPABASE LOG CONSOLE ANIMATION
                            log_grid_placeholder = st.empty()
                            with log_grid_placeholder.container():
                                st.code("🔍 Resolving municipal current grid gateway address...", language="sql")
                                time.sleep(0.3)
                                if "30-Day" in commercial_model:
                                    st.code("📝 REGISTERING AUTO-RENEWAL MANDATE IN BILLING ENGINE...", language="sql")
                                    time.sleep(0.2)
                                st.code("⚡ CONNECTING TO SUPABASE POSTGRES CLUSTER...", language="sql")
                                time.sleep(0.2)
                                st.code(f"📝 INSERT INTO smart_meters (client_id, meter_id, location) VALUES ('{active_id}', ...);", language="sql")
                                time.sleep(0.2)
                                st.code("✅ TRANSACTION COMMITTED. Supabase database tables synchronized.", language="sql")
                            
                            log_grid_placeholder.empty()
                            
                            # Save records dynamically to active memory array
                        st.session_state["DB_GRIDTECH"][active_id] = database.REMOTE_MUNICIPAL_GRID_JSON[input_grid_token]
                        st.session_state["user_data"]["is_gridtech_active"] = True
                        for record in st.session_state["DB_CLIENTS"]:
                            if record["client_id"] == active_id:
                                record["is_gridtech_active"] = True
                                break
                    else:
                        st.error("Connection Failed: Remote utility endpoint handshake rejected.")
                        
        st.write("")
        
        # 🏥 5. HEALTHTECH TILES
        with st.container(border=True):
            st.markdown("##### 🏥 Legacy Cold Chain (HealthTech)")
            st.markdown("*Wireless sensor data streaming and predictive trajectory analysis inside clinic vaccine fridges to prevent thermal spoilage.*")
            if user_profile.get("is_healthtech_active", False):
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀  Initialize HealthTech Thermal Integration"):
                    st.markdown("### 💳 Hardware-as-a-Service Fulfillment Console")
                    
                    commercial_model = st.radio(
                        "Choose Onboarding Tier:",
                        [
                            "🎁 30-Day Free Trial (Link up to 3 medical refrigerators at R0.00)",
                            "💎 Direct Premium Enterprise Suite (Full Clinic Network Security)"
                        ],
                        key="model_healthTech"
                    )
                    st.divider()

                    fridge_count = st.number_input("Number of physical medication fridges to protect:", min_value=1, max_value=5, value=1)
                    delivery_address = st.text_input("Clinic Delivery Street Address", "10 Hospital Street, Braamfontein")
                    st.divider()
                    
                    if "30-Day" in commercial_model:
                        st.warning("⚠️ **Subscription Policy Notice:** Your account will automatically transition into a paid contract at R400/fridge per month upon completion of the 30-day trial, unless a cancellation prompt is manually submitted.")
                    else:
                        st.info("ℹ️ **Billing Policy Notice:** Corporate invoicing cycles will initialize immediately at a flat R400 per refrigeration asset per month.")
                    
                    st.divider()
                    
                    if st.button("Authorize Payment & Initialize Dispatch", key="btn_confirm_health"):
                        if delivery_address and fridge_count:
                            log_placeholder = st.empty()
                            with log_placeholder.container():
                                st.code("🔍 Processing merchant gateway checkout authentication token...", language="sql")
                                time.sleep(0.4)
                                if "30-Day" in commercial_model:
                                    st.code("📝 REGISTERING AUTO-RENEWAL PROFILES IN CONTRACT ENGINE...", language="sql")
                                    time.sleep(0.2)
                                    st.code(f"⚡ CONNECTING TO SUPABASE POSTGRES CLUSTER — WHITELISTING {int(fridge_count)} HARDWARE TRANSCIEVERS...", language="sql")
                                    time.sleep(0.2)
                                for i in range(int(fridge_count)):
                                    generated_sn = f"PRB-992{random.randint(1,9)}-X"
                                    st.code(f"📝 INSERT INTO cold_chain_probes (client_healthcare_id, physical_probe_serial) VALUES ('{active_id}', '{generated_sn}');", language="sql")
                                    time.sleep(0.2)
                                st.code("📡 ASSEMBLING ENTERPRISE DROPSHIP PAYLOAD TO HARDWARE DISTRIBUTOR...", language="sql")
                                time.sleep(0.2)
                                st.code(f"🚚 ROUTING COURIER API DELIVERY DESPATCH TO: {delivery_address}...", language="sql")
                                time.sleep(0.2)
                                st.code("✅ INVENTORY COMMITTED. Bootloader configuration whitelists synchronized with GitHub cloud source repositories.", language="sql")
                                time.sleep(0.2)
                            log_placeholder.empty()
                            
                        st.session_state["DB_HEALTHTECH"][active_id] = database.MOCK_HEALTH_TELEMETRY.get("CLIENT-442", [])
                        st.session_state["user_data"]["is_healthtech_active"] = True
                        for record in st.session_state["DB_CLIENTS"]:
                            if record["client_id"] == active_id:
                                record["is_healthtech_active"] = True
                                break
                    else:
                        st.error("Fulfillment Failed: Secure delivery street parameters are strictly mandatory.")

    with col3:
        # 🛡️ 3. CYBERTECH DYNAMIC ACTIVATION CARD
        with st.container(border=True):
            st.markdown("##### 🛡️ Legacy Sybil Gate (CyberTech)")
            st.markdown("*Protecting on-demand checkouts from automated promo abuse rings via unalterable device fingerprint hashes and location coordinate clustering.*")
            if user_profile.get("is_cybertech_active", False):
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Initialize CyberTech Protection Gateway"):
                    st.markdown("### 💳 Select Your Billing Alignment Model")
                    
                    commercial_model = st.radio(
                        "Choose Onboarding Tier:",
                        [
                            "🎁 30-Day Free Trial (First 10,000 checkout security sweeps at R0.00)",
                            "💎 Direct Premium Enterprise Suite (Uncapped High-Frequency Scale)"
                        ],
                        key="model_cyberTech"
                    )
                    st.divider()

                    if "30-Day" in commercial_model:
                        st.warning("⚠️ **Subscription Policy Notice:** Your account will automatically transition into a contract billed at R0.50 per scan upon completion of the 30-day trial, unless a cancellation prompt is manually submitted.")
                    else:
                        st.info("ℹ️ **Billing Policy Notice:** Operational API consumption counters will initialize immediately at R0.50 per individual transaction sweep.")
                        
                    st.divider()
                    st.markdown("### 📡 API SDK Integration Handshake")
                    st.caption("Presentation Hint: Type `secure_sybil_verification_endpoint_token` into the field below.")
                    input_token = st.text_input("Enter Operational SDK Integration Token ID", key="tk_cyber")
                    
                    if st.button("Connect Application Checkout SDK", key="btn_confirm_cybertech"):
                        if input_token == "secure_sybil_verification_endpoint_token":
                            log_placeholder = st.empty()
                            with log_placeholder.container():
                                st.code("🔍 Injecting asynchronous verification SDK listener loops...", language="sql")
                                time.sleep(0.3)
                                if "30-Day" in commercial_model:
                                    st.code("📝 REGISTERING AUTO-RENEWAL MANDATE IN BILLING ENGINE...", language="sql")
                                    time.sleep(0.2)
                                st.code("🛡️ CORE MODULE LINKED: sybil_gate_sdk.py compiled into client application checkout layer...", language="python")
                                time.sleep(0.2)
                                st.code("📝 payload = generate_checkout_verification_payload('" + active_id + "', user_alias, ...)", language="python")
                                time.sleep(0.2)
                                st.code("⚡ CONNECTING TO SUPABASE POSTGRES CLUSTER...", language="sql")
                                time.sleep(0.2)
                                st.code("✅ TRANSACTION COMMITTED. App checkout perimeter hardened.", language="sql")
                            log_placeholder.empty()
                            
                        st.session_state["DB_CYBERTECH"][active_id] = database.MOCK_CYBER_TELEMETRY.get("CLIENT-442", [])
                        st.session_state["user_data"]["is_cybertech_active"] = True
                        for record in st.session_state["DB_CLIENTS"]:
                            if record["client_id"] == active_id:
                                record["is_cybertech_active"] = True
                                break
                    else:
                        st.error("Connection Failed: Operational application server rejected integration keys.")

    with st.sidebar.popover("❌ Prompt Contract Cancellation"):
         st.markdown("### 🔏 Cancel Subscription / Trial Renewals")
         st.caption("Select which active industrial runtime pipelines you would like to terminate instantly.")
         cancel_logtech = st.checkbox("Terminate Legacy Freight Lines (LogTech)", value=False) if user_profile["is_logtech_active"] else False
         cancel_gridtech = st.checkbox("Terminate Legacy Utility Labs (GridTech)", value=False) if user_profile["is_gridtech_active"] else False
         cancel_cybertech = st.checkbox("Terminate Legacy Sybil Gate (CyberTech)", value-False) if user_profile["is_cybertech_active"] else False
         cancel_transittech = st.checkbox("Terminate Legacy Transit Token (TransitTech)", value=False) if user_profile["is_transittech_active"] else False
         cancel_healthtech = st.checkbox("Terminate Legacy Cold Chain (HealthTech)", value=False) if user_profile["is_healthtech_active"] else False

         if st.button("Confirm Immediate Pipeline Termination", key="btn_cancel_execution"):
             if cancel_logtech:
                 st.session_state["user_data"]["is_logtech_active"] = False
                 st.session_state["DB_LOGTECH"][active_id] = [] 
            
             if cancel_gridtech:
                 st.session_state["user_data"]["is_gridtech_active"] = False
                 st.session_state["DB_GRIDTECH"][active_id] = [] 
                
             if cancel_cybertech:
                 st.session_state["user_data"]["is_cybertech_active"] = False
                 st.session_state["DB_CYBERTECH"][active_id] = []
            
             if cancel_transittech:
                 st.session_state["user_data"]["is_transittech_active"] = False
                 st.session_state["DB_TRANSITTECH"][active_id] = []

             if cancel_healthtech:
                 st.session_state["user_data"]["is_healthtech_active"] = False
                 st.session_state["DB_HEALTHTECH"][active_id] = []

             for record in st.session_state["DB_CLIENTS"]:
                 if record["client_id"] == active_id:
                     if cancel_logtech: 
                         record["is_logtech_active"] = False
                     if cancel_gridtech: 
                         record["is_gridtech_active"] = False
                     if cancel_cybertech: 
                         record["is_cybertech_active"] = False
                     if cancel_transittech: 
                         record["is_transittech_active"] = False
                     if cancel_healthtech: 
                         record["is_healthtech_active"] = False
                     break

             st.toast("⚠️ Subscriptions terminated successfully. Relational nodes disconnected.", icon="🔒")
             time.sleep(1.0)

    st.rerun()

# 4. --- CONTEXT CONDITIONAL CONTROL INTERFACE REGISTRY ---
if not st.session_state["authenticated"]:
    # 🌟 NEW FEATURE: FULL WIDTH REGISTRATION & LOGIN TAB HUB
    st.title("🛡️ FUZE TECH HOLDINGS — Control Portal")
    st.markdown("### Enterprise Multi-Tenant Infrastructure Gateway")
    st.divider()
    tab_login, tab_register = st.tabs(["🔒 Account Login", "📝 New Client Registration"])
    with tab_login:
        st.info("""💡 Demo Instruction Panel for the Tshimologong Selectors:\n
        • To test an Unsubscribed Lead (Enables popover API trials): `lead@fuzetech.co.za` (Password: `password123`)\n
        • To test an Active Subscribed Client:** `operations@supergroup.co.za` (Password: `superfleet2026`)\n
        • Or use the Registration tab to create an entirely new human account live!""")
        
        login_email = st.text_input("Corporate Account Email", key="log_email")
        login_password = st.text_input("Security Access Password", type="password", key="log_pass")
        
        if st.button("Authenticate Session", key="btn_login_submit"):
            matched_user = None
            cleaned_email = login_email.lower().strip()
            
            for record in st.session_state["DB_CLIENTS"]:
                if record["email"].lower().strip() == cleaned_email and record["password"] == login_password:
                    matched_user = record.copy()
                    break
                    
            if matched_user:
                st.session_state["authenticated"] = True
                st.session_state["user_data"] = matched_user
                st.success("Access Token Authorized. Routing Workspace...")
                st.rerun()
            else:
                st.error("Authentication Denied: Invalid cryptographic identifier matching.")
                
    with tab_register:
        st.markdown("#### 📋 Establish Your Shared Multi-Tenant Tenant Profile")
        st.caption("Please input your official firm metadata parameters. This creates an isolated database row state instantly.")
        
        reg_company = st.text_input("Corporate Company Name (e.g., Barloworld Transport)")
        reg_email = st.text_input("Corporate Operational Email Address")
        reg_password = st.text_input("Create Security Password", type="password")
        reg_confirm_password = st.text_input("Confirm Security Password", type="password")
        
        if st.button("Commit Registration to Cloud Database", key="btn_register_submit"):
            # Operational Edge Case Input Validation Checks
            if not reg_company or not reg_email or not reg_password:
                st.error("Submission Failed: All registration entry variables are strictly mandatory.")
            elif reg_password != reg_confirm_password:
                st.error("Submission Failed: Password validation conflict. Confirmation string must match.")
            else:
                # Check if email is already taken inside session memory
                email_exists = any(r["email"].lower().strip() == reg_email.lower().strip() for r in st.session_state["DB_CLIENTS"])
                if email_exists:
                    st.error("Submission Failed: Email identifier already occupies an active tenant slot.")
                else:
                    # Dynamically generate unique client structural metadata values
                    new_tenant_id = f"CLIENT-{random.randint(500, 999)}"
                    new_profile = {
                        "email": reg_email.lower().strip(),
                        "password": reg_password,
                        "account_name": reg_company,
                        "client_id": new_tenant_id,
                        "is_logtech_active": False,
                        "is_gridtech_active": False,
                        "is_cybertech_active": False,
                        "is_transittech_active": False,
                        "is_healthtech_active": False
                    }
                    
                    # Dynamically append the new row into the global database state memory array
                    st.session_state["DB_CLIENTS"].append(new_profile)
                    st.success(f"🎉 Registration Committed Successfully! Profile row established. Tenant UUID assigned: {new_tenant_id}. Please toggle back to the 'Account Login' tab above and sign in.")

else:
    user_profile = st.session_state["user_data"]
    active_id = user_profile["client_id"]
    
    st.sidebar.title("🏢 Fuze Tech Gateway")
    st.sidebar.markdown(f"Operator Group:\n{user_profile['account_name']}")
    st.sidebar.markdown(f"Tenant UUID: {active_id}")
    
    if st.sidebar.button("Secure Session Sign Out"):
        handle_logout()
    st.sidebar.divider()
    
    home_page = st.Page(render_home_portal, title="Home Control Center", icon="🏢")
    navigation_pool = [home_page]
    
    if user_profile["is_logtech_active"]:
        logtech_page = st.Page("freight_lines.py", title="Legacy Freight Lines", icon="🚚")
        navigation_pool.append(logtech_page)
        
    if user_profile["is_gridtech_active"]:
        gridtech_page = st.Page("utility_labs.py", title="Legacy Utility Labs", icon="⚡")
        navigation_pool.append(gridtech_page)
        
    if user_profile.get("is_cybertech_active", False):
        cybertech_page = st.Page("sybil_gate.py", title="Legacy Sybil Gate", icon="🛡️")
        navigation_pool.append(cybertech_page)
        
    if user_profile.get("is_transittech_active", False):
        transittech_page = st.Page("transit_token.py", title="Legacy Transit Token", icon="🚌")
        navigation_pool.append(transittech_page)
        
    if user_profile.get("is_healthtech_active", False):
        healthtech_page = st.Page("cold_chain.py", title="Legacy Cold Chain", icon="🏥")
        navigation_pool.append(healthtech_page)
        
    nav = st.navigation(navigation_pool)
    nav.run()
