from binance.client import Client
import plotly.offline as pyo
import plotly.graph_objs as go
import keys

from datetime import datetime

from pandas import DataFrame as df


client = Client(keys.APIKey, keys.SecretKey)

#Call on API for Data
candles = client.get_klines(symbol='LTCUSDT', interval=Client.KLINE_INTERVAL_1DAY)
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

#last_dataframe = datedataframe.concat(candles_data_frame2)
#finaldataframe['open'].plot(figsize=(16,6))
#print(finaldataframe.head())


x_values= finaldataframe.index[:]
y_values= finaldataframe['open']
x_volume = finaldataframe['low']

trace = go.Scatter(x=x_values, y=y_values, mode='lines', name='close')

# x_values2= finaldataframe.index[:]
# y_values2= finaldataframe['asset_volume']
#
#
#
# trace2 = go.Scatter(x=x_values2, y=y_values2, mode='lines', name='open')

volume = go.Histogram(x=x_volume)

layout = go.Layout(title='BNB/USDT Number of Trades - Crypto Potluck Research')

data = [trace]

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)