from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import BaseModel


class Hotel(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    location: Mapped[str] = mapped_column(nullable=False)
    image_id: Mapped[int] = mapped_column()
    
    rooms = relationship("Room", back_populates="hotel")
