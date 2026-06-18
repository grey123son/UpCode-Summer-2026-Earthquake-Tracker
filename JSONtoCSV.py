import urllib.request, json
import pandas as pd
import requests
import calendar
from datetime import date
import json




def get_month_quakes(m, y):
    start_date = date(y, m, 1)
    _, last_day = calendar.monthrange(start_date.year, start_date.month)
    end_of_month_date = date(start_date.year, start_date.month, last_day)
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_of_month_date}"
    response = requests.get(url)
    return response.json()["features"]


all_entries = []
for month in range(1, 13):
    rows = get_month_quakes(month, 2026)
    all_entries += rows

f = open('tsvfile.tsv','w')
f.write('id\tmag\ttime\turl\tmmi\tmagType\ttype\ttitle\tx\ty\tz\n')

id = 0
for entry in all_entries:
    toApp = f"{id}\t{entry['properties']['mag']}\t{entry['properties']['time']}\t{entry['properties']['url']}\t{entry["properties"]["mmi"]}\t{entry['properties']['magType']}\t{entry['properties']['type']}\t{entry['properties']['title']}\t{"\t".join(str(c) for c in entry['geometry']['coordinates'])}\n"
    f.write(toApp)
    id += 1

f.close()