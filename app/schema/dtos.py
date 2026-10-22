from pydantic import BaseModel, Field


class WeatherResponse(BaseModel):
    city: str
    temperature: float
    condition: str
    humidity: int


class JokeResponse(BaseModel):
    joke_text: str
    category: str


class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=2000)


class SummaryResponse(BaseModel):
    summary: str
