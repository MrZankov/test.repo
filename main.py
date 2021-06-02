from flask import Flask, render_template
app = Flask('app')
import requests
import json

api_key = "f77b8ad7c7df72c5a9169681620e91ce"
lat = "48.208176"
lon = "16.373819"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data)


@app.route('/')
def index():
  return render_template('index.html', data=data)

app.run(host='0.0.0.0', port=8080)