"""Tests for the Summary Service logic."""

import pytest
from unittest import mock
from app.exception.handlers import AppException
from app.service.summary_service import generate_llm_summary


@pytest.mark.asyncio
@mock.patch("app.service.summary_service.settings")
async def test_generate_llm_summary_mock_fallback(mock_settings):
    """Test summary service returns fallback mock summary when API key is unset."""
    mock_settings.OPENAI_API_KEY = None
    mock_settings.MAX_SUMMARY_LENGTH = 2000

    result = await generate_llm_summary("Hello world summary test.")
    assert "[Mock Summary Provider]" in result


@pytest.mark.asyncio
@mock.patch("app.service.summary_service.settings")
async def test_generate_llm_summary_empty_text(mock_settings):
    """Test summary validation triggers 400 error on empty string."""
    mock_settings.MAX_SUMMARY_LENGTH = 2000

    with pytest.raises(AppException) as exc_info:
        await generate_llm_summary("   ")
    assert exc_info.value.status_code == 400
