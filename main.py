import dash
import dash_bootstrap_components as dbc

import dash_bootstrap_components as dbc

def fluid_layout(contents):
    jumbotron = dash.html.Div(
        dbc.Container(
            contents,
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
        style = {
            "height" : "100%",
        }
    )
    return jumbotron

        

navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Harmonic Signals", href="/lesson1"),
                dbc.DropdownMenuItem("Lesson 2", href="/lesson2"),
                dbc.DropdownMenuItem("Lesson 3", href="lesson3"),
            ],
            nav=True,
            in_navbar=True,
            label="Lessons",
        ),
    ],
    brand="InterSP",
    brand_href="/",
    color="primary",
    dark=True,
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], use_pages=True)
app.title = "InterSP"

app.layout = dash.html.Div([
    navbar,
    fluid_layout(
        dash.page_container
    )
])

if __name__ == '__main__':
    app.run(debug=True)
