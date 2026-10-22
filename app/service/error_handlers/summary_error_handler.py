from app.config.settings import settings
from app.exception.handlers import AppException
from app.utils.logger import logger


def validate_summary_payload(text: str):
    """Validates summary input boundaries before processing."""
    if not text.strip():
        raise AppException(400, "Text field cannot be empty.")

    if len(text) > settings.MAX_SUMMARY_LENGTH:
        raise AppException(
            400, f"Text exceeds maximum limit of {settings.MAX_SUMMARY_LENGTH} chars."
        )


def handle_summary_provider_error(exc: Exception):
    """Handles exceptions raised during LLM generation and maps them safely."""
    logger.error(f"LLM summary provider error: {str(exc)}")
    # Falling back or returning error based on design
    raise AppException(502, "Summary generation service failed.")