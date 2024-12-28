from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import BaseModel


class Room(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotel.id"), nullable=False)
    number: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int]

    hotel = relationship("Hotel", back_populates="rooms")
    bookings = relationship("Booking", back_populates="room")
