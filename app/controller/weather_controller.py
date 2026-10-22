"""Weather Controller Module.

Exposes endpoints related to fetching current weather data for given cities.
"""

from fastapi import APIRouter, Query
from app.schema.dtos import WeatherResponse
from app.service.weather_service import fetch_weather_data

router = APIRouter(prefix="", tags=["Weather"])

"""Fetch current weather details for a specified city.

  Args:
      city (str): Name of the target city.

  Returns:
      dict: Weather details containing city name, temperature, condition, and
      humidity.
  """
@router.get(
    "/weather",
    response_model=WeatherResponse,
    responses={
        404: {"description": "City not found"},
        502: {"description": "Upstream API failure"},
    },
)
async def get_weather(city: str = Query(..., description="Name of the city")):
    return await fetch_weather_data(city)
