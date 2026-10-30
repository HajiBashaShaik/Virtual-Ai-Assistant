
import requests


def weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 15.8281,
        "longitude": 78.0373,
        "current": "temperature_2m,weather_code",
        "timezone": "Asia/Kolkata"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()
    data = response.json()
    temp = data["current"]["temperature_2m"]
    unit = data["current_units"]["temperature_2m"]
    code = data["current"]["weather_code"]

    weather_conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Heavy rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail"
    }

    desc = weather_conditions.get(
        code,
        "Unknown weather condition"
    )

    return f"Temperature is {temp} {unit}. {desc}"
