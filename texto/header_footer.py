import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    id = 'bloco1',
    children = [
        html.H1('Meu Programa'),
        html.Label('Utilizando Dash'),
        html.Header('Cabeçalho de alguma seção'),
        html.Footer('Rodapé para alguma seção')
    ]
)

app.run(debug=True)
