# -*- coding: utf-8 -*-
import dash
# import dash_html_components as html
# import dash_core_components as dcc
from dash import dcc
from dash import html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
}

# app.layout = html.H1('第一个给Dash应用')
app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(
            children='Hello Dash',
            style={
                'textAlign': 'center',
                'color': colors['text'],
            }
        ),

        html.Div(
            style={
                'textAlign': 'center',
                'color': colors['text'],
            },
            children='''
            Dash: A web application framework for Python.
            '''
        ),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 3, 4], 'type': 'bar', 'name': u'Montreal'},
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'title': 'Dash Data Visualization',
                }
            }
        )

    ]
)
if __name__ == '__main__':
    app.run_server(debug=True)
