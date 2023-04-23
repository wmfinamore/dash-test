import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H2('Meu Programa'),
    html.Label('Cadastro de Pacientes'),
    html.H6(['Cadastro de Medicamentos', dbc.Badge(' Novo ')])
])

app.run(debug=True)
