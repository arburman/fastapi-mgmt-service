"""Tests for global custom exception classes and FastAPI exception handlers."""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.exception.handlers import AppException, register_exception_handlers

app = FastAPI()
register_exception_handlers(app)


@app.get("/trigger-app-exception")
def trigger_app_exc():
    raise AppException(400, "Custom application error")


@app.get("/trigger-unhandled")
def trigger_unhandled():
    raise RuntimeError("Unexpected failure")


client = TestClient(app)


def test_app_exception_handler():
    """Test global handling of custom AppExceptions."""
    response = client.get("/trigger-app-exception")
    assert response.status_code == 400
    assert response.json() == {
        "error": "Custom application error",
        "status_code": 400,
    }


def test_global_exception_handler():
    """Test global fallback handling of unhandled python exceptions."""
    response = client.get("/trigger-unhandled")
    assert response.status_code == 500
    assert response.json() == {"error": "Internal Server Error", "status_code": 500}
