import dash
from dash import html, dcc

app = dash.Dash()

app.layout = html.Div()

@app.callback()
def func1(*arg):
    return f'Saída: {arg}'

app.run()
