"""Joke Controller Module.

Exposes endpoints for fetching random jokes.
"""

from fastapi import APIRouter
from app.schema.dtos import JokeResponse
from app.service.joke_service import fetch_random_joke

router = APIRouter(prefix="", tags=["Joke"])


@router.get("/joke", response_model=JokeResponse)
async def get_joke() -> dict:
  """Fetch a random joke with its category.

  Returns:
      dict: Joke text and category.
  """
  return await fetch_random_joke()