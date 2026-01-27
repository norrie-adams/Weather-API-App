import requests

#Used to declare a city invalid
invalid = False

#API Key
API_key = "12407454b28300b217a183936ecfe7e1"

#Retrieves data from OpenWeatherMap API
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "appid=" + API_key + "&q=" + city + "&units=imperial"

    data = requests.get(url).json()

    #Checks for invalid cities
    if "main" not in data:
        invalid_city()
    
    #Pulls data from API
    else:
        temps = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]

        return temps, feels_like, description

#Displays data from API
def provide_data(temps, feels_like, description):
    print(f"The temperature is {temps}, it feels like {feels_like}, and it is {description}")

#Prints invalid city message
def invalid_city():
    print("Please enter in a valid city")
    invalid = True

#Asks for user input
city = input("Enter a City: ")

#Actually displays data
if invalid is not True:
    temps, feels_like, description = get_weather(city)
    provide_data(temps, feels_like, description)