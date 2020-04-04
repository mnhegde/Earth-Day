from bs4 import BeautifulSoup
import json

#js = open('static/maplogic.js', 'r')

#html_file = BeautifulSoup(open('Templates/map.html', 'r').read(), features="html.parser")
#print(html_file(text='marker'))

#script = html_file.find_all('script')
#map_logic = html_file.new_tag('script')
#map_logic.string = js.read()

#script[-1].insert_after(map_logic)

#new_file = open('Templates/map.html', 'w')
#new_file.write(str(html_file))
import csv

def addMarkers():
    markers = []

    numbersOfItemsAdd = int(input('how many markers do you want to add'))

    for i in range (0, numbersOfItemsAdd):
        lat = input('Latitude: ')
        lng = input('Longitude: ')
        title = input('Title: ')
        popup = input('Popup: ')

        marker = {}
        marker['coords'] = [lat, lng]
        marker['title'] = title
        marker['popup'] = popup

        markers.append(marker)

    with open('data/markers.json', 'a') as fp:
        fp.write(json.dump(markers, fp))



fp = open('data\Countries_Carbon_Dioxide_2014.csv', 'r')
reader = csv.reader(fp)

countries = {}
i=0

for row in reader:
    if i == 0:
        i += 1
        continue
    countries[row[0]] = row[2]
    i += 1

with open('data/countries.geojson.txt', 'r') as fp:
    geoJSON = json.load(fp)

country_list = []
for key in countries.keys():
    country_list.append(key)

#for feature in geoJSON['features']:

for feature in geoJSON['features']:
    if feature['properties']['ADMIN'].upper() in country_list:
        if feature['properties']['carbon_dioxide_level']:
            continue
        else:
            feature['properties']['carbon_dioxide_level'] = countries[feature['properties']['ADMIN'].upper()]
    if feature['properties']['ADMIN'] == 'China':
        feature['properties']['carbon_dioxide_level'] = countries['CHINA (MAINLAND)']


with open('data/countries.geojson.txt', 'w') as fp:
    json.dump(geoJSON, fp)















