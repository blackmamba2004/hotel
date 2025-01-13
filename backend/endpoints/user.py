from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud.user import crud_user
from backend.schemas.user import CreatingUser, GettingUser


router = APIRouter(
    prefix="/users",
    tags=["Пользователи / Админ-панель"]
)


@router.get(
    path="",
    response_model = list[GettingUser],
    name="Получить всех пользователей"
)
async def get_users(
    db: AsyncSession = Depends()
):
    return await crud_user.get_many(db)


@router.post(
    path="",
    response_model=GettingUser,
    name="Создать пользователя"
)
async def create_user(
    body: CreatingUser,
    db: AsyncSession = Depends()
):
    return await crud_user.create(db, body)


@router.get(
    path="/{user_id}",
    response_model=GettingUser,
    name="Получить пользователя"
)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends()
):
    return await crud_user.get(db, user_id)
