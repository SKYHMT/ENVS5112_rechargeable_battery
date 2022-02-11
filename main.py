from flask import Flask, render_template, Response
import folium
import requests
import json
import csv

app = Flask(__name__)

@app.route("/")
def base():
    # this is base map
    map = folium.Map(
        location=[22.3122029,114.1667126],
        zoom_start=13
    )
    # map.add_child(folium.ClickForMarker())

    with open('./data/rechareable_batteries.csv') as f:
        f_csv = csv.reader(f)
        index = 0
        for row in f_csv:
            lat = row[9]
            lon = row[10]
            # still not good way to repeat
            iconRecycle = folium.features.CustomIcon('./images/recycle-bin.png', icon_size=(50,50))
            folium.Marker([lat,lon], tooltip=row[4],  icon=iconRecycle).add_to(map)  
            index = index + 1
            # limit show 500
            if (index>500):
                break
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