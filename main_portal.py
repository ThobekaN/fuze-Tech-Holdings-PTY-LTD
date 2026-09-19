import streamlit as st

# 1. Establish the Page Config for the Central Control Center
st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

# 2. Simulate User Profile and Subscription Flags from the Database
user_profile = {
    "account_name": "Super Group Operations",
    "is_logtech_active": True,
    "is_gridtech_active": True,  # Set to True/False for access testing
}

# 3. Sidebar Corporate Identity Configuration
st.sidebar.title("🏢 Fuze Tech Gateway")
st.sidebar.markdown(f"👤 **Operator Security Profile:**\n`{user_profile['account_name']}`")
st.sidebar.divider()

# 4. Define the Home Page Content Layout (The Executive Landing Page Dashboard)
def render_home_portal():
    # Top Identity Brand Banner
    st.title("🛡️ FUZE TECH HOLDINGS — Gateway Portal")
    st.markdown("### *Central Infrastructure Control Center — Multi-Tenant Operating Hub*")
    st.divider()
    
    # Welcome & Active Notice Alert Strip
    st.success(f"🔓 **Secure Authentication Verified.** Welcome back, team analyst for **{user_profile['account_name']}**. Your holding group security tokens are fully synchronized with our cloud relational data nodes.")
    
    # 🌟 NEW FEATURE: Executive Portfolio KPI Layout Grid
    st.markdown("#### 📊 Consolidated Portfolio Infrastructure Health")
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    with kpi_col1:
        st.metric(label="🚚 LogTech Assets Tracked", value="68 Trucks Active", delta="Initial Corridor Runway")
    with kpi_col2:
        st.metric(label="⚡ GridTech Nodes Managed", value="450 Smart Meters", delta="Perimeter Intact")
    with kpi_col3:
        st.metric(label="🛡️ Global System Latency", value="14ms SAST", delta="Supabase Cloud Engine Connection Optimal", delta_color="normal")
        
    st.divider()
    
    # 🗂️ NEW FEATURE: Product Showcase & Commercial Trial Activation Board
    st.markdown("#### 🏢 Market-Facing Brand Overview & Trial Matrix")
    st.info("💡 Pro-Tip: Select an active industrial vertical from the sidebar navigation menu on the left to swap into your live streaming telemetry stream dashboards.")
    
    # 2x2 Column Block Layout grid to display all ecosystem solutions clearly
    card_col1, card_col2 = st.columns(2)
    
    with card_col1:
        with st.container(border=True):
            st.markdown("##### 🚚 Legacy Freight Lines (LogTech Division)")
            st.markdown("*Real-time cross-border asset tracking, anomaly metric calculation, and 2026 BURS custom gateway automation.*")
            st.markdown("**Status:** `ACTIVE SUBSCRIPTION` ✅")
            
        st.write("") # Spacing element
        
        with st.container(border=True):
            st.markdown("##### ⚡ Legacy Utility Labs (GridTech Division)")
            st.markdown("*Cross-referencing smart meter telemetry against localized transformer endpoints to pinpoint active prepaid bridging fraud loops instantly.*")
            st.markdown("**Status:** `ACTIVE SUBSCRIPTION` ✅" if user_profile["is_gridtech_active"] else "**Status:** `TRIAL AVAILABLE` 🔒")
            if not user_profile["is_gridtech_active"]:
                st.button("Activate 30-Day Free Trial Subscription", key="grid_trial")
                
    with card_col2:
        with st.container(border=True):
            st.markdown("##### 🛡️ Legacy Sybil Gate (CyberTech Division)")
            st.markdown("*Protecting on-demand delivery food networks from automated promotion abuse fraud via advanced hardware device fingerprinting and address coordinate clustering.*")
            st.markdown("**Status:** `TRIAL AVAILABLE` 🔒")
            st.button("Activate 30-Day Free Trial Subscription", key="cyber_trial")
            
        st.write("") # Spacing element
        
        with st.container(border=True):
            st.markdown("##### 🚌 Legacy Transit Token (TransitTech Division)")
            st.markdown("*Eliminating student bus card-sharing and screenshot forgery via strict relational database anti-passback state machines and 30-second cryptographic token rotations.*")
            st.markdown("**Status:** `TRIAL AVAILABLE` 🔒")
            st.button("Activate 30-Day Free Trial Subscription", key="transit_trial")

# 5. Define the Global Navigation Architecture Mappings
home_page = st.Page(render_home_portal, title="Home Control Center", icon="🏢")

# Setup clean, icon-enabled paths to point straight into your subfolder layout scripts
logtech_page = st.Page("freight_lines.py", title="Legacy Freight Lines", icon="🚚")
gridtech_page = st.Page("utility_labs.py", title="Legacy Utility Labs", icon="⚡")

# 6. Initialize and Run the Multi-Page Navigation Engine
nav = st.navigation([home_page, logtech_page, gridtech_page])
nav.run()
