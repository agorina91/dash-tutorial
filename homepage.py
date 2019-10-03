import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


def Homepage():

    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),

        ],
        brand="Demo",
        brand_href="/home",
        sticky="top",
        color='primary'
    )

    body = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2("Heading"),
                            html.P(
                                """\
    Donec id elit non mi porta gravida at eget metus.
    Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
    nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
    malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non
    mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
    commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
    amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed
    odio dui."""
                            ),
                            dbc.Button("View details", color="secondary"),
                        ],
                        md=4,
                    ),
                    dbc.Col(
                        [
                            html.H2("Graph"),
                            dcc.Graph(
                                figure={
                                    "data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                            ),
                        ]
                    ),
                ]
            )
        ],
        className="mt-4",
    )

    return html.Div([navbar, body])
