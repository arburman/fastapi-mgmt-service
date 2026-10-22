"""Summary Service Module.

Handles business logic for generating text summaries using LLM providers.
"""

import openai
from app.config.settings import settings
from app.service.error_handlers.summary_error_handler import (
    handle_summary_provider_error,
    validate_summary_payload,
)


async def generate_llm_summary(text: str) -> str:
  """Validate payload and generate an LLM summary.

  Args:
      text (str): Input text to be summarized.

  Returns:
      str: Summarized text output.
  """
  validate_summary_payload(text)

  try:
    client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Summarize the following text concisely in 1-2 sentences."
                ),
            },
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content.strip()
  except Exception as exc:
    if not settings.OPENAI_API_KEY:
      return f"[Mock Summary Provider]: {text[:100]}..."
    handle_summary_provider_error(exc)