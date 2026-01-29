import requests
import os
from dotenv import load_dotenv
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("weather-app-icon.png"))

        label = QLabel("The weather in ___ is ___", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0, 300, 500, 500)
        label.setAlignment(Qt.AlignHCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

#Used to declare a city invalid
invalid = False

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