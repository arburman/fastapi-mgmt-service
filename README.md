# FastAPI Management Service

Production-grade FastAPI microservice built with clean separation of concerns, structured logging, custom error handling, environment-specific configurations, and Swagger documentation.

## Project Structure
- `app/config/`: Dynamic environment-based settings
- `app/controller/`: API routers / endpoints
- `app/service/`: Business logic and external API integrations
- `app/exception/`: Custom exception handlers
- `app/schema/`: Pydantic DTOs
- `app/utils/`: Logging and utilities

## Running the Application

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
