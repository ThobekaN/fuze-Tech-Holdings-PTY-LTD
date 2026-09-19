import streamlit as st

user_session = {
    "account_name": "super_group_admin",
    "is_logtech_subscribed": True,       # Active subscription
    "is_gridtech_subscribed": False,     # No subscription
    "is_cybertech_subscribed": True,    # Active subscription
}

st.sidebar.title("Fuze Tech Gateway")
st.sidebar.markdown(f"**Logged in:** {user_profile['account_name']}")

pages = {}

home_page = st.Page("main_portal.py", title="Home Control Center")

if user_profile["is_logtech_active"]:
    logtech_page = st.Page("freight_lines.py", title="Legacy Freight Lines")
else:
    logtech_page = st.Page("freight_lines.py", title="Legacy Freight Lines (Locked 🔒)")

if user_profile["is_gridtech_active"]:
    gridtech_page = st.Page("utility_labs.py", title="Legacy Utility Labs")
else:
    gridtech_page = st.Page("utility_labs.py", title="Legacy Utility Labs (Locked 🔒)")

nav = st.navigation([home_page, logtech_page, gridtech_page])
nav.run()
