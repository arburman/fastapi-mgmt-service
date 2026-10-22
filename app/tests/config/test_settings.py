"""Tests for configuration settings and environment variable loading."""

import os
from unittest import mock
from app.config.settings import Settings


def test_settings_default_values():
    """Test that settings load default app name and expected attributes."""
    with mock.patch.dict(os.environ, {"API_KEY": "test-api-key"}):
        settings = Settings()
        assert settings.APP_NAME == "fastapi-mgmt-service"
        assert settings.API_KEY == "test-api-key"
        assert settings.MAX_SUMMARY_LENGTH == 2000
