# from typing import Any
from fastapi import Request

from datetime import date

from sqlalchemy import and_, exists, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import CTE, Select

from backend.crud.base import CRUDBase
from backend.models import Booking, Room


class CRUDRoom(CRUDBase):
    def get_booked_rooms(
        self, date_from, date_to, as_cte=False
    ) -> CTE | Select:
        query = (
            select(Room.id)
            .join(Booking, Room.id == Booking.room_id)
            .where(
                and_(
                    Booking.date_to >= date_from,
                    Booking.date_from <= date_to,
                )
            )
        )
        return (
            query.cte("booked_rooms") if as_cte 
            else query
        )

    @classmethod
    async def is_booked(
        cls,
        db: AsyncSession, 
        room_id: int,
        date_from: date, 
        date_to: date,
    ) -> bool:
        query = (
            select(
               exists(
                   select(1)
                   .select_from(Room)
                   .join(Booking, Room.id == Booking.room_id)
                   .where(
                       and_(
                           Room.id == room_id,
                           Booking.date_to >= date_from,
                           Booking.date_from <= date_to
                       )
                   )
                   .limit(1)
                )
            )
        )

        return (await db.execute(query)).scalar()
    
    async def get_rooms_with_images(
        self, 
        db: AsyncSession, 
        base_url: str,
        date_from: date, 
        date_to: date,
    ):
        booked_rooms: CTE = self.get_booked_rooms(date_from, date_to, as_cte=True)

        get_rooms_left = (
            select(
                Room.id,
                Room.hotel_id,
                Room.number, 
                Room.description,
                Room.price,
                (base_url + Room.image_url).label("image_url")
            )
            .outerjoin(booked_rooms, Room.id == booked_rooms.c.id)
            .where(booked_rooms.c.id == None)
        )

        rooms = (await db.execute(get_rooms_left)).mappings().all()

        return rooms

crud_room = CRUDRoom(Room)
