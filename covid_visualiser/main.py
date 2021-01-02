import os
import folium
import requests
import json

r = requests.get(url='https://api.covid19india.org/data.json')
statewise_covid_data = json.loads(r.content)['statewise']

with open('capital_data.json', 'r') as f:
    json_text = f.read()

city_data = json.loads(json_text)


for i in range(1,len(statewise_covid_data)):
    for j in range(len(city_data)):
        if statewise_covid_data[i]['statecode'] == city_data[j]['statecode']:
            city_data[j]['confirmed'] = statewise_covid_data[i]['confirmed']
            city_data[j]['deaths'] = statewise_covid_data[i]['deaths']
            break


mp = folium.Map(location = [city_data[1]['lat'],city_data[1]['lng']],zoom_start= 5)

for i in range(len(city_data)):
    if "deaths" in city_data[i]:
        if float(city_data[i]['deaths']) > 50:
            folium.Marker(location = [city_data[i]['lat'],city_data[i]['lng']],
                          popup = city_data[i]['state'],
                          icon=folium.Icon(color='darkred',icon_color='white',icon='remove-sign',),
                          tooltip = 'deaths: ' + city_data[i]['deaths'] + ' confirmed: ' + city_data[i]['confirmed']
                         ).add_to(mp)
        elif float(city_data[i]['deaths']) > 20:
            folium.Marker(location = [city_data[i]['lat'],city_data[i]['lng']],
                          popup = city_data[i]['state'],
                          icon=folium.Icon(color='red',icon_color='white',icon='ban-circle',),
                          tooltip = 'deaths: ' + city_data[i]['deaths'] + ' confirmed: ' + city_data[i]['confirmed']
                         ).add_to(mp)
        elif float(city_data[i]['deaths']) > 0:
            folium.Marker(location = [city_data[i]['lat'],city_data[i]['lng']],
                          popup = city_data[i]['state'],
                          icon=folium.Icon(color='orange',icon_color='white',icon='warning-sign',),
                          tooltip = 'deaths: ' + city_data[i]['deaths'] + ' confirmed: ' + city_data[i]['confirmed']
                         ).add_to(mp)

        elif float(city_data[i]['deaths']) == 0:
            folium.Marker(location = [city_data[i]['lat'],city_data[i]['lng']],
                          popup = city_data[i]['state'],
                          icon=folium.Icon(color='green',icon_color='white',icon='ok-circle',),
                          tooltip = 'deaths: ' + city_data[i]['deaths'] + ' confirmed: ' + city_data[i]['confirmed']
                         ).add_to(mp)

mp.save('map.html')

os.system('firefox map.html')
