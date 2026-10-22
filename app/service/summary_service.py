import openai
from app.config.settings import settings
from app.exception.handlers import AppException


async def generate_llm_summary(text: str) -> str:
    if not text.strip():
        raise AppException(400, "Text field cannot be empty.")

    if len(text) > settings.MAX_SUMMARY_LENGTH:
        raise AppException(
            400, f"Text exceeds maximum limit of {settings.MAX_SUMMARY_LENGTH} chars."
        )

    try:
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Summarize the following text concisely in 1-2 sentences."},
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return f"[Mock Summary Provider]: {text[:100]}..."
