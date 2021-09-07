import dash
import dash_bootstrap_components as dbc


external_stylesheets = ['https://cdn.staticfile.org/twitter-bootstrap/4.5.2/css/bootstrap.min.css']
app = dash.Dash(
    __name__,
    # 从国内可顺畅访问的cdn获取所需的原生bootstrap对应css
    # external_stylesheets=external_stylesheets
    
    # 直接填写assets下css文件路径+文件名
    external_stylesheets=['css/bootstrap.min.css'])

app.layout = dbc.Alert(
    ' 你好， dash_bootstrap_components'
)

if __name__ == "__main__":
    app.run_server()
