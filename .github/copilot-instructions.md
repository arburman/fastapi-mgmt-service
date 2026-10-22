# GitHub Copilot Instructions - FastAPI Management Service

## Project Overview
This repository contains a production-grade FastAPI microservice named `fastapi-mgmt-service` utilizing structured logging, type-safe settings, decoupled error handling, and robust OpenAPI documentation.

## Directory Layout & Rules
- `app/config/`: Configuration via Pydantic `BaseSettings` loading from `.env.dev`, `.env.test`, or `.env.prod`.
- `app/controller/`: API endpoints (`weather_controller.py`, `joke_controller.py`, `summary_controller.py`).
- `app/service/`: Business logic. Services only execute upstream HTTP calls and data mapping.
- `app/exception/`: Custom exception handlers and domain error mapping (`weather_error_handler.py`, `joke_error_handler.py`, `summary_error_handler.py`).
- `app/schema/`: Pydantic DTOs.
- `app/utils/`: `structlog` logging initialization.

## Code Standards
1. **Decoupled Error Handling:** Never catch or map HTTP errors inline inside services. Delegate all error transformation to service-specific error handlers (`app/exception/*_error_handler.py`) which raise `AppException`.
2. **Documentation:** Add descriptive Python docstrings on every function, class, controller, and service.
3. **Async / Sync:** Use `async def` for endpoints and service operations making external HTTP/LLM calls.
4. **Testing:** Mirror all production code changes inside the `tests/` directory and run via `python -m pytest -v`.