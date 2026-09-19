from __future__ import annotations
import csv,json,time
from dataclasses import dataclass
from datetime import datetime,timezone
from pathlib import Path
import requests,yfinance as yf

ROOT=Path(__file__).resolve().parents[1]; CFG=ROOT/'smc_config.json'; DATA=ROOT/'data'; REPORTS=ROOT/'reports'
@dataclass(frozen=True)
class Bar: open_time:int; open:float; high:float; low:float; close:float; close_time:int

def cfgload():
    c=json.loads(CFG.read_text()); c.setdefault('fee_rate',0.0); c.setdefault('min_trade_inr',1.0); c.setdefault('source_note',''); return c

def closed(xs):
    now=int(time.time()*1000); return [x for x in xs if x.close_time<now]

def binance(c):
    r=requests.get('https://data-api.binance.vision/api/v3/klines',params={'symbol':c['ticker'],'interval':c['timeframe'],'limit':1000},timeout=25); r.raise_for_status()
    return closed([Bar(int(x[0]),float(x[1]),float(x[2]),float(x[3]),float(x[4]),int(x[6])) for x in r.json()])

def yahoo(c):
    d=yf.download(c['ticker'],period='10d',interval='15m',auto_adjust=False,prepost=False,progress=False,threads=False)
    if d is None or d.empty: raise RuntimeError('No Yahoo 15m data for '+c['ticker'])
    if getattr(d.columns,'nlevels',1)>1:d.columns=[x[0] for x in d.columns]
    out=[]
    for ts,r in d.dropna(subset=['Open','High','Low','Close']).iterrows():
        t=ts.to_pydatetime(); t=t.replace(tzinfo=timezone.utc) if t.tzinfo is None else t.astimezone(timezone.utc); ms=int(t.timestamp()*1000)
        out.append(Bar(ms,float(r['Open']),float(r['High']),float(r['Low']),float(r['Close']),ms+900000-1))
    return closed(sorted(out,key=lambda x:x.open_time))

def usdinr():
    d=yf.download('INR=X',period='5d',interval='15m',auto_adjust=False,progress=False,threads=False)
    if d is None or d.empty:d=yf.download('INR=X',period='1mo',interval='1d',auto_adjust=False,progress=False,threads=False)
    if getattr(d.columns,'nlevels',1)>1:d.columns=[x[0] for x in d.columns]
    return float(d['Close'].dropna().iloc[-1])

def bars(c): return binance(c) if c['source']=='binance_spot' else yahoo(c)
def inr(px,c,fx): return px if c['quote_currency'].upper()=='INR' else px*fx

def signal(xs,i,s):
    p=i-s; l=p-s
    if l<0:return None
    w=xs[l:i+1]; z=xs[p]; ph=z.high==max(x.high for x in w); pl=z.low==min(x.low for x in w)
    if ph==pl:return None
    return {'signal':'BUY' if pl else 'SELL','confirmed_close_time':xs[i].close_time,'confirmed_price':xs[i].close,'pivot_open_time':z.open_time,'pivot_price':z.low if pl else z.high,'sig_sens':s}

def paths(c):
    q=c['slug']; return {k:(DATA/f'{q}_{k}.csv') for k in ['signals','orders','trades','snapshots']}|{'state':DATA/f'{q}_state.json','report':REPORTS/f'{q}_latest.md'}

def initial(c):
    a=float(c['starting_capital_inr'])
    return {
        'version':2,'strategy':'SMC Clean Wave major swings','symbol':c['display_symbol'],'timeframe':c['timeframe'],
        'starting_capital_inr':a,'cash_inr':a,'realized_pnl_inr':0.0,'position':None,
        'last_processed_close_time':None,'last_signal':None,'last_sequence_direction':None,
        'buy_step':0,'sell_step':0,'equity_peak_inr':a,'max_drawdown_pct':0.0,
        'sell_executions':0,'wins':0,'losses':0,
        'last_executed_side':None,'last_executed_qty':0.0,'last_executed_notional_inr':0.0
    }

def load(c,p):
    s=json.loads(p['state'].read_text()) if p['state'].exists() else initial(c)
    defaults={
        'version':2,'last_executed_side':None,'last_executed_qty':0.0,'last_executed_notional_inr':0.0,
        'buy_step':0,'sell_step':0,'last_sequence_direction':None
    }
    for k,v in defaults.items(): s.setdefault(k,v)
    return s

def save(s,p): p['state'].parent.mkdir(parents=True,exist_ok=True); p['state'].write_text(json.dumps(s,indent=2,sort_keys=True))
def eq(s,px):
    p=s.get('position'); mv=float(p['qty'])*px if p else 0.0; un=mv-float(p['cost_basis_inr']) if p else 0.0; return float(s['cash_inr'])+mv,un

def addcsv(path,rows,fields):
    if not rows:return
    path.parent.mkdir(parents=True,exist_ok=True); exists=path.exists() and path.stat().st_size>0
    with path.open('a',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); (None if exists else w.writeheader()); w.writerows(rows)

def frac(step): return 0.5 if int(step)==0 else 0.125/(2**(int(step)-1))
def fmt(ms): return datetime.fromtimestamp(int(ms)/1000,tz=timezone.utc).isoformat() if ms else '-'

def trade(s,g,b,c,fx):
    o=[]; t=[]
    rate=float(c['fee_rate']); pxq=float(b.close); pxi=inr(pxq,c,fx)
    d=g['signal']; prior_exec=s.get('last_executed_side'); reversal=prior_exec is not None and prior_exec!=d
    min_trade=float(c['min_trade_inr'])

    if d=='BUY':
        cash=float(s['cash_inr'])
        if reversal and float(s.get('last_executed_qty',0.0))>0:
            target_qty=float(s['last_executed_qty'])
            max_qty=(cash/(1+rate))/pxi if pxi>0 else 0.0
            qty=min(target_qty,max_qty)
            n=qty*pxi
            sizing_rule='RESTORE_LAST_SELL_QTY'
            fraction_pct=''
            ladder_step=0
            s['buy_step']=0
        else:
            st=int(s.get('buy_step',0))
            f=frac(st)
            n=min(cash*f,cash/(1+rate))
            qty=n/pxi if pxi>0 else 0.0
            sizing_rule='LADDER'
            fraction_pct=f*100
            ladder_step=st+1
        if n>=min_trade and qty>0:
            fee=n*rate
            p=s.get('position') or {'first_entry_time':b.close_time,'qty':0.0,'cost_basis_inr':0.0}
            p['qty']=float(p['qty'])+qty; p['cost_basis_inr']=float(p['cost_basis_inr'])+n+fee
            p['avg_entry_price_inr']=p['cost_basis_inr']/p['qty']; p['last_buy_time']=b.close_time
            s['position']=p; s['cash_inr']=cash-n-fee
            if not reversal: s['buy_step']=int(s.get('buy_step',0))+1
            else: s['buy_step']=0
            s['sell_step']=0
            s['last_executed_side']='BUY'; s['last_executed_qty']=qty; s['last_executed_notional_inr']=n
            o.append({'close_time':b.close_time,'signal':'BUY','side':'BUY','sizing_rule':sizing_rule,'ladder_step':ladder_step,
                      'fraction_pct':fraction_pct,'sequence_base':'current_cash','price_quote':pxq,'price_inr':pxi,'qty':qty,
                      'gross_notional_inr':n,'fee_inr':fee,'cash_after_inr':s['cash_inr']})

    else:
        p=s.get('position')
        if p:
            before=float(p['qty'])
            if reversal and float(s.get('last_executed_qty',0.0))>0:
                qty=min(float(s['last_executed_qty']),before)
                sizing_rule='RESTORE_LAST_BUY_QTY'
                fraction_pct=''
                ladder_step=0
                s['sell_step']=0
            else:
                st=int(s.get('sell_step',0))
                f=frac(st)
                qty=min(before*f,before)
                sizing_rule='LADDER'
                fraction_pct=f*100
                ladder_step=st+1
            gross=qty*pxi
            if gross>=min_trade and qty>0:
                fee=gross*rate; proceeds=gross-fee
                cb=float(p['cost_basis_inr']); cost=cb*qty/before; net=proceeds-cost
                remq=before-qty; remc=max(0,cb-cost)
                s['cash_inr']=float(s['cash_inr'])+proceeds; s['realized_pnl_inr']=float(s['realized_pnl_inr'])+net
                s['sell_executions']=int(s['sell_executions'])+1
                s['wins']=int(s['wins'])+(1 if net>0 else 0); s['losses']=int(s['losses'])+(1 if net<0 else 0)
                if not reversal: s['sell_step']=int(s.get('sell_step',0))+1
                else: s['sell_step']=0
                s['buy_step']=0
                s['last_executed_side']='SELL'; s['last_executed_qty']=qty; s['last_executed_notional_inr']=gross
                o.append({'close_time':b.close_time,'signal':'SELL','side':'SELL','sizing_rule':sizing_rule,'ladder_step':ladder_step,
                          'fraction_pct':fraction_pct,'sequence_base':'current_position','price_quote':pxq,'price_inr':pxi,'qty':qty,
                          'gross_notional_inr':gross,'fee_inr':fee,'cash_after_inr':s['cash_inr']})
                t.append({'entry_time':p['first_entry_time'],'exit_time':b.close_time,'exit_ladder_step':ladder_step,
                          'fraction_pct':fraction_pct,'exit_price_quote':pxq,'exit_price_inr':pxi,'qty':qty,
                          'allocated_cost_inr':cost,'exit_proceeds_inr':proceeds,'net_pnl_inr':net,
                          'return_pct':net/cost*100 if cost else 0})
                if remq<=1e-12 or remc<=1e-8: s['position']=None
                else:
                    p['qty']=remq; p['cost_basis_inr']=remc; p['avg_entry_price_inr']=remc/remq; p['last_sell_time']=b.close_time
                    s['position']=p

    s['last_sequence_direction']=d; s['last_signal']=g
    return o,t

def report(s,c,p,last,fx):
    px=inr(last.close,c,fx); equity,un=eq(s,px); start=float(s['starting_capital_inr'])
    pos=s.get('position'); g=s.get('last_signal'); side=s.get('last_executed_side')
    if side=='BUY': nxt=f"{frac(int(s.get('buy_step',0)))*100:.6f}% of current cash unless a SELL reverses first"
    elif side=='SELL': nxt=f"{frac(int(s.get('sell_step',0)))*100:.6f}% of current position unless a BUY reverses first"
    else: nxt="50.000000% on the first executable signal"
    L=[f"# {c['display_symbol']} {c['timeframe']} SMC Major-Swing Paper Trader — Latest",'',
       f"- Starting demo money: **₹{start:,.2f}**",f"- Current equity: **₹{equity:,.2f}**",
       f"- Cash: **₹{float(s['cash_inr']):,.2f}**",f"- Total P&L: **₹{equity-start:,.2f} ({(equity/start-1)*100 if start else 0:.2f}%)**",
       f"- Realized / unrealized: **₹{float(s['realized_pnl_inr']):,.2f} / ₹{un:,.2f}**",
       f"- Max drawdown: **{float(s['max_drawdown_pct']):.2f}%**",
       f"- Last processed candle: **{fmt(s['last_processed_close_time'])}**",f"- Next same-side size: **{nxt}**",'','## Position','']
    L += [f"- LONG qty: **{float(pos['qty']):.10f}** | cost basis: **₹{float(pos['cost_basis_inr']):,.2f}**" if pos else '_Flat. SELL while flat does not open a short._',
          '', '## Latest confirmed major swing','']
    L += [f"- **{g['signal']}** confirmed {fmt(g['confirmed_close_time'])}; pivot candle {fmt(g['pivot_open_time'])}; pivot {float(g['pivot_price']):,.6f} {c['quote_currency']}" if g else '_None recorded since initialization._',
          '', '## Updated sizing rules','',
          '- **SELL → BUY:** first BUY buys back the **same quantity as the immediately preceding executed SELL** (limited by available cash).',
          '- If another BUY follows without an intervening SELL: buy **50% of current cash**.',
          '- Next consecutive BUY: buy **12.5% of current cash**; then **6.25%, 3.125%, ...** on further BUY signals.',
          '- **BUY → SELL:** first SELL sells the **same quantity as the immediately preceding executed BUY** (limited by current holding).',
          '- If another SELL follows without an intervening BUY: sell **50% of the current position**.',
          '- Next consecutive SELL: sell **12.5% of the current position**; then **6.25%, 3.125%, ...** on further SELL signals.',
          '- The restore trade is based on **quantity**, not the old rupee value, so it reverses the actual units previously traded.',
          '- BUY = confirmed pivot low; SELL = confirmed pivot high.',
          '- Execute at confirmation-candle close, never on the older back-plotted pivot candle.',
          '- No historical trade replay on initialization.',f"- Data: **{c['source']} / {c['ticker']}**.",f"- Note: {c.get('source_note','')}",'',
          '_Paper trading only; no real orders._','']
    p['report'].parent.mkdir(parents=True,exist_ok=True); p['report'].write_text('\n'.join(L))

def main():
    c=cfgload();p=paths(c);xs=bars(c);sens=int(c['sig_sens']);fx=1.0 if c['quote_currency'].upper()=='INR' else usdinr();s=load(c,p);new=xs[-1];last=s.get('last_processed_close_time')
    if last is None:
        s['last_processed_close_time']=new.close_time; equity,un=eq(s,inr(new.close,c,fx));s['equity_peak_inr']=max(float(s['equity_peak_inr']),equity);save(s,p);addcsv(p['snapshots'],[{'close_time':new.close_time,'utc':fmt(new.close_time),'price_quote':new.close,'price_inr':inr(new.close,c,fx),'cash_inr':s['cash_inr'],'equity_inr':equity,'unrealized_pnl_inr':un,'position_qty':0,'note':'initialized_no_historical_replay'}],['close_time','utc','price_quote','price_inr','cash_inr','equity_inr','unrealized_pnl_inr','position_qty','note']);report(s,c,p,new,fx);return
    if new.close_time<=int(last):report(s,c,p,new,fx);return
    start=next((i for i,x in enumerate(xs) if x.close_time>int(last)),None); sigs=[];orders=[];trades=[]
    if start is not None:
        for i in range(start,len(xs)):
            g=signal(xs,i,sens)
            if g:sigs.append(g);o,t=trade(s,g,xs[i],c,fx);orders+=o;trades+=t
    s['last_processed_close_time']=new.close_time; equity,un=eq(s,inr(new.close,c,fx));peak=max(float(s['equity_peak_inr']),equity);s['equity_peak_inr']=peak;s['max_drawdown_pct']=max(float(s['max_drawdown_pct']),(peak-equity)/peak*100 if peak else 0);save(s,p)
    addcsv(p['signals'],sigs,['signal','confirmed_close_time','confirmed_price','pivot_open_time','pivot_price','sig_sens'])
    addcsv(p['orders'],orders,['close_time','signal','side','sizing_rule','ladder_step','fraction_pct','sequence_base','price_quote','price_inr','qty','gross_notional_inr','fee_inr','cash_after_inr'])
    addcsv(p['trades'],trades,['entry_time','exit_time','exit_ladder_step','fraction_pct','exit_price_quote','exit_price_inr','qty','allocated_cost_inr','exit_proceeds_inr','net_pnl_inr','return_pct'])
    addcsv(p['snapshots'],[{'close_time':new.close_time,'utc':fmt(new.close_time),'price_quote':new.close,'price_inr':inr(new.close,c,fx),'cash_inr':s['cash_inr'],'equity_inr':equity,'unrealized_pnl_inr':un,'position_qty':float((s.get('position') or {}).get('qty',0)),'note':''}],['close_time','utc','price_quote','price_inr','cash_inr','equity_inr','unrealized_pnl_inr','position_qty','note'])
    report(s,c,p,new,fx);print(c['display_symbol'],'signals',len(sigs),'orders',len(orders),'equity',round(equity,2))
if __name__=='__main__':main()
