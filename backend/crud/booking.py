from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud.base import CRUDBase
from backend.crud.room import CRUDRoom
from backend.exceptions import RoomFullyBooked
from backend.models import Booking, Room
from backend.schemas.booking import CreatingBooking, UpdatingBooking


class CRUDBooking(CRUDBase[Booking, CreatingBooking, UpdatingBooking]):
    async def create(
        self,
        db: AsyncSession,
        obj_in: CreatingBooking,
        user_id: int
    ):
        room_id = obj_in.room_id
        date_from = obj_in.date_from
        date_to = obj_in.date_to
        
        is_booked = await CRUDRoom.is_booked(
            db, room_id, date_from, date_to
        )

        if is_booked:
            raise RoomFullyBooked

        get_price = (
            await db.execute(
                select(Room.price).where(Room.id == room_id)
            )
        ).scalar()

        price = (date_to - date_from).days * get_price
        
        return await super().create(
            db, obj_in, user_id=user_id, price=price
        )


crud_booking = CRUDBooking(Booking)
