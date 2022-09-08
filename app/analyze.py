import yfinance as yf
import json


msft = yf.Ticker("MSFT")


f = open("/data/winnershares.json", "r")

winners = json.load(f)

read = open("/data/losershares.json", "r")

losers = json.load(read)


def analyze(stocks):
    newlist = {}
    for k, v in stocks.items():
        if k != "totalcost":
            ticker = yf.Ticker(k)
            currentprice = ticker.info["regularMarketPrice"]
            newlist[k] = (currentprice * 100) - float(stocks[k]["cost"])
            print(newlist[k])
    return newlist

def gettotal(stocks):
    total=0
    for k,v in stocks.items():
        total += v
    return total

loserdict = analyze(losers)
winnerdict = analyze(winners)

totalloser = gettotal(loserdict)
totalwinner = gettotal(winnerdict)

daywinner = ""

if totalwinner > totalloser:
    daywinner = f"Biggest gainers had a better day with {totalwinner} dollars"
else:
    daywinner = f"Biggest losers had a better day with {totalloser} dollars"
    
message = f"""
    Biggest losers yesterday had ${totalloser} dollars
    
    {loserdict}
    
    Biggest winners yesterday had ${totalwinner} dollars

    {winnerdict}
    
   {daywinner} 
"""

f = open("/data/analysis.txt", "w")
f.write(message)