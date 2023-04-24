import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    id = 'bloco1',
    children = [
        html.H1('Meu Programa'),
        html.Label('Cadastro de Aluno'),
        html.Br(),
        dcc.Input(value = 'Digite o nome completo: ',
                  type = 'text',
                  id = 'entrada_01')
    ]
)

app.run(debug=True)

