from pydantic import BaseModel
from typing import List

class UserInput(BaseModel):
    budget : float
    experience : List(str)
    location : str
    

class RankingData(BaseModel):
    hotel_name : str
    image_url : str
    rating : float

class AspectData(BaseModel):
    aspect: str
    sentiment : float

class DestinationInfo(RankingData):
    description: str
    amenities : List(str)
    aspect_rating : List(AspectData)
    