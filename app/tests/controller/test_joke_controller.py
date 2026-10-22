"""Tests for the Joke Controller endpoint."""

from unittest import mock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@mock.patch("app.controller.joke_controller.fetch_random_joke")
def test_get_joke_success(mock_fetch):
    """Test successful random joke retrieval via the API route."""
    mock_fetch.return_value = {
        "joke_text": "Why do programmers prefer dark mode? Because light attracts bugs.",
        "category": "Programming",
    }

    response = client.get("/joke")
    assert response.status_code == 200
    data = response.json()
    assert "joke_text" in data
    assert data["category"] == "Programming"
