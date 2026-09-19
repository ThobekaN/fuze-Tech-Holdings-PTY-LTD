import streamlit as st
import pandas as pd

# 🔄 DATA LAYER INTEGRATION LOOP
from database import MOCK_CLIENTS_DB, MOCK_FLEET_TELEMETRY, MOCK_GRID_TELEMETRY, MOCK_CYBER_TELEMETRY, MOCK_TRANSIT_TELEMETRY, MOCK_HEALTH_TELEMETRY

# Global Framework Page Configurations
st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "user_data" not in st.session_state:
    st.session_state["user_data"] = None

def handle_logout():
    st.session_state["authenticated"] = False
    st.session_state["user_data"] = None
    st.rerun()

if not st.session_state["authenticated"]:
    st.title("🔒 FUZE TECH HOLDINGS — Secure Login Gateway")
    st.markdown("### *Enterprise Multi-Tenant Infrastructure Portal*")
    st.divider()
    
    st.info("""💡 **Demo Instruction Panel for the Tshimologong Selectors:**
- **To test an Unsubscribed Lead (Marketplace/All Trials Open):** `lead@fuzetech.co.za` (Password: `password123`)
- **To test Subscribed Client A (Super Group Logistics):** `operations@supergroup.co.za` (Password: `superfleet2026`)
- **To test Subscribed Client B (Imperial Group — FULL ENTERPRISE SUITE):** `director@imperial.co.za` (Password: `enterpriseultra`)""")
    
    login_email = st.text_input("Corporate Account Email")
    login_password = st.text_input("Security Access Token Key", type="password")
    
    if st.button("Authenticate Session"):
        matched_user = None
        cleaned_email = login_email.lower().strip()
        for record in MOCK_CLIENTS_DB:
            if record["email"].lower().strip() == cleaned_email and record["password"] == login_password:
                matched_user = record
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
    st.sidebar.markdown(f"**Operator Group:**\n`{user_profile['account_name']}`")
    st.sidebar.markdown(f"**Tenant UUID:** `{active_id}`")
    if st.sidebar.button("Secure Session Sign Out"):
        handle_logout()
    st.sidebar.divider()
    
    # --- INTERFACE WORKSPACE 1: EXECUTIVE HOME DIRECTORY PANEL ---
    def render_home_portal():
        st.title("🛡️ FUZE TECH HOLDINGS — Gateway Portal")
        st.markdown("### *Central Infrastructure Control Center — Multi-Tenant Operating Hub*")
        st.divider()
        
        # General Status Alert Strip
        if any([user_profile["is_logtech_active"], user_profile["is_gridtech_active"], user_profile["is_cybertech_active"], user_profile["is_transittech_active"], user_profile["is_healthtech_active"]]):
            st.success(f"🔓 **Active Database Session Token Verified.** Custom permission matrix mapped to: **{user_profile['account_name']}**.")
        else:
            st.error(f"🔒 **Limited Execution Mode:** Account `{active_id}` carries no active product tier licenses. All analytics sidebar routes are dynamically hidden.")
        
        # Portfolio Infrastructure Overview Data Metrics Block
        st.markdown("#### 📊 Real-Time Monitored Infrastructure Footprint")
        kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
        with kpi_col1:
            truck_count = len(MOCK_FLEET_TELEMETRY.get(active_id, []))
            st.metric(label="🚚 Connected Fleet Assets", value=f"{truck_count} Trucks Active" if user_profile["is_logtech_active"] else "0 Trucks Connected")
        with kpi_col2:
            meter_count = len(MOCK_GRID_TELEMETRY.get(active_id, []))
            st.metric(label="⚡ Monitored Grid Nodes", value=f"{meter_count} Smart Meters" if user_profile["is_gridtech_active"] else "0 Smart Meters Connected")
        with kpi_col3:
            st.metric(label="🛡️ Pipeline Security Perimeter", value="Active", delta="Multi-Tenant Row Isolation Intact")
            
        st.divider()
        
        # 🚀 30-DAY FREE TRIAL DYNAMIC SUBSCRIPTION WORKSPACE BOARDS
        st.markdown("#### 🏢 Unified Platform Ecosystem & Subscription Status")
        st.info("💡 *How it works:* Subscribed modules unlock secure data visualization paths in your sidebar. Unsubscribed modules dynamically render a zero-risk 30-Day Free Trial activation module right below.")
        st.write("")
        
        # Grid Matrix Layout for all 5 Software Verticals
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # 1. LOGTECH TILES
            with st.container(border=True):
                st.markdown("##### 🚚 Legacy Freight Lines (LogTech)")
                st.markdown("*Cross-border telematics, siphoning engines, and 2026 BURS custom declaration automation.*")
                if user_profile["is_logtech_active"]:
                    st.success("🟢 Active Subscription Billed")
                else:
                    st.error("🔴 License Status: Unsubscribed")
                    if st.button("🚀 Activate 30-Day Free Trial", key="trial_logtech"):
                        st.balloons()
                        st.success("LogTech Pipeline Active! Refreshing network keys...")
            
            st.write("") # Layout spacer element
            
            # 4. TRANSITTECH TILES
            with st.container(border=True):
                st.markdown("##### 🚌 Legacy Transit Token (TransitTech)")
                st.markdown("*Shuttle access management using strict anti-passback rules and 30s rotating tokens.*")
                if user_profile.get("is_transittech_active", False):
                    st.success("🟢 Active Subscription Billed")
                else:
                    st.error("🔴 License Status: Unsubscribed")
                    if st.button("🚀 Activate 30-Day Free Trial", key="trial_transit"):
                        st.balloons()
                        st.success("TransitTech Pipeline Active! Syncing scanner nodes...")

        with col2:
            # 2. GRIDTECH TILES
            with st.container(border=True):
                st.markdown("##### ⚡ Legacy Utility Labs (GridTech)")
                st.markdown("*Cross-referencing smart meters against sectional line current transformers to identify grid bypass fraud.*")
                if user_profile["is_gridtech_active"]:
                    st.success("🟢 Active Subscription Billed")
                else:
                    st.error("🔴 License Status: Unsubscribed")
                    if st.button("🚀 Activate 30-Day Free Trial", key="trial_gridtech"):
                        st.balloons()
                        st.success("GridTech Pipeline Active! Syncing transformer metrics...")
            
            st.write("") # Layout spacer element
            
            # 5. HEALTHTECH TILES
            with st.container(border=True):
                st.markdown("##### 🏥 Legacy Cold Chain (HealthTech)")
                st.markdown("*Wireless temperature sensor analytics and predictive trajectory tracking inside clinical fridges.*")
                if user_profile.get("is_healthtech_active", False):
                    st.success("🟢 Active Subscription Billed")
                else:
                    st.error("🔴 License Status: Unsubscribed")
                    if st.button("🚀 Activate 30-Day Free Trial", key="trial_health"):
                        st.balloons()
                        st.success("HealthTech Pipeline Active! Initializing thermal alarms...")

        with col3:
            # 3. CYBERTECH TILES
            with st.container(border=True):
                st.markdown("##### 🛡️ Legacy Sybil Gate (CyberTech)")
                st.markdown("*Defeating coupon abuse fraud on fast food aggregator checkouts via unalterable hardware profiling and geographic address clustering.*")
                if user_profile.get("is_cybertech_active", False):
                    st.success("🟢 Active Subscription Billed")
                else:
                    st.error("🔴 License Status: Unsubscribed")
                    if st.button("🚀 Activate 30-Day Free Trial", key="trial_cybertech"):
                        st.balloons()
                        st.success("CyberTech Pipeline Active! Generating secure API tokens...")

    # --- 🛠️ AUTOMATED NAVIGATION MANAGER MAPS ---
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
