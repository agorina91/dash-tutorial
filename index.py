import pandas as pd

import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import pickle
import sys
from time import sleep
from app import build_bar, bar_page


df = pd.read_csv('insta_yearly.csv')
df.set_index(df.iloc[:, 0], drop=True, inplace=True)
df = df.iloc[:, 1:]

with open('dropdown', 'rb') as fp:
    options = pickle.load(fp)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.config.suppress_callback_exceptions = True


def index_page():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Bar Graph", href="/bar")),

        ],
        brand="Home",
        brand_href="#",
        sticky="top",
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


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/bar':
        return bar_page()
    else:
        return index_page()


@app.callback(
    Output('output', 'children'),
    [Input('year-dropdown', 'value')])
def update_graph(year):

    return build_bar(year=int(year))


if __name__ == '__main__':
    app.run_server(debug=True)
