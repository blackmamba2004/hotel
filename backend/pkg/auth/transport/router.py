from fastapi import APIRouter, Depends, Request, Security
from sqlalchemy.ext.asyncio import AsyncSession

from backend.deps import get_db
from backend.schemas.user import CreatingUser

from backend.pkg.auth.middlewares.jwt.service import jwt_config
from backend.pkg.auth.middlewares.jwt.base.auth import JWTAuth
from backend.pkg.auth.service import AuthService

from backend.pkg.auth.transport.requests import UserCredentialsIn
from backend.pkg.auth.transport.responses import AccessTokenOut
from backend.pkg.errors import get_bad_request_error_response
from backend.pkg.responses import ErrorOut


router = APIRouter(
    prefix="/auth"
)


def get_auth_service() -> AuthService:
    return AuthService(jwt_auth=JWTAuth(config=jwt_config))


@router.post(
    path='/register',
    tags=['Регистрация / Клиентское приложение'],
    name="Зарегистрироваться",
    responses={
        200 : {'model': AccessTokenOut},
        400 : {'model': ErrorOut}
    }
)
async def register_user(
    body: CreatingUser,
    db: AsyncSession = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service)
) -> AccessTokenOut:
    data, error = await auth_service.register(db, body)

    if error:
        return get_bad_request_error_response(error=error)

    return data


@router.post(
    path='/login',
    tags=['Вход / Клиентское приложение'],
    name="Войти в приложение",
    responses={
        200 : {'model': AccessTokenOut},
        400 : {'model': ErrorOut}
    }
)
async def login_user(
    body: UserCredentialsIn,
    db: AsyncSession = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service)
) -> AccessTokenOut:
    data, error = await auth_service.login(db, body)

    if error:
        return get_bad_request_error_response(error=error)

    return data
