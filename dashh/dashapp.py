import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
            html.H1('Hello DASH!'),
            html.Div('Dash: Web Dashboards with Python'),
            dcc.Graph(id='example',
                      figure={'data':[
                            {'x':[1,2,3], 'y':[4,1,3], 'type':'bar','name':'SF'},
                            {'x':[1,2,3], 'y':[5,3,6], 'type':'bar','name':'NYC'}
                      ],
                                'layout':{
                                    'title':'BAR PlOTS!'
                                }})
])

if __name__ == '__main__':
    app.run_server()