import csv
import random
import json
name = []
latitude = []
longitude = []
eventsJ=[]
events = ['Wildfire','Tsunami','Hurricane','Earthquake','Increase in carbon emissions','Increase in wildlife poaching','More plastic is dumped in the ocean','Tornado','Volcanic Euruption','Flood','Blizzard','Drought','Famine','Sinkholes','Hail Storm','Heat Waves',]
dot = [6,3,3,9,5,2,4,9,4,5,6,10,3,9,7,8]
hp = [10,6,8,6,5,3,7,10,4,6,12,15,7,4,3,5]  
def genEvent():
    with open(r'data\average-latitude-longitude-countries.csv', mode='r') as f:
        reader = csv.DictReader(f, delimiter=',')  
        for n, row in enumerate(reader):
            if not n:#skip header
                continue
            name.append(row['Country']) 
            latitude.append(row['Latitude']) 
            longitude.append(row['Longitude'])
    for i in range (0,49):
        e = random.randint(0,15)
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








    
