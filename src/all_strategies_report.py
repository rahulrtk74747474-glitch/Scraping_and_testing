
import csv, io, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports" / "all_strategies_combined_latest.md"

OB = [
 ("OB NIFTY 15m","ob-nifty-15m-paper","ob_nifty"),
 ("OB BANKNIFTY 15m","ob-banknifty-15m-paper","ob_banknifty"),
 ("OB BTCUSDT 15m","ob-btcusdt-15m-paper","ob_btcusdt"),
 ("OB XAUUSDT 15m","ob-xauusdt-15m-paper","ob_xauusdt"),
]
VERTEX = [
 ("Vertex 3:15","vertex-315-paper"),
 ("Vertex 500 3:15","vertex-500-315-paper"),
 ("Vertex 500 Daily","vertex-500-paper"),
]
BTC_BRANCH = "btcusdt-paper"
SMC = [
 ("SMC NIFTY 15m","smc-nifty-15m-paper","smc_nifty"),
 ("SMC BANKNIFTY 15m","smc-banknifty-15m-paper","smc_banknifty"),
 ("SMC BTCUSDT 4h","smc-btcusdt-4h-paper","smc_btcusdt"),
]

def show(branch, path):
    p = subprocess.run(["git","show",f"origin/{branch}:{path}"], cwd=ROOT, text=True, capture_output=True)
    return p.stdout if p.returncode == 0 else ""

def j(branch, path):
    raw = show(branch,path)
    return json.loads(raw) if raw else {}

def last(branch, path):
    raw = show(branch,path)
    if not raw.strip(): return {}
    rows = list(csv.DictReader(io.StringIO(raw)))
    return rows[-1] if rows else {}

def n(v, d=0.0):
    try: return float(v)
    except: return float(d)

def ni(v):
    return "₹" + format(n(v), ",.2f")

def usd(v):
    return "$" + format(n(v), ",.4f")

def pc(v):
    return format(n(v), ".2f") + "%"

def mst(v):
    try: return datetime.fromtimestamp(int(float(v))/1000, tz=timezone.utc).isoformat()
    except: return "-"

def ob(name, branch, slug):
    s=j(branch,f"data/{slug}_state.json")
    snap=last(branch,f"data/{slug}_snapshots.csv")
    sig=last(branch,f"data/{slug}_signals.csv")
    order=last(branch,f"data/{slug}_orders.csv")
    trade=last(branch,f"data/{slug}_trades.csv")
    start=n(s.get("starting_capital_inr",100000))
    eq=n(snap.get("equity_inr"),s.get("cash_inr",start))
    return dict(kind="ob",name=name,branch=branch,slug=slug,state=s,snap=snap,sig=sig,order=order,trade=trade,
                start=start,equity=eq,pnl=eq-start,ret=((eq/start)-1)*100 if start else 0)

def vertex(name, branch):
    s=j(branch,"data/state.json")
    snap=last(branch,"data/daily_snapshots.csv")
    sig=last(branch,"data/signals.csv")
    order=last(branch,"data/orders.csv")
    start=n(s.get("starting_capital",100000))
    eq=n(snap.get("equity"),s.get("cash",start))
    return dict(kind="vertex",name=name,branch=branch,state=s,snap=snap,sig=sig,order=order,
                positions=s.get("positions") or {},start=start,equity=eq,pnl=eq-start,
                ret=((eq/start)-1)*100 if start else 0)

def btc():
    s=j(BTC_BRANCH,"data/btc_state.json")
    snap=last(BTC_BRANCH,"data/btc_snapshots.csv")
    sig=last(BTC_BRANCH,"data/btc_signals.csv")
    order=last(BTC_BRANCH,"data/btc_orders.csv")
    trade=last(BTC_BRANCH,"data/btc_trades.csv")
    start=n(s.get("starting_capital",100))
    eq=n(snap.get("equity"),s.get("balance",start))
    return dict(kind="btc",name="BTCUSDT 15m Existing Strategy",branch=BTC_BRANCH,state=s,snap=snap,sig=sig,order=order,trade=trade,
                start=start,equity=eq,pnl=eq-start,ret=((eq/start)-1)*100 if start else 0)

def smc(name, branch, slug):
    s=j(branch,f"data/{slug}_state.json")
    snap=last(branch,f"data/{slug}_snapshots.csv")
    sig=last(branch,f"data/{slug}_signals.csv")
    order=last(branch,f"data/{slug}_orders.csv")
    trade=last(branch,f"data/{slug}_trades.csv")
    start=n(s.get("starting_capital_inr",100000))
    eq=n(snap.get("equity_inr"),s.get("cash_inr",start))
    return dict(kind="smc",name=name,branch=branch,slug=slug,state=s,snap=snap,sig=sig,order=order,trade=trade,
                start=start,equity=eq,pnl=eq-start,ret=((eq/start)-1)*100 if start else 0)

def detail_smc(d):
    s=d["state"]; sig=d["sig"]; o=d["order"]; t=d["trade"]; snap=d["snap"]; pos=s.get("position")
    x=["## "+d["name"],"",
       "- Branch: "+d["branch"],
       "- Status: **"+("LONG" if pos else "FLAT")+"**",
       "- Starting: **"+ni(d["start"])+"**",
       "- Equity: **"+ni(d["equity"])+"**",
       "- P&L: **"+ni(d["pnl"])+" ("+pc(d["ret"])+")**",
       "- Cash: **"+ni(s.get("cash_inr",d["start"]))+"**",
       "- Realized / unrealized: **"+ni(s.get("realized_pnl_inr",0))+" / "+ni(snap.get("unrealized_pnl_inr",0) if snap else 0)+"**",
       "- Last candle: **"+mst(s.get("last_processed_close_time"))+"**","",
       "### Latest activity","",
       "- Confirmed swing: **"+(sig.get("signal","None") if sig else "None")+"**",
       "- Executed order: **"+(((o.get("side","")+" "+o.get("sizing_rule","")).strip()+" / "+((o.get("fraction_pct","")+"%") if o.get("fraction_pct","") else "restore exact qty")) if o else "None")+"**"]
    if o: x.append("- Executed value: **"+ni(o.get("gross_notional_inr"))+"**")
    if t: x.append("- Latest realized slice: **"+ni(t.get("net_pnl_inr"))+" ("+pc(t.get("return_pct"))+")**")
    if pos:
        x += ["","### Open position","",
              "- Quantity: **"+format(n(pos.get("qty")),".10f")+"**",
              "- Remaining cost basis: **"+ni(pos.get("cost_basis_inr"))+"**"]
    url="https://github.com/rahulrtk74747474-glitch/Scraping_and_testing/blob/"+d["branch"]+"/reports/"+d["slug"]+"_latest.md"
    return x+["","[Open individual report]("+url+")",""]

def detail_ob(d):
    s=d["state"]; sig=d["sig"]; o=d["order"]; t=d["trade"]; snap=d["snap"]; pos=s.get("position")
    x=["## "+d["name"],"",
       "- Branch: "+d["branch"],
       "- Status: **"+("LONG" if pos else "FLAT")+"**",
       "- Starting: **"+ni(d["start"])+"**",
       "- Equity: **"+ni(d["equity"])+"**",
       "- P&L: **"+ni(d["pnl"])+" ("+pc(d["ret"])+")**",
       "- Cash: **"+ni(s.get("cash_inr",0))+"**",
       "- Realized / unrealized: **"+ni(s.get("realized_pnl_inr",0))+" / "+ni(snap.get("unrealized_pnl_inr",0) if snap else 0)+"**",
       "- Closed trades: **"+str(int(n(s.get("closed_trades",0))))+"**",
       "- Last candle: **"+mst(s.get("last_processed_close_time"))+"**","",
       "### Latest activity","",
       "- Signal: **"+(sig.get("signal","None") if sig else "None")+"**"]
    x.append("- Executed order: **"+(o.get("side","")+" "+o.get("signal","") if o else "None")+"**")
    if o: x.append("- Executed value: **"+ni(o.get("gross_notional_inr"))+"**")
    x.append("- Latest closed trade: **"+(ni(t.get("net_pnl_inr"))+" ("+pc(t.get("return_pct"))+")" if t else "None")+"**")
    if pos:
        x += ["","### Open position","",
              "- Entry INR: **"+ni(pos.get("entry_price_inr"))+"**",
              "- Quantity: **"+format(n(pos.get("qty")),".10f")+"**"]
    url="https://github.com/rahulrtk74747474-glitch/Scraping_and_testing/blob/"+d["branch"]+"/reports/"+d["slug"]+"_latest.md"
    return x+["","[Open individual report]("+url+")",""]

def detail_vertex(d):
    s=d["state"]; sig=d["sig"]; o=d["order"]; snap=d["snap"]; positions=d["positions"]
    x=["## "+d["name"],"",
       "- Branch: "+d["branch"],
       "- Starting: **"+ni(d["start"])+"**",
       "- Equity: **"+ni(d["equity"])+"**",
       "- P&L: **"+ni(d["pnl"])+" ("+pc(d["ret"])+")**",
       "- Cash: **"+ni(s.get("cash",0))+"**",
       "- Realized / unrealized: **"+ni(s.get("realized_pnl",0))+" / "+ni(snap.get("unrealized_pnl_est",0) if snap else 0)+"**",
       "- Open positions: **"+str(len(positions))+"**",
       "- Last run: **"+str(s.get("last_run_date","-"))+"**","",
       "### Latest activity","",
       "- Scanner signal: **"+((sig.get("symbol","-")+" — "+sig.get("name","-")) if sig else "None")+"**",
       "- Executed order: **"+((o.get("event","")+" "+o.get("side","")+" "+o.get("symbol","")).strip() if o else "None")+"**"]
    if positions:
        x += ["","### Open positions","","| Symbol | Qty | Entry | Avg | Capital |","|---|---:|---:|---:|---:|"]
        for sym,p in positions.items():
            x.append("| "+sym+" | "+str(int(n(p.get("qty"))))+" | "+format(n(p.get("entry_price")),".2f")+" | "+format(n(p.get("weighted_avg_price")),".2f")+" | "+ni(p.get("total_buy_cost"))+" |")
    url="https://github.com/rahulrtk74747474-glitch/Scraping_and_testing/blob/"+d["branch"]+"/reports/latest.md"
    return x+["","[Open individual report]("+url+")",""]

def detail_btc(d):
    s=d["state"]; sig=d["sig"]; o=d["order"]; t=d["trade"]; snap=d["snap"]; pos=s.get("open_position")
    x=["## "+d["name"],"",
       "- Branch: "+d["branch"],
       "- Status: **"+(pos.get("dir","flat").upper() if pos else "FLAT")+"**",
       "- Starting: **"+usd(d["start"])+"**",
       "- Equity: **"+usd(d["equity"])+"**",
       "- P&L: **"+usd(d["pnl"])+" ("+pc(d["ret"])+")**",
       "- Balance: **"+usd(s.get("balance",0))+"**",
       "- Realized / unrealized: **"+usd(s.get("realized_pnl",0))+" / "+usd(snap.get("unrealized_pnl",0) if snap else 0)+"**",
       "- Closed trades: **"+str(int(n(s.get("closed_trades",0))))+"**",
       "- Last candle: **"+mst(s.get("last_processed_close_time"))+"**","",
       "### Latest activity","",
       "- Strategy event: **"+(sig.get("event","None") if sig else "None")+"**",
       "- Executed order: **"+((o.get("event","")+" / "+o.get("side","")).strip() if o else "None")+"**",
       "- Latest closed trade: **"+(usd(t.get("net_pnl"))+" ("+pc(t.get("return_pct"))+")" if t else "None")+"**"]
    if pos:
        x += ["","### Open position","",
              "- Direction: **"+pos.get("dir","-").upper()+"**",
              "- Entry: **$"+format(n(pos.get("entry")),",.2f")+"**",
              "- Stop / target: **$"+format(n(pos.get("stop")),",.2f")+" / $"+format(n(pos.get("target")),",.2f")+"**"]
    url="https://github.com/rahulrtk74747474-glitch/Scraping_and_testing/blob/btcusdt-paper/reports/btc_latest.md"
    return x+["","[Open individual report]("+url+")",""]

def main():
    obs=[ob(*x) for x in OB]
    verts=[vertex(*x) for x in VERTEX]
    smcs=[smc(*x) for x in SMC]
    b=btc()
    rupee=obs+verts+smcs
    st=sum(x["start"] for x in rupee); eq=sum(x["equity"] for x in rupee)
    lines=["# All Strategies — Combined Paper-Trading Report","",
           "_Auto-updated from every current strategy branch. Generated "+datetime.now(timezone.utc).isoformat()+"._","",
           "## Master summary","",
           "- INR accounts: **"+str(len(rupee))+"**",
           "- INR starting capital: **"+ni(st)+"**",
           "- INR current equity: **"+ni(eq)+"**",
           "- INR total P&L: **"+ni(eq-st)+" ("+pc(((eq/st)-1)*100 if st else 0)+")**",
           "- Existing BTC account: **"+usd(b["equity"])+" equity; "+usd(b["pnl"])+" P&L ("+pc(b["ret"])+")**","",
           "USD and INR are intentionally kept separate.","",
           "## At-a-glance","",
           "| Strategy | Currency | Status | Equity | P&L | Return | Latest |",
           "|---|---|---|---:|---:|---:|---|"]
    for d in obs:
        status="LONG" if d["state"].get("position") else "FLAT"
        latest=d["order"].get("side") if d["order"] else d["sig"].get("signal") if d["sig"] else "-"
        lines.append("| "+d["name"]+" | INR | "+status+" | "+ni(d["equity"])+" | "+ni(d["pnl"])+" | "+pc(d["ret"])+" | "+latest+" |")
    for d in verts:
        latest=(d["order"].get("event","")+" "+d["order"].get("symbol","")).strip() if d["order"] else d["sig"].get("symbol","-") if d["sig"] else "-"
        lines.append("| "+d["name"]+" | INR | "+str(len(d["positions"]))+" open | "+ni(d["equity"])+" | "+ni(d["pnl"])+" | "+pc(d["ret"])+" | "+latest+" |")
    for d in smcs:
        latest=(((d["order"].get("side","")+" "+d["order"].get("sizing_rule","")).strip()+" "+((d["order"].get("fraction_pct","")+"%") if d["order"].get("fraction_pct","") else "exact qty")) if d["order"] else d["sig"].get("signal","-") if d["sig"] else "-")
        status="LONG" if d["state"].get("position") else "FLAT"
        lines.append("| "+d["name"]+" | INR | "+status+" | "+ni(d["equity"])+" | "+ni(d["pnl"])+" | "+pc(d["ret"])+" | "+latest+" |")
    status=b["state"].get("open_position",{}).get("dir","FLAT").upper() if b["state"].get("open_position") else "FLAT"
    latest=b["order"].get("event") if b["order"] else b["sig"].get("event") if b["sig"] else "-"
    lines.append("| "+b["name"]+" | USD | "+status+" | "+usd(b["equity"])+" | "+usd(b["pnl"])+" | "+pc(b["ret"])+" | "+latest+" |")
    lines += ["","---","","# Order Block Strategies",""]
    for d in obs: lines += detail_ob(d)+["---",""]
    lines += ["# SMC Clean Wave Strategies",""]
    for d in smcs: lines += detail_smc(d)+["---",""]
    lines += ["# Vertex Strategies",""]
    for d in verts: lines += detail_vertex(d)+["---",""]
    lines += ["# Other Strategy",""]+detail_btc(b)+["---","","Paper trading only. This report does not place real orders.",""]
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text("\n".join(lines),encoding="utf-8")
    print("Wrote",OUT)

if __name__=="__main__":
    main()
