import dash
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

fig = px.scatter(x=range(10), y=range(10), height=400)
fig.update_layout(clickmode='event+select')  # 设置点击模式


app.layout = html.Div(
    [
        html.H1('标题1'),
        html.H1('标题2'),
        html.P(['测试', html.Br(), '测试']),
        html.Table(
            html.Tr(
                [
                    html.Td('第一列'),
                    html.Td('第二列'),
                ],
            ),
        ),
        html.H1('嵌入plotly图表'),
        dcc.Graph(figure=fig),

        html.H1('根据省名称查询省会城市'),
        html.Br(),
        dcc.Dropdown(
            id='province',
            options=[
                {'label': '四川省', 'value': '四川省'},
                {'label': '陕西省', 'value': '陕西省'},
                {'label': '广东省', 'value': '广东省'},
            ],
            value='四川省'
        ),
        html.P(id='city'),
    ],
)

province2city_dict = {
    '四川省': '成都市',
    '陕西省': '西安市',
    '广东省': '广州市',
}


@app.callback(Output('city', 'children'),
              Input('province', 'value'))
def province2city(province):

    return province2city_dict['province']


if __name__ == '__main__':
    app.run_server(debug=True)
