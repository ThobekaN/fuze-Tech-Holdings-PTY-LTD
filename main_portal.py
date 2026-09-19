import streamlit as st

st.set_page_config(page_title="Fuze Tech Holdings - Portal Gateway", layout="wide")

def render_home_portal():
    st.title("FUZE TECH HOLDINGS — Gateway Portal")
    st.markdown("### *Central Infrastructure Control Center*")
    st.divider()
    
    st.write(f"Welcome back, **{user_profile['account_name']}**.")
    st.info("Select an active industrial vertical from the sidebar navigation menu to load your live telemetry stream dashboards.")

user_profile = {
    "account_name": "super_group_admin",
    "is_logtech_subscribed": True,       # Active subscription
    "is_gridtech_subscribed": False,     # No subscription
}

st.sidebar.title("Fuze Tech Gateway")
st.sidebar.markdown(f"**Logged in:** {user_profile['account_name']}")

pages = {}

home_page = st.Page(render_home_portal, title="Home Control Center")

logtech_page = st.Page("freight_lines.py", title="Legacy Freight Lines")
gridtech_page = st.Page("utility_labs.py", title="Legacy Utility Labs")

nav = st.navigation([home_page, logtech_page, gridtech_page])
nav.run()
