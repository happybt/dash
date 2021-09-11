"""
控制部分回调输出不更新

在很多应用场景下，我们给某个回调函数绑定了多个Output()，
这时如果这些Output()并不是每次触发回调都需要被更新，
那么就可以根据Input()值的不同，
来配合dash.no_update作为对应Output()的返回值，
从而实现部分Output()不更新，
"""

import dash
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
import time

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    dbc.Button('按钮',
                               color='primary',
                               id='button',
                               n_clicks=0)
                )
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col('尚未触发', id='record-1'),
                    dbc.Col('尚未触发', id='record-2'),
                    dbc.Col('尚未触发', id='record-n'),
                ]
            )
        ]
    )
)


@app.callback(
    [Output('record-1', 'children'),
     Output('record-2', 'children'),
     Output('record-n', 'children')
     ],
    Input('button', 'n_clicks'),
    prevent_initial_call=True
)
def record_click_event(n_clicks):
    if n_clicks == 1:
        return (
            '第一次点击: {}'.format(time.strftime('%H:%M:%S', time.localtime(time.time()))),
            dash.no_update,
            dash.no_update
        )
    elif n_clicks == 2:
        return (
            dash.no_update,
            '第二次点击: {}'.format(time.strftime('%H:%M:%S', time.localtime(time.time()))),
            dash.no_update
        )
    elif n_clicks >= 3:
        return (
            dash.no_update,
            dash.no_update,
            '第3次及以上的点击: {}'.format(time.strftime('%H:%M:%S', time.localtime(time.time())))
        )


"""
可以观察到，我们根据n_clicks数值的不同，在对应各个Output()返回值中对符合条件的部件进行更新，
其他的都用dash.no_update来代替，从而实现了局部更新，非常实用且简单。
"""
if __name__ == '__main__':
    app.run_server(debug=True)
