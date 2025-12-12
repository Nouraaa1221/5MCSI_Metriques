from flask import Flask, jsonify, render_template
from urllib.request import urlopen
import json
from datetime import datetime
import sqlite3  # Si vous en avez besoin pour d'autres ateliers

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Page d'accueil de l'application Flask</h1>"


@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"


@app.route('/tawarano/')
def meteo():
    response = urlopen(
        'https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx'
    )
    raw_content = response.read()

    json_content = json.loads(raw_content.decode('utf-8'))

    results = []

    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = (
            list_element.get('main', {}).get('temp') - 273.15
            if list_element.get('main', {}).get('temp') is not None
            else None
        )
        results.append({'Jour': dt_value, 'temp': temp_day_value})

    return jsonify(results=results)


@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")


if __name__ == "__main__":
    app.run(debug=True)
