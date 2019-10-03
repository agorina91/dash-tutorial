import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import pandas as pd

import plotly.graph_objs as go

import pickle


df = pd.read_csv('population_il_cities.csv')
df.index = df.iloc[:, 0]
df.index = pd.to_datetime(df.index)
df = df.iloc[:, 1:]

with open('dropdown', 'rb') as fp:
    dropdown = pickle.load(fp)

# COMPONENTS
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

drop = html.Div(dcc.Dropdown(
    id='pop_dropdown',
    options=dropdown,
    value='Springfield city, Illinois'),
    style={'width': '60%', 'display': 'inline-block'})

header = html.H3(
    "Type the name of an Illinois city to see its population change:",
    style={'padding': '10px'})

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),

    ],
    brand="Demo",
    brand_href="/home",
    sticky="top",
    color='primary'
)


output = html.Div(id='output',
                  children=[
                      dcc.Graph(
                          id='group-time-series',
                          hoverData={'points': [
                              {'customdata': 'Springfield city, Illinois'}]}
                      )
                  ],
                  style={'display': 'inline-block'})


# LAYOUT
def app_layout():
    layout = html.Div([
        navbar,
        header,
        drop,
        output
    ])
    return layout


app.layout = html.Div([
    header,
    drop,
    output,
    # side
])

# GRAPH


def build_graph(city):
    data = [go.Scatter(x=df.index,
                       y=df[city],
                       mode='lines+markers',
                       name=city,
                       marker={'color': 'red'},
                       customdata=[city for x in range(len(df.index))])]

    graph = dcc.Graph(figure={

        'data': data,


        'layout': go.Layout(
            title='{} Population Change'.format(city),
            yaxis={'title': 'Population'},
            hovermode='closest'
        )
    })

    return graph


@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='pop_dropdown', component_property='value')])
def update_graph(value):

    graph = build_graph(value)

    return graph




server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)
