# app.py - Veekstar Retail Intelligence (Executive Overview)
# Run: streamlit run app.py
import streamlit as st
from pathlib import Path
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import importlib.util
# ---------------------------
#  Paths
# ---------------------------
BASE = Path(__file__).resolve().parent
ASSETS = BASE / "assets"
BG_IMAGE = ASSETS / "bg_retail.jpg"

# ---------------------------
#  Load config.yaml (Credentials)
# ---------------------------
with open(BASE / "config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# ---------------------------
#  Page Config
# ---------------------------
st.set_page_config(page_title="Veekstar Retail Intelligence", page_icon="💫", layout="wide")

# ---------------------------
#  Inject Custom CSS
# ---------------------------
# -----------------------------------------------
# Login Page Styling + Background (Veekstar Gold Glow)
# -----------------------------------------------
import base64
from pathlib import Path

# Path to your background image
BG_IMAGE = Path(__file__).resolve().parent / "assets" / "bg_retail.jpg"

# Safely embed the background image in base64
if BG_IMAGE.exists():
    with open(BG_IMAGE, "rb") as img_file:
        b64_img = base64.b64encode(img_file.read()).decode()
    bg_css = f"background: linear-gradient(120deg, rgba(0,0,0,0.92), rgba(12,8,2,0.75)), url('data:image/jpeg;base64,{b64_img}');"
else:
    bg_css = "background: linear-gradient(120deg, rgba(0,0,0,0.92), rgba(12,8,2,0.75));"

st.markdown(f"""
    <style>
    /* ---- Background & shimmer ---- */
    .stApp {{
        {bg_css}
        background-size: cover;
        background-position: center center;
        background-attachment: fixed;
        color: #ffd27a !important;
        font-family: 'Poppins', sans-serif;
        animation: veek_shimmer 16s ease-in-out infinite alternate;
    }}

    @keyframes veek_shimmer {{
        0% {{ filter: brightness(0.9) saturate(0.95); }}
        50% {{ filter: brightness(1.12) saturate(1.08); }}
        100% {{ filter: brightness(0.95) saturate(1); }}
    }}

    /* ---- Login Card ---- */
    .stForm, .stTextInput, .stTextInput > div > div > input {{
        background: rgba(0,0,0,0.55) !important;
        border: 1px solid rgba(255,215,100,0.25) !important;
        border-radius: 12px !important;
        color: #ffd27a !important;
        font-weight: 500;
        transition: all 0.25s ease-in-out;
    }}

    .stTextInput > div > div > input::placeholder {{
        color: rgba(255,215,100,0.6) !important;
    }}

    /* ---- Focus Glow on Input ---- */
    .stTextInput > div > div > input:focus {{
        border: 1px solid #ffd27a !important;
        box-shadow: 0 0 14px rgba(255,210,122,0.55) !important;
        transform: scale(1.02);
    }}

    /* ---- Login Button with Gold Glow & Hover Pop ---- */
    div.stButton > button {{
        background: linear-gradient(90deg, #c9a437, #ffd27a, #c9a437);
        color: #000 !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6em 1.8em !important;
        cursor: pointer !important;
        transition: all 0.25s ease-in-out;
        box-shadow: 0 0 15px rgba(255,210,122,0.55);
        animation: buttonGlow 3s ease-in-out infinite alternate;
    }}

    div.stButton > button:hover {{
        transform: scale(1.08) translateY(-3px);
        background: linear-gradient(90deg, #ffd27a, #c9a437, #ffd27a);
        box-shadow: 0 0 25px rgba(255,215,0,0.95);
        transition: all 0.25s ease-in-out;
    }}

    @keyframes buttonGlow {{
        0% {{ box-shadow: 0 0 12px rgba(255,210,122,0.45); }}
        50% {{ box-shadow: 0 0 26px rgba(255,210,122,0.95); }}
        100% {{ box-shadow: 0 0 12px rgba(255,210,122,0.45); }}
    }}
    </style>
""", unsafe_allow_html=True)

# ---------------------------
#  Authentication Setup
# ---------------------------
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

# ---------------------------
# ---------------------------
#  Login Logic (Updated for Streamlit-Authenticator v0.4+)
# ---------------------------

try:
    name, authentication_status, username = authenticator.login(
        fields={
            "Form name": "💫 Veekstar Executive Login",
            "Username": "Username",
            "Password": "Password",
            "Login": "Login"
        },
        location="main"
    )
except Exception as e:
    st.error(f"Authentication error: {e}")
    name = authentication_status = username = None

# Show demo note ONLY on the login screen
if authentication_status is None:
    st.markdown(
        """
        <div style='margin-top:20px; padding:10px; border-radius:8px; background:rgba(255,255,255,0.08); color:#ccc; font-size:13px;'>
        <b>Demo credentials:</b> <code>guest</code> / <code>veekstar2025</code><br>
        <i>For reviewers only — in production, user-level authentication (e.g. OAuth / Firebase) would be implemented for executive-only access.</i>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------
#  Conditional Dashboard Load
# ---------------------------
if authentication_status:
    st.sidebar.success(f"Welcome, {name or username} 👑")
    authenticator.logout("Logout", "sidebar")

    dashboard_path = BASE / "dashboard_main.py"
    if dashboard_path.exists():
        spec = importlib.util.spec_from_file_location("dashboard_main", dashboard_path)
        dashboard = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(dashboard)
    else:
        st.error("❌ Dashboard file not found (dashboard_main.py missing).")

elif authentication_status is False:
    st.error("❌ Incorrect username or password.")
else:
    st.markdown("<h2 style='text-align:center;'>💫 Welcome to Veekstar Retail Intelligence</h2>", unsafe_allow_html=True)
    st.info("Please log in to continue.")
