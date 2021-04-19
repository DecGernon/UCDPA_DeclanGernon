import pandas as pd
import matplotlib.pyplot as plt

BTC = pd.read_csv('Binance_BTCUSD.csv', parse_dates=['date'], index_col='date')
BTC = BTC.sort_index(ascending=True)
BTC_Close = BTC['close']
BTC_Close = pd.DataFrame(BTC_Close)

ETH = pd.read_csv('Binance_ETHUSD.csv', parse_dates=['date'], index_col='date')
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

DJI = pd.read_csv('DJI_HistoricalPrices.csv', parse_dates=['Date'])
SP500 = pd.read_csv('SP500_HistoricalPrices.csv', parse_dates=['Date'])
