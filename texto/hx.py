import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    id = 'bloco1',
    children = [
        html.H1('Meu Programa'),
        html.H2('Meu Programa'),
        html.H3('Meu Programa'),
        html.H4('Meu Programa'),
        html.H5('Meu Programa'),
        html.H6('Meu Programa'),
    ]
)

app.run(debug=True)
