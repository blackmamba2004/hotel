from typing import List

from backend.schemas.base import BaseSchema


class GettingHotel(BaseSchema):
    id: int
    name: str
    location: str
    image_id: int


class GettingHotelInfo(GettingHotel):
    rooms_left: int
