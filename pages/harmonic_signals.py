import dash
import dash_bootstrap_components as dbc
import dash_latex as dl
import numpy as np
import plotly.graph_objs as go

dash.register_page(__name__, "/lesson1")

A = 1
omega = 1
phi = 0
D = 0

def harmonic(t, A, omega, phi, D):
    return A * np.sin(omega*t + phi) + D

x = np.linspace(0, 2*np.pi, 200)
y = harmonic(x, A, omega, phi, D)
fig = go.Figure(
    data=[go.Scatter(x=x, y=y)],
    layout=go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    ),
)
fig.update_yaxes(range=[-6, 6])

# plot = dash.dcc.Graph(figure=fig, id="harmonic", animate=True)
plot = dash.dcc.Graph(figure=fig, id="harmonic")

layout = dash.html.Div(
    [
        dash.dcc.Markdown(
            '''
                # Harmonic Signals

                Let's introduce a function which is called harmonic signal:
                $$
                        w(t) = A \\cos(\\omega t + \\phi) + D
                $$
                Where:

                * $A$ is amplitude of a signal
                * $\\omega$ is an angular frequency of a signal
                * $\\phi$ is a phase shift of a signal
                * $D$ is vertical shift of a signal
            ''',
            mathjax=True
        ),
        plot,
        dbc.Row(
            [
                dbc.Col(dash.dcc.Markdown("$A$:", mathjax=True), lg=1),
                dbc.Col(
                    dash.dcc.Slider(-5, 5, marks=None,
                            value=1,
                            id='A-slider'
                    ),
                    lg=11
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dash.dcc.Markdown("$\\omega$:", mathjax=True), lg=1),
                dbc.Col(
                    dash.dcc.Slider(-3, 3, marks=None,
                            value=1,
                            id='omega-slider'
                    ),
                    lg=11
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dash.dcc.Markdown("$\\phi$:", mathjax=True), lg=1),
                dbc.Col(
                    dash.dcc.Slider(-np.pi, np.pi, marks=None,
                            value=0,
                            id='phi-slider'
                    ),
                    lg=11
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dash.dcc.Markdown("$D$:", mathjax=True), lg=1),
                dbc.Col(
                    dash.dcc.Slider(-3, 3, marks=None,
                            value=0,
                            id='D-slider'
                    ),
                    lg=11
                )
            ]
        ),
    ]
)

@dash.callback(
    dash.Output('harmonic', 'figure', allow_duplicate=True),
    dash.Input('A-slider', 'value'),
    prevent_initial_call=True
    )
def update_output(value):
    global A, omega, phi, D, x
    A = value
    fig = go.Figure(
        data=[go.Scatter(x=x, y=harmonic(x, A, omega, phi, D))],
        layout=go.Layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
        )
    fig.update_yaxes(range=[-A-1, A+1])
    return fig

@dash.callback(
    dash.Output('harmonic', 'figure', allow_duplicate=True),
    dash.Input('omega-slider', 'value'),
    prevent_initial_call=True
    )
def update_output(value):
    global A, omega, phi, D, x
    omega = value
    fig = go.Figure(
        data=[go.Scatter(x=x, y=harmonic(x, A, omega, phi, D))],
        layout=go.Layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
        )
    fig.update_yaxes(range=[-A-1, A+1])
    return fig

@dash.callback(
    dash.Output('harmonic', 'figure', allow_duplicate=True),
    dash.Input('phi-slider', 'value'),
    prevent_initial_call=True
    )
def update_output(value):
    global A, omega, phi, D, x
    phi = value
    fig = go.Figure(
        data=[go.Scatter(x=x, y=harmonic(x, A, omega, phi, D))],
        layout=go.Layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
        )
    fig.update_yaxes(range=[-A-1, A+1])
    return fig

@dash.callback(
    dash.Output('harmonic', 'figure', allow_duplicate=True),
    dash.Input('D-slider', 'value'),
    prevent_initial_call=True
    )
def update_output(value):
    global A, omega, phi, D, x
    D = value
    fig = go.Figure(
        data=[go.Scatter(x=x, y=harmonic(x, A, omega, phi, D))],
        layout=go.Layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
        )
    fig.update_yaxes(range=[-A-1, A+1])
    return fig