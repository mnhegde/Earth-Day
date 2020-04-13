import csv
import random
import json
name = []
latitude = []
longitude = []
eventsJ=[]
events = ['wildfire','tsunami','hurricane','earthquake','increase in carbon emitions','increase in wildlife poaching','more plastic is dumped in the ocean']
dot = [6,3,3,9,5,2,4]
hp = [10,6,8,6,5,3,7]  
def genEvent():
    with open('data\\average-latitude-longitude-countries.csv', mode='r') as f:
        reader = csv.DictReader(f, delimiter=',')  
        for n, row in enumerate(reader):
            if not n:#skip header
                continue
            name.append(row['Country']) 
            latitude.append(row['Latitude']) 
            longitude.append(row['Longitude'])
    for i in range (0,49):
        e = random.randint(0,6)
        country = random.randint(1,230)
        newEvent={}
        newEvent['event']=events[e]
        newEvent['country']=name[country]
        newEvent['coord']=[latitude[country],longitude[country]]
        newEvent['damage']=dot[e]
        newEvent['health']=hp[e]
        eventsJ.append(newEvent)
    
  
    with open('data\game.json','w') as fp:
            json.dump(eventsJ,fp)

genEvent()








    
