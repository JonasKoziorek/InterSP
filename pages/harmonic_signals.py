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
        xaxis={
            "range" : (-6, 6)
        }
    ),
    )
fig.update_xaxes(range=[-6, 6])

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
        dash.dcc.Slider(-5, 5, 0.01,
                value=1,
                id='A-slider'
        ),
    ]
)

fig = go.Figure(
    data=[go.Scatter(x=x, y=y)],
    layout=go.Layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
    )
@dash.callback(
    dash.Output('harmonic', 'figure'),
    dash.Input('A-slider', 'value'))
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
    return fig
