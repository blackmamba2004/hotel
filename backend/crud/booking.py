from datetime import date
from typing import Any

from sqlalchemy import and_, func, insert, or_, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud.base import CRUDBase
from backend.exceptions import RoomFullyBooked
from backend.models.booking import Booking
from backend.models.room import Room
from backend.schemas.base import BaseSchema
# from backend.schemas.booking import *

# from app.logger import logger


#переделать потом
class CRUDBooking(CRUDBase[Booking, BaseSchema, BaseSchema]):
    async def find_all_with_images(self, db: AsyncSession, user_id: int):
        query = (
            select(
                # __table__.columns нужен для отсутствия вложенности в ответе Алхимии
                Booking.__table__.columns,
                Room.__table__.columns,
            )
            .join(Room, Room.id == Booking.room_id, isouter=True)
            .where(Booking.user_id == user_id)
        )
        result = await db.execute(query)
        return result.mappings().all()

    async def add(
        self,
        db: AsyncSession,
        user_id: int,
        room_id: int,
        date_from: date,
        date_to: date,
    ):
        """
        WITH booked_rooms AS (
            SELECT * FROM bookings
            WHERE room_id = 1 AND
                (date_from >= '2023-05-15' AND date_from <= '2023-06-20') OR
                (date_from <= '2023-05-15' AND date_to > '2023-05-15')
        )
        SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
        LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        WHERE rooms.id = 1
        GROUP BY rooms.quantity, booked_rooms.room_id
        """
        try:
            booked_rooms = (
                select(Booking)
                .where(
                    and_(
                        Booking.room_id == room_id,
                        or_(
                            and_(
                                Booking.date_from >= date_from,
                                Booking.date_from <= date_to,
                            ),
                            and_(
                                Booking.date_from <= date_from,
                                Booking.date_to > date_from,
                            ),
                        ),
                    )
                )
                .cte("booked_rooms")
            )

            """
            SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
            LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
            WHERE rooms.id = 1
            GROUP BY rooms.quantity, booked_rooms.room_id
            """

            get_rooms_left = (
                select(
                    (Room.quantity - func.count(booked_rooms.c.room_id)).label(
                        "rooms_left"
                    )
                )
                .select_from(Room)
                .join(booked_rooms, booked_rooms.c.room_id == Room.id, isouter=True)
                .where(Room.id == room_id)
                .group_by(Room.quantity, booked_rooms.c.room_id)
            )

            # logger.debug(get_rooms_left.compile(engine, compile_kwargs={"literal_binds": True}))
            
            rooms_left: int = (await db.execute(get_rooms_left)).scalar()

            # logger.debug(f"{rooms_left=}")

            if rooms_left > 0:
                get_price = select(Room.price).filter_by(id=room_id)
                price: int = (await db.execute(get_price)).scalar()
                add_booking = (
                    insert(Booking)
                    .values(
                        room_id=room_id,
                        user_id=user_id,
                        date_from=date_from,
                        date_to=date_to,
                        price=price,
                    )
                    .returning(
                        Booking.id,
                        Booking.user_id, 
                        Booking.room_id,
                        Booking.date_from,
                        Booking.date_to,
                    )
                )

                new_booking = await db.execute(add_booking)
                await db.commit()
                return new_booking.mappings().one()
            else:
                raise RoomFullyBooked
        except RoomFullyBooked:
            raise RoomFullyBooked
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc: Cannot add booking"
            elif isinstance(e, Exception):
                msg = "Unknown Exc: Cannot add booking"
            extra = {
                "user_id": user_id,
                "room_id": room_id,
                "date_from": date_from,
                "date_to": date_to,
            }
            # logger.error(msg, extra=extra, exc_info=True)


crud_booking = CRUDBooking(Booking)
