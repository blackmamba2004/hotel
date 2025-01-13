from datetime import date

from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import BaseModel


class Booking(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    room_id: Mapped[int] = mapped_column(
        ForeignKey("room.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True
    )
    date_from: Mapped[date] = mapped_column(nullable=False, index=True)
    date_to: Mapped[date] = mapped_column(nullable=False, index=True)
    price: Mapped[float] = mapped_column(nullable=False)
    # total_cost: Mapped[float] = mapped_column(Computed("(date_to - date_from) * price"))
    # total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))

    __table_args__ = (
        CheckConstraint("date_from < date_to", name="check_date"),
    )

    user = relationship("User", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")
