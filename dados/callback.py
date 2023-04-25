import dash
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Meu Programa'),
    html.Label('Cadastro de Alunos'),
    html.Div([
        'Nome: ',
        dcc.Input(id = 'entrada_01',
                  value = '',
                  type = 'text')]),
    html.P(),
    html.Div(id = 'saida_01')
])

@app.callback(Output(component_id = 'saida_01', component_property = 'children'),
              [Input(component_id = 'entrada_01', component_property = 'value')])
def mostra_nome(e):
    return f'Bem vindo(a) {e} !!!'

app.run(debug=True)
