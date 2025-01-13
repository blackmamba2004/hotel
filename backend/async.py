import asyncio

from datetime import date

from sqlalchemy import and_, func, insert, or_, select

from backend.deps import get_db
from backend.models import *

{'date_from': date(2023, 6, 15), 
'date_to': date(2023, 6, 30)}

async def main():
    async for db in get_db():
        booked_rooms = (
            select(Booking)
            .where(
                and_(
                    Booking.date_from <= date(2023, 6, 30),
                    Booking.date_to >= date(2023, 6, 15)
                )
            ).cte("booked_rooms")
        )

        get_rooms_left = (
            select(Room.__table__.columns)
            .join(
                booked_rooms, 
                booked_rooms.c.room_id == Room.id, 
                isouter=True
            )
        )

        booked_rooms = await db.execute(get_rooms_left)
        print(booked_rooms.mappings().all())

asyncio.run(main())

# import sys
# print(sys.path)