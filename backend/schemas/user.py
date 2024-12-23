from backend.enums.user import Gender
from backend.schemas.base import BaseSchema


class CreatingUser(BaseSchema):
    first_name: str | None = None
    last_name: str | None = None
    patronymic: str | None = None
    email: str
    password: str
    gender: Gender | None = None


class UpdatingUser(BaseSchema):
    first_name: str | None = None
    last_name: str | None = None
    patronymic: str | None = None
    email: str | None = None
    gender: Gender | None = None


class GettingUser(BaseSchema):
    id: int
    first_name: str | None = None
    last_name: str | None = None
    patronymic: str | None = None
    email: str
    gender: Gender | None = None
