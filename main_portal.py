import streamlit as st
import pandas as pd

# 🔄 DATA LAYER INTEGRATION LOOP
from database import MOCK_CLIENTS_DB, MOCK_FLEET_TELEMETRY, MOCK_GRID_TELEMETRY

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
- **To test an Unsubscribed Lead (Marketplace/30-Day Offer):** `lead@fuzetech.co.za` (Password: `password123`)
- **To test Subscribed Client A (Super Group Data Split):** `operations@supergroup.co.za` (Password: `superfleet2026`)
- **To test Subscribed Client B (Imperial Group Data Split):** `director@imperial.co.za` (Password: `enterpriseultra`)""")
    
    login_email = st.text_input("Corporate Account Email")
    login_password = st.text_input("Security Access Token Key", type="password")
    
       # Locate this section inside your main_portal.py code:
    if st.button("Authenticate Session"):
        # The Automated Token Loop: Standardizing inputs to prevent case errors
        matched_user = None
        cleaned_email = login_email.lower().strip() # <-- Forces lowercase and strips empty spaces
        
        for record in MOCK_CLIENTS_DB:
            if record["email"].lower().strip() == cleaned_email and record["password"] == login_password:
                matched_user = record
                break
        
        if matched_user:
            # Token Loop Validated: Assign values to session memory state
            st.session_state["authenticated"] = True
            st.session_state["user_data"] = matched_user
            st.success("Session Token Generated Successfully! Redirecting...")
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
    
    def render_home_portal():
        st.title("🛡️ FUZE TECH HOLDINGS — Gateway Portal")
        st.markdown("### *Central Infrastructure Control Center — Multi-Tenant Operating Hub*")
        st.divider()
        
        if user_profile["is_logtech_active"] or user_profile["is_gridtech_active"]:
            st.success(f"🔓 **Active Database Isolation Token Verified.** Currently streaming isolated data blocks mapped to **{user_profile['account_name']}**.")
        else:
            st.error(f"🔒 **Limited Execution Mode:** Account `{active_id}` does not carry an authorized runtime software license. Active data pipelines are locked.")
            with st.container(border=True):
                st.markdown("### 🚀 Initialize Your 30-Day Free Trial Subscription")
                st.markdown("Deploy our automated stream-processing algorithms over your assets for 30 days risk-free. Catch anomalies, stop fuel theft, or track grid fraud with zero upfront capital hardware expenditure.")
                b_col1, b_col2 = st.columns(2)
                with b_col1:
                    if st.button("Activate 30-Day Legacy Freight Lines Trial"):
                        st.balloons()
                        st.success("LogTech Trial Pipeline Request Scheduled.")
                with b_col2:
                    if st.button("Activate 30-Day Legacy Utility Labs Trial"):
                        st.balloons()
                        st.success("GridTech Trial Pipeline Request Scheduled.")
            st.divider()
        
        st.markdown("#### 📊 Real-Time Node Telematics Overview")
        kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
        with kpi_col1:
            truck_count = len(MOCK_FLEET_TELEMETRY.get(active_id, []))
            st.metric(label="Connected Fleet Assets", value=f"{truck_count} Trucks Active" if user_profile["is_logtech_active"] else "0 Trucks Connected")
        with kpi_col2:
            meter_count = len(MOCK_GRID_TELEMETRY.get(active_id, []))
            st.metric(label="Monitored Grid Nodes", value=f"{meter_count} Smart Meters" if user_profile["is_gridtech_active"] else "0 Smart Meters Connected")
        with kpi_col3:
            st.metric(label="Cloud Pipeline Integrity", value="100% Secure", delta="Row-Level Security Active")

    # --- 🛠️ AUTOMATED NAVIGATION MANAGER MAPS ---
    home_page = st.Page(render_home_portal, title="Home Control Center", icon="🏢")
    navigation_pool = [home_page]
    
    # Point the routing targets to your external view paths inside the subfolder
    if user_profile["is_logtech_active"]:
        logtech_page = st.Page("views/freight_lines.py", title="Legacy Freight Lines", icon="🚚")
        navigation_pool.append(logtech_page)
        
    if user_profile["is_gridtech_active"]:
        gridtech_page = st.Page("views/utility_labs.py", title="Legacy Utility Labs", icon="⚡")
        navigation_pool.append(gridtech_page)
        
    nav = st.navigation(navigation_pool)
    nav.run()
