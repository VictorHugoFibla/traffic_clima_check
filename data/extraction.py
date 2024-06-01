import requests
import json
from config import OPENWEATHER_API_KEY, GOOGLE_MAPS_API_KEY

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    return response.json()

def get_traffic_data(origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    return response.json()
