import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 🔄 GLOBAL DATA LAYER IMPORT
import database

# Global Framework Page Configurations
st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

# 🔐 STATE ENGINE ARCHITECTURE (Initializes your separate data tables into session memory)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "user_data" not in st.session_state:
    st.session_state["user_data"] = None

# Centralize your separate database matrices into active browser memory states
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

# --- CONTEXT CONDITIONAL CONTROL: LOGIN ENVELOPE OR ACCOUNT WORKSPACE ---
if not st.session_state["authenticated"]:
    st.title("🔒 FUZE TECH HOLDINGS — Secure Login Gateway")
    st.markdown("### *Enterprise Multi-Tenant Infrastructure Portal*")
    st.divider()
    
    st.info("""💡 **Demo Instruction Panel for the Tshimologong Selectors:**
- **To test an Unsubscribed Lead (Best for testing the live popover activation):** `lead@fuzetech.co.za` (Password: `password123`)
- **To test a Subscribed LogTech Client:** `operations@supergroup.co.za` (Password: `superfleet2026`)""")
    
    login_email = st.text_input("Corporate Account Email")
    login_password = st.text_input("Security Access Token Key", type="password")
    
    if st.button("Authenticate Session"):
        matched_user = None
        cleaned_email = login_email.lower().strip()
        
        # Query our active session database state layer instead of the static file
        for record in st.session_state["DB_CLIENTS"]:
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
    
    # Configure Corporate Shared Sidebar Access Controls
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
        
        if any([user_profile["is_logtech_active"], user_profile["is_gridtech_active"], user_profile["is_cybertech_active"], user_profile["is_transittech_active"], user_profile["is_healthtech_active"]]):
            st.success(f"🔓 **Active Database Session Token Verified.** Custom permission matrix mapped to: **{user_profile['account_name']}**.")
        else:
            st.error(f"🔒 **Limited Execution Mode:** Account `{active_id}` carries no active product tier licenses. All analytics sidebar routes are dynamically hidden.")
        
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
        
        # 🚀 30-DAY FREE TRIAL DYNAMIC SUBSCRIPTION WORKSPACE BOARDS
        st.markdown("#### 🏢 Unified Platform Ecosystem & Subscription Status")
        st.info("💡 *How it works:* Click any unsubscribed trial module below. Input assets and inject parameters to dynamically update your custom database slice.")
        st.write("")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # 🚚 1. LOGTECH DYNAMIC ACTIVATION CARD
            with st.container(border=True):
                st.markdown("##### 🚚 Legacy Freight Lines (LogTech)")
                st.markdown("*Cross-border telematics, siphoning engines, and 2026 BURS customs automation.*")
                if user_profile["is_logtech_active"]:
                    st.success("🟢 Active Subscription Billed")
                else:
                    st.error("🔴 License Status: Unsubscribed")
                    with st.popover("🚀 Start 30-Day Free Trial"):
                        st.markdown("### 📋 LogTech System Initialization")
                        fleet_size = st.number_input("Number of heavy vehicles to provision:", min_value=1, max_value=5, value=1)
                        drivers_input = st.text_input("Driver Names (Comma separated):", "Sipho M., Thabo N.")
                        routes_input = st.text_input("Routes (Comma separated):", "JHB -> Gaborone, JHB -> Windhoek")
                        
                        if st.button("Confirm Allocation & Launch Pipeline", key="btn_confirm_logtech"):
                            drivers = [d.strip() for d in drivers_input.split(",")]
                            routes = [r.strip() for r in routes_input.split(",")]
                            
                            # Build randomized data streams for the trial client
                            generated_fleet = []
                            for i in range(int(fleet_size)):
                                idx_d = drivers[i % len(drivers)] if drivers else "Unknown Driver"
                                idx_r = routes[i % len(routes)] if routes else "Internal Corridor"
                                generated_fleet.append({
                                    "Truck_ID": f"TRK-{random.randint(100, 999)}",
                                    "Driver": idx_d,
                                    "Route": idx_r,
                                    "Speed_KMH": float(random.choice([0.0, 65.0, 80.0, 110.0])),
                                    "Fuel_Liters": round(random.uniform(150.0, 450.0), 1),
                                    "BURS_Clearance": random.choice(["PROCEED TO BORDER", "HOLD AT STAGING"])
                                })
                            
                            # DYNAMIC PUSH MUTATION LAYER: Appends data rows straight to active session tables
                            st.session_state["DB_LOGTECH"][active_id] = generated_fleet
                            
                            # Update account subscription status inside state memory
                            for user_record in st.session_state["DB_CLIENTS"]:
                                if user_record["client_id"] == active_id:
                                    user_record["is_logtech_active"] = True
                                    break
                            
                            st.session_state["user_data"]["is_logtech_active"] = True
                            st.balloons()
                            st.success("Database records linked successfully! Rerouting workspace rails...")
                            st.button("Reload Workspace Console")
            
            st.write("") 
            
            # 🚌 4. TRANSITTECH TILES
            with st.container(border=True):
                st.markdown("##### 🚌 Legacy Transit Token (TransitTech)")
                st.markdown("*Shuttle access management using strict anti-passback rules and 30s rotating tokens.*")
                if user_profile.get("is_transittech_active", False):
                    st.success("🟢 Active Subscription Billed")
                else:
                    st.error("🔴 License Status: Unsubscribed")
                    with st.popover("🚀 Start 30-Day Free Trial"):
                        if st.button("Generate Cryptographic Token Keys", key="btn_confirm_transit"):
                            st.session_state["user_data"]["is_transittech_active"] = True
                            st.balloons()
                            st.rerun()

        with col2:
            # ⚡ 2. GRIDTECH DYNAMIC ACTIVATION CARD
            with st.container(border=True):
                st.markdown("##### ⚡ Legacy Utility Labs (GridTech)")
                st.markdown("*Cross-referencing smart meters against sectional line current transformers to identify grid bypass fraud.*")
                if user_profile["is_gridtech_active"]:
                    st.success("🟢 Active Subscription Billed")
                else:
                    st.error("🔴 License Status: Unsubscribed")
