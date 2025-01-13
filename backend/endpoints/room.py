from datetime import date

from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud import crud_room
from backend.schemas.room import GettingRoom

router = APIRouter(prefix="/hotels", tags=["Отели / Комнаты"])


@router.get("/rooms")
async def get_rooms_by_time(
    date_from: date,
    date_to: date,
    request: Request,
    db: AsyncSession = Depends()
) -> list[GettingRoom]:
    base_url = str(request.base_url)
    return await crud_room.get_rooms_with_images(db, base_url, date_from, date_to)
