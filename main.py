from flask import Flask # type: ignore
import folium # type: ignore

app = Flask(__name__)

@app.route("/")
def base():
    # this is base map
    map = folium.Map(
        location=[20.695934, 76.581062],
        zoom_start=13
    )
    return map._repr_html_()

@app.route("/street-map")
def open_street_map():
    # this map using stamen toner
    map = folium.Map(
        location=[20.695934, 76.581062],
        tiles='Stamen Toner',
        zoom_start=13
    )

    folium.Marker(
        location=[20.695934, 76.581062],
        popup="<b>Marker here</b>",
        tooltip="Click Here!"
    ).add_to(map)
    
    return map._repr_html_()

@app.route("/map-marker")
def map_marker():
    # this map using stamen terrain
    # we add some marker here
    map = folium.Map(
        location=[20.695934, 76.581062],
        tiles='Stamen Terrain',
        zoom_start=13
    )

    folium.Marker(
        location=[20.695934, 76.581062],
        popup="<b>Marker here</b>",
        tooltip="Click Here!"
    ).add_to(map)

    folium.Marker(
        location=[20.695934, 76.581062],
        popup="<b>Marker 2 here</b>",
        tooltip="Click Here!",
        icon=folium.Icon(color='green')
    ).add_to(map)

    folium.Marker(
        location=[20.695934, 76.581062],
        popup="<b>Marker 3 here</b>",
        tooltip="Click Here!",
        icon=folium.Icon(color='red')
    ).add_to(map)

    return map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)