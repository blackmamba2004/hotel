from datetime import datetime, timezone, timedelta
from typing import Any
import uuid
import jwt

from backend.config import JWTConfig
from backend.pkg.auth.middlewares.jwt.base.token_types import TokenType
from backend.pkg.utils import convert_to_timestamp


class JWTAuth:
    def __init__(self, config: JWTConfig):
        self._config=config

    def generate_unlimited_access_token(
        self, subject: str, payload: dict[str, Any] = None
    ) -> str:
        return self.__sign_token(
            token_type=TokenType.ACCESS.value,
            subject=subject, payload=payload
        )

    def generate_access_token(
        self, subject: str, payload: dict[str, Any]
    ) -> str:
        return self.__sign_token(
            token_type=TokenType.ACCESS.value,
            subject=subject,
            payload=payload,
            ttl=self._config.access_token_ttl
        )

    def __sign_token(
        self, token_type: str, subject: str,
        payload: dict[str, Any] = None,
        ttl: timedelta = None
    ) -> str:
        current_timestamp = convert_to_timestamp(datetime.now(tz=timezone.utc))

        payload = dict(
            iss='labyrinth@auth_service',
            sub=subject,
            type=token_type,
            jti=self.__generate_jti(),
            iat=current_timestamp,
        )

        return jwt.encode(payload, self._config.secret, self._config.algorithm)

    @staticmethod
    def __generate_jti() -> str:
        return str(uuid.uuid4())
