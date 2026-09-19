import streamlit as st
import pandas as pd
from datetime import datetime

# 🔄 DATA LAYER INTEGRATION LOOP
from database import MOCK_CLIENTS_DB, MOCK_FLEET_TELEMETRY, MOCK_GRID_TELEMETRY

# Global Framework Page Configurations
st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

# Initialize Context Memory Tokens (Session State Flags)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "user_data" not in st.session_state:
    st.session_state["user_data"] = None

def handle_logout():
    st.session_state["authenticated"] = False
    st.session_state["user_data"] = None
    st.rerun()

# --- CONTEXT CONDITIONAL CONTROL: LOGIN ENVELOPE OR ACCOUNT WORKSPACE ---
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
    
    if st.button("Authenticate Session"):
        matched_user = None
        for record in MOCK_CLIENTS_DB:
            if record["email"] == login_email and record["password"] == login_password:
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
    
    # Configure Corporate Shared Sidebar Access Controls
    st.sidebar.title("🏢 Fuze Tech Gateway")
    st.sidebar.markdown(f"👤 **Operator Group:**\n`{user_profile['account_name']}`")
    st.sidebar.markdown(f"🆔 **Tenant UUID:** `{active_id}`")
    if st.sidebar.button("Secure Session Sign Out"):
        handle_logout()
    st.sidebar.divider()
    
    # --- INTERFACE WORKSPACE 1: EXECUTIVE HOME DIRECTORY PANEL ---
    def render_home_portal():
        st.title("🛡️ FUZE TECH HOLDINGS — Gateway Portal")
        st.markdown("### *Central Infrastructure Control Center — Multi-Tenant Operating Hub*")
        st.divider()
        
        if user_profile["is_logtech_active"] or user_profile["is_gridtech_active"]:
            st.success(f"🔓 **Active Database Isolation Token Verified.** Currently streaming isolated data blocks mapped to **{user_profile['account_name']}**.")
        else:
            # 🚨 COMMERCIAL TRIAL RETENTION HOOK FOR UNSUBSCRIBED PROSPECTS
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
        
        # Portfolio Infrastructure Overview Data Metrics Block
        st.markdown("#### 📊 Real-Time Node Telematics Overview")
        kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
        with kpi_col1:
            truck_count = len(MOCK_FLEET_TELEMETRY.get(active_id, []))
            st.metric(label="🚚 Connected Fleet Assets", value=f"{truck_count} Trucks Active" if user_profile["is_logtech_active"] else "0 Trucks Connected")
        with kpi_col2:
            meter_count = len(MOCK_GRID_TELEMETRY.get(active_id, []))
            st.metric(label="⚡ Monitored Grid Nodes", value=f"{meter_count} Smart Meters" if user_profile["is_gridtech_active"] else "0 Smart Meters Connected")
        with kpi_col3:
            st.metric(label="🛡️ Cloud Pipeline Integrity", value="100% Secure", delta="Row-Level Security Active")
            
        st.divider()
        st.markdown("#### 🏢 Brand Portfolio Mapping & Marketplace Matrix")
        card_col1, card_col2 = st.columns(2)
        with card_col1:
            with st.container(border=True):
                st.markdown("##### 🚚 Legacy Freight Lines (LogTech Division)")
                st.markdown("**Status:** `ACTIVE SUBSCRIPTION` ✅" if user_profile["is_logtech_active"] else "**Status:** `LOCKED — TRIAL AVAILABLE` 🔒")
            with st.container(border=True):
                st.markdown("##### ⚡ Legacy Utility Labs (GridTech Division)")
                st.markdown("**Status:** `ACTIVE SUBSCRIPTION` ✅" if user_profile["is_gridtech_active"] else "**Status:** `LOCKED — TRIAL AVAILABLE` 🔒")
        with card_col2:
            with st.container(border=True):
                st.markdown("##### 🛡️ Legacy Sybil Gate (CyberTech Division)")
                st.markdown("**Status:** `LOCKED — TRIAL AVAILABLE` 🔒")
            with st.container(border=True):
                st.markdown("##### 🚌 Legacy Transit Token (TransitTech Division)")
                st.markdown("**Status:** `LOCKED — TRIAL AVAILABLE` 🔒")

    # --- INTERFACE WORKSPACE 2: LOGTECH DISPATCH PIPELINE VIEW ---
    def render_freight_lines():
        st.title("🚚 LEGACY FREIGHT LINES — B2B LogTech Platform")
        st.markdown(f"### *Multi-Tenant Telematics Isolation Stream — Client Node: {active_id}*")
        st.divider()

        # 🚨 ISOLATION BLOCK: Query ONLY the current client's data matrix
        client_fleet = MOCK_FLEET_TELEMETRY.get(active_id, [])
        df_fleet = pd.DataFrame(client_fleet)

        simulate_theft = st.sidebar.button("🚨 Simulate Fuel Theft Anomaly")

        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.metric(label="📊 Monitored Fleet Size", value=f"{len(df_fleet)} Heavy Vehicles")
        with m_col2:
            if simulate_theft:
                st.metric(label="🛡️ System Security Profile", value="CRITICAL ALERT", delta="-45L Sudden Siphon", delta_color="inverse")
            else:
                st.metric(label="🛡️ System Security Profile", value="SECURE", delta="All Probes Normal")

        st.divider()
        col_l, col_r = st.columns(2)
        with col_l:
            st.subheader("📋 Isolated Client Fleet Log Registry")
            if simulate_theft and len(df_fleet) > 0:
                df_fleet.loc[0, "Fuel_Liters"] = df_fleet.loc[0, "Fuel_Liters"] - 45.0
                df_fleet.loc[0, "Speed_KMH"] = 0.0
                st.error(f"🚨 CRITICAL TELEMETRY EXPOSURE: Sudden slope drop detected on Vehicle {df_fleet.loc[0, 'Truck_ID']} while stationary! Alarm fired.")
            st.dataframe(df_fleet, use_container_width=True, hide_index=True)
        with col_r:
            st.subheader("🚧 Automated Border Compliance Status")
            for index, row in df_fleet.iterrows():
                st.markdown(f"**🆔 Vehicle ID:** {row['Truck_ID']} | **👤 Operator:** {row['Driver']}")
                if row['BURS_Clearance'] == "PROCEED TO BORDER":
                    st.success(f"✅ BURS Clearance Approved. Status: **{row['BURS_Clearance']}**")
                else:
                    st.warning(f"⚠️ BURS Clearance Blocked. Status: **{row['BURS_Clearance']}**")
                st.divider()

    # --- INTERFACE WORKSPACE 3: GRIDTECH DISPATCH UTILITY VIEW ---
    def render_utility_labs():
        st.title("⚡ LEGACY UTILITY LABS — B2B GridTech Platform")
        st.markdown(f"### *Multi-Tenant Grid Isolation Stream — Client Node: {active_id}*")
        st.divider()

        # 🚨 ISOLATION BLOCK: Query ONLY the current client's data matrix
        client_meters = MOCK_GRID_TELEMETRY.get(active_id, [])
        df_meter = pd.DataFrame(client_meters)

        simulate_bypass = st.sidebar.button("🚨 Simulate Smart Meter Bypassing")

        met_col1, met_col2 = st.columns(2)
        with met_col1:
            st.metric(label="📊 Active Utility Nodes", value=f"{len(df_meter)} Smart Meters")
        with met_col2:
            if simulate_bypass:
                st.metric(label="🚨 Revenue Protection Status", value="FRAUD INTERCEPTED", delta="-45A Diverted Load", delta_color="inverse")
            else:
                st.metric(label="🚨 Revenue Protection Status", value="100% INTACT", delta="Zero Leakage")

        st.divider()
        col_l, col_r = st.columns(2)
        with col_l:
            st.subheader("📋 Isolated Client Meter Data Array")
            if simulate_bypass and len(df_meter) > 0:
                df_meter.loc[len(df_meter)-1, "Metered_Usage_kW"] = 0.0
                df_meter.loc[len(df_meter)-1, "Substation_Line_Current_Amps"] = 65.2
                df_meter.loc[len(df_meter)-1, "System_Status"] = "CRITICAL FRAUD BYPASS"
