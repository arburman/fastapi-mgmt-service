"""Tests for the Weather Controller endpoint."""

from unittest import mock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@mock.patch("app.controller.weather_controller.fetch_weather_data")
def test_get_weather_success(mock_fetch):
    """Test successful weather retrieval via the API route."""
    mock_fetch.return_value = {
        "city": "London",
        "temperature": 15.5,
        "condition": "clear sky",
        "humidity": 60,
    }

    response = client.get("/weather?city=London")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "London"
    assert data["temperature"] == 15.5
