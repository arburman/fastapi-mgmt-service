# FastAPI Management Service

Production-grade FastAPI microservice built with clean separation of concerns, structured logging, custom error handling, environment-specific configurations, and Swagger documentation.

## Python Version: `3.15.1`

## Project Structure
- `app/config/`: Dynamic environment-based settings
- `app/controller/`: API routers / endpoints
- `app/service/`: Business logic and external API integrations
- `app/exception/`: Custom exception handlers
- `app/schema/`: Pydantic DTOs
- `app/utils/`: Logging and utilities
- `app/tests/`: Unit tests

## Running the Application

### Environment Variables
```bash
API_KEY=
MAX_SUMMARY_LENGTH=
OLLAMA_BASE_URL=
OPENAI_API_KEY=
OPENAI_MODEL_SEMVER=
WEATHER_API_KEY=
```

### Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Development (Default)
```bash
uvicorn app.main:app --reload
```

### Test
```bash
ENVIRONMENT=test uvicorn app.main:app --reload
```

### Production
```bash
ENVIRONMENT=prod uvicorn app.main:app --reload
```
