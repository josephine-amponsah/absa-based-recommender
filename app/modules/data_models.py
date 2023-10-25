from pydantic import BaseModel, Json
from typing import List


class UserInput(BaseModel):
    budget: str
    experience: list
    region: str


class HotelData(BaseModel):
    id: str
    reviews_count: int
    total_score: float
    price: float
    experience: Json
    latitude: float
    longitude: float
    price_bins: str
    title: str
    city: str
    phone: str
    image_urls: Json
    website: str
    category_name: str
    region: str


class RankingData(HotelData):
    cosine_similarity: float
    weighted_score: float


class OutputData(HotelData):
    cos_sim: float
    weighted_score: float


class AspectData(BaseModel):
    aspect: str
    sentiment: float


class DestinationInfo(RankingData):
    description: str
    amenities: list
    aspect_rating: AspectData
