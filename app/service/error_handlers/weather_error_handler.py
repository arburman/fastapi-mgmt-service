import httpx
from app.exception.handlers import AppException
from app.utils.logger import logger


def handle_weather_upstream_error(city: str, response: httpx.Response = None, exc: Exception = None):
    """Maps upstream weather API failures or connection errors to clean AppExceptions."""
    if response is not None:
        if response.status_code == 404:
            raise AppException(404, f"City '{city}' not found.")
        logger.error(f"Upstream weather API error ({response.status_code}): {response.text}")
        raise AppException(502, "Upstream weather API failed.")
    
    if exc is not None:
        logger.error(f"HTTP Request failed for weather service: {exc}")
        raise AppException(502, "Upstream weather service unreachable.")
    
    raise AppException(502, "Unknown weather service error.")