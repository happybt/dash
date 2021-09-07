import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    external_stylesheets=['css/bootstrap.min.css'],
)

app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col('第一行'),
            style={
                'background-color': 'lightgreen',
            },
        ),
        dbc.Row(
            [
                dbc.Col('第二行第一列', width=6, style={'background-color': 'lightblue'}),
                dbc.Col(
                    dbc.Row(
                        [
                            dbc.Col('嵌套1', width=6, style={'background-color': 'Moccasin'}),
                            dbc.Col('嵌套2', width=3, style={'background-color': 'lightskyblue'}),
                            dbc.Col('嵌套3', width=3, style={'background-color': 'Moccasin'}),
                        ],
                    ),
                    width=6, style={'background-color': 'lightskyblue'}),
            ],
        ),
        dbc.Row(
            [
                dbc.Col('第三行第一列', width=2, style={'background-color': 'HotPink'}),
                dbc.Col('第三行第二列', width=10, style={'background-color': 'IndianRed'}),
            ],
        ),
        dbc.Row(
            [
                dbc.Col('第四行第一列', width=2, style={'background-color': 'HotPink'}),
                dbc.Col('第四行第二列', width=2, style={'background-color': 'IndianRed'}),
                dbc.Col('第四行第三列', width=2, style={'background-color': 'HotPink'}),
            ],
        ),
        dbc.Row(
            [
                dbc.Col('第五行第一列', width=2, style={'background-color': 'LightSteelBlue'}),
                dbc.Col('第五行第二列', width=11, style={'background-color': 'MistyRose'}),
            ],

        ),
    ],
)

if __name__ == '__main__':
    app.run_server()
