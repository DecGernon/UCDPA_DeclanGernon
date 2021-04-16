import pandas as pd
BTC = pd.read_csv('Binance_BTCUSD.csv', parse_dates=['date'], index_col='date')
print(BTC.head())
ETH = pd.read_csv('Binance_ETHUSD.csv', parse_dates=['date'], index_col='date')
print(ETH.head())
DJI = pd.read_csv('DJI_HistoricalPrices.csv', parse_dates=['Date'])
print(DJI.head())
SP500 = pd.read_csv('SP500_HistoricalPrices.csv', parse_dates=['Date'])
print(SP500.head())

data = BTC['close'].describe()
print(data)
