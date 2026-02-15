from weather import get_weather
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QIcon, QFont, QPixmap
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
        self.image = QLabel(self)
        pixmap = QPixmap("partly-cloudy-icon.png")
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)
        self.image.hide()
        text_font = QFont("Cosmic Sans", 14)
        self.label.setFont(text_font)
        self.initUI()


    def initUI(self):
        self.button.setGeometry(200, 270, 100, 40)
        self.button.clicked.connect(self.submit)
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setWordWrap(True)
        self.label.move(0, 350)
        self.label.setGeometry(20, 350, 460, 160)
        self.line_edit.setGeometry(150, 200, 200, 50)
        self.line_edit.setPlaceholderText("Enter a city")
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.image.setGeometry(110, 50, 275, 275)
        

    def submit(self):
        city = self.line_edit.text()
        try:
            temps, feels_like, description = get_weather(city)
            text = (f"The temperature in {city} is {temps}, it feels like {feels_like} and it is {description}")
            weather_icons = {
                "few clouds": "partly-cloudy-icon.png",
                "rain": "rainy-weather-icon.png",
                "sunny": "sunny-weather-icon.png",
                "overcast": "cloudy-weather-icon.png",
                "snow": "snow-weather-icon.png",
                "cloudy": "cloudy-weather-icon.png"
            }
            for key, icon_file in weather_icons.items():
                if key in description.lower():
                    self.pixmap = QPixmap(icon_file)
                    self.image.setPixmap(self.pixmap)
                    self.image.show()
                    break
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