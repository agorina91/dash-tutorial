import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app_layout, build_graph

from homepage import Homepage

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
app.config.suppress_callback_exceptions = True


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/time-series':
        return app_layout()
    else:
        return Homepage()


@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='pop_dropdown', component_property='value')])
def update_graph(value):

    graph = build_graph(value)

    return graph


if __name__ == '__main__':
    app.run_server(debug=True)
