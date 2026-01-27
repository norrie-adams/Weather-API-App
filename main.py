import requests

#API Key
API_key = "12407454b28300b217a183936ecfe7e1"

#Retrieves data from OpenWeatherMap API
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "appid=" + API_key + "&q=" + city + "&units=imperial"

    data = requests.get(url).json()

    temps = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]

    return temps, feels_like, description

#Displays data from API
def provide_data(temps, feels_like, description):
#Asks for user input

#Actually displays data
temps, feels_like, description = get_weather(city)
provide_data(temps, feels_like, description)