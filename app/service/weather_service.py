import httpx
from app.config.settings import settings
from app.exception.handlers import AppException
from app.utils.logger import logger


async def fetch_weather_data(city: str):
  if not settings.WEATHER_API_KEY:
    logger.error("WEATHER_API_KEY is not configured in settings.")
    raise AppException(502, "Weather service API key is not configured.")

  url = "https://api.openweathermap.org/data/2.5/weather"
  params = {"q": city, "units": "metric", "appid": settings.WEATHER_API_KEY}

  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(url, params=params, timeout=5.0)
      if response.status_code == 404:
        raise AppException(404, f"City '{city}' not found.")
      if response.status_code != 200:
        logger.error(f"Upstream weather API error: {response.text}")
        raise AppException(502, "Upstream weather API failed.")

      data = response.json()
      return {
          "city": data["name"],
          "temperature": data["main"]["temp"],
          "condition": data["weather"][0]["description"],
          "humidity": data["main"]["humidity"],
      }
    except httpx.RequestError as exc:
      logger.error(f"HTTP Request failed: {exc}")
      raise AppException(502, "Upstream weather service unreachable.")