from pydantic import ConfigDict, EmailStr, Field
from backend.schemas.base import BaseSchema

class UserCredentialsIn(BaseSchema):
    email: EmailStr = Field(min_length=1, max_length=254)
    password: str = Field(min_length=1)

    model_config = ConfigDict(str_strip_whitespace=True)
