import csv
import random
import json
name = []
latitude = []
longitude = []
events = ['wildfire','tsunami','hurricane','earthquake','increase in carbon emitions','increase in wildlife poaching','more plastic is dumped in the ocean']
dot = [6,3,3,9,5,2,4]
hp = [10,6,8,6,5,3,7]  
def genEvent():
    e = random.randint(0,4)
    country = random.randint(1,241)
    with open('data\\average-latitude-longitude-countries.csv', mode='r') as f:
        reader = csv.DictReader(f, delimiter=',')  
        for n, row in enumerate(reader):
            if not n:#skip header
                continue
            name.append(row['Country']) 
            latitude.append(row['Latitude']) 
            longitude.append(row['Longitude'])
    return (name[country],latitude[country],longitude[country],events[e],dot[e],hp[e])

with open('data\game.json','w') as fp:
        json.dump(genEvent(),fp)








    
