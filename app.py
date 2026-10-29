import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GOLD HUNTER V4", layout="centered")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=900, scrolling=True)
