import pandas as pd
import matplotlib.pyplot as plt

BTC = pd.read_csv('Binance_BTCUSD.csv', parse_dates=['date'], index_col='date')
print(BTC.info())
BTC = BTC.sort_index(ascending=True)
BTC_Close = BTC['close']
BTC_Close = pd.DataFrame(BTC_Close)

ETH = pd.read_csv('Binance_ETHUSD.csv', parse_dates=['date'], index_col='date')
print(ETH.info())
ETH = ETH.sort_index(ascending=True)
ETH_Close = ETH['close']
ETH_Close = pd.DataFrame(ETH_Close)

plt.style.use('bmh')
fig, ax = plt.subplots(2, 1)
ax[0].plot(BTC_Close, label='BTC')
ax[1].plot(ETH_Close, label='ETH')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('USD')
ax[0].set_title('BTC/USD')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('USD')
ax[1].set_title('ETH/USD')
plt.show()

DJI = pd.read_csv('DJI_HistoricalPrices.csv', parse_dates=['Date'], index_col='Date')
print(DJI.info())
DJI = DJI.sort_index(ascending=True)
DJI_Close = DJI['Close']
DJI_Close = pd.DataFrame(DJI_Close)
print(DJI_Close.head())

SP500 = pd.read_csv('SP500_HistoricalPrices.csv', parse_dates=['Date'], index_col='Date')
print(SP500.info())
SP500 = SP500.sort_index(ascending=True)
SP500_Close = SP500['Close']
SP500_Close = pd.DataFrame(SP500_Close)
print(SP500_Close.head())

plt.style.use('bmh')
fig, ax = plt.subplots(2, 1)
ax[0].plot(SP500_Close, label='SP500')
ax[1].plot(DJI_Close, label='DJI')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('USD')
ax[0].set_title('SP500 Index')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('USD')
ax[1].set_title('Dow Jones Index')
plt.show()