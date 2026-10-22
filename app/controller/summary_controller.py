from fastapi import APIRouter, Security
from fastapi.security import APIKeyHeader
from app.config.settings import settings
from app.exception.handlers import AppException
from app.schema.dtos import SummaryRequest, SummaryResponse
from app.service.summary_service import generate_llm_summary

router = APIRouter(prefix="", tags=["Summary"])
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


@router.post(
    "/summary",
    response_model=SummaryResponse,
    responses={
        400: {"description": "Invalid payload or length"},
        401: {"description": "Missing or invalid API key"},
    },
)
async def post_summary(
    payload: SummaryRequest, x_api_key: str = Security(api_key_header)
):
    if not x_api_key or x_api_key != settings.API_KEY:
        raise AppException(401, "Invalid or missing X-API-Key header.")

    summary_text = await generate_llm_summary(payload.text)
    return {"summary": summary_text}
