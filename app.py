from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent; DATA = ROOT / "data"
st.set_page_config(page_title="Vertex 500 Paper Trader", layout="wide"); st.title("Vertex 500 Paper Trader"); st.caption("Vertex-500 end-of-day Chartink paper-trading dashboard")

def read_csv(name: str) -> pd.DataFrame:
    path = DATA / name
    if not path.exists() or path.stat().st_size == 0: return pd.DataFrame()
    return pd.read_csv(path)

snap = read_csv("daily_snapshots.csv"); trades = read_csv("trades.csv"); orders = read_csv("orders.csv"); signals = read_csv("signals.csv")
if snap.empty: st.info("No daily run has been completed yet.")
else:
    last = snap.iloc[-1]; c1, c2, c3, c4 = st.columns(4); c1.metric("Equity", f"₹{last['equity']:,.2f}", f"{last['total_return_pct']:.2f}%"); c2.metric("Total P&L", f"₹{last['total_profit']:,.2f}"); c3.metric("Cash", f"₹{last['cash']:,.2f}"); c4.metric("Open positions", int(last["open_positions"])); st.line_chart(snap.set_index("date")[["equity"]])
st.subheader("Closed trades"); st.caption("No closed trades yet.") if trades.empty else st.dataframe(trades.iloc[::-1], use_container_width=True)
st.subheader("Orders"); st.caption("No orders yet.") if orders.empty else st.dataframe(orders.iloc[::-1], use_container_width=True)
st.subheader("Scanner signals"); st.caption("No scanner signals stored yet.") if signals.empty else st.dataframe(signals.iloc[::-1], use_container_width=True)
