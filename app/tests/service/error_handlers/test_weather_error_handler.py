"""Tests for the Weather service error handler mappings."""

import httpx
import pytest
from unittest import mock
from app.exception.handlers import AppException
from app.service.error_handlers.weather_error_handler import handle_weather_upstream_error


def test_handle_weather_404():
    """Test mapping of upstream 404 response to city not found exception."""
    mock_response = mock.MagicMock(spec=httpx.Response)
    mock_response.status_code = 404

    with pytest.raises(AppException) as exc_info:
        handle_weather_upstream_error(city="Berlin", response=mock_response)
    assert exc_info.value.status_code == 404
    assert "City 'Berlin' not found" in exc_info.value.message


def test_handle_weather_request_error():
    """Test mapping of transport errors to 502 service unreachable exceptions."""
    with pytest.raises(AppException) as exc_info:
        handle_weather_upstream_error(city="Berlin", exc=httpx.RequestError("Timeout"))
    assert exc_info.value.status_code == 502
