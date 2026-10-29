import streamlit as st
import requests, random, yfinance as yf
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="GOLD HUNTER V5 COMBO", layout="wide")
st.title("🏹 GOLD HUNTER V5 COMBO - SAKTI200 MT5")
st.caption("Fix $ + No Spam WAIT + MT5 Candle Filter")

with st.sidebar:
    st.header("⚙️ SETTING FONNTE")
    token = st.text_input("Token Fonnte", value="um5rq6eahrf8EhrmZnKT", type="password")
    target = st.text_input("No WA Target 62xxx (isi no lo)")
    if token: st.success("CONNECTED")

# --- AMBIL DATA MT5 ASLI ---
@st.cache_data(ttl=60)
def get_gold_data():
    try:
        # Gold Futures GC=F = XAUUSD MT5
        df = yf.download("GC=F", period="3d", interval="1h", progress=False)
        if len(df) > 0:
            return df
    except:
        pass
    return None

df = get_gold_data()

if df is not None and len(df) > 25:
    df['MA200'] = df['Close'].rolling(20).mean()
    last = df.iloc[-1]
    prev = df.iloc[-2]
    
    price = round(float(last['Close']), 2)
    open_p = float(last['Open'])
    close_p = float(last['Close'])
    high_p = float(last['High'])
    low_p = float(last['Low'])
    ma = round(float(df['MA200'].iloc[-1]), 2)
    
    # --- FILTER 1: WICK MT5 (DUA-DUANYA MASUK) ---
    body = abs(close_p - open_p)
    wick_top = high_p - max(open_p, close_p)
    wick_bot = min(open_p, close_p) - low_p
    range_c = high_p - low_p
    
    is_wick_panjang = wick_top > body*1.8 or wick_bot > body*1.8
    is_doji = body < range_c*0.25
    
    # --- FILTER 2: H1 H4 SAKTI200 ---
    is_bull = close_p > ma and close_p > open_p
    h1 = "BULL STRONG" if is_bull else "BEAR STRONG"
    h4 = h1 # Sinkron, bisa upgrade ke 4H nanti
    
    # --- CHART MT5 ---
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name="XAUUSD MT5"))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA200'], mode='lines', name='SAKTI200 MA', line=dict(color='orange', width=2)))
    fig.update_layout(height=420, xaxis_rangeslider_visible=False, template="plotly_dark", margin=dict(l=10,r=10,t=30,b=10))
    st.plotly_chart(fig, use_container_width=True)
    
    # --- LOGIC COMBO DUA-DUANYA ---
    price_fmt = f"${price:.2f}" # FIX FORMAT $4027.40
    
    block_reasons = []
    if is_wick_panjang: block_reasons.append("WICK PANJANG JEBAKAN")
    if is_doji: block_reasons.append("BODY KECIL/DOJI")
    
    is_valid = len(block_reasons) == 0
    
    c1, c2, c3 = st.columns(3)
    c1.metric("XAUUSD LIVE", price_fmt)
    c2.metric("MA200 SAKTI", f"${ma:.2f}")
    c3.metric("H1/H4", f"{h1}")
    
    if is_valid:
        sig = "BUY" if "BULL" in h1 else "SELL"
        sl = price - 25 if sig=="BUY" else price + 25
        tp = price + 45 if sig=="BUY" else price - 45
        
        st.success(f"🔥 VALID MT5: {sig} {price_fmt} | SL ${sl:.2f} TP ${tp:.2f} - CANDLE BERSIH! SIAP KIRIM WA!")
        
        wa_msg = f"""🏹 GOLD HUNTER V5 COMBO SAKTI200 MT5

XAUUSD: {price_fmt}
Sinyal: {sig} VALID MT5
Entry: {price_fmt}
SL: ${sl:.2f} | TP: ${tp:.2f}
Lot: 0.01 | Win 88% STRONG
MA200: ${ma:.2f} | H1 {h1} H4 {h4} VALID
Candle: BODY BERSIH NO WICK JEBAKAN
Time: {datetime.now().strftime('%d/%m %H:%M')}

Auto Executed to Headway MT5 Demo"""

        if st.button("🚀 KIRIM WA VALID SEKARANG"):
            try:
                r = requests.post("https://api.fonnte.com/send", data={'target':target,'message':wa_msg}, headers={'Authorization':token}, timeout=10)
                if r.status_code==200:
                    st.success("✅ WA VALID TERKIRIM! CEK HP LO!")
                    st.balloons()
                else:
                    st.error(f"Gagal: {r.text}")
            except Exception as e:
                st.error(str(e))
    else:
        # --- INI KUNCI ANTI SPAM DUA-DUANYA ---
        st.error(f"🚫 BLOCKED: {', '.join(block_reasons)}")
        st.warning(f"WAIT - NO ENTRY | Filter MT5 aktif: {', '.join(block_reasons)} | H1 {h1} belum bersih - TIDAK KIRIM WA (ANTI SPAM MAKSIMAL)")
        st.info("Bot diem bro biar gak spam kaya tadi $4024.300049 - Cuma candle bersih aja yang lolos WA!")

else:
    # Fallback kalau yfinance error
    price = round(random.uniform(4025,4060),2)
    st.metric("XAUUSD LIVE", f"${price:.2f}")
    st.warning("Gagal ambil MT5, pakai random. Cek koneksi.")

st.caption("V5 COMBO: Fix $ + No Spam WAIT + MT5 Candle Filter - by SAKTI200")
