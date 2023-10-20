from dash import register_page
import dash
import dash_bootstrap_components as dbc

register_page(__name__, path="/")

layout = [
        dash.html.H1("Interactive Signal Procesing", className="display-3"),
        dash.html.P(
            "Dear students, here you will learn about signal processing interactively.",
            className="lead",
        ),
        dash.html.Hr(className="my-2"),
        dash.html.P(
            "Our first lesson will be about harmonic signals"
        ),
        dash.html.P(
            dbc.Button("First lesson", color="primary", href="/lesson1"), className="lead"
        ),
        dash.html.P(
            dbc.Button("Second lesson", color="primary", href="/lesson2"), className="lead"
        ),
    ]