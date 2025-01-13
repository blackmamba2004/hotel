from pydantic import Field

from backend.schemas.base import BaseSchema


class GettingRoom(BaseSchema):
    id: int
    hotel_id: int
    number: int
    description: str | None = Field(None)
    price: int
    image_url: str | None = Field(None)
