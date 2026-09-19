import streamlit as st
import pandas as pd
import time

# 🔄 GLOBAL DATA LAYER IMPORT
import database

# Global Framework Page Configurations
st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

# 🔐 STATE ENGINE ARCHITECTURE (Initializes data records inside active browser memory)
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

# --- VIEW 1: EXECUTIVE HOME DIRECTORY PANEL RENDER FUNCTION ---
def render_home_portal():
    user_profile = st.session_state["user_data"]
    active_id = user_profile["client_id"]
    
    st.title("🛡️ FUZE TECH HOLDINGS — Gateway Portal")
    st.markdown("### *Central Infrastructure Control Center — Multi-Tenant Operating Hub*")
    st.divider()
    
    if any([user_profile["is_logtech_active"], user_profile["is_gridtech_active"], user_profile.get("is_cybertech_active", False)]):
        st.success(f"🔓 **Active Database Session Token Verified.** Custom permission matrix mapped to: **{user_profile['account_name']}**.")
    else:
        st.error(f"🔒 **Limited Execution Mode:** Account `{active_id}` carries no active product tier licenses. Analytics routes are locked.")
    
    # Portfolio Infrastructure Overview Data Metrics Block
    st.markdown("#### 📊 Real-Time Monitored Infrastructure Footprint")
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    with kpi_col1:
        truck_count = len(st.session_state["DB_LOGTECH"].get(active_id, []))
        st.metric(label="🚚 Connected Fleet Assets", value=f"{truck_count} Trucks Active" if user_profile["is_logtech_active"] else "0 Trucks Connected")
    with kpi_col2:
        meter_count = len(st.session_state["DB_GRIDTECH"].get(active_id, []))
        st.metric(label="⚡ Monitored Grid Nodes", value=f"{meter_count} Smart Meters" if user_profile["is_gridtech_active"] else "0 Smart Meters Connected")
    with kpi_col3:
        st.metric(label="🛡️ Pipeline Security Perimeter", value="Active", delta="Multi-Tenant Row Isolation Intact")
        
    st.divider()
    
    # 🚀 REAL-WORLD API HANDSHAKE WORKSPACE BOARDS
    st.markdown("#### 🏢 Unified Platform Ecosystem & Subscription Status")
    st.info("💡 *Live Demo Instructions:* Click an unsubscribed free trial module below. Paste the secure tracking provider API token from the hint box to simulate a real-world JSON telemetry fetch loop.")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # 🚚 1. LOGTECH AUTOMATED API ONBOARDING TILES
        with st.container(border=True):
            st.markdown("##### 🚚 Legacy Freight Lines (LogTech)")
            st.markdown("*Automated 2026 BURS custom clearance checks and real-time fuel-siphoning derivative analysis.*")
            if user_profile["is_logtech_active"]:
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Connect Third-Party Telematics API"):
                    st.markdown("### 📡 API Token Gateway Handshake")
                    st.caption("Hint: Paste `cartrack_oauth2_token_881` to initiate automated json fetch.")
                    input_token = st.text_input("Enter Telematics Provider Read-Token ID", key="tk_logtech")
                    
                    if st.button("Establish API Loop Link", key="btn_connect_logtech"):
                        if input_token in database.REMOTE_TRACKING_SERVERS_JSON:
                            with st.spinner("Executing secure handshake... Fetching remote hardware JSON arrays..."):
                                time.sleep(1.5) # Simulates network latency
                            
                            # Real-World Simulation Loop: Grabs JSON dictionary array and writes straight to memory
                            fetched_json = database.REMOTE_TRACKING_SERVERS_JSON[input_token]
                            st.session_state["DB_LOGTECH"][active_id] = fetched_json
                            st.session_state["user_data"]["is_logtech_active"] = True
                            
                            for record in st.session_state["DB_CLIENTS"]:
                                if record["client_id"] == active_id:
                                    record["is_logtech_active"] = True
                                    break
                                    
                            st.balloons()
                            st.success("API Link Established! 3 Trucks successfully mapped via telemetry stream in 1.5s with zero manual input.")
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
                    if st.button("Link Student Portal Gateway", key="btn_confirm_transit"):
                        st.session_state["user_data"]["is_transittech_active"] = True
                        st.balloons()
                        st.rerun()

    with col2:
        # ⚡ 2. GRIDTECH AUTOMATED API ONBOARDING TILES
        with st.container(border=True):
            st.markdown("##### ⚡ Legacy Utility Labs (GridTech)")
            st.markdown("*Cross-referencing smart meters against sectional line current transformers to identify grid bypass fraud.*")
            if user_profile["is_gridtech_active"]:
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Connect Municipal Smart Grid API"):
                    st.markdown("### 📡 Municipal Grid Handshake Console")
                    st.caption("Hint: Paste `city_power_grid_key_442` to pull local substation datasets.")
                    input_grid_token = st.text_input("Enter Smart Grid API Key", key="tk_grid")
                    
                    if st.button("Establish Grid Handshake Link", key="btn_connect_gridtech"):
                        if input_grid_token in database.REMOTE_MUNICIPAL_GRID_JSON:
                            with st.spinner("Connecting municipal endpoints... Syncing transformer telemetry..."):
                                time.sleep(1.5)
                            
                            fetched_grid_json = database.REMOTE_MUNICIPAL_GRID_JSON[input_grid_token]
                            st.session_state["DB_GRIDTECH"][active_id] = fetched_grid_json
                            st.session_state["user_data"]["is_gridtech_active"] = True
                            
                            for record in st.session_state["DB_CLIENTS"]:
                                if record["client_id"] == active_id:
                                    record["is_gridtech_active"] = True
                                    break
                                    
                            st.balloons()
                            st.success("Grid Connection Secure! 3 Sectional meters balanced and live mapped.")
                            st.rerun()
                        else:
                            st.error("Connection Failed: Remote utility endpoint handshake rejected.")
        st.write("") 
        
        # 🏥 5. HEALTHTECH TILES
        with st.container(border=True):
            st.markdown("##### 🏥 Legacy Cold Chain (HealthTech)")
            st.markdown("*Wireless temperature sensor analytics and predictive trajectory tracking inside clinical fridges.*")
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
            st.markdown("*Defeating coupon abuse fraud on fast food aggregator checkouts via unalterable hardware profiling and geographic address clustering.*")
            if user_profile.get("is_cybertech_active", False):
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Link CyberTech API Gateway"):
                    if st.button("Connect Application Checkout SDK", key="btn_confirm_cybertech"):
                        st.session_state["user_data"]["is_cybertech_active"] = True
                        st.rerun()
if not st.session_state["authenticated"]:
    st.title("🔒 FUZE TECH HOLDINGS — Secure Login Gateway")
    st.markdown("### Enterprise Multi-Tenant Infrastructure Portal")
    st.divider()
    st.info("""💡 Demo Instruction Panel for the Tshimologong Selectors:
- **To test an Unsubscribed Lead (Enables popover API trials):** `lead@fuzetech.co.za` (Password: `password123`)
- **To test an Active Subscribed Client:** `operations@supergroup.co.za` (Password: `superfleet2026`)""")
    
    login_email = st.text_input("Corporate Account Email")
    login_password = st.text_input("Security Access Password", type="password")
    
    if st.button("Authenticate Session"):
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

