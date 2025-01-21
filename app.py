from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '88d825d30ad48bc74c265bbc89bb337f'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        url = f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)