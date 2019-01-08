import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import quandl as ql


api_key = '4aFKuHcqTM1Wuquxra6L'

data = ql.get("LBMA/GOLD", authtoken="4aFKuHcqTM1Wuquxra6L")

data = data.dropna()

#data = data.index

#print(data)
trace0 = go.Scatter(x=data.index,
                    y=data['USD (AM)'],
                    mode='lines',
                    name='open')

trace1 = go.Scatter(x=data.index,
                    y=data['USD (PM)'],
                    mode='lines',
                    name='close',
                    fillcolor='#F72F2D'
                    )


#bring into a list
data = [trace0,trace1]

layout = go.Layout(title='Line Charts')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatterpotluck.html')


