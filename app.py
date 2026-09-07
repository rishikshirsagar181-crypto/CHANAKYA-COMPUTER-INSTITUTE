import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Chanakya ERP",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_path = Path(__file__).parent / "index.html"
html = html_path.read_text(encoding="utf-8")

# Run the existing HTML/CSS/JavaScript app inside Streamlit.
components.html(
    html,
    height=1000,
    scrolling=True,
)
