from app.config.settings import settings

def get_openai_client_configs(text: str) -> dict:
    """Generate client initialization and chat completion configurations."""
    messages = [
        {
            "role": "system",
            "content": "Summarize the following text concisely in 1-2 sentences.",
        },
        {"role": "user", "content": text},
    ]
    params = {
        "api_key": settings.OPENAI_API_KEY,
        "model": settings.OPENAI_MODEL_SEMVER,
        "messages": messages,
    }

    if settings.OPENAI_API_KEY == "ollama":
        return {
            "base_url": settings.OLLAMA_BASE_URL,
            **params
        }

    return params