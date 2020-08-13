import plotly.express as px

def save_as_html():
    df = px.data.election()
    geojson = px.data.election_geojson()
    fig1 = px.choropleth_mapbox(df,
                            geojson=geojson,
                            color="Bergeron",
                            locations="district",
                            featureidkey="properties.district",
                            center={"lat": 45.5517, "lon": -73.7073},
                            mapbox_style="carto-positron",
                            zoom=9)
    fig1.write_html("election.html")

    gapminder = px.data.gapminder()
    fig2 = px.choropleth(gapminder,
                     locations="iso_alpha",
                     color="lifeExp",
                     hover_name="country",
                     animation_frame="year",
                     color_continuous_scale='Plasma',
                     height=600
                     )
    fig2.write_html("gapminder.html")

if __name__ == '__main__':
    save_as_html()