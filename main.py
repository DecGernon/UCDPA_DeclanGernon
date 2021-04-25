"""import required libraries"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy_financial as npf
import seaborn as sns

"""import, clean & sort data from CSV files"""

BTC = pd.read_csv('Binance_BTCUSD.csv', parse_dates=['date'], index_col='date', na_values='n/a')
BTC = BTC.dropna(axis=1)
print(BTC.info())
BTC = BTC.sort_index(ascending=True)

"""Selecting column which contains closing prices and displaying summary statistics"""

BTC_Close = BTC['close']
BTC_Close = pd.DataFrame(BTC_Close)
print(BTC_Close.describe())

"""Normalising the Closing Price data for comparison purposes"""

BTC_FirstPrice = BTC.close.iloc[0]
BTC_Normalised = BTC.close.div(BTC_FirstPrice).mul(100)
BTC_NormalisedDF = pd.DataFrame(BTC_Normalised)
print(BTC_NormalisedDF.head())

"""Repeat above process for next CSV file"""

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

"""Merge the above DataFrames and rename columns"""

MergedCrypto = pd.merge_ordered(BTC_NormalisedDF, ETH_NormalisedDF, on='date')
MergedCrypto = MergedCrypto.set_index('date')
MergedCrypto.rename(columns={'close_x': 'BTC Normalised Growth Rate', 'close_y': 'ETH Normalised Growth Rate'},
                    inplace=True)

CryptoClose = pd.merge_ordered(BTC_Close, ETH_Close, on='date')
CryptoClose = CryptoClose.set_index('date')
CryptoClose.rename(columns={'close_x': 'BTC Close', 'close_y': 'ETH Close'}, inplace=True)
print(CryptoClose.head())

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

"""import, clean & sort data from CSV files"""

DJI = pd.read_csv('DJI_HistoricalPrices.csv', parse_dates=['date'], index_col='date')
print(DJI.info())
DJI = DJI.sort_index(ascending=True)

"""Selecting column which contains closing prices and displaying summary statistics"""

DJI_Close = DJI['close']
DJI_Close = pd.DataFrame(DJI_Close)
print(DJI_Close.head())
print(DJI_Close.describe())

"""User defined function to automate the normalising process"""


def normalise(x):

    x_first_price = x.close.iloc[0]
    x_normalised = x.close.div(x_first_price).mul(100)
    x_normalised_df = pd.DataFrame(x_normalised)

    return x_normalised_df


DJI_NormalisedDF = normalise(DJI)
print(DJI_NormalisedDF.info())
print(DJI_NormalisedDF.head())

"""import, clean & sort data from CSV files"""

SP500 = pd.read_csv('SP500_HistoricalPrices.csv', parse_dates=['date'], index_col='date')
print(SP500.info())
SP500 = SP500.sort_index(ascending=True)

"""Selecting column which contains closing prices and displaying summary statistics"""

SP500_Close = SP500['close']
SP500_Close = pd.DataFrame(SP500_Close)
print(SP500_Close.head())
print(SP500_Close.describe())

"""Use user defined function"""

SP500_NormalisedDF = normalise(SP500)
print(SP500_NormalisedDF.info())
print(SP500_NormalisedDF.head())

"""Merge above DataFrame"""

MergedIndices = pd.merge_ordered(DJI_NormalisedDF, SP500_NormalisedDF, on='date')
MergedIndices = MergedIndices.set_index('date')
MergedIndices.rename(columns={'close_x': 'Dow Jones Normalised Growth Rate', 'close_y':
                     'SP500 Normalised Growth Rate'},
                     inplace=True)
print(MergedIndices.head())
print(MergedIndices.info())

IndicesClose = pd.merge_ordered(DJI_Close, SP500_Close, on='date')
IndicesClose = IndicesClose.set_index('date')
IndicesClose.rename(columns={'close_x': 'Dow Jones Close', 'close_y': 'SP500 Close'}, inplace=True)
print(IndicesClose.head())

"""Create merged data frames showing Closing Prices & Normalised Growth Rates for all of the assets data"""

MergedDataFrames = pd.merge_ordered(MergedIndices, MergedCrypto, on='date')
MergedDataFrames = MergedDataFrames.set_index('date')
print(MergedDataFrames.head())
MergedDataFrames = MergedDataFrames.dropna(axis=0)
print(MergedDataFrames.head())

MergedClose = pd.merge_ordered(CryptoClose, IndicesClose, on='date')
MergedClose = MergedClose.set_index('date')
print(MergedClose.head())
MergedClose = MergedClose.dropna(axis=0)
print(MergedClose.head())

"""Calculate correlation between asset prices and display using heatmap """

ClosePriceCorrelation = MergedClose.corr()
print(ClosePriceCorrelation.head())
sns.heatmap(ClosePriceCorrelation, annot=True, cmap="coolwarm").set_title('Price Correlation')

plt.style.use('bmh')
fig1, ax = plt.subplots(2, 1)
ax[0].plot(SP500_Close, label='SP500')
ax[1].plot(DJI_Close, label='DJI')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('USD')
ax[0].set_title('SP500 Index')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('USD')
ax[1].set_title('Dow Jones Index')
plt.show()

"""Show the future value of 10000 USD invested in each asset on 2017-08-17 until 2021-04-01"""

EndDateGrowthRate = MergedDataFrames.loc['2021-04-01']
print(EndDateGrowthRate)
FutureValue = 10000 * EndDateGrowthRate/100
FutureValue = FutureValue.rename(index={'Dow Jones Normalised Growth Rate': 'Dow Jones Future Value',
                                        'SP500 Normalised Growth Rate': 'SP500 Future Value',
                                        'BTC Normalised Growth Rate': 'BTC Future Value',
                                        'ETH Normalised Growth Rate': 'ETH Future Value'})
print(FutureValue)

"""Discount the future values assuming an inflation rate 2% and approx 4 year period"""

DiscountedValue = npf.pv(rate=0.02, nper=4, pmt=0, fv=-FutureValue)
print(DiscountedValue)
