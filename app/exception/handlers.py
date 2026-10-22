"""Global Exception Handlers Module.

Defines custom application exceptions and registers global FastAPI exception
handlers.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.utils.logger import logger


class AppException(Exception):
  """Custom application-level exception with status codes and messages."""

  def __init__(self, status_code: int, message: str):
    """Initializes the AppException.

    Args:
        status_code (int): HTTP status code for the response.
        message (str): Error description message.
    """
    self.status_code = status_code
    self.message = message


def register_exception_handlers(app: FastAPI) -> None:
  """Registers custom exception handlers on the FastAPI application instance.

  Args:
      app (FastAPI): The main FastAPI app instance.
  """

  @app.exception_handler(AppException)
  async def app_exception_handler(request: Request, exc: AppException):
    logger.error(
        f"AppException: {exc.message} | Path: {request.url.path} | Status:"
        f" {exc.status_code}"
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message, "status_code": exc.status_code},
    )

  @app.exception_handler(Exception)
  async def global_exception_handler(request: Request, exc: Exception):
    logger.critical(f"Unhandled Exception: {str(exc)} | Path: {request.url.path}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "status_code": 500,
        },
    )