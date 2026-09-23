import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime

# 🔄 GLOBAL DATA LAYER IMPORT
import database

# 1. Global Framework Page Configurations
st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

# 2. 🔐 STATE ENGINE ARCHITECTURE (Initializes data records inside active browser memory)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "user_data" not in st.session_state:
    st.session_state["user_data"] = None

if "DB_CLIENTS" not in st.session_state:
    st.session_state["DB_CLIENTS"] = database.MOCK_CLIENTS_DB.copy()
if "DB_LOGTECH" not in st.session_state:
    st.session_state["DB_LOGTECH"] = database.MOCK_FLEET_TELEMETRY.copy()
if "DB_GRIDTECH" not in st.session_state:
    st.session_state["DB_GRIDTECH"] = database.MOCK_GRID_TELEMETRY.copy()
if "DB_CYBERTECH" not in st.session_state:
    st.session_state["DB_CYBERTECH"] = database.MOCK_CYBER_TELEMETRY.copy()

def handle_logout():
    st.session_state["authenticated"] = False
    st.session_state["user_data"] = None
    st.rerun()

# 3. --- VIEW 1: EXECUTIVE HOME DIRECTORY PANEL RENDER FUNCTION ---
def render_home_portal():
    user_profile = st.session_state["user_data"]
    active_id = user_profile["client_id"]

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

    st.title("🛡️ FUZE TECH HOLDINGS — Gateway Portal")
    st.markdown("### *Central Infrastructure Control Center — Multi-Tenant Operating Hub*")
    st.divider()
    
    # Session Status Validation Alert Bar
    if any([user_profile["is_logtech_active"], user_profile["is_gridtech_active"], user_profile.get("is_cybertech_active", False)]):
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
        # Check if the specific client data row occupies a slot inside the TransitTech table
        transit_count = len(database.MOCK_TRANSIT_TELEMETRY.get(active_id, []))
        st.metric(label="🚌 Fleet Scanner Modules", value=f"{transit_count} Busses Active" if user_profile.get("is_transittech_active", False) else "0 Busses Active")
        
    with kpi_col5:
        # Check if the specific client data row occupies a slot inside the HealthTech table
        health_count = len(database.MOCK_HEALTH_TELEMETRY.get(active_id, []))
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
                    input_token = st.text_input("Enter Telematics Provider Read-Token ID", key="tk_logtech")
                    
                    if st.button("Establish API Loop Link", key="btn_connect_logtech"):
                        if input_token in database.REMOTE_TRACKING_SERVERS_JSON:
                            
                            # LIVE SUPABASE LOG CONSOLE ANIMATION
                            log_placeholder = st.empty()
                            with log_placeholder.container():
                                st.code("🔍 Initializing client handshake routing...", language="sql")
                                time.sleep(0.5)
                                st.code("⚡ Access token validated. Requesting raw telematics metadata payload...", language="sql")
                                time.sleep(0.6)
                                st.code("📦 JSON payload received from remote server tracking endpoints...", language="sql")
                                time.sleep(0.5)

                                if "30-Day" in commercial_model:
                                    st.code("📝 REGISTERING AUTO-RENEWAL MANDATE IN BILLING ENGINE...", language="sql")
                                    time.sleep(0.4)
                                st.code("⚡ CONNECTING TO SUPABASE POSTGRES CLUSTER...", language="sql")
                                time.sleep(0.4)
                                st.code(f"📝 INSERT INTO vehicles (client_id, registration, driver, route) VALUES ('{active_id}', ...);", language="sql")
                                time.sleep(0.5)
                                st.code("✅ TRANSACTION COMMITTED. Supabase cache tables synchronized.", language="sql")
                                time.sleep(0.4)
                            
                            log_placeholder.empty() 
                            
                            # Real-World Simulation Loop: Grabs JSON data block and writes to memory state
                            fetched_json = database.REMOTE_TRACKING_SERVERS_JSON[input_token]
                            st.session_state["DB_LOGTECH"][active_id] = fetched_json
                            
                            # Mutate active user token state metrics
                            st.session_state["user_data"]["is_logtech_active"] = True
                            for record in st.session_state["DB_CLIENTS"]:
                                if record["client_id"] == active_id:
                                    record["is_logtech_active"] = True
                                    break
                                    
                            st.balloons()
                            if "30-Day" in commercial_model:
                                st.success("Supabase Link Secure! 3 Trucks successfully mapped under your 30-Day Trial. Auto-renew parameters registered.")
                            else:
                                st.success("Supabase Link Secure! 3 Trucks successfully mapped under your Premium Enterprise contract. Invoicing active.")
                            st.rerun()
                        else:
                            st.error("Connection Failed: Invalid or unauthorized API token string footprint.")
        st.write("") 
        
        # 🚌 4. TRANSITTECH TILES
        with st.container(border=True):
            st.markdown("##### 🚌 Legacy Transit Token (TransitTech)")
            st.markdown("*Shuttle access management using strict anti-passback rules and 30s rotating tokens.*")
            if user_profile.get("is_transittech_active", False):
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Connect Transit API"):
                    if st.button("Establish Campus Network API Link", key="btn_confirm_transit"):
                        st.session_state["user_data"]["is_transittech_active"] = True
                        st.balloons()
                        st.rerun()

    with col2:
        # ⚡ 2. GRIDTECH AUTOMATED API ONBOARDING CARD (SUPABASE DEMO)
        with st.container(border=True):
            st.markdown("##### ⚡ Legacy Utility Labs (GridTech)")
            st.markdown("*Cross-referencing smart meters against sectional line current transformers to identify grid bypass fraud.*")
            if user_profile["is_gridtech_active"]:
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Connect Municipal Smart Grid API"):
                    st.markdown("### 📡 Municipal Grid Handshake Console")
                    st.caption("Presentation Hint: Paste `city_power_grid_key_442` into the field below.")
                    input_grid_token = st.text_input("Enter Smart Grid API Key", key="tk_grid")
                    
                    if st.button("Establish Grid Handshake Link", key="btn_connect_gridtech"):
                        if input_grid_token in database.REMOTE_MUNICIPAL_GRID_JSON:
                            
                            # LIVE SUPABASE LOG CONSOLE ANIMATION
                            log_grid_placeholder = st.empty()
                            with log_grid_placeholder.container():
                                st.code("🔍 Resolving municipal current grid gateway address...", language="sql")
                                time.sleep(0.5)
                                st.code("📦 Fetching live sectional line transformer load objects...", language="sql")
                                time.sleep(0.6)
                                st.code("⚡ CONNECTING TO SUPABASE POSTGRES CLUSTER...", language="sql")
                                time.sleep(0.4)
                                st.code(f"📝 INSERT INTO smart_meters (client_id, meter_id, location) VALUES ('{active_id}', ...);", language="sql")
                                time.sleep(0.5)
                                st.code("✅ TRANSACTION COMMITTED. Supabase database tables synchronized.", language="sql")
                                time.sleep(0.4)
                            
                            log_grid_placeholder.empty()
                            
                            # Save records dynamically to active memory array
                        fetched_grid_json = database.REMOTE_MUNICIPAL_GRID_JSON[input_grid_token]
                        st.session_state["DB_GRIDTECH"][active_id] = fetched_grid_json
                        st.session_state["user_data"]["is_gridtech_active"] = True
                        
                        for record in st.session_state["DB_CLIENTS"]:
                            if record["client_id"] == active_id:
                                record["is_gridtech_active"] = True
                                break
                                
                        st.balloons()
                        st.success("Supabase Link Secure! 3 Sectional meters balanced and live mapped.")
                        st.rerun()
                    else:
                        st.error("Connection Failed: Remote utility endpoint handshake rejected.")
                        
        st.write("")
        
        # 🏥 5. HEALTHTECH TILES
        with st.container(border=True):
            st.markdown("##### 🏥 Legacy Cold Chain (HealthTech)")
            st.markdown("Wireless temperature sensor analytics and predictive trajectory tracking inside clinical fridges.")
            if user_profile.get("is_healthtech_active", False):
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Connect HealthTech API"):
                    if st.button("Link Wireless Thermal Probes", key="btn_confirm_health"):
                        st.session_state["user_data"]["is_healthtech_active"] = True
                        st.balloons()
                        st.rerun()

    with col3:
        # 🛡️ 3. CYBERTECH DYNAMIC ACTIVATION CARD
        with st.container(border=True):
            st.markdown("##### 🛡️ Legacy Sybil Gate (CyberTech)")
            st.markdown("Defeating coupon abuse fraud on fast food aggregator checkouts via unalterable hardware profiling and geographic address clustering.")
            if user_profile.get("is_cybertech_active", False):
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Link CyberTech API Gateway"):
                    if st.button("Connect Application Checkout SDK", key="btn_confirm_cybertech"):
                        st.session_state["user_data"]["is_cybertech_active"] = True
                        st.balloons()
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
