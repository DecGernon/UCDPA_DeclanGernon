import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

BTC = pd.read_csv('Binance_BTCUSD.csv', parse_dates=['date'], index_col='date')
print(BTC.info())
BTC = BTC.sort_index(ascending=True)
BTC_Close = BTC['close']
BTC_Close = pd.DataFrame(BTC_Close)
print(BTC_Close.describe())
BTC_FirstPrice = BTC.close.iloc[0]
BTC_Normalised = BTC.close.div(BTC_FirstPrice).mul(100)
BTC_NormalisedDF = pd.DataFrame(BTC_Normalised)
print(BTC_NormalisedDF.head())


ETH = pd.read_csv('Binance_ETHUSD.csv', parse_dates=['date'], index_col='date', low_memory=False)
print(ETH.info())
ETH = ETH.sort_index(ascending=True)
ETH_Close = ETH['close']
ETH_Close = pd.DataFrame(ETH_Close)
print(ETH_Close.describe())
ETH_FirstPrice = ETH.close.iloc[0]
ETH_Normalised = ETH.close.div(ETH_FirstPrice).mul(100)
ETH_NormalisedDF = pd.DataFrame(ETH_Normalised)
print(ETH_NormalisedDF.head())
print(ETH_NormalisedDF.info())

MergedCrypto = pd.merge_ordered(BTC_NormalisedDF, ETH_NormalisedDF, on='date')
MergedCrypto = MergedCrypto.set_index('date')
MergedCrypto.rename(columns={'close_x': 'BTC Normalised Daily Returns', 'close_y': 'ETH Normalised Daily Returns'},
                    inplace=True)
print(MergedCrypto.head())
MergedCrypto.plot(title='Normalised Crypto Returns')
plt.show()


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
print(DJI_Close.describe())

DJI_FirstPrice = DJI.Close.iloc[0]
DJI_Normalised = DJI.Close.div(DJI_FirstPrice).mul(100)
DJI_Normalised.plot()
plt.show()

SP500 = pd.read_csv('SP500_HistoricalPrices.csv', parse_dates=['Date'], index_col='Date')
print(SP500.info())
SP500 = SP500.sort_index(ascending=True)
SP500_Close = SP500['Close']
SP500_Close = pd.DataFrame(SP500_Close)
print(SP500_Close.head())
print(SP500_Close.describe())

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

