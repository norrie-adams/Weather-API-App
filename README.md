# Weather-API-App
A Python application that pulls real-time weather data from the OpenWeatherMap API and displays it in a PyQt5 GUI.

Tech Stack:
- Python - Language
- PyQt5 - GUI Library
- OpenWeatherMap API - Weather API

Description:
When you run the app, it opens a GUI asking for a city name. The app then:

- Displays the current weather, temperature, and "feels like" temperature  
- Shows a description of the weather (e.g., rainy, sunny, cloudy)  
- Includes an icon corresponding to the weather description  
- Handles invalid city names gracefully with an error message

What I Learned:
- Python Basics: variables, functions, loops, lists, objects, and classes  
- APIs: connecting with an API, reading JSON data  
- Frontend / GUI Design**: adding images, styling text, organizing the window, displaying backend data  
- Networking Concepts: understanding how frontend, APIs, and backend communicate  
  - Enter a city → API validates city  
  - If valid → request data from backend → return data to user  
  - If invalid → send error message
 
