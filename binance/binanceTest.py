from binance.client import Client

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import dateparser
import pytz
from datetime import datetime
import keys
import pandas as pd
import json

client = Client(keys.APIKey, keys.SecretKey)

def date_to_milliseconds(date_str):
    epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
    # parse our date string
    d = dateparser.parse(date_str)
    # if the date is not timezone aware apply UTC timezone
    if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
        d = d.replace(tzinfo=pytz.utc)

    # return the difference in time
    return int((d - epoch).total_seconds() * 1000.0)

def interval_to_milliseconds(interval):
    """Convert a Binance interval string to milliseconds
    :param interval: Binance interval string 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
    :type interval: str
    :return:
         None if unit not one of m, h, d or w
         None if string not in correct format
         int value of interval in milliseconds
    """
    ms = None
    seconds_per_unit = {
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
        "w": 7 * 24 * 60 * 60
    }

    unit = interval[-1]
    if unit in seconds_per_unit:
        try:
            ms = int(interval[:-1]) * seconds_per_unit[unit] * 1000
        except ValueError:
            pass
    return ms


address = client.get_deposit_address(asset='BTC')
klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")
client = Client(keys.APIKey, keys.SecretKey)
candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
trades = client.get_historical_trades(symbol='BNBBTC')
# fetch 1 minute klines for the last day up until now
#klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")

df = pd.DataFrame(candles)
#print(df)

df.columns = ['Open_time','Open','High','Low','Close','Volume','Close_time','Q_asset_Volume','Num_of_treades','Taker_buy_base','Taker_buy_quote','Ignore']

df.Open_time.astype(int)

#info = client.get_account()


#print(info)

#print(address)
print(df.iloc[1])

#trace1 = go.Bar(x=df['NOC'],
                #y=df['Gold'],
                #name='Gold',
                #marker={'color': '#FFD700'})


