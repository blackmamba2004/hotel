from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.enums.user import Gender
from backend.models.base import BaseModel


class User(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(index=True, nullable=True)
    last_name: Mapped[str] = mapped_column(index=True, nullable=True)
    patronymic: Mapped[str] = mapped_column(index=True, nullable=True)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[Gender | None] = mapped_column(default=Gender.MALE, server_default=text("'MALE'"))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    bookings = relationship("Booking", back_populates="user")
