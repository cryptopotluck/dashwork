from binance.client import Client
import plotly.offline as pyo
import plotly.graph_objs as go
import keys

from datetime import datetime

from pandas import DataFrame as df


client = Client(keys.APIKey, keys.SecretKey)
def create_coin_dataframe():
    #Call on API for Data
    candles = client.get_klines(symbol='LTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR)
    #put data in a dataframe
    candles_data_frame2 = df(candles)

    #Parse dataframe for only the date in milliseconds
    candles_data_frame = candles_data_frame2[0]

    #create empty list
    finaldate = []

    #create a loop for each date
    for time2 in candles_data_frame.unique():
        #turn date into something thats actually readable
        readable = datetime.fromtimestamp(int(time2/1000))
        #add date to empty list
        finaldate.append(readable)



    #candles=(candles[0][0]/1000)
    #readable = datetime.fromtimestamp(int(candles))

    #call on origional list & remove junk
    candles_data_frame2.pop(0)
    candles_data_frame2.pop(11)

    #put the new dates in a dataframe
    datedataframe = df(finaldate)


    #rename date dataframe to have column date
    datedataframe.columns = ['date']
    #bring the two dataframes together
    finaldataframe= datedataframe.join(candles_data_frame2)
    #set date column as the index
    finaldataframe.set_index('date', inplace=True)
    #rename the blank columns to match what they represent
    finaldataframe.columns = ['open', 'high', 'low', 'close', 'volume', 'close_time', 'asset_volume', 'trade_number', 'taker_buy_base', 'taker_buy_quote']
    #finaldataframe['date'] = pd.to_datetime(finaldataframe['date'])
    return finaldataframe

table_trace1 = go.Table(
    domain=dict(x=[0, 0.5],
                y=[0, 1.0]),
    columnwidth = [30] + [33, 35, 33],
    columnorder=[0, 1, 2, 3, 4],
    header = dict(height = 50,
                  values = [['<b>Date</b>'], ['<b>Open Price</b>'], ['<b>High Price</b>'],
                            ['<b>Low Price</b>'], ['<b>Close Price</b>'],
                            ['<b>Volume</b>'], ['<b>Number<br>of<br>Trades</b>']],
                  line = dict(color='rgb(50, 50, 50)'),
                  align = ['left'] * 5,
                  font = dict(color=['rgb(45, 45, 45)'] * 5, size=14),
                  fill = dict(color='rgb(135, 193, 238)')),

    cells = dict(values = [create_coin_dataframe().index[:], create_coin_dataframe()['open'],create_coin_dataframe()['high'], create_coin_dataframe()['low'], create_coin_dataframe()['close'], create_coin_dataframe()['volume'], create_coin_dataframe()['trade_number']],
                 line = dict(color='#106784'),
                 align = ['left'] * 5,
                 font = dict(color=['rgb(40, 40, 40)'] * 5, size=12),
                 format = [None] + [", .2f"] * 2 + [',.4f'],
                 prefix = [None] * 2 + ['$', u'\u20BF'],
                 suffix=[None] * 4,
                 height = 27,
                 fill = dict(color=['rgb(135, 193, 238)', 'rgba(128, 222, 249, 0.65)']))
)
trace4 = go.Ohlc(x=create_coin_dataframe().index[:],
                 open=create_coin_dataframe()['open'],
                 high=create_coin_dataframe()['high'],
                 low=create_coin_dataframe()['low'],
                 close=create_coin_dataframe()['close']

)


trace1=go.Scatter(
    x=create_coin_dataframe().index[:],
    y=create_coin_dataframe()['open'],
    xaxis='x1',
    yaxis='y1',
    mode='lines',
    line=dict(width=2, color='#9748a1'),
    name='Open Price'
)

trace2=go.Scatter(
    x=create_coin_dataframe().index[:],
    y=create_coin_dataframe()['volume'],
    xaxis='x2',
    yaxis='y2',
    mode='lines',
    line=dict(width=2, color='#b04553'),
    name='Volume'
)

trace3=go.Scatter(
    x=create_coin_dataframe().index[:],
    y=create_coin_dataframe()['trade_number'],
    xaxis='x3',
    yaxis='y3',
    mode='lines',
    line=dict(width=2, color='#af7bbd'),
    name='# of Trades'
)

data = [trace4]

axis=dict(
    showline=True,
    zeroline=False,
    showgrid=True,
    mirror=True,
    ticklen=4,
    gridcolor='#ffffff',
    tickfont=dict(size=10)
)

layout1 = dict(
    width=950,
    height=800,
    autosize=False,
    title='Trade data',
    margin = dict(t=100),
    showlegend=False,
    xaxis1=dict(axis, **dict(domain=[0.55, 1], anchor='y1', showticklabels=False)),
    xaxis2=dict(axis, **dict(domain=[0.55, 1], anchor='y2', showticklabels=False)),
    xaxis3=dict(axis, **dict(domain=[0.55, 1], anchor='y3')),
    yaxis1=dict(axis, **dict(domain=[0.66, 1.0], anchor='x1', hoverformat='.2f')),
    yaxis2=dict(axis, **dict(domain=[0.3 + 0.03, 0.63], anchor='x2', tickprefix='$', hoverformat='.2f')),
    yaxis3=dict(axis, **dict(domain=[0.0, 0.3], anchor='x3', tickprefix=u'\u20BF', hoverformat='.2f')),
    plot_bgcolor='rgba(128, 222, 249, 0.65)'
)

fig1 = dict(data=[table_trace1, trace4, trace2, trace3], layout=layout1)
pyo.plot(fig1, filename='table-right-aligned-plots.html')


#print(finaldataframe)