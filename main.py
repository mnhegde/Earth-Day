from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True, port=9000)