"""Tests for Summary payload validation and error handlers."""

import pytest
from unittest import mock
from app.config.settings import settings
from app.exception.handlers import AppException
from app.service.error_handlers.summary_error_handler import (
    handle_summary_provider_error,
    validate_summary_payload,
)


def test_validate_summary_too_long():
    """Test validation exception when text exceeds max length."""
    with mock.patch.object(settings, "MAX_SUMMARY_LENGTH", 10):
        with pytest.raises(AppException) as exc_info:
            validate_summary_payload("This text is way too long for the limit.")
        assert exc_info.value.status_code == 400
        assert "exceeds maximum limit" in exc_info.value.message


def test_handle_summary_provider_error():
    """Test mapping of LLM provider exceptions."""
    with pytest.raises(AppException) as exc_info:
        handle_summary_provider_error(Exception("OpenAI rate limit exceeded"))
    assert exc_info.value.status_code == 502
