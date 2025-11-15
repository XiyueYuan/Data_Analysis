### Opening
This repo is my personal record of exploring machine learning and playing with data. All the code here reflects my learning process — experiments, notes, and ideas I’ve picked up along the way.

I also document my experiences from Kaggle, including useful tricks, good code patterns, and insights that helped me improve. Later on, I plan to connect free market APIs to this repo to explore financial data and build small projects around it.

The jupyter notebook files document everything I’ve learned along the way — kind of like a personal notebook that can also serve as a beginner-friendly handbook for anyone starting out in data analysis.

### Tools
1. Free Public API from CoinGecko 
>the root URL for CoinGecko Public Demo API is https://api.coingecko.com/api/v3/

2. Free Public API from AlphaVantage
>https://www.alphavantage.co/query

| **Parameter**               | **Purpose**                                     | **Possible Values / Examples**                                      |
| --------------------------- | ----------------------------------------------- | ------------------------------------------------------------------- |
| **function**                | Specifies which API endpoint or feature to call | e.g. `TIME_SERIES_DAILY`, `GLOBAL_QUOTE`, `RSI`, `SMA`, `OVERVIEW`  |
| **symbol**                  | The asset or security to query                  | Stocks (`AAPL`, `IBM`), Crypto (`BTC`, `ETH`), Forex (`EURUSD`)     |
| **interval**                | Time interval between data points               | For intraday data: `1min`, `5min`, `15min`, `30min`, `60min`        |
| **outputsize**              | Controls how much data is returned              | `compact` (latest 100 records) or `full` (complete historical data) |
| **datatype**                | Format of the response                          | `json` (default) or `csv`                                           |
| **market**                  | Market currency (used for crypto endpoints)     | e.g. `USD`, `EUR`, `JPY`                                            |
| **apikey**                  | Your personal API key                           | Obtain it by registering on Alpha Vantage                           |
| **series_type**             | Data type used for indicator calculation        | `close`, `open`, `high`, `low`                                      |
| **time_period**             | Window length for technical indicators          | e.g. `10`, `20`, `50` (for SMA or RSI periods)                      |
| **fastperiod / slowperiod** | Parameters for indicators like MACD             | Adjusts the indicator’s sensitivity                                 |
| **adjusted**                | Whether to include dividends/splits             | `true` or `false`                                                   |
3. Kaggle
> kaggle.com
