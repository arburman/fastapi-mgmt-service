"""Tests for the Weather Service logic and HTTP client integration."""

import httpx
import pytest
from unittest import mock
from app.exception.handlers import AppException
from app.service.weather_service import fetch_weather_data


@pytest.mark.asyncio
@mock.patch("app.service.weather_service.settings")
async def test_fetch_weather_success(mock_settings):
    """Test weather service successfully parses external API payload."""
    mock_settings.WEATHER_API_KEY = "fake-key"

    mock_response = mock.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "name": "Tokyo",
        "main": {"temp": 22.0, "humidity": 45},
        "weather": [{"description": "few clouds"}],
    }

    with mock.patch("httpx.AsyncClient.get", return_value=mock_response):
        result = await fetch_weather_data("Tokyo")
        assert result["city"] == "Tokyo"
        assert result["temperature"] == 22.0
        assert result["condition"] == "few clouds"


@pytest.mark.asyncio
@mock.patch("app.service.weather_service.settings")
async def test_fetch_weather_city_not_found(mock_settings):
    """Test weather service raises 404 when city is missing upstream."""
    mock_settings.WEATHER_API_KEY = "fake-key"

    mock_response = mock.MagicMock()
    mock_response.status_code = 404

    with mock.patch("httpx.AsyncClient.get", return_value=mock_response):
        with pytest.raises(AppException) as exc_info:
            await fetch_weather_data("InvalidCity")
        assert exc_info.value.status_code == 404
