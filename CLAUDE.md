# CLAUDE.md - FastAPI Management Service Guidelines

## Architecture & Directory Structure
- Follow clean separation of concerns:
  - `app/main.py`: Application entry point and router registration.
  - `app/config/settings.py`: Type-safe configuration using Pydantic `BaseSettings`.
  - `app/controller/`: FastAPI routers and endpoints handling HTTP request parameters and responses.
  - `app/service/`: Pure business logic and upstream API client wrappers (`httpx`, OpenAI).
  - `app/exception/`: Custom application exceptions (`AppException`) and domain-specific error handlers (e.g., `weather_error_handler.py`).
  - `app/schema/`: Pydantic models (DTOs) for request payloads and response serialization.
  - `app/utils/`: Shared utilities including structured logging (`structlog`).
  - `tests/`: Mirror of `app/` structure containing unit and integration tests.

## Coding Patterns & Conventions
- **Error Handling:** Services must *never* return error codes directly or handle HTTP mapping inline. They must call domain-specific error handlers located in `app/exception/` to raise clean `AppException` instances.
- **Environment Management:** Support environment-specific configuration files (`.env.dev`, `.env.test`, `.env.prod`) dynamically controlled via the `ENVIRONMENT` environment variable (defaulting to `dev`).
- **Documentation:** Every controller, service, exception class, validator, and error handler function **must** include comprehensive Python docstrings (typedocs) detailing args, returns, and behavior.
- **Logging:** Use `structlog` for structured logging across services and handlers.

## Testing
- Framework: `pytest` with `pytest-asyncio` and `TestClient`.
- Run command: `python -m pytest -v`
- Mock all external HTTP and LLM integrations (`httpx.AsyncClient`, `openai`) during unit testing.