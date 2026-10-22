import httpx
from app.exception.handlers import AppException


async def fetch_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=5.0)
            if response.status_code != 200:
                raise AppException(502, "Failed to fetch joke from upstream.")
            data = response.json()
            return {
                "joke_text": data.get("joke", "No joke found"),
                "category": data.get("category", "General"),
            }
        except Exception:
            raise AppException(502, "Joke service currently unavailable.")
