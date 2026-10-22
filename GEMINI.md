# GEMINI.md - FastAPI Management Service Context & Standards

## Core Architecture Principles
- **Strict Separation of Concerns:** Routers (`controller/`) handle transport; business logic (`service/`) handles processing; error handlers (`exception/`) manage telemetry and exception mapping.
- **Configuration:** Managed via Pydantic v2 `BaseSettings` supporting `.env.dev`, `.env.test`, and `.env.prod` configurations based on the `ENVIRONMENT` variable.
- **Logging:** Structured logging implemented via `structlog`.

## Implementation Rules
- **Error Propagation:** When an upstream integration (`httpx`, OpenAI) fails, delegate the response or exception to its corresponding error handler file in `app/exception/`.
- **Documentation Standards:** Every file, class, and function must feature clear docstrings outlining purpose, arguments, and return types.
- **Testing Requirements:** Maintain an identical file/directory hierarchy inside the `tests/` directory. All asynchronous functions must be tested using `pytest-asyncio` with mocked dependencies.
- **Test Execution:** `python -m pytest -v`