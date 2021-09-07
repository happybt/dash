import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    external_stylesheets=['css/bootstrap.min.css'],
)

app.layout = html.Div(
    [
        # fluid默认用来False
        dbc.Container(
            [
                dcc.Dropdown(),
                '测试_False',
                dcc.Dropdown(),
            ],
        ),
        html.Hr(),  # 水平分割线

        # fluid设置为True
        dbc.Container(
            [
                dcc.Dropdown(),
                '测试_True',
                dcc.Dropdown(),
            ],
            fluid=True,
        ),
    ],
)

if __name__ == '__main__':
    app.run_server()
