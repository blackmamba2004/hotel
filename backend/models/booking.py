from datetime import date

from sqlalchemy import Computed, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import BaseModel


class Booking(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id", ondelete="CASCADE", onupdate="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"))
    date_from: Mapped[date] = mapped_column(nullable=False)
    date_to: Mapped[date] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    total_cost: Mapped[float] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))

    user = relationship("User", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")
