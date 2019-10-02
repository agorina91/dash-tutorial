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

df = pd.read_csv('insta_yearly.csv')
df.set_index(df.iloc[:, 0], drop=True, inplace=True)
df = df.iloc[:, 1:]

with open('dropdown', 'rb') as fp:
    options = pickle.load(fp)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])


dropdown = html.Div([dcc.Dropdown(id='year-dropdown',
                                  options=options,
                                  value='2018')],
                    style={'width': '50vh',
                           'margin': 'auto'}
                    )


bar_nav = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Home",
    brand_href="/home",
    color="primary",
    dark=True,
)


def build_bar(year=2018):

    labels = list(df.columns)
    values = list(df.loc[year].values)
    print(labels, sys.stdout)
    print(values, sys.stdout)
    graph = html.Div(id='output',
                     children=[dcc.Graph(id='bar-graph',

                                         figure={'data': [go.Bar(
                                             x=labels, y=values)],
                                             'layout': go.Layout(
                                             title='{} Instagram Stories'.format(
                                                 year),
                                             xaxis={
                                                 'title': 'Day of the Week'},
                                             yaxis={'title': 'Number of Stories in {}'.format(year)})})])

    return graph


def bar_page():
    layout = html.Div([bar_nav,
                       dbc.Row([
                           dbc.Col(dropdown,
                                   align='center'),
                           dbc.Col(
                               dcc.Loading(
                                   build_bar()
                               ),
                               align='center')], justify='center')])

    return layout
