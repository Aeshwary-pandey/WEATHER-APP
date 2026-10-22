import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv(dotenv_path=".env", override=True)

API_KEY = os.getenv("API_KEY")

# Check API key
if not API_KEY:
    print("API key not found!")
    print("Please check your .env file.")
    exit()

print("API key loaded successfully!")

# Get city name
city = input("\nEnter city name: ").strip()

if not city:
    print("Please enter a city name.")
    exit()

# OpenWeather API URL
url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if response.status_code == 200:
        # Get weather information
        city_name = data["name"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        condition = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display professional weather report
        print("\n" + "=" * 38)
        print("          WEATHER REPORT")
        print("=" * 38)
        print(f"  City        : {city_name}")
        print(f"  Temperature : {temperature} °C")
        print(f"  Feels Like  : {feels_like} °C")
        print(f"  Condition   : {condition}")
        print(f"  Humidity    : {humidity}%")
        print(f"  Wind Speed  : {wind_speed} m/s")
        print("=" * 38)

    elif response.status_code == 401:
        print("\nInvalid API key or key not activated.")
        print("Check your OpenWeather API key.")

    elif response.status_code == 404:
        print("\nCity not found!")
        print("Please check the spelling and try again.")

    else:
        print("\nUnable to fetch weather information.")
        print("Error:", data.get("message", "Unknown error"))

except requests.exceptions.Timeout:
    print("\nRequest timed out. Please try again.")

except requests.exceptions.ConnectionError:
    print("\nConnection failed. Check your internet connection.")


