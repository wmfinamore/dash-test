import dash
from dash import html

app = dash.Dash()

app.layout = html.Div('Olá Mundo!!!')

if __name__ == '__main__':
    app.run_server(debug = True)
