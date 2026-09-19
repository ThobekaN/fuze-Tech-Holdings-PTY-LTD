import streamlit as st

# 1. Establish the Page Config for the Central Control Center
st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

# 2. Simulate User Subscription Flags from the Database
# In production, these fields are pulled dynamically from your PostgreSQL 'clients' table
user_profile = {
    "account_name": "Super Group Operations",
    "is_logtech_active": True,
    "is_gridtech_active": False, # Offers a 30-Day Free Trial hook
    "is_transit_active": True
}

st.sidebar.title("Fuze Tech Gateway")
st.sidebar.markdown(f"**Logged in:** {user_profile['account_name']}")

# 3. Define the Global Multi-Tenant Navigation Architecture
# Streamlit reads these files as separate views based on database permissions
pages = {}

# All clients see the Central Entry Home Portal
home_page = st.Page("main_portal.py", title="Home Control Center", icon="🏢")

# Dynamically gate visibility or access paths based on user subscription matrices
if user_profile["is_logtech_active"]:
    logtech_page = st.Page("views/freight_lines.py", title="Legacy Freight Lines", icon="🚚")
else:
    logtech_page = st.Page("views/freight_lines.py", title="Legacy Freight Lines (Locked 🔒)", icon="🚚")

if user_profile["is_gridtech_active"]:
    gridtech_page = st.Page("views/utility_labs.py", title="Legacy Utility Labs", icon="⚡")
else:
    gridtech_page = st.Page("views/utility_labs.py", title="Legacy Utility Labs (Locked 🔒)", icon="⚡")

# Initialize and run the multi-page engine cleanly
nav = st.navigation([home_page, logtech_page, gridtech_page])
nav.run()
