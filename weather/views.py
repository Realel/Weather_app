import requests
from django.shortcuts import render
import os
from dotenv import load_dotenv
load_dotenv()

def weather_view(request):
    city = request.GET.get("city", "Dnipro")  # Город по умолчанию

    api_key =  os.getenv("OPENWEATHER_API_KEY")  # Твой API-ключ
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=ru"

    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)

    weather = None
    hourly_forecast = []

    if weather_response.status_code == 200:
        data = weather_response.json()
        weather = {
            "city": data["name"],
            "temperature": round(data["main"]["temp"]),
            "description": data["weather"][0]["description"].capitalize(),
            "icon": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png",
        }

    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()
        hourly_forecast = [
            {
                "time": item["dt_txt"][11:16],  # Вытаскиваем время в формате ЧЧ:ММ
                "temperature": round(item["main"]["temp"]),
                "icon": f"https://openweathermap.org/img/wn/{item['weather'][0]['icon']}.png",
            }
            for item in forecast_data["list"][:5]  # Берем только 5 ближайших часов
        ]

    return render(request, "weather/home.html", {"weather": weather, "city": city, "hourly": hourly_forecast})
