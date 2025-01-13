from datetime import date

from backend.schemas.base import BaseSchema


class GettingBooking(BaseSchema):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int


class CreatingBooking(BaseSchema):
    room_id: int
    date_from: date
    date_to: date
    

class UpdatingBooking(BaseSchema):
    date_from: date
    date_to: date
