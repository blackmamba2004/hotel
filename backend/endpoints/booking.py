from fastapi import APIRouter, BackgroundTasks, Depends, Request, Security
# from pydantic import parse_obj_as

from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud import crud_booking
from backend.deps import get_db
from backend.exceptions import RoomCannotBeBooked
from backend.pkg.auth.middlewares.jwt.service import check_access_token
from backend.schemas.booking import GettingBookingInfo, CreatingBooking


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
    dependencies=[Security(check_access_token)]
)


@router.get(
    path="", 
    name="Получить все бронирования пользователя"
)
async def get_bookings(
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> list[GettingBookingInfo]:
    return await crud_booking.find_all_with_images(db, user_id=request.state.user.id)


@router.post(
    path="",
    name="Забронировать номер",
    status_code=201
)
async def add_booking(
    request: Request,
    booking: CreatingBooking,
    db: AsyncSession = Depends(get_db)
):
    booking = await crud_booking.add(
        db, request.state.user.id,
        booking.room_id,
        booking.date_from,
        booking.date_to,
    )
    if not booking:
        raise RoomCannotBeBooked
    return booking


@router.delete(
    path="/{booking_id}",
    name="Удалить бронь"
)
async def remove_booking(
    request: Request,
    booking_id: int,
    db: AsyncSession = Depends(get_db)
):
    await crud_booking.delete(
        db, id=booking_id, user_id=request.state.user.id
    )
