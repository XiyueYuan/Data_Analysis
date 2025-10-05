### Knowledge

##### API
1. The Structure of an API URL
```mathematica
Root URL + EndPoint + Query Parameters
```
Example: 
`https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currecncy=usd&days=30`

Part | Meaning | Example
---| ---| ---|
Root URL | The main base of the API | https://api.coingecko.com/api/v3/
Endpoint | The specific kind of data you want | coins/bitcoin/market_chart
Query Parameters | The options you specify | vs_currency=usd&days=30

2. Endpoint Table for easy use

| Purpose | Endpoint | Example | Description |
|----------|-----------|----------|--------------|
| List all supported coins | `/coins/list` | [coins/list](https://api.coingecko.com/api/v3/coins/list) | Returns every coin ID, symbol, and name |
| Get details for one coin | `/coins/{id}` | [coins/bitcoin](https://api.coingecko.com/api/v3/coins/bitcoin) | Market cap, supply, description, links |
| Get market data for coins | `/coins/markets` | `/coins/markets?vs_currency=usd&ids=bitcoin,ethereum` | Current price, market cap, volume, and change |
| Historical price chart | `/coins/{id}/market_chart` | `/coins/bitcoin/market_chart?vs_currency=usd&days=30` | Price, market cap, and volume for the last N days |
| Historical data for one date | `/coins/{id}/history` | `/coins/bitcoin/history?date=01-01-2023&localization=false` | Price info on a specific date |
| Supported currencies | `/simple/supported_vs_currencies` | [supported_vs_currencies](https://api.coingecko.com/api/v3/simple/supported_vs_currencies) | Lists all supported fiat currencies (usd, eur, cny, etc.) |
