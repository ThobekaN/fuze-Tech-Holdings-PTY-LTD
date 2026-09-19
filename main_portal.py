import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 🔄 GLOBAL DATA LAYER IMPORT
import database

# 1. Global Framework Page Configurations (MUST be the absolute first command)
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
    
    st.title("🛡️ FUZE TECH HOLDINGS — Gateway Portal")
    st.markdown("### *Central Infrastructure Control Center — Multi-Tenant Operating Hub*")
    st.divider()
    
    # Session Status Validation Alert Bar
    if any([user_profile["is_logtech_active"], user_profile["is_gridtech_active"], user_profile.get("is_cybertech_active", False)]):
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
    
    # 🚀 THE 30-DAY FREE TRIAL DYNAMIC SUBSCRIPTION WORKSPACE BOARDS
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
                        
                        st.session_state["DB_LOGTECH"][active_id] = generated_fleet
                        st.session_state["user_data"]["is_logtech_active"] = True
                        
                        for user_record in st.session_state["DB_CLIENTS"]:
                            if user_record["client_id"] == active_id:
                                user_record["is_logtech_active"] = True
                                break
                                
                        st.balloons()
                        st.success("Database records linked successfully!")
                        st.rerun()
        
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
                with st.popover("🚀 Start 30-Day Free Trial"):
                    st.markdown("### 📋 GridTech System Initialization")
                    meter_count = st.number_input("Number of prepaid smart meters to mount:", min_value=1, max_value=5, value=1)
                    property_name = st.text_input("Facility Name / Property Fund:", "Braamfontein Residential")
                    
                    if st.button("Confirm Deployment & Connect Grid", key="btn_confirm_gridtech"):
                        generated_meters = []
                        for i in range(int(meter_count)):
                            generated_meters.append({
                                "Meter_ID": f"MTR-{random.randint(500, 999)}",
                                "Property_Fund": property_name,
                                "Metered_Usage_kW": float(random.choice([0.0, 1.2, 4.5, 8.9])),
                                "Substation_Line_Current_Amps": round(random.uniform(5.0, 50.0), 1),
                                "System_Status": random.choice(["NORMAL", "NORMAL", "SUSPECTED BYPASS"])
                                })
                        
                        st.session_state["DB_GRIDTECH"][active_id] = generated_meters
                        st.session_state["user_data"]["is_gridtech_active"] = True
                        
                        for user_record in st.session_state["DB_CLIENTS"]:
                            if user_record["client_id"] == active_id:
                                user_record["is_gridtech_active"] = True
                                break
                                
                        st.balloons()
                        st.success("Database records linked successfully!")
                        st.rerun()
        
        st.write("") 
        
        # 🏥 5. HEALTHTECH TILES
        with st.container(border=True):
            st.markdown("##### 🏥 Legacy Cold Chain (HealthTech)")
            st.markdown("*Wireless temperature sensor analytics and predictive trajectory tracking inside clinical fridges.*")
            if user_profile.get("is_healthtech_active", False):
                st.success("🟢 Active Subscription Billed")
            else:
                st.error("🔴 License Status: Unsubscribed")
                with st.popover("🚀 Start 30-Day Free Trial"):
                    if st.button("Initialize Thermal Probe Matrix", key="btn_confirm_health"):
                        st.session_state["user_data"]["is_healthtech_active"] = True
                        st.balloons()
                        st.rerun()

        with col3:
        # 🛡️ 3. CYBERTECH DYNAMIC ACTIVATION CARD
