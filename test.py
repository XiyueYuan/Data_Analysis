import requests
import pandas as pd
import time

url = 'https://www.alphavantage.co/query'
API_key = '15ZXDWG4HOKVSBRR'
sp500_symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "META", "TSLA",
                 "BRK.B", "JPM", "V", "JNJ", "PG", "XOM", "MA", "HD", "LLY",
                 "UNH", "ABBV", "KO", "PEP", "CVX", "NFLX", "ORCL", "NKE"]

def get_market_cap(symbol):
    url = "https://www.alphavantage.co/query"
    params = {"function": "OVERVIEW", "symbol": symbol, "apikey": API_key}
    r = requests.get(url, params=params)
    data = r.json()
    cap = data.get("MarketCapitalization")
    return {"symbol": symbol, "marketcap": int(cap) if cap else None}

caps = []
for sym in sp500_symbols:
    print(f"Fetching {sym}...")
    caps.append(get_market_cap(sym))
print(caps)