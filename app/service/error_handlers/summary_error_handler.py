"""Summary Validation and Error Handler Module.

Validates summary payloads and handles errors during LLM generation.
"""

from app.config.settings import settings
from app.exception.handlers import AppException
from app.utils.logger import logger


def validate_summary_payload(text: str) -> None:
  """Validates summary input boundaries before processing.

  Args:
      text (str): Input text string.

  Raises:
      AppException: If text is empty or exceeds character limits.
  """
  if not text.strip():
    raise AppException(400, "Text field cannot be empty.")

  if len(text) > settings.MAX_SUMMARY_LENGTH:
    raise AppException(
        400, f"Text exceeds maximum limit of {settings.MAX_SUMMARY_LENGTH} chars."
    )


def handle_summary_provider_error(exc: Exception) -> None:
  """Handles exceptions raised during LLM generation and maps them safely.

  Args:
      exc (Exception): The caught upstream provider exception.
  """
  logger.error(f"LLM summary provider error: {str(exc)}")
  raise AppException(502, "Summary generation service failed.")