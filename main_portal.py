import streamlit as st

# 1. Establish the Page Config for the Central Control Center
st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

# 2. 🚨 LIVE SIMULATION DEMO: Profile Account Switcher (Interactive Portal Demo)
st.sidebar.title("🏢 Fuze Tech Gateway")
st.sidebar.markdown("### 🔑 Live Profile Switcher")
demo_profile = st.sidebar.radio(
    "Select Demo Login State:",
    ["1. Unsubscribed Lead (Free Trial Offer)", "2. LogTech Client (Super Group Operations)", "3. Enterprise Client (Full Suite Active)"]
)
st.sidebar.divider()

# 3. Dynamically set User Subscription Flags based on the sidebar selection
if "1." in demo_profile:
    user_profile = {
        "account_name": "Prospective Client Account (Lead-Tier)",
        "is_logtech_active": False,
        "is_gridtech_active": False,
    }
elif "2." in demo_profile:
    user_profile = {
        "account_name": "Super Group Operations (LogTech Tier)",
        "is_logtech_active": True,
        "is_gridtech_active": False,
    }
else:
    user_profile = {
        "account_name": "Imperial Logistics Group (Enterprise Suite)",
        "is_logtech_active": True,
        "is_gridtech_active": True,
    }

st.sidebar.markdown(f"👤 **Operator Security Profile:**\n`{user_profile['account_name']}`")
st.sidebar.divider()

# 4. Define the Home Page Content Layout (The Executive Landing Page Dashboard)
def render_home_portal():
    st.title("🛡️ FUZE TECH HOLDINGS — Gateway Portal")
    st.markdown("### *Central Infrastructure Control Center — Multi-Tenant Operating Hub*")
    st.divider()
    
    # Dynamic Security Banner based on authentication states
    if user_profile["is_logtech_active"] or user_profile["is_gridtech_active"]:
        st.success(f"🔓 **Secure Authentication Verified.** Welcome back, operator for **{user_profile['account_name']}**. Your subscription keys are active.")
    else:
        st.warning(f"🔒 **Limited Access Profile.** Welcome, **{user_profile['account_name']}**. You are currently viewing our platform marketplace. Select any vertical below to initiate your 30-Day Free Trial Subscription.")
    
    # Portfolio Infrastructure Health Matrix
    st.markdown("#### 📊 Consolidated Portfolio Infrastructure Health")
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    with kpi_col1:
        st.metric(label="🚚 LogTech Assets Tracked", value="68 Trucks Configured" if user_profile["is_logtech_active"] else "0 Trucks Connected", delta="Initial Corridor Runway")
    with kpi_col2:
        st.metric(label="⚡ GridTech Nodes Managed", value="450 Smart Meters" if user_profile["is_gridtech_active"] else "0 Smart Meters Connected", delta="Perimeter Status")
    with kpi_col3:
        st.metric(label="🛡️ Global System Latency", value="14ms SAST", delta="Supabase Cloud Engine Connection Optimal", delta_color="normal")
        
    st.divider()
    
    # Product Showcase & Commercial Trial Activation Board
    st.markdown("#### 🏢 Market-Facing Brand Overview & Trial Matrix")
    st.info("💡 Pro-Tip: Use the sidebar navigation menu on the left to swap into your live streaming telemetry stream dashboards.")
    
    card_col1, card_col2 = st.columns(2)
    
    with card_col1:
        with st.container(border=True):
            st.markdown("##### 🚚 Legacy Freight Lines (LogTech Division)")
            st.markdown("*Real-time cross-border asset tracking, anomaly metric calculation, and 2026 BURS custom gateway automation.*")
            if user_profile["is_logtech_active"]:
                st.markdown("**Status:** `ACTIVE SUBSCRIPTION` ✅")
            else:
                st.markdown("**Status:** `TRIAL AVAILABLE` 🔒")
                st.button("Activate 30-Day Free Trial", key="freight_trial")
            
        st.write("") 
        
        with st.container(border=True):
            st.markdown("##### ⚡ Legacy Utility Labs (GridTech Division)")
            st.markdown("*Cross-referencing smart meter telemetry against localized transformer endpoints to pinpoint active prepaid bridging fraud loops instantly.*")
            if user_profile["is_gridtech_active"]:
                st.markdown("**Status:** `ACTIVE SUBSCRIPTION` ✅")
            else:
                st.markdown("**Status:** `TRIAL AVAILABLE` 🔒")
                st.button("Activate 30-Day Free Trial", key="grid_trial")
                
    with card_col2:
        with st.container(border=True):
            st.markdown("##### 🛡️ Legacy Sybil Gate (CyberTech Division)")
            st.markdown("*Protecting on-demand delivery food networks from automated promotion abuse fraud via advanced hardware device fingerprinting and address coordinate clustering.*")
            st.markdown("**Status:** `TRIAL AVAILABLE` 🔒")
            st.button("Activate 30-Day Free Trial", key="cyber_trial")
            
        st.write("") 
        
        with st.container(border=True):
            st.markdown("##### 🚌 Legacy Transit Token (TransitTech Division)")
            st.markdown("*Eliminating student bus card-sharing and screenshot forgery via strict relational database anti-passback state machines and 30-second cryptographic token rotations.*")
            st.markdown("**Status:** `TRIAL AVAILABLE` 🔒")
            st.button("Activate 30-Day Free Trial", key="transit_trial")

# 5. Define the Global Navigation Architecture Mappings
home_page = st.Page(render_home_portal, title="Home Control Center", icon="🏢")

# 🛠️ GATED ACCESS LOGIC: The pages change dynamically based on who is logged in
navigation_pool = [home_page]

if user_profile["is_logtech_active"]:
    logtech_page = st.Page("views/freight_lines.py", title="Legacy Freight Lines", icon="🚚")
    navigation_pool.append(logtech_page)

if user_profile["is_gridtech_active"]:
    gridtech_page = st.Page("views/utility_labs.py", title="Legacy Utility Labs", icon="⚡")
    navigation_pool.append(gridtech_page)

# 6. Initialize and Run the Multi-Page Navigation Engine
nav = st.navigation(navigation_pool)
nav.run()
