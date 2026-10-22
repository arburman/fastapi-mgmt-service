"""Tests for the Joke service error handler mappings."""

import httpx
import pytest
from unittest import mock
from app.exception.handlers import AppException
from app.service.error_handlers.joke_error_handler import handle_joke_upstream_error


def test_handle_joke_upstream_error():
    """Test mapping of generic upstream joke error to 502."""
    mock_response = mock.MagicMock(spec=httpx.Response)
    mock_response.status_code = 502
    mock_response.text = "Bad Gateway"

    with pytest.raises(AppException) as exc_info:
        handle_joke_upstream_error(response=mock_response)
    assert exc_info.value.status_code == 502
