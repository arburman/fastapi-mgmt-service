from fastapi import APIRouter
from app.schema.dtos import JokeResponse
from app.service.joke_service import fetch_random_joke

router = APIRouter(prefix="", tags=["Joke"])


@router.get("/joke", response_model=JokeResponse)
async def get_joke():
    return await fetch_random_joke()
