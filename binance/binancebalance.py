from binance.client import Client
import plotly.offline as pyo
import plotly.graph_objs as go
import keys
from binance.enums import *
from datetime import datetime
import certifi
import urllib3
import pandas as pd
from pycoingecko import CoinGeckoAPI
# proxies = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'http://10.10.1.10:1080'
# }

client = Client(keys.APIKey, keys.SecretKey)


from pandas import DataFrame as df




#time_res = client.get_server_time()
#time_res = time_res['serverTime']
#time_res = (time_res/1000)
#readable = datetime.fromtimestamp(int(time_res))

#Call on API for Data
# trades = client.get_account()
# http = urllib3.PoolManager(
#      cert_reqs='CERT_REQUIRED',
#      ca_certs=certifi.where())

def grab_assets():
    asset_list = ['BTC', 'LTC', 'BNB', 'WABI', 'EOS', 'MANA', 'EVX', 'CELR',
                  'ETH', 'RVN', 'FET', 'ADA', 'BAT', 'ADA', 'XRP', 'QLC',
                  'NULS', 'VIB', 'WTC', 'XRP', 'GXS']

    new_asset_list =[]


    for asset in asset_list:
        balance = client.get_asset_balance(asset=asset)
        new_asset_list.append(balance)


    asset_dataframe = df(new_asset_list)

    prices = client.get_all_tickers()

    # put price data in a DF
    prices_dataframe = df(prices)
    prices_dataframe.set_index('symbol', inplace=True)

    BTCUSDprice = prices_dataframe[prices_dataframe.index[:].str.contains('BTCUSDT')]


    asset_dataframe.set_index('asset', inplace=True)

    BTCUSDprice = float(BTCUSDprice['price']['BTCUSDT'])

    USD_value = asset_dataframe.astype(float) * BTCUSDprice
    return USD_value


def needs_work():
    #call price API to get price data
    prices = client.get_all_tickers()

    #put price data in a DF
    prices_dataframe = df(prices)
    #set index to symbol
    prices_dataframe.set_index('symbol', inplace=True)

    #filer data with the word BTC in it
    words_not_BTC = ['BTC']

    for word in words_not_BTC:
        new = prices_dataframe[prices_dataframe.index[:].str.contains(word)]

    #call just BTC USD Price
    BTCUSDprice = prices_dataframe[prices_dataframe.index[:].str.contains('BTCUSDT')]

    #grab just the price
    BTCUSDprice= BTCUSDprice['price']['BTCUSDT']

    #turn BTC price into a float
    BTCUSDprice = float(BTCUSDprice)

    #turn the list of price data into a float & multiply with BTCUSD price
    new_price = new['price'].astype(float) * BTCUSDprice

    regular_price = []

    #change format of pricechange out of scientific mode
    for pricechange in new_price:
        x = '{:.4f}'.format(float(pricechange))
        regular_price.append(x)

    #bring regular_price data into a dataframe
    regular_price_dataframe = df(regular_price)

    regular_price_dataframe.drop([6, 158, 160, 162], axis=0, inplace=True)

    prices_dataframe.drop(['BTCUSDT', 'BTCPAX', 'BTCUSDC', 'BTCUSDS'], axis=0, inplace=True)

    prices_dataframe_index = prices_dataframe.index[:]

    blank = []
    for index_b in prices_dataframe_index:
        blank.append(index_b)

    #regular_price_dataframe_finished =  pd.merge(blank, regular_price_dataframe)


    prices_dataframe.reset_index(level=0, inplace=True)

    Final_df = prices_dataframe.join(regular_price_dataframe,how='outer')

    Final_df.set_index('symbol', inplace=True)
    Final_df = Final_df.dropna(how='any')
   # Final_BTC_value = Final_df[Final_df.index[:].str.contains('BTC')]

    return Final_df

def round2():
    # call price API to get price data
    prices = client.get_all_tickers()

    # put price data in a DF
    prices_dataframe = df(prices)
    # set index to symbol
    #prices_dataframe.set_index('symbol', inplace=True)

    # filer data with the word BTC in it
    words_not_BTC = ['BTC']
    blank =[]

    # for neo in prices_dataframe:
    #     blank.append(prices_dataframe[prices_dataframe['symbol'].contains('NEO')])
    #     blank.append(x)

    prices_dataframe=prices_dataframe[prices_dataframe['symbol'].__contains__('NEO')]
    #new_BTC_list='NEO' in prices_dataframe.index.values
    return prices_dataframe

print(grab_assets())
