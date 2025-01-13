from fastapi import Depends, Request, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from jwt import decode, InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession

from backend.config import jwt_config
from backend.deps import get_db
from backend.pkg.auth.middlewares.jwt.base.token_types import TokenType
from backend.pkg.auth.middlewares.jwt.errors import AccessError
from backend.crud.user import crud_user


def __try_to_get_clean_token(authorization_header: str | None) -> str:
    if authorization_header is None:
        raise HTTPException(detail=dict(AccessError.get_token_is_not_specified_error()), status_code=400)

    if 'Bearer' not in authorization_header:
        raise HTTPException(detail=dict(AccessError.get_incorrect_auth_header_form_error()), status_code=400)

    return authorization_header.replace('Bearer ', '')


async def check_access_token(
    request: Request,
    db: AsyncSession = Depends(get_db),
    authorization_header: str = Security(APIKeyHeader(name='Authorization', auto_error=False))
):
    clear_token = __try_to_get_clean_token(authorization_header)

    try:
        payload = decode(jwt=clear_token, key=jwt_config.secret, algorithms=[jwt_config.algorithm])
        if payload['type'] != TokenType.ACCESS.value:
            raise HTTPException(detail=dict(AccessError.get_incorrect_token_type_error()), status_code=403)

    except InvalidTokenError:
        raise HTTPException(detail=dict(AccessError.get_invalid_token_error()), status_code=403)
    
    user = await crud_user.get_by(db, id=int(payload['sub']))
    if not user:
        raise HTTPException(detail=dict(AccessError.get_token_owner_not_found()), status_code=403)

    request.state.user = user
