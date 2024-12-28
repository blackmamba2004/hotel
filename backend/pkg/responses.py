from backend.schemas.base import BaseSchema


class ErrorOut(BaseSchema):
    type: str
    message: str
