from datetime import date, datetime, timedelta
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud import crud_hotel
from backend.exceptions import CannotBookHotelForLongPeriod, DateFromCannotBeAfterDateTo
from backend.schemas.hotel import GettingHotel, GettingHotelInfo

router = APIRouter(prefix="/hotels", tags=["Отели"])


# @router.get("")
# async def get_hotels_by_location_and_time(
#     location: str,
#     db: AsyncSession = Depends(),
#     date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
#     date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
# ) -> List[GettingHotelInfo]:
#     if date_from > date_to:
#         raise DateFromCannotBeAfterDateTo
#     if (date_to - date_from).days > 31:
#         raise CannotBookHotelForLongPeriod 
#     hotels = await crud_hotel.find_all(db, location, date_from, date_to)
#     return hotels


# @router.get("/{hotel_id}", include_in_schema=True)
# async def get_hotel_by_id(
#     hotel_id: int,
#     db: AsyncSession = Depends(get_db)
# ) -> Optional[GettingHotel]:
#     return await crud_hotel.get(db, id=hotel_id)
