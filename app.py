import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GOLD HUNTER V4 SAKTI200", layout="wide")

# BACA INDEX.HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=900, scrolling=True)
