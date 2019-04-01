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

client = Client(keys.APIKey, keys.SecretKey)



from pandas import DataFrame as df


def grab_assets_BTC_value():
    cg = CoinGeckoAPI()

    assets = ['ethereum', 'ripple', 'eos', 'litecoin', 'bitcoin-cash', 'binancecoin', 'cardano', 'stellar', 'tron', 'bitcoin-cash-sv', 'monero', 'iota', 'dash']

    # 'holotoken', 'true-usd', 'omisego', 'qtum', 'lisk', 'decred', 'chainlink', '0x',
    # 'bitcoin-gold', 'zilliqa', 'bitcoin-diamond', 'augur', 'icon',
    # 'usd-coin', 'ethereum', 'dogecoin', 'tezos', 'vechain', 'waves', 'ontology', 'zcash', 'ripple', 'eos',
    # 'litecoin', 'bitcoin-cash', 'tether', 'stellar', 'tron', 'binancecoin', 'bitcoin-cash-sv', 'cardano',
    # 'monero', 'iota', 'dash', 'maker', 'neo', 'ethereum-classic', 'nem'

    btc_asstet_list = []

    for btcvalue in assets:
        simple_price = cg.get_price(ids=btcvalue, vs_currencies='btc')
        btc_asstet_list.append(simple_price)
        return btc_asstet_list

    blank_price_list = []

    for price in btc_asstet_list:
        blank_price_list.append(price)
        return blank_price_list

    return blank_price_list

print(grab_assets_BTC_value())