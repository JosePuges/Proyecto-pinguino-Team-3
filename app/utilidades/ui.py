import streamlit as st

ARCTIC_COLORS = {
    "navy": "#0B3C5D",
    "ocean": "#1D6FA3",
    "sky": "#4FB3D9",
    "ice": "#DFF3FA",
    "mist": "#F5FAFF",
    "slate": "#6B7C8F",
    "white": "#FFFFFF",
}

def apply_arctic_theme():
    st.markdown(f"""
    <style>
    html, body, [class*="css"] {{
        font-family: "Segoe UI", "Inter", sans-serif;
        color: {ARCTIC_COLORS["navy"]};
    }}

    .stApp {{
        background-color: {ARCTIC_COLORS["white"]};
        color: {ARCTIC_COLORS["navy"]};
    }}

    .block-container {{
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        max-width: 1320px;
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {ARCTIC_COLORS["mist"]} 0%, {ARCTIC_COLORS["white"]} 100%);
        border-right: 1px solid {ARCTIC_COLORS["ice"]};
    }}

    section[data-testid="stSidebar"] * {{
        color: {ARCTIC_COLORS["navy"]} !important;
    }}

    [data-testid="stSidebarNav"] a {{
        border-radius: 10px;
        margin-bottom: 4px;
    }}

    [data-testid="stSidebarNav"] a:hover {{
        background-color: {ARCTIC_COLORS["ice"]};
    }}

    [data-testid="stSidebarNav"] a span {{
        color: {ARCTIC_COLORS["navy"]} !important;
        font-weight: 600 !important;
        opacity: 1 !important;
    }}

    [data-testid="stSidebarNav"] a[aria-current="page"] {{
        background: linear-gradient(90deg, {ARCTIC_COLORS["ocean"]}, {ARCTIC_COLORS["sky"]});
    }}

    [data-testid="stSidebarNav"] a[aria-current="page"] span {{
        color: white !important;
    }}

    h1 {{
        color: {ARCTIC_COLORS["navy"]};
        font-weight: 800;
        letter-spacing: -0.02em;
    }}

    h2, h3, h4 {{
        color: {ARCTIC_COLORS["ocean"]};
        font-weight: 700;
        letter-spacing: -0.01em;
    }}

    .hero {{
        background: linear-gradient(135deg, {ARCTIC_COLORS["navy"]} 0%, {ARCTIC_COLORS["ocean"]} 55%, {ARCTIC_COLORS["sky"]} 100%);
        color: white;
        padding: 28px 30px;
        border-radius: 20px;
        margin-bottom: 1.1rem;
        box-shadow: 0 16px 32px rgba(11, 60, 93, 0.15);
    }}

    .hero h1 {{
        color: white;
        margin: 0 0 8px 0;
    }}

    .hero p {{
        color: #F8FCFF;
        margin: 0;
        font-size: 1.02rem;
        line-height: 1.55;
        max-width: 900px;
    }}

    .page-header {{
        background: {ARCTIC_COLORS["mist"]};
        border: 1px solid {ARCTIC_COLORS["ice"]};
        border-radius: 18px;
        padding: 20px 22px;
        margin-bottom: 1rem;
    }}

    .page-header h2 {{
        margin: 0 0 6px 0;
        color: {ARCTIC_COLORS["navy"]};
    }}

    .page-header p {{
        margin: 0;
        color: {ARCTIC_COLORS["slate"]};
    }}

    .card {{
        background: #F8FCFF;
        border: 1px solid {ARCTIC_COLORS["ice"]};
        border-radius: 16px;
        padding: 18px 18px 12px 18px;
        margin-bottom: 1rem;
        box-shadow: 0 8px 22px rgba(29, 111, 163, 0.05);
    }}

    .story-block {{
        background: {ARCTIC_COLORS["mist"]};
        border-left: 5px solid {ARCTIC_COLORS["sky"]};
        border-radius: 14px;
        padding: 16px 18px;
        margin-bottom: 1rem;
    }}

    .story-block p:last-child {{
        margin-bottom: 0;
    }}

    div[data-testid="stMetric"] {{
        background: #F8FCFF;
        border: 1px solid {ARCTIC_COLORS["ice"]};
        border-radius: 14px;
        padding: 10px;
        box-shadow: 0 6px 18px rgba(29, 111, 163, 0.04);
    }}

    div[data-testid="stMetricLabel"] {{
        color: {ARCTIC_COLORS["slate"]};
        font-weight: 600;
    }}

    div[data-testid="stMetricValue"] {{
        color: {ARCTIC_COLORS["navy"]};
        font-weight: 800;
    }}

    .stButton > button, .stDownloadButton > button {{
        background: {ARCTIC_COLORS["ocean"]};
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
    }}

    .stButton > button:hover, .stDownloadButton > button:hover {{
        background: {ARCTIC_COLORS["navy"]};
        color: white;
    }}

    .stSelectbox label, .stMultiSelect label, .stRadio label {{
        color: {ARCTIC_COLORS["navy"]} !important;
        font-weight: 600;
    }}

    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        border-bottom: 1px solid {ARCTIC_COLORS["ice"]};
    }}

    .stTabs [data-baseweb="tab"] {{
        color: {ARCTIC_COLORS["ocean"]};
        font-weight: 700;
    }}

    .stTabs [aria-selected="true"] {{
        color: {ARCTIC_COLORS["navy"]} !important;
        border-bottom: 3px solid {ARCTIC_COLORS["sky"]};
    }}

    .stDataFrame, div[data-testid="stTable"] {{
        border: 1px solid {ARCTIC_COLORS["ice"]};
        border-radius: 12px;
        overflow: hidden;
    }}

    code, pre {{
        border-radius: 12px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

def render_hero(title, subtitle):
    st.markdown(f"""
    <div class="hero">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def render_page_header(title, subtitle):
    st.markdown(f"""
    <div class="page-header">
        <h2>{title}</h2>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def open_card():
    st.markdown('<div class="card">', unsafe_allow_html=True)

def close_card():
    st.markdown('</div>', unsafe_allow_html=True)

def render_story(markdown_text):
    if markdown_text and markdown_text.strip():
        st.markdown('<div class="story-block">', unsafe_allow_html=True)
        st.markdown(markdown_text)
        st.markdown('</div>', unsafe_allow_html=True)
