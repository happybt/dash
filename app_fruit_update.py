# -*- coding: utf-8 -*-

import dash
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html

external_stylesheets = ['./templates/css/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#121111',
    'text': '#7FDBFF',
}
df = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal'],
})

fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)
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
            children='Dash: A web application framework for Python'
        ),
        dcc.Graph(
            id='example-graph',
            figure=fig,
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
