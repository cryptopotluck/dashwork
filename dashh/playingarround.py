from alpha_vantage.timeseries import TimeSeries
from pandas import DataFrame as df
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
ts = TimeSeries(key='G8L62BYFX5JJH9QX', retries=10, output_format='pandas', indexing_type='date')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
#print(data.head())

app = dash.Dash()

features = data.columns

colors = {'background': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis',
                     options=[{'label': i, 'value': i} for i in features],
                     value='displacement')
    ], style={'width': '48%', 'display': 'inline-block'}),
    html.Div([
        dcc.Dropdown(id='yaxis',
                     options=[{'label': i, 'value': i} for i in features],
                     value='1. open'
                     )
    ], style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id='feature-graphic')

], style={'backgroundColor': colors['background'], 'padding': 10})


@app.callback(Output('feature-graphic', 'figure'), [Input('xaxis', 'value'),
                                                    Input('yaxis', 'value')])
def update_graph(x_axis_name, y_axis_name):
    return {'data': [go.Scatter(x=df[x_axis_name],
                                y=df[y_axis_name],
                                text=df['name'],
                                mode='markers',
                                marker={'size': 15,
                                        'opacity':0.5,
                                        'line':{'width':0.5, 'color':'black'}}
                                )]

        , 'layout': go.Layout(title='My Dashboard for MPG', xaxis={'title': x_axis_name},
                              yaxis={'title': y_axis_name},
                              hovermode='closest')

            }


if __name__ == '__main__':
    app.run_server()

