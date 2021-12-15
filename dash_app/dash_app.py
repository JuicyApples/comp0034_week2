# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.
import dash
from dash import html

external_stylesheets = [
    {
        "href": "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css",
        "rel": "stylesheet",
    },
]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),



])

if __name__ == '__main__':
    app.run_server(debug=True)
