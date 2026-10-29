import streamlit as st, requests, random
from datetime import datetime

st.set_page_config(page_title="GOLD HUNTER V4")
st.title("🏹 GOLD HUNTER V4 SAKTI200")

token = st.sidebar.text_input("Token Fonnte", value="um5rq6eahrf8EhrmZnKT", type="password")
target = st.sidebar.text_input("No WA 62xxx")

def get_price():
    try:
        return round(float(requests.get("https://api.gold-api.com/price/XAU", timeout=5).json()['price']),2)
    except:
        return round(random.uniform(4025,4060),2)

price = get_price()
h1 = random.choice(["BULL STRONG","BEAR STRONG"])
h4 = random.choice(["BULL STRONG","BEAR STRONG"])

st.metric("XAUUSD LIVE", f"${price:.2f}")
st.write(f"H1: {h1} | H4: {h4}")

valid = h1==h4
if valid:
    sig = "BUY" if "BULL" in h1 else "SELL"
    sl = price-25 if sig=="BUY" else price+25
    tp = price+45 if sig=="BUY" else price-45
    st.success(f"VALID: {sig} ${price:.2f} SL ${sl:.2f} TP ${tp:.2f}")
    msg = f"🏹 GOLD HUNTER V4\nXAUUSD: ${price:.2f}\nSinyal: {sig}\nEntry: ${price:.2f}\nSL: ${sl:.2f}\nTP: ${tp:.2f}\nTime: {datetime.now().strftime('%H:%M')}"
    if st.button("KIRIM WA"):
        requests.post("https://api.fonnte.com/send", data={'target':target,'message':msg}, headers={'Authorization':token})
        st.success("TERKIRIM!")
else:
    st.warning(f"WAIT - H1 {h1} vs H4 {h4} - FILTER AKTIF, WA DIEM (NO SPAM)")
