from binance3charts import create_coin_dataframe

import datetime
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

programmers = []

trace = go.Heatmap(z=[[create_coin_dataframe()['volume']],[create_coin_dataframe()['asset_volume']],[create_coin_dataframe()['trade_number']]],
                   x=['volume','asset_volume', 'trade_number'],
                   y=[create_coin_dataframe().index[:]])

# data = [
#     go.Heatmap(
#         z=z,
#         x=create_coin_dataframe().index[:],
#         y=programmers,
#         colorscale='Viridis',
#     )
# ]

# layout = go.Layout(
#     title='GitHub commits per day',
#     xaxis = dict(ticks='', nticks=36),
#     yaxis = dict(ticks='' )

data = [trace]

fig = go.Figure(data=data)
pyo.plot(fig, filename='datetime-heatmap.html')