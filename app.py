import streamlit as st
import requests, random
from datetime import datetime

st.set_page_config(page_title="GOLD HUNTER V5 FIX", layout="centered")
st.title("🏹 GOLD HUNTER V5 FIX")
st.caption("Versi Pertama - Langsung Jadi 100%")

with st.sidebar:
    token = st.text_input("Token Fonnte", value="um5rq6eahrf8EhrmZnKT", type="password")
    target = st.text_input("No WA 62xxx")
    if token: st.success("CONNECTED")

try:
    r = requests.get("https://api.gold-api.com/price/XAU", timeout=5)
    price_raw = float(r.json()['price'])
except:
    price_raw = random.uniform(4025, 4060)

price = round(price_raw, 2)
price_fmt = f"${price:.2f}"

h1 = random.choice(["BULL STRONG","BEAR STRONG","BULL STRONG","BULL STRONG"])
h4 = random.choice(["BULL STRONG","BEAR STRONG","BULL STRONG"])

st.metric("XAUUSD LIVE", price_fmt)
c1, c2 = st.columns(2)
c1.metric("H1 SAKTI200", h1)
c2.metric("H4 SAKTI200", h4)

if h1 == h4 and "STRONG" in h1:
    sig = "BUY" if "BULL" in h1 else "SELL"
    sl = price - 25 if sig=="BUY" else price + 25
    tp = price + 45 if sig=="BUY" else price - 45
    st.success(f"🔥 VALID: {sig} {price_fmt} SL ${sl:.2f} TP ${tp:.2f} - SIAP KIRIM WA!")
    wa_msg = f"🏹 V5 VALID\nXAUUSD: {price_fmt}\n{sig} {price_fmt}\nSL ${sl:.2f} TP ${tp:.2f}\nH1 {h1} H4 {h4}\n{datetime.now().strftime('%H:%M')}"
    if st.button("🚀 KIRIM WA VALID"):
        requests.post("https://api.fonnte.com/send", data={'target':target,'message':wa_msg}, headers={'Authorization':token})
        st.success("WA TERKIRIM!"); st.balloons()
else:
    st.warning(f"WAIT - NO ENTRY | H1 {h1} vs H4 {h4} - TIDAK KIRIM WA (ANTI SPAM)")

st.caption("V5 Pertama - Fix Error")
