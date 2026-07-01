import requests
from flask import current_app

def obtener_clima_actual():
    api_key = current_app.config["OPENWEATHER_API_KEY"]
    lat = current_app.config["OPENWEATHER_LAT"]
    lon = current_app.config["OPENWEATHER_LON"]

    if not api_key:
        return None, "No se configuró la API Key de OpenWeather"

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        if response.status_code != 200:
            return None, data.get("message", "Error al consultar OpenWeather")

        descripcion = data["weather"][0]["description"]
        condicion = data["weather"][0]["main"]
        temperatura = data["main"]["temp"]

        hay_lluvia = condicion.lower() in ["rain", "drizzle", "thunderstorm"]

        clima = {
            "ciudad": current_app.config["OPENWEATHER_CITY"],
            "temperatura": temperatura,
            "descripcion": descripcion,
            "condicion": condicion,
            "hay_lluvia": hay_lluvia
        }

        return clima, None

    except Exception:
        return None, "No se pudo conectar con OpenWeather"