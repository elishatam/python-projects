from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve #serve our application

app = Flask(__name__) #This makes it a flask app

#This is the route for the home page
@app.route('/')
@app.route('/index')
def index():
    #return "Hello World!"
    return render_template('index.html')

#This is the route for weather
@app.route('/weather')
def get_weather():
    city = request.args.get('city') #Parameter sent in the URL

    # Check for empty strings or string with only spaces
    if not bool(city.strip()): #strip spaces
        city = "San Jose"      #Default to San Jose

    weather_data = get_current_weather(city)

    #City is not found by API
    if not weather_data['cod'] == 200: #200 is success
        return render_template('city-not-found.html')

    return render_template(  #Send weather data to the template
        "weather.html",      #This is the template
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}", #format fstring
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8002) #Will run on local host
    serve(app, host="0.0.0.0", port=8002) #Will run on local host