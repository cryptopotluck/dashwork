import dash
import dash_core_components as dcc
import dash_html_components as html
from alpha_vantage.timeseries import TimeSeries
from pandas import DataFrame as df
ts = TimeSeries(key='G8L62BYFX5JJH9QX', retries=10, output_format='pandas', indexing_type='date')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
print(data.columns)
#data = data.loc[:, '1. open']






# app = dash.Dash()
# app.layout = html.Div(children=[
#             html.H1('Hello DASH!'),
#             html.Label('Dropdown'),
#             dcc.Dropdown(options=[{'label':'New York',
#                                    'value':'NYC'},
#                                     {'label':'Houston',
#                                    'value':'H-Town'},
#                                   ],
#                          value='H-Town'),
#
#             html.Label('Slider'),
#             dcc.Slider(min=-10, max=10, step=0.5, value=0, marks={i:i for i in range(-10,10)})
# ])
#
# if __name__ == '__main__':
#     app.run_server()