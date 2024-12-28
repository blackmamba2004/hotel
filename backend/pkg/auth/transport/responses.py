from backend.schemas.base import BaseSchema


class AccessTokenOut(BaseSchema):
    access_token: str
