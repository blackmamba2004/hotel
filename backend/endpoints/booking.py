from fastapi import APIRouter, Depends, Request, Security

from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud import crud_booking
from backend.exceptions import RoomCannotBeBooked
from backend.pkg.auth.middlewares.jwt.service import check_access_token
from backend.schemas.booking import GettingBooking, CreatingBooking


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
    dependencies=[Security(check_access_token)]
)


@router.get(
    path="/me",
    name="Получить все бронирования пользователя"
)
async def get_me_bookings(
    request: Request,
    db: AsyncSession = Depends(),
) -> list[GettingBooking]:
    return await crud_booking.get_many_by(db, user_id=request.state.user.id)


@router.post(
    path="",
    name="Забронировать номер",
    status_code=201
)
async def add_booking(
    request: Request,
    obj_in: CreatingBooking,
    db: AsyncSession = Depends()
) -> GettingBooking:
    booking = await crud_booking.create(
        db, obj_in, request.state.user.id
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
    db: AsyncSession = Depends()
) -> None:
    await crud_booking.delete(
        db, id=booking_id, user_id=request.state.user.id
    )
