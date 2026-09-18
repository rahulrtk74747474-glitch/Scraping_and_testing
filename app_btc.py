from pathlib import Path
import json
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
STATE = DATA / "btc_state.json"

st.set_page_config(page_title="BTCUSDT Paper Trader", layout="wide")
st.title("BTCUSDT 15m Paper Trader")
st.caption("$100 virtual account · AMD Po3 default logic · paper only")

state = json.loads(STATE.read_text()) if STATE.exists() else {}

def read_csv(name):
    p = DATA / name
    return pd.read_csv(p) if p.exists() and p.stat().st_size else pd.DataFrame()

snaps = read_csv("btc_snapshots.csv")
trades = read_csv("btc_trades.csv")
orders = read_csv("btc_orders.csv")
signals = read_csv("btc_signals.csv")

if snaps.empty:
    st.info("No BTC paper-trading run has completed yet.")
else:
    last = snaps.iloc[-1]
    start = float(state.get("starting_capital", 100.0))
    equity = float(last["equity"])
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Equity", f"${equity:.4f}", f"{(equity/start-1)*100:.2f}%")
    c2.metric("Balance", f"${float(state.get('balance', start)):.4f}")
    c3.metric("Closed trades", int(state.get("closed_trades",0)))
    c4.metric("Max drawdown", f"{float(state.get('max_drawdown_pct',0)):.2f}%")
    chart = snaps.copy()
    chart["utc"] = pd.to_datetime(chart["utc"], utc=True)
    st.line_chart(chart.set_index("utc")[["equity"]])

st.subheader("Open position")
pos = state.get("open_position")
st.json(pos) if pos else st.caption("No open position.")

st.subheader("Closed trades")
st.caption("No closed trades yet.") if trades.empty else st.dataframe(trades.iloc[::-1], use_container_width=True)
st.subheader("Orders")
st.caption("No orders yet.") if orders.empty else st.dataframe(orders.iloc[::-1], use_container_width=True)
st.subheader("Strategy events")
st.caption("No strategy events yet.") if signals.empty else st.dataframe(signals.iloc[::-1], use_container_width=True)
