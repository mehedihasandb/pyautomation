import math

from math import sqrt, pi

import random

number = random.randint(1,10)
choice = random.choice(["mango","apple", "banana"])

import datetime
today = datetime.datetime.now()

print(today.month)

import os
current_dir = os.listdir()
print(current_dir)

import json
data = {"name": "Maek", "age": 60}
json_string = json.dumps(data)


import requests

# We need coordinates to get weather data
latitude = 23.8103 ,  # Paris latitude
longitude = 90.4125,   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

temperature = data["current"]["temperature_2m"]

# ------------------------------------------------------

import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(23.8103, 90.4125)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")
