import weather
from weather import get_weather
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("weather-app-icon.png"))

        label = QLabel("The weather in ___ is ___", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0, 300, 500, 500)
        label.setAlignment(Qt.AlignHCenter)

#Used to declare a city invalid
invalid = False

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