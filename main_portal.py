import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Establish Page Configurations
st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

# 🗄️ MOCK PRODUCTION DATABASE TABLE (Simulating your Supabase 'clients' table)
MOCK_CLIENTS_DB = [
    {
        "email": "lead@fuzetech.co.za",
        "password": "password123",
        "account_name": "Prospective Client (Lead-Tier)",
        "is_logtech_active": False,
        "is_gridtech_active": False
    },
    {
        "email": "operations@supergroup.co.za",
        "password": "superfleet2026",
        "account_name": "Super Group Operations (LogTech Tier)",
        "is_logtech_active": True,
        "is_gridtech_active": False
    },
    {
        "email": "director@imperial.co.za",
        "password": "enterpriseultra",
        "account_name": "Imperial Logistics Group (Enterprise Suite)",
        "is_logtech_active": True,
        "is_gridtech_active": True
    }
]

# 2. INITIALIZE SESSION STATE TOKENS (The Automated Background Memory Loop)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "user_data" not in st.session_state:
    st.session_state["user_data"] = None

# 3. LOGOUT MECHANISM ROUTINE
def handle_logout():
    st.session_state["authenticated"] = False
    st.session_state["user_data"] = None
    st.rerun()

# 4. CONDITIONAL LAYOUT LOGIC LAYER: RENDER LOGIN OR RENDER PORTAL
if not st.session_state["authenticated"]:
    # --- RENDER SECURE LOGIN SCREEN GATEWAY ---
    st.title("🔒 FUZE TECH HOLDINGS — Secure Login Gateway")
    st.markdown("### *Enterprise Multi-Tenant Infrastructure Portal*")
    st.divider()
    
    st.info("💡 Presentation Hint: Login using `operations@supergroup.co.za` with password `superfleet2026` to unlock LogTech, or `director@imperial.co.za` with password `enterpriseultra` to unlock the Full Enterprise Suite.")
    
    login_email = st.text_input("Corporate Email Address")
    login_password = st.text_input("Security Access Password", type="password")
    
    if st.button("Authenticate Session"):
        # The Automated Token Loop: Querying the mock database array
        matched_user = None
        for record in MOCK_CLIENTS_DB:
            if record["email"] == login_email and record["password"] == login_password:
                matched_user = record
                break
        
        if matched_user:
            # Token Loop Validated: Assign values to session memory state
            st.session_state["authenticated"] = True
            st.session_state["user_data"] = matched_user
            st.success("Session Token Generated Successfully! Redirecting...")
            st.rerun()
        else:
            st.error("Access Denied: Invalid email identifier or security password credentials.")

else:
    # --- RENDER DYNAMIC ACTIVE PORTAL ---
    user_profile = st.session_state["user_data"]
    
    # Configure Corporate Sidebar Controls
    st.sidebar.title("🏢 Fuze Tech Gateway")
    st.sidebar.markdown(f"👤 **Active Operator:**\n`{user_profile['account_name']}`")
    st.sidebar.markdown(f"📧 **Session ID:** `{user_profile['email']}`")
    if st.sidebar.button("Secure Sign Out"):
        handle_logout()
    st.sidebar.divider()
    
    # --- VIEW 1: HOME PORTAL PAGE ---
    def render_home_portal():
        st.title("🛡️ FUZE TECH HOLDINGS — Gateway Portal")
        st.markdown("### *Central Infrastructure Control Center — Multi-Tenant Operating Hub*")
        st.divider()
        
        if user_profile["is_logtech_active"] or user_profile["is_gridtech_active"]:
            st.success(f"🔓 **Active Database Session Token Verified.** Welcome back, operator for **{user_profile['account_name']}**.")
        else:
            st.warning(f"🔒 **Trial Profile Mode.** Welcome, **{user_profile['account_name']}**. Select a vertical below to initiate your 30-Day Free Trial.")
        
        st.markdown("#### 📊 Consolidated Portfolio Infrastructure Health")
        kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
        with kpi_col1:
            st.metric(label="🚚 LogTech Assets Tracked", value="68 Trucks Configured" if user_profile["is_logtech_active"] else "0 Trucks Connected")
        with kpi_col2:
            st.metric(label="⚡ GridTech Nodes Managed", value="450 Smart Meters" if user_profile["is_gridtech_active"] else "0 Smart Meters Connected")
        with kpi_col3:
            st.metric(label="🛡️ Global System Latency", value="14ms SAST", delta="Mock Array Query Successful")
            
        st.divider()
        
        st.markdown("#### 🏢 Market-Facing Brand Overview & Trial Matrix")
        card_col1, card_col2 = st.columns(2)
        with card_col1:
            with st.container(border=True):
                st.markdown("##### 🚚 Legacy Freight Lines (LogTech Division)")
                st.markdown("**Status:** `ACTIVE SUBSCRIPTION` ✅" if user_profile["is_logtech_active"] else "**Status:** `TRIAL AVAILABLE` 🔒")
            with st.container(border=True):
                st.markdown("##### ⚡ Legacy Utility Labs (GridTech Division)")
                st.markdown("**Status:** `ACTIVE SUBSCRIPTION` ✅" if user_profile["is_gridtech_active"] else "**Status:** `TRIAL AVAILABLE` 🔒")
        with card_col2:
            with st.container(border=True):
                st.markdown("##### 🛡️ Legacy Sybil Gate (CyberTech Division)")
                st.markdown("**Status:** `TRIAL AVAILABLE` 🔒")
            with st.container(border=True):
                st.markdown("##### 🚌 Legacy Transit Token (TransitTech Division)")
                st.markdown("**Status:** `TRIAL AVAILABLE` 🔒")
            with st.container(border=True):
                st.markdown("##### 🏥 Legacy Cold Chain (HealthTech Division)")
                st.markdown("**Status:** `TRIAL AVAILABLE` 🔒")

    # --- VIEW 2: LOGTECH INTERFACE ---
    def render_freight_lines():
        st.title("🚚 LEGACY FREIGHT LINES — B2B LogTech Platform")
        st.markdown("### *Fuze Tech Holdings Innovation: Real-Time SADC Logistics Management*")
        st.divider()

        fleet_data = {
            "Truck_ID": ["LFL-001", "LFL-002", "LFL-003", "LFL-004"],
            "Client_Company": ["Super Group Logistics", "Imperial Transport", "Value Logistics", "Cargo Carriers"],
            "Route": ["JHB -> Gaborone", "JHB -> Windhoek", "JHB -> Lobatse", "JHB -> Gaborone"],
            "Speed_KMH": [0.0, 80.0, 0.0, 70.0],
            "Fuel_Liters": [280.5, 300.0, 195.0, 420.8],
            "BURS_Clearance": ["PROCEED TO BORDER", "HOLD AT STAGING", "HOLD AT STAGING", "PROCEED TO BORDER"]
        }
        df_fleet = pd.DataFrame(fleet_data)

        simulate_theft = st.sidebar.button("🚨 Simulate Fuel Theft Event (LFL-001)")

        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.metric(label="📊 Active Managed Fleet", value=f"{len(df_fleet)} Heavy Vehicles", delta="B2B SaaS Model")
        with m_col2:
            cleared_trucks = len(df_fleet[df_fleet["BURS_Clearance"] == "PROCEED TO BORDER"])
            st.metric(label="规 BURS Border Cleared", value=f"{cleared_trucks} / {len(df_fleet)} Trucks", delta="Automated Validation")
        with m_col3:
            if simulate_theft:
                st.metric(label="🛡️ System Security Status", value="ALERT", delta="-45L Sudden Drop!", delta_color="inverse")
            else:
                st.metric(label="🛡️ System Security Status", value="SECURE", delta="All Probes Normal")

        st.divider()
        col_l, col_r = st.columns(2)
        with col_l:
            st.subheader("📋 Active Fleet Registry & Telematics Status")
            if simulate_theft:
                df_fleet.loc[df_fleet["Truck_ID"] == "LFL-001", "Fuel_Liters"] = 235.5
                df_fleet.loc[df_fleet["Truck_ID"] == "LFL-001", "Speed_KMH"] = 0
                st.error("🚨 CRITICAL TELEMETRY ALERT: Sudden fuel volume drop detected on LFL-001 while stationary! System flags unauthorized siphoning hazard.")
            st.dataframe(df_fleet, use_container_width=True, hide_index=True)
        with col_r:
            st.subheader("🚧 Automated Border Compliance Engine")
            st.info("ℹ️ Ensuring strict alignment with the 2026 BURS Pre-Border Electronic Mandate.")
            for index, row in df_fleet.iterrows():
                st.markdown(f"**🆔 Vehicle ID:** {row['Truck_ID']} | **💼 Client:** {row['Client_Company']}")
                if row['BURS_Clearance'] == "PROCEED TO BORDER":
                    st.success(f"✅ BURS Clearance Approved. Status: **{row['BURS_Clearance']}**")
                else:
                    st.warning(f"⚠️ BURS Clearance Blocked. Status: **{row['BURS_Clearance']}**")
                st.divider()

    # --- VIEW 3: GRIDTECH INTERFACE ---
    def render_utility_labs():
        st.title("⚡ LEGACY UTILITY LABS — B2B GridTech Platform")
        st.markdown("### *Fuze Tech Holdings Innovation: Real-Time Prepaid Meter Bypassing Detection*")
        st.divider()

        meter_data = {
            "Meter_ID": ["MTR-801", "MTR-802", "MTR-803", "MTR-804"],
            "Property_Fund": ["Growthpoint Braamfontein", "Redefine Parktown", "City Property CBD", "Wits Student Housing"],
            "Metered_Usage_kW": [4.2, 0.8, 0.0, 1.5],
            "Substation_Line_Current_Amps": [18.5, 4.1, 45.2, 6.8],
            "System_Status": ["NORMAL", "NORMAL", "SUSPECTED BYPASS", "NORMAL"]
        }
        df_meter = pd.DataFrame(meter_data)

        simulate_bypass = st.sidebar.button("🚨 Simulate Meter Bypassing Event (MTR-804)")

        met_col1, met_col2, met_col3 = st.columns(3)
        with met_col1:
            st.metric(label="📊 Total Monitored Nodes", value=f"{len(df_meter)} Smart Meters", delta="Fuze Tech Group Core")
        with met_col2:
            bypassed_meters = len(df_meter[df_meter["System_Status"] == "SUSPECTED BYPASS"])
