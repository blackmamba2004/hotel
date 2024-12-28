from datetime import date
from typing import Optional

from backend.schemas.base import BaseSchema


class GettingBooking(BaseSchema):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int


class GettingBookingInfo(GettingBooking):
    image_id: int
    name: str
    description: Optional[str]


class CreatingBooking(BaseSchema):
    room_id: int
    date_from: date
    date_to: date
