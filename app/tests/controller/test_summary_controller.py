"""Tests for the Summary Controller endpoint."""

from unittest import mock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@mock.patch("app.controller.summary_controller.generate_llm_summary")
@mock.patch("app.controller.summary_controller.settings")
def test_post_summary_success(mock_settings, mock_generate):
    """Test successful authenticated summary generation route."""
    mock_settings.API_KEY = "secure-key-123"
    mock_generate.return_value = "This is a concise summary."

    response = client.post(
        "/summary",
        headers={"X-API-Key": "secure-key-123"},
        json={"text": "Long text to summarize..."},
    )
    assert response.status_code == 200
    assert response.json() == {"summary": "This is a concise summary."}


@mock.patch("app.controller.summary_controller.settings")
def test_post_summary_unauthorized(mock_settings):
    """Test summary endpoint fails when API key is missing or invalid."""
    mock_settings.API_KEY = "secure-key-123"

    response = client.post(
        "/summary",
        headers={"X-API-Key": "wrong-key"},
        json={"text": "Test text"},
    )
    assert response.status_code == 401
    assert "Invalid or missing X-API-Key" in response.json()["error"]
