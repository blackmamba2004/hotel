from typing import Optional

from backend.schemas.base import BaseSchema


class GettingRoom(BaseSchema):
    id: int
    hotel_id: int
    name: str
    description: Optional[str]
    price: int
    image_id: int


class GettingRoomInfo(GettingRoom):
    total_cost: int
    rooms_left: int
