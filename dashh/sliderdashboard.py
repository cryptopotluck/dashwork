import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go


app = dash.Dash()

app.layout = html.Div([
    html.Div([dcc.RangeSlider(
        marks={i: '{}'.format(i) for i in range(-10, 50)},
        min=-10,
        max=50,
        value=[-3, 4],
        id='num'
    ),
        ], style={'width': '48%', 'display': 'inline-block'}),
    html.H1(id='results', style={'margin':20, 'justify-content': 'center'})
])

@app.callback(Output(component_id='results', component_property='children'), [Input(component_id='num', component_property='value')])
def update_output_div(input_value):
    return "You multiplied {}".format(input_value), " and received: {}".format(input_value[0] * input_value[1])


if __name__ == '__main__':
    app.run_server()