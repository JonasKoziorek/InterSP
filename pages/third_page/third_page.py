from dash import html, register_page, callback
from pages.third_page.controller import display, update
from dash import Input, Output, ctx, callback


register_page(__name__, path="/lesson2")

layout = html.Div([
    html.Button('Button 1', id='btn-1'),
    html.Button('Button 2', id='btn-2'),
    html.Button('Button 3', id='btn-3'),
    html.Div(id='container'),
    html.Div(id='container-no-ctx')
])

@callback(
    Output('container-no-ctx', 'children'),
    Input('btn-1', 'n_clicks'),
    Input('btn-2', 'n_clicks'))
def update_(btn1, btn2):
    return update({btn1}, {btn2})


@callback(Output('container','children'),
            Input('btn-1', 'n_clicks'),
            Input('btn-2', 'n_clicks'),
            Input('btn-3', 'n_clicks'))
def display_(btn1, btn2, btn3):
    return display(btn1, btn2, btn3, ctx)