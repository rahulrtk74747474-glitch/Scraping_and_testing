from __future__ import annotations
import csv, io, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REPORTS=ROOT/"reports"; CHARTS=REPORTS/"charts"; OUT=REPORTS/"live_dashboard.md"

VERTEX=[("Vertex Daily","main","vertex_daily"),("Vertex 3:15","vertex-315-paper","vertex_315"),("Vertex 500 Daily","vertex-500-paper","vertex_500_daily"),("Vertex 500 3:15","vertex-500-315-paper","vertex_500_315")]
OB=[("OB NIFTY 15m","ob-nifty-15m-paper","ob_nifty"),("OB BANKNIFTY 15m","ob-banknifty-15m-paper","ob_banknifty"),("OB BTCUSDT 15m","ob-btcusdt-15m-paper","ob_btcusdt"),("OB XAUUSDT 15m","ob-xauusdt-15m-paper","ob_xauusdt")]
SMC=[("SMC NIFTY 15m","smc-nifty-15m-paper","smc_nifty"),("SMC BANKNIFTY 15m","smc-banknifty-15m-paper","smc_banknifty"),("SMC BTCUSDT 4h","smc-btcusdt-4h-paper","smc_btcusdt")]

def show(branch,path):
    p=subprocess.run(["git","show",f"origin/{branch}:{path}"],cwd=ROOT,text=True,capture_output=True)
    return p.stdout if p.returncode==0 else ""

def j(branch,path):
    raw=show(branch,path); return json.loads(raw) if raw.strip() else {}

def rows(branch,path):
    raw=show(branch,path); return list(csv.DictReader(io.StringIO(raw))) if raw.strip() else []

def n(v,d=0.0):
    try:return float(v)
    except:return float(d)

def money(v,cur="INR"):
    x=n(v); return ("$"+format(x,",.4f")) if cur=="USD" else ("₹"+format(x,",.2f"))

def ms(v):
    try:return datetime.fromtimestamp(int(float(v))/1000,tz=timezone.utc).isoformat()
    except:return "-"

def last(xs): return xs[-1] if xs else {}

def svg(path,title,values,labels):
    if len(values)<2:return False
    w,h=820,250; l,r,t,b=64,24,34,42; iw=w-l-r; ih=h-t-b; lo=min(values); hi=max(values)
    if hi==lo:hi=lo+1
    pts=[]
    for i,v in enumerate(values):
        x=l+iw*i/max(1,len(values)-1); y=t+ih*(1-(v-lo)/(hi-lo)); pts.append(f"{x:.1f},{y:.1f}")
    first=labels[0] if labels else ""; lastlab=labels[-1] if labels else ""
    body=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<rect width="100%" height="100%" fill="#ffffff"/>
<text x="{l}" y="22" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="#111827">{title}</text>
<line x1="{l}" y1="{t+ih}" x2="{w-r}" y2="{t+ih}" stroke="#d1d5db"/>
<line x1="{l}" y1="{t}" x2="{l}" y2="{t+ih}" stroke="#d1d5db"/>
<polyline fill="none" stroke="#2563eb" stroke-width="3" points="{' '.join(pts)}"/>
<text x="8" y="{t+8}" font-family="Arial,sans-serif" font-size="12" fill="#4b5563">{hi:,.2f}</text>
<text x="8" y="{t+ih}" font-family="Arial,sans-serif" font-size="12" fill="#4b5563">{lo:,.2f}</text>
<text x="{l}" y="{h-14}" font-family="Arial,sans-serif" font-size="11" fill="#6b7280">{first}</text>
<text x="{w-r}" y="{h-14}" text-anchor="end" font-family="Arial,sans-serif" font-size="11" fill="#6b7280">{lastlab}</text>
</svg>"""
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(body,encoding="utf-8"); return True

def latest_activity(order,sig):
    if order:
        return " ".join(str(x) for x in [order.get("side"),order.get("signal") or order.get("event"),order.get("symbol")] if x)
    if sig:
        return " ".join(str(x) for x in [sig.get("signal") or sig.get("event"),sig.get("symbol")] if x)
    return "-"

def vertex(name,branch,slug):
    s=j(branch,"data/state.json"); snaps=rows(branch,"data/daily_snapshots.csv"); ps=rows(branch,"data/position_snapshots.csv")
    o=rows(branch,"data/orders.csv"); g=rows(branch,"data/signals.csv"); z=last(snaps)
    return dict(name=name,branch=branch,slug=slug,kind="vertex",state=s,snaps=snaps,ps=ps,order=last(o),sig=last(g),equity=n(z.get("equity"),s.get("cash")),pnl=n(z.get("total_profit")),updated=s.get("last_run_date","-"))

def ob(name,branch,slug):
    s=j(branch,f"data/{slug}_state.json"); snaps=rows(branch,f"data/{slug}_snapshots.csv"); o=rows(branch,f"data/{slug}_orders.csv"); g=rows(branch,f"data/{slug}_signals.csv"); z=last(snaps)
    eq=n(z.get("equity_inr"),s.get("cash_inr"))
    return dict(name=name,branch=branch,slug=slug,kind="ob",state=s,snaps=snaps,order=last(o),sig=last(g),equity=eq,pnl=eq-n(s.get("starting_capital_inr",100000)),updated=ms(s.get("last_processed_close_time")))

def smc(name,branch,slug):
    s=j(branch,f"data/{slug}_state.json"); snaps=rows(branch,f"data/{slug}_snapshots.csv"); o=rows(branch,f"data/{slug}_orders.csv"); g=rows(branch,f"data/{slug}_signals.csv"); z=last(snaps)
    eq=n(z.get("equity_inr"),s.get("cash_inr"))
    return dict(name=name,branch=branch,slug=slug,kind="smc",state=s,snaps=snaps,order=last(o),sig=last(g),equity=eq,pnl=eq-n(s.get("starting_capital_inr",100000)),updated=ms(s.get("last_processed_close_time")))

def btc():
    branch="btcusdt-paper"; s=j(branch,"data/btc_state.json"); snaps=rows(branch,"data/btc_snapshots.csv"); o=rows(branch,"data/btc_orders.csv"); g=rows(branch,"data/btc_signals.csv"); z=last(snaps)
    eq=n(z.get("equity"),s.get("balance"))
    return dict(name="BTCUSDT 15m Existing Strategy",branch=branch,slug="btc_15m",kind="btc",state=s,snaps=snaps,order=last(o),sig=last(g),equity=eq,pnl=eq-n(s.get("starting_capital",100)),updated=ms(s.get("last_processed_close_time")))

def make_chart(d):
    p=CHARTS/(d["slug"]+".svg")
    if d["kind"]=="vertex":
        xs=d["snaps"][-40:]; vals=[n(x.get("equity")) for x in xs]; labels=[x.get("date","") for x in xs]
    else:
        xs=d["snaps"][-48:]; key="price" if d["kind"]=="btc" else "price_inr"; vals=[n(x.get(key)) for x in xs]; labels=[x.get("utc","")[:16] for x in xs]
    return ("charts/"+p.name) if svg(p,d["name"]+" — recent snapshots",vals,labels) else None

def open_block(d,chart):
    s=d["state"]; out=[]
    if d["kind"]=="vertex":
        for sym,p in (s.get("positions") or {}).items():
            hist=[x for x in d.get("ps",[]) if x.get("symbol")==sym]; z=last(hist)
            out += [f"### {d['name']} — {sym}","", "- Status: **OPEN LONG**",f"- Entry date: **{p.get('entry_date','-')}**",f"- Entry / average: **₹{n(p.get('entry_price')):,.2f} / ₹{n(p.get('weighted_avg_price')):,.2f}**",f"- Quantity: **{p.get('qty','-')}**",f"- Capital in trade: **₹{n(p.get('total_buy_cost')):,.2f}**",f"- Latest stored close: **{('₹'+format(n(z.get('latest_close')),',.2f')) if z else 'not yet persisted'}**",f"- Unrealized P&L: **{('₹'+format(n(z.get('unrealized_net_pnl_est')),',.2f')) if z else 'available after next position snapshot'}**",f"- Latest activity: **{latest_activity(d['order'],d['sig'])}**",""]
            if len(hist)>=2:
                vals=[n(x.get("latest_close")) for x in hist[-40:]]; labels=[x.get("date","") for x in hist[-40:]]; pp=CHARTS/(d["slug"]+"_"+sym.lower()+".svg")
                if svg(pp,d["name"]+" — "+sym+" price",vals,labels): out += [f"![{sym} price](charts/{pp.name})",""]
            else: out += ["_Position price chart appears automatically after at least two stored position snapshots._",""]
        return out
    if d["kind"]=="btc":
        p=s.get("open_position")
        if not p:return []
        z=last(d["snaps"])
        out=[f"### {d['name']} — BTCUSDT","",f"- Status: **OPEN {str(p.get('dir','')).upper()}**",f"- Entry: **$"+format(n(p.get("entry")),",.2f")+"**",f"- Current stored price: **$"+format(n(z.get("price")),",.2f")+"**",f"- Quantity: **{n(p.get('qty')):.8f} BTC**",f"- Stop / target: **$"+format(n(p.get("stop")),",.2f")+" / $"+format(n(p.get("target")),",.2f")+"**",f"- Unrealized P&L: **$"+format(n(z.get("unrealized_pnl")),",.4f")+"**",f"- Latest activity: **{latest_activity(d['order'],d['sig'])}**",""]
    else:
        p=s.get("position")
        if not p:return []
        z=last(d["snaps"]); avg=p.get("avg_entry_price_inr",p.get("entry_price_inr",0))
        out=[f"### {d['name']} — {s.get('symbol',d['name'])}","", "- Status: **OPEN LONG**",f"- Average/entry: **₹{n(avg):,.2f}**",f"- Current stored price: **₹{n(z.get('price_inr')):,.2f}**",f"- Quantity: **{n(p.get('qty')):.10f}**",f"- Unrealized P&L: **₹{n(z.get('unrealized_pnl_inr')):,.2f}**",f"- Latest activity: **{latest_activity(d['order'],d['sig'])}**",""]
        if d["kind"]=="ob": out += ["- Exit rule: **Confirmed bearish order block; no fixed numeric stop/target.**",""]
        else: out += ["- Exit rule: **Confirmed opposite major swing; no fixed numeric stop/target.**",""]
    if chart: out += [f"![{d['name']} chart]({chart})",""]
    return out

def main():
    CHARTS.mkdir(parents=True,exist_ok=True)
    for p in CHARTS.glob("*.svg"):p.unlink()
    data=[vertex(*x) for x in VERTEX]+[ob(*x) for x in OB]+[smc(*x) for x in SMC]+[btc()]
    charts={d["slug"]:make_chart(d) for d in data}
    opened=[]
    for d in data: opened += open_block(d,charts.get(d["slug"]))
    L=["# Live Strategy Dashboard","",f"_Auto-generated from the latest committed strategy state at {datetime.now(timezone.utc).isoformat()}._","","> **Live = latest completed GitHub strategy run/candle, not tick-by-tick streaming quotes.**","","[Combined performance](all_strategies_combined_latest.md) · [Full trade journal](all_trades_journal.md)","","## Open positions",""]
    L += opened if opened else ["_No strategy currently has an open position._",""]
    L += ["## Strategy status","","| Strategy | Status | Equity | P&L | Latest activity | Last processed |","|---|---|---:|---:|---|---|"]
    for d in data:
        s=d["state"]
        if d["kind"]=="vertex": status=str(len(s.get("positions") or {}))+" open"; cur="INR"
        elif d["kind"]=="btc": status=str((s.get("open_position") or {}).get("dir","FLAT")).upper() if s.get("open_position") else "FLAT"; cur="USD"
        else: status="LONG" if s.get("position") else "FLAT"; cur="INR"
        L.append(f"| {d['name']} | {status} | {money(d['equity'],cur)} | {money(d['pnl'],cur)} | {latest_activity(d['order'],d['sig'])} | {d['updated']} |")
    L += ["","## Recent strategy charts",""]
    anyc=False
    for d in data:
        c=charts.get(d["slug"])
        if c: anyc=True; L += [f"### {d['name']}","",f"![{d['name']} chart]({c})",""]
    if not anyc:L += ["_Charts appear after at least two stored snapshots._",""]
    L += ["## Automation","","- Dashboard rebuilds automatically in the master GitHub reporting workflow.","- The trade journal also updates from GitHub without ChatGPT.","- No ChatGPT subscription or open ChatGPT session is required.",""]
    OUT.write_text("\n".join(L),encoding="utf-8")
    print("Wrote",OUT)

if __name__=="__main__":main()
