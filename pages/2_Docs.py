import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# MUST be first Streamlit command
st.set_page_config(
    page_title="Team XGBoost",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="collapsed"
)





# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
/* Target the REAL button element inside link_button */
div[data-testid="stLinkButton"] a {
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
}

/* Remove hover background */
div[data-testid="stLinkButton"] a:hover {
    background: transparent !important;
}

/* Optional — if you still see outline */
div[data-testid="stLinkButton"] a:focus {
    outline: none !important;
    box-shadow: none !important;
}
/* Push page content down so it isn't hidden */
.block-container {
    padding-top: 90px !important;
}

/* Sticky full-width header */
.sticky-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;

    background: black;
    padding: 12px 40px;

    z-index: 9999;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}
[data-testid="column"] {
    display: flex;
    align-items: center;
}

/* Remove extra spacing around header text */
h2, h3 {
    margin: 0 !important;
    padding: 0 !important;
}
/* Make Streamlit buttons look like navbar items */
div.stLinkButton > link_button {
    background: transparent;
    color: white;
    border: none;
    font-weight: 600;
}

div.stLinkButton > link_button:hover {
    color: #E0E0E0;
}


/* Target link buttons specifically */
a[data-testid="stLinkButton"] {
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
}

/* Optional — remove hover gray background */
a[data-testid="stLinkButton"]:hover {
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)


# ---------- STICKY HEADER ----------
header = st.container()

with header:
    st.markdown('<div class="sticky-header">', unsafe_allow_html=True)

    col1, col2, col3, = st.columns([6,2,1])

    with col1:
        st.markdown("<p style='font-size:28px; font-weight:700; margin:0;'>Team XGBoosted</p>",unsafe_allow_html=True)

    with col2:
        st.link_button("Meet the Team", url="/Team")

    with col3:
        st.link_button("Docs", url="/Docs")


    st.markdown("</div>", unsafe_allow_html=True)

with open("README.md", "r") as file:
    readme_content = file.read()
st.write(readme_content)
