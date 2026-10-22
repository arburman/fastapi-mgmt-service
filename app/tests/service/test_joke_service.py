"""Tests for the Joke Service logic."""

import pytest
from unittest import mock
from app.exception.handlers import AppException
from app.service.joke_service import fetch_random_joke


@pytest.mark.asyncio
async def test_fetch_random_joke_success():
    """Test joke service successfully fetches and formats a joke."""
    mock_response = mock.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "joke": "Test joke text",
        "category": "Misc",
    }

    with mock.patch("httpx.AsyncClient.get", return_value=mock_response):
        result = await fetch_random_joke()
        assert result["joke_text"] == "Test joke text"
        assert result["category"] == "Misc"


@pytest.mark.asyncio
async def test_fetch_random_joke_failure():
    """Test joke service handles upstream failure status codes."""
    mock_response = mock.MagicMock()
    mock_response.status_code = 500

    with mock.patch("httpx.AsyncClient.get", return_value=mock_response):
        with pytest.raises(AppException) as exc_info:
            await fetch_random_joke()
        assert exc_info.value.status_code == 502
