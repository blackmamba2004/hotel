from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud.base import CRUDBase
from backend.models.user import User
from backend.schemas.base import BaseSchema
from backend.schemas.user import CreatingUser, UpdatingUser
from backend.utils.security import get_password_hash, verify_password


class CRUDUser(CRUDBase[User, CreatingUser, UpdatingUser]):
    async def authenticate(
        self,
        db: AsyncSession,
        email: str,
        password: str
    ) -> User | None:
        user: User | None = await super().get_by(db, email=email)
        if (
            (password is None) or
            (user is None) or 
            not verify_password(password, user.hashed_password) 
        ):
            return None
        return user


    async def _get_db_obj_fields(
        self, obj_in: dict[str, Any] | BaseSchema, **kwargs
    ) -> dict[str, Any]:
        fields = await super()._get_db_obj_fields(obj_in, **kwargs)
        if "password" in fields:
            fields["hashed_password"] = get_password_hash(fields.pop("password"))
        return fields


crud_user = CRUDUser(User)
