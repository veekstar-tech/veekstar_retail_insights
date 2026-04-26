# app.py - Veekstar Retail Intelligence (Executive Overview)
# Run: streamlit run app.py

import streamlit as st
from pathlib import Path
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import importlib.util
import base64

# ---------------------------
# Paths
# ---------------------------
BASE = Path(__file__).resolve().parent
ASSETS = BASE / "assets"
BG_IMAGE = ASSETS / "bg_retail.jpg"

# ---------------------------
# Load config.yaml (Credentials)
# ---------------------------
with open(BASE / "config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Veekstar Retail Intelligence",
    page_icon="💫",
    layout="wide"
)

# ---------------------------
# Background Image (Safe)
# ---------------------------
if BG_IMAGE.exists():
    with open(BG_IMAGE, "rb") as img_file:
        b64_img = base64.b64encode(img_file.read()).decode()
    bg_css = f"""
        background: linear-gradient(120deg, rgba(0,0,0,0.92), rgba(12,8,2,0.75)),
        url('data:image/jpeg;base64,{b64_img}');
    """
else:
    bg_css = "background: linear-gradient(120deg, rgba(0,0,0,0.92), rgba(12,8,2,0.75));"

# ---------------------------
# GLOBAL CSS (FIXED + FINAL)
# ---------------------------
st.markdown(f"""
<style>

/* =========================
   FORCE FULL APP BACKGROUND
========================= */
.stApp {{
    {bg_css}
    background-size: cover !important;
    background-position: center !important;
    background-attachment: fixed !important;
}}

/* =========================
   🚨 NUCLEAR SIDEBAR FIX (REMOVES ALL WHITE LAYERS)
========================= */

/* kill ALL sidebar backgrounds (every layer Streamlit creates) */
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] * ,
section[data-testid="stSidebarContent"],
div[data-testid="stSidebarNav"],
nav,
ul {{
    background: transparent !important;
    box-shadow: none !important;
}}

/* force ONLY image background */
section[data-testid="stSidebar"] {{
    background: url("assets/bg_retail.jpg") center/cover no-repeat !important;
}}

/* overlay for readability */
section[data-testid="stSidebar"]::before {{
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.35);
    z-index: 0;
}}

/* keep content above overlay */
section[data-testid="stSidebar"] > div {{
    position: relative;
    z-index: 1;
}}

/* =========================
   FORCE REMOVE STREAMLIT WHITE BLOCKS (IMPORTANT)
========================= */
div[data-testid="stSidebarContent"] {{
    background: transparent !important;
}}

div[data-testid="stSidebarNav"] {{
    background: transparent !important;
}}

.block-container {{
    background: transparent !important;
}}

/* =========================
   DROPDOWN DARK FIX
========================= */
div[data-baseweb="select"] > div {{
    background: rgba(10,10,10,0.75) !important;
    color: #ffd27a !important;
}}

div[data-baseweb="popover"],
div[role="listbox"] {{
    background: rgba(10,10,10,0.96) !important;
}}

div[role="option"] {{
    color: #ffd27a !important;
}}

div[role="option"]:hover {{
    background: rgba(255,215,100,0.15) !important;
}}

</style>
""", unsafe_allow_html=True)
# ---------------------------
# Authentication Setup
# ---------------------------
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

# ---------------------------
# Login Logic
# ---------------------------
try:
    authenticator.login(
        fields={
            "Form name": "💫 Veekstar Executive Login",
            "Username": "Username",
            "Password": "Password",
            "Login": "Login"
        },
        location="main"
    )

    authentication_status = st.session_state.get("authentication_status", None)
    name = st.session_state.get("name", "")
    username = st.session_state.get("username", "")

except Exception as e:
    st.error(f"Authentication error: {e}")
    authentication_status = None
    name = username = ""

# ---------------------------
# Login Screen Note
# ---------------------------
if authentication_status is None:
    st.markdown("""
        <div style='margin-top:20px; padding:10px;
        border-radius:8px; background:rgba(255,255,255,0.08);
        color:#ccc; font-size:13px;'>
        <b>Demo credentials:</b> <code>guest</code> / <code>veekstar2025</code>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------
# Logout fix
# ---------------------------
if "mobile_logout" in st.session_state and st.session_state["mobile_logout"]:
    authenticator.logout("Logout", "main")

# ---------------------------
# Dashboard Loader (UNCHANGED LOGIC)
# ---------------------------
if authentication_status:
    st.sidebar.success(f"Welcome, {name or username} 👑")
    authenticator.logout("🚪 Logout", "sidebar", key="main_logout")

    dashboard_path = BASE / "dashboard_main.py"
    if dashboard_path.exists():
        spec = importlib.util.spec_from_file_location("dashboard_main", dashboard_path)
        dashboard = importlib.util.module_from_spec(spec)

        dashboard.authenticator = authenticator
        spec.loader.exec_module(dashboard)

    else:
        st.error("❌ Dashboard file not found (dashboard_main.py missing).")

elif authentication_status is False:
    st.error("❌ Incorrect username or password.")

else:
    st.markdown("<h2 style='text-align:center;'>💫 Welcome to Veekstar Retail Intelligence</h2>",
                unsafe_allow_html=True)
    st.info("Please log in to continue.")