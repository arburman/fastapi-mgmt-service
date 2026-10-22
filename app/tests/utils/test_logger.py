"""Tests for logger initialization and configuration utility."""

from app.utils.logger import logger


def test_logger_instance():
    """Test that logger is correctly initialized and bound."""
    assert logger is not None
    assert hasattr(logger, "info")
    assert hasattr(logger, "error")
