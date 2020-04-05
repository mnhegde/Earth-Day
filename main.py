#Created by Manu Hegde on April 2020

from flask import Flask, render_template
import csv, json

app = Flask(__name__)

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/api/markers')
def markers():
    with open('data/markers.json', 'r') as read_file:
        return read_file.read()

@app.route('/api/countries')
def countries():
    with open('data/countries.geojson.txt', 'r') as read_file:
        return read_file.read()

@app.route('/api/global_carbon')
def global_carbon():
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
    return json.dumps(global_carbon)

@app.route('/graph')
def graph():
    return render_template('graph.html')


@app.route('/test')
def test():
    return render_template('map(testing doc).html')


if __name__ == '__main__':
    app.run(debug=True, port=9000)