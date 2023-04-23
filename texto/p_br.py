import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    id = 'bloco1',
    children = [
        html.H1('Meu Programa'),
        html.Label('Utilizando Dash'),
        html.P('Teste de parágrafo'),
        html.Br(),
        html.P('Teste de parágrafo'),
    ]
)

app.run(debug=True)
