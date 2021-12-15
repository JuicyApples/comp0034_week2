# COMP0034 week 2 materials

## Set-up

1. Accept the GitHub classroom assignment
2. Clone the repository in your IDE
3. Create and activate a venv e.g.

   `python3 -m venv venv`

   `source venv/bin/activate`
5. Install the libraries from requirements.txt

PyCharm and VS Code provide built in support for CSS and HTML.

You may find that an online editor such as [Codepen](https://codepen.io) or [JSFiddle](https://jsfiddle.net) is more
convenient to quickly write and see HTML and CSS combined.

## web_app_intro

The web_app_intro folder contains code that is used in the teaching video for students that want to try and follow the
video by coding the examples.

## Lab session 2 activities

### Activity 1: Create an html document

Create an html file. By convention the main page of a website is often called `index.html` so you may wish to create a
file with that name.

The basic html page structure is shown below. Add this to your HTML (it may already have been created if you used an
IDE):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add page title here</title>
</head>
<body>
<!-- Add the elements here -->
</body>
</html>
```

Add the html elements listed below to the body of the html page.

The any content you wish to each of the elements.

[W3 schools HTML element reference](https://www.w3schools.com/tags/default.asp)

```html
<title></title>
<h1></h1>
<ol></ol>
<a href=""></a>
<img src="" alt="" height="" width="">
<table>
    <tr>
        <td></td>
    </tr>
</table>
```

### Activity 2: Add CSS styling your html

Create a stylesheet called `mystyles.css`

Add a link to the stylesheet in the `<head>` section of your html, e.g.

```html

<head>
    <link rel="stylesheet" type="text/css" href="mystyles.css">
</head>
```

Add styling for the html elements you included in your html.

The general syntax is explained here: [W3Schools CSS syntax](https://www.w3schools.com/css/css_syntax.asp)

A reference for the selectors is here: [W3Schools CSS reference](https://www.w3schools.com/cssref/default.asp)

```css
h1 {
    color: plum;
    text-decoration-line: underline;
}

img {

}

ol {

}

li {

}

a {

}

table {

}

tr {

}

th {

}

td {

}
```

### Activity 3: Apply Bootstrap styling to your html

Replace your stylesheet with the [Bootstrap styles](https://getbootstrap.com/docs/5.1/getting-started/introduction/).

What does your page look like now?

Can you improve the design by applying a [grid layout](https://getbootstrap.com/docs/5.1/layout/grid/) and/or use of
the [Bootstrap examples](https://getbootstrap.com/docs/5.0/examples/)?

### Activity 4: Add HTML elements to a dash app

Open the basic dash app in `dash_app/dash_app.py`.

The first line of code after the imports creates and instance of a Dash app.

The HTML layout of the page is provided in the code following `app.layout =`.

The `main` function then runs the app.

Run this app with `python dash_app.py` from the terminal and visit http://127.0.0.1:8050/ in your web browser. In
PyCharm and VS Code you should be able to run it using run options (often a triangle symbol like a music or video player
start button).

```python
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

You should be able to access this at [http://127.0.0.1:8050/](http://127.0.0.1:8050/).

Add the same html elements you added to the html file earlier to your dash app.

The syntax is different. See [Dash HTML components documentation](https://dash.plotly.com/dash-html-components).

Dash components are always created in the <body> so you will not be able to add the <title> element.

```python
from dash import html

html.H1(children='My title'),

html.Ol(children=[
    html.Li(children='List item 1'),
]),

html.A(children='Google', href='http://www.google.com'),

html.Img(src="https://www.ucl.ac.uk/cam/sites/cam/files/styles/medium_image/public/migrated-images/ucl-logo-colours-notext.gif?itok=dQiHrzS8", alt="UCL logo"),

html.Table(
   [
      html.Tr([
         html.Td(children='row 1 col 1'),
         html.Td(children='row 1 col 2')
      ]),
      html.Tr([
         html.Td(children='row 2 col 1'),
         html.Td(children='row 2 col 2')
      ])
   ]
),

```

### Activity 5: Add bootstrap CSS styling to the app

The `dash-bootstrap-components` library should have been installed from requirements.txt.

Apply the bootstrap styling to your dash_app e.g.:

```python
import dash
import dash_bootstrap_components as dbc
from dash import html

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
])

if __name__ == '__main__':
    app.run_server(debug=True)

```

### Activity 6: Apply a different external stylesheet

Replace bootstrap with another external stylesheet such as [Pure.css](https://purecss.io/start/)
or [materialize](https://materializecss.com/getting-started.html) e.g.

```python
external_stylesheets = [
    {
        "href": "https://unpkg.com/purecss@2.0.6/build/pure-min.css",
        "integrity": "sha384-Uu6IeWbM+gzNVXJcM9XV3SohHtmWE+3VGi496jvgX1jyvDTXfdK+rfZc8C1Aehk5",
        "crossorigin": "anonymous",
        "rel": "stylesheet",
    },
]
```

```python
external_stylesheets = [
    {
        "href": "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css",
        "rel": "stylesheet",
    },
]
```

### Activity 7: Apply a style sheet to your coursework dash app
Apply the HTML and CSS techniques covered today to your coursework.