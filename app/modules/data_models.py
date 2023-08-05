from pydantic import BaseModel, Json
from typing import List


class UserInput(BaseModel):
    budget: str
    experience: List(str)
    region: str


class HotelData(BaseModel):
    id: str
    reviews_count: int
    rating: float
    price: float
    experience: Json
    latitude: float
    longitude: float
    price_bins: str


class RankingData(HotelData):
    cosine_similarity: str
    weighted_score: str


class OutputData(BaseModel):
    id: str
    hotel_name: str
    price: float
    rating: float
    city: str
    experience: Json
    images: Json


class AspectData(BaseModel):
    aspect: str
    sentiment: float


class DestinationInfo(RankingData):
    description: str
    amenities: List(str)
    aspect_rating: List(AspectData)
