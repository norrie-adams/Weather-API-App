import requests

base_url = f"http://api.openweathermap.org/data/2.5/weather?"
API_key = "12407454b28300b217a183936ecfe7e1"
city = input("Enter a City: ")

url = base_url + "appid=" + API_key + "&q=" + city

data = requests.get(url).json()

temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]

print(f"The temperature is {temp}, it feels like {feels_like}, and it is {description}")