from weather import get_weather
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("weather-app-icon.png"))
        self.button = QPushButton("Enter", self)
        self.line_edit = QLineEdit(self)
        self.label = QLabel(self)
        self.initUI()

    def initUI(self):
        #data = QLabel(f"The temperature in {city} is {temps}, it feels like {feels_like}, and it is {description}", self)
        #data.setFont(QFont("Arial", 20))
        #data.setGeometry(0, 300, 500, 500)
        #data.setAlignment(Qt.AlignHCenter)
        self.line_edit.setGeometry(150, 350, 200, 50)
        self.button.setGeometry(210, 10, 100, 40)
        self.button.clicked.connect(self.submit)
        self.label.setGeometry(0, 100, 400, 110)

    def submit(self):
        city = self.line_edit.text()
        try:
            temps, feels_like, description = get_weather(city)
            text = (f"The temperature in {city} is {temps}, it feels like {feels_like} and it is {description}")
        except:
            text = ("Please enter in a valid city")
        self.label.setText(text)

#Used to declare a city invalid
invalid = False

#Displays data from API
def provide_data(temps, feels_like, description):
    temps = temps
    feels_like = feels_like
    description = description