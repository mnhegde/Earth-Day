#Created by Manu Hegde, Pierre Lessard, and Spencer Evans-Cole on April 2020
from game import genEvent
from flask import Flask, render_template, request
import csv, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('transition.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/test')
def test():
    return render_template('map(testing doc).html')

@app.route('/game')
def game():
    return render_template('map_game.html')
@app.route('/api/game')
def gameInfo():
    with open('data/game.json','r') as read_file:
        return read_file.read()

@app.route('/api/markers')
def markers():
    with open('data/markers.json', 'r') as read_file:
        return read_file.read()

@app.route('/api/carboncountries')
def countries():
    with open('data/carboncountries.geojson.txt', 'r') as read_file:
        return read_file.read()

@app.route('/api/forestcountries')
def forestCountries():
    with open('data/forestcountries.geojson.txt', 'r') as read_file:
        return read_file.read()

@app.route('/api/agriculturecountries')
def wasteCountries():
    with open('data/agriculturecountries.geojson.txt', 'r') as read_file:
        return read_file.read()

@app.route('/api/global_carbon')
def global_carbon():
    data = []
    fp = open("data/archive.csv", 'r')
    reader = csv.reader(fp)
    global_carbon = {}
    i=0
    for row in reader:
        if i==0:
            i += 1
        else:
            if row[1] == '12':
                if row[3]:
                    global_carbon[row[0]] = row[3]
            else:
                i += 1
    data.append(global_carbon)

    fp = open('data/forest_global_data.csv')
    reader = csv.reader(fp)
    global_forest = {}
    i=0
    for row in reader:
        if i==0:
            i += 1
        else:
            global_forest[row[0]] = row[1]
    data.append(global_forest)

    fp = open('data/agriculture_global_data.csv')
    reader  =csv.reader(fp)
    global_agriculture = {}
    i = 0
    for row in reader:
        if i==0:
            i+=1
        else:
            global_agriculture[row[0]] = row[1]
    data.append(global_agriculture)

    
    return json.dumps(data)

@app.route('/api/global_carbon_increase')
def global_carbon_increase():
    fp = open(r"data/archive.csv", 'r')
    reader = csv.reader(fp)
    global_carbon_increase = []
    f = 0
    date=[]
    h=False
    for row in reader:
        if row[0] == '1960':
            h=True
        if h==True:
            if row[1] == '12':
                f+=1
                if f == 1:
                    date = [row[0],row[3]]
                elif f == 5:
                    global_carbon_increase.append({'year':str(date[0])+'-'+str(row[0]),'dif':format(float(row[3])-float(date[1]),'.2f')})
                    f=0
    return json.dumps(global_carbon_increase)

@app.route('/api/global_carbon_pierre')
def global_carbon_pierre():
    fp = open(r"data/archive.csv", 'r')
    reader = csv.reader(fp)
    global_carbon = {}
    i=0
    for row in reader:
        if i==0:
            i += 1
        else:
            if row[1] == '12':
                if row[3]:
                    global_carbon[row[0]] = row[3]
            else:
                i += 1
    return json.dumps(global_carbon)

@app.route('/chart')
def chart_page():
    return render_template('chart.html')


@app.route('/api/markerinfo', methods = ['GET', 'POST'])
def markerInfo():
    if request.method == 'POST':
        data = request.json
        coords = [data['lat'], data['lng']]
        markers = json.loads(open('data/markers.json', 'r').read())
        for marker in markers:
            if marker['coords'] == coords:
                filename = 'Templates/' + marker['title'].split('.')[0] + '.html'

        markerDescription = open(filename, 'r').read()

        return json.dumps(markerDescription)



if __name__ == '__main__':
    print(open('static/instructions.txt', 'r').read())
    app.run(debug=True, port=9000)
