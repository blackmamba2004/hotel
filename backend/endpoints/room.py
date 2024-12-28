from datetime import date, datetime, timedelta
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud import crud_room
from backend.deps import get_db
from backend.schemas.room import GettingRoomInfo

router = APIRouter(prefix="/hotels", tags=["Отели / Комнаты"])


@router.get("/{hotel_id}/rooms")
async def get_rooms_by_time(
    hotel_id: int,
    db: AsyncSession = Depends(get_db),
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
) -> List[GettingRoomInfo]:
    rooms = await crud_room.find_all(db, hotel_id, date_from, date_to)
    return rooms
