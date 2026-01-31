import requests
import os
from dotenv import load_dotenv

#API Key
load_dotenv()
API_key = os.getenv("WEATHER_API_KEY")

#Retrieves data from OpenWeatherMap API
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "appid=" + API_key + "&q=" + city + "&units=imperial"

    data = requests.get(url).json()

    #Checks for invalid cities
    if "main" not in data:
        invalid = True
    
    #Pulls data from API
    else:
        temps = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        return temps, feels_like, description