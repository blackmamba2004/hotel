from backend.schemas.base import BaseSchema


class UserCredentialsDTO(BaseSchema):
    email: str
    password: str


class AccessTokenDTO(BaseSchema):
    access_token: str
