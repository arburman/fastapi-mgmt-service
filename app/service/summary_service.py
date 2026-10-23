"""Summary Service Module.

Handles business logic for generating text summaries using LLM providers.
"""

import openai
from app.config.openai_client_configs import get_openai_client_configs
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
    config = get_openai_client_configs(text)

    try:
        client_kwargs = {"api_key": config["api_key"]}
        if "base_url" in config:
            client_kwargs["base_url"] = config["base_url"]

        client = openai.OpenAI(**client_kwargs)
        
        response = client.chat.completions.create(
            model=config["model"],
            messages=config["messages"],
        )
        return response.choices[0].message.content.strip()
    except Exception as exc:
        if not settings.OPENAI_API_KEY:
            return f"[Mock Summary Provider]: {text[:100]}..."
        handle_summary_provider_error(exc)