"""Joke Error Handler Module.

Maps errors and unexpected responses from the upstream joke provider to AppExceptions.
"""

import httpx
from app.exception.handlers import AppException
from app.utils.logger import logger


def handle_joke_upstream_error(
    response: httpx.Response = None, exc: Exception = None
) -> None:
  """Maps upstream joke API failures or connection errors to clean AppExceptions.

  Args:
      response (httpx.Response, optional): HTTP response from upstream provider.
      exc (Exception, optional): Raised exception during request execution.
  """
  if response is not None:
    logger.error(
        f"Upstream joke API error ({response.status_code}): {response.text}"
    )
    raise AppException(502, "Failed to fetch joke from upstream.")

  if exc is not None:
    logger.error(f"HTTP Request failed for joke service: {exc}")
    raise AppException(502, "Joke service currently unreachable.")

  raise AppException(502, "Unknown joke service error.")