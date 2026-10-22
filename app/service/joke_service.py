import httpx
from app.service.error_handlers.joke_error_handler import handle_joke_upstream_error


async def fetch_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=5.0)
            if response.status_code != 200:
                handle_joke_upstream_error(response=response)
                
            data = response.json()
            return {
                "joke_text": data.get("joke", "No joke found"),
                "category": data.get("category", "General"),
            }
        except httpx.RequestError as exc:
            handle_joke_upstream_error(exc=exc)