from fastapi import APIRouter, Query
from app.schema.dtos import WeatherResponse
from app.service.weather_service import fetch_weather_data

router = APIRouter(prefix="", tags=["Weather"])


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
