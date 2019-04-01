import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#%matplotlib inline

import pandas_datareader
import datetime
import plotly.offline as pyo
import plotly.graph_objs as go

import pandas_datareader.data as web

start= datetime.datetime(2012,1,1)
end = datetime.datetime(2017,1,1)

tesla = web.DataReader('FB', 'yahoo', start, end)
ford = web.DataReader('AAPL', 'yahoo', start, end)
gm = web.DataReader('TWTR', 'yahoo', start, end)

trace = go.Ohlc(x=tesla.index[:],
                open=tesla['Open'],
                high=tesla['High'],
                low=tesla['Low'],
                close=tesla['Close'],
                name='FB',
                increasing=dict(line=dict(color='#545e49')),
                decreasing=dict(line=dict(color='red')))

trace2 = go.Ohlc(x=ford.index[:],
                open=ford['Open'],
                high=ford['High'],
                low=ford['Low'],
                close=ford['Close'],
                name='AAPL',
                increasing=dict(line=dict(color='#17BECF')),
                decreasing=dict(line=dict(color='red')))


trace3 = go.Ohlc(x=gm.index[:],
                open=gm['Open'],
                high=gm['High'],
                low=gm['Low'],
                close=gm['Close'],
                name='TWTR',
                increasing=dict(line=dict(color='#17BECF')),
                decreasing=dict(line=dict(color='red')))

data = [trace, trace2, trace3]
layout = {
    'title': 'Facebppl vs Apple vs Twitter',
    'yaxis': {'title': 'Price per stock'},

}
fig = dict(data=data, layout=layout)
pyo.plot(fig, filename='aapl-recession-candlestick.html')

