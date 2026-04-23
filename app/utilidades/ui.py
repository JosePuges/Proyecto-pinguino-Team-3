import streamlit as st

def apply_global_styles():
    st.markdown("""
    <style>
    .main > div { padding-top: 1.1rem; }
    .block-container { padding-top: 1rem; padding-bottom: 2rem; }
    .hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0ea5e9 100%);
        padding: 28px 30px;
        border-radius: 22px;
        color: white;
        box-shadow: 0 14px 30px rgba(15, 23, 42, 0.16);
        margin-bottom: 1rem;
    }
    .hero h1 { margin: 0 0 8px 0; font-size: 2.15rem; }
    .hero p { margin: 0; opacity: .95; font-size: 1rem; }
    .metric-card {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid rgba(15, 23, 42, 0.08);
        border-radius: 18px;
        padding: 16px;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
        margin-bottom: .5rem;
    }
    .metric-label { font-size: .95rem; color: #475569; margin-bottom: .2rem; }
    .metric-value { font-size: 1.85rem; font-weight: 700; color: #0f172a; }
    .page-title {
        padding: 18px 20px;
        border-radius: 18px;
        background: #ffffff;
        border: 1px solid rgba(15, 23, 42, 0.08);
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
        margin-bottom: 1rem;
    }
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #eff6ff 0%, #f8fafc 100%);
        border-right: 1px solid rgba(15, 23, 42, 0.06);
    }
    </style>
    """, unsafe_allow_html=True)

def render_hero(title, subtitle):
    st.markdown(f"""
    <div class="hero">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def render_metric_cards(items):
    cols = st.columns(len(items))
    for col, (label, value) in zip(cols, items):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

def render_page_header(title, subtitle):
    st.markdown(f"""
    <div class="page-title">
        <h2 style="margin:0 0 6px 0;">{title}</h2>
        <div style="color:#64748b;">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)
