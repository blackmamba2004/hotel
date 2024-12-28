from fastapi import APIRouter

from backend.config import settings
from backend.endpoints import booking, hotel, room, user
from backend.pkg.auth import router as auth_router


api_router = APIRouter(prefix=settings.API_STR)
api_router.include_router(auth_router)
api_router.include_router(booking.router)
api_router.include_router(hotel.router)
api_router.include_router(room.router)
api_router.include_router(user.router)
