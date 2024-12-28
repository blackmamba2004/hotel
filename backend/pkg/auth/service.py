from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud.user import crud_user
from backend.pkg.auth.dto import UserCredentialsDTO, AccessTokenDTO
from backend.pkg.auth.middlewares.jwt.base.auth import JWTAuth
from backend.pkg.auth.errors import AuthError
from backend.pkg.errors import ErrorObj
from backend.schemas.user import CreatingUser


class AuthService:
    def __init__(self, jwt_auth: JWTAuth):
        self._jwt_auth = jwt_auth

    async def register(
        self, db: AsyncSession, obj_in: CreatingUser
    ) -> tuple[AccessTokenDTO, None] | tuple[None, ErrorObj]:
        if await crud_user.get_by(db, email=obj_in.email) is not None:
            return None, AuthError.get_email_occupied_error()

        user = await crud_user.create(db, obj_in)

        access_token = self._jwt_auth.generate_unlimited_access_token(subject=str(user.id))

        return AccessTokenDTO(access_token=access_token), None
    
    async def login(
        self, db: AsyncSession, obj_in: UserCredentialsDTO
    ) -> tuple[AccessTokenDTO, None] | tuple[None, ErrorObj]:
        
        user = await crud_user.authenticate(
            db, email=obj_in.email,
            password=obj_in.password
        )

        if not user:
            return None, AuthError.get_invalid_credentials_error()
        
        access_token = self._jwt_auth.generate_unlimited_access_token(subject=str(user.id))

        return AccessTokenDTO(access_token=access_token), None
