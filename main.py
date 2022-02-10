from flask import Flask, render_template, Response
import folium
import requests
import json

app = Flask(__name__)


iconSpiderman = folium.features.CustomIcon('./images/spiderman.png', icon_size=(100,100))
iconHulk = folium.features.CustomIcon('./images/hulk.png', icon_size=(100,100))
iconWolverine = folium.features.CustomIcon('./images/wolverine.png', icon_size=(100,100))

#create superhero popup descriptions
popupSpiderman = "<strong>Spiderman</strong><br>Realname: Peter Parker<br>City of birth: Forest Hills, Queens, New York, USA"
popupHulk = "<strong>Hulk</strong><br>Realname: Bruce Banner<br>City of birth: Dayton, Ohio, USA"
popupWolverine = "<strong>Wolverine</strong><br>Realname: James Howlett (Logan)<br>City of birth: Cold Lake, Alberta, Canada"

@app.route("/")
def base():
    # this is base map
    map = folium.Map(
        location=[22.3122029,114.1667126],
        zoom_start=15
    )
    # map.add_child(folium.ClickForMarker())
    #create superhero markers and add them to map object
    folium.Marker([22.3122029,114.1667126], tooltip="Spiderman", popup=popupSpiderman, icon=iconSpiderman).add_to(map)
    folium.Marker([22.3087399,114.1776188], tooltip="Hulk", popup=popupHulk, icon=iconHulk).add_to(map)
    folium.Marker([22.3051009, 114.173681], tooltip="Wolverine", popup=popupWolverine, icon=iconWolverine).add_to(map)


    return map._repr_html_()


@app.route("/json")
def waste_api():
    r = requests.get('https://api.data.gov.hk/v1/nearest-recyclable-collection-points?lat=22.2812&long=114.152&max=10')
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content-type'],
    )

if __name__ == "__main__":
    app.run(debug=True)