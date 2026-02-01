from weather import get_weather
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget
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
        self.button.setGeometry(200, 270, 100, 40)
        self.button.clicked.connect(self.submit)
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setWordWrap(True)
        self.label.adjustSize()
        self.label.move(0, 350)
        self.label.resize(self.width(), self.label.height())
        self.line_edit.setGeometry(150, 200, 200, 50)
        self.line_edit.setPlaceholderText("Enter a city")
        self.line_edit.setAlignment(Qt.AlignCenter)

    def submit(self):
        city = self.line_edit.text()
        try:
            temps, feels_like, description = get_weather(city)
            text = (f"The temperature in {city} is {temps}, it feels like {feels_like} and it is {description}")
        except:
            text = ("Please enter in a valid city")
        self.label.setText(text)
        self.line_edit.hide()
        self.button.hide()

#Used to declare a city invalid
invalid = False

#Displays data from API
def provide_data(temps, feels_like, description):
    temps = temps
    feels_like = feels_like
    description = description