import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(
    __name__,
    external_stylesheets=['css/bootstrap.min.css'],
    # 忽略回调匹配错误
    suppress_callback_exceptions=True
)

app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Input(id='input1'),
                    width=4
                ),
                dbc.Col(
                    dbc.Label(id='output1'),
                    width=4
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Input(id='input2'),
                    width=4
                ),
                dbc.Col(
                    dbc.Label(id='output2'),
                    width=4
                )
            ]
        )
    ]
)


@app.callback(
    Output('output1', 'children'),
    Input('input1', 'value'),
    # 阻止初始回调的参数
    prevent_initial_call=True
)
def callback1(value):
    if value:
        # 此处故意不处理默认状态下输入值为None的情况
        return int(value) ** 2


@app.callback(
    # 此处故意写错为不存在的ID
    Output('output2', 'children'),
    Input('input2', 'value')
)
def callback2(value):
    if value:
        return int(value) ** 0.5


if __name__ == '__main__':
    app.run_server(debug=True)
