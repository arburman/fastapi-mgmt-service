import httpx
from app.config.settings import settings
from app.exception.handlers import AppException
from app.service.error_handlers.weather_error_handler import handle_weather_upstream_error


async def fetch_weather_data(city: str):
    if not settings.WEATHER_API_KEY:
        raise AppException(502, "Weather service API key is not configured.")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "units": "metric", "appid": settings.WEATHER_API_KEY}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params, timeout=5.0)
            
            if response.status_code != 200:
                handle_weather_upstream_error(city=city, response=response)

            data = response.json()
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "condition": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
            }
        except httpx.RequestError as exc:
            handle_weather_upstream_error(city=city, exc=exc)