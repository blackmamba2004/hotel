from datetime import timedelta
from dataclasses import dataclass

from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env'
    )

    API_STR: str

    JWT_SECRET_KEY: str
    ALGORITHM: str

    ACCESS_TOKEN_TTL: int
    REFRESH_TOKEN_TTL: int

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_DB: str

    SQLALCHEMY_ASYNC_DATABASE_URI: PostgresDsn | str | None = None

    @field_validator("SQLALCHEMY_ASYNC_DATABASE_URI", mode="before")
    @classmethod
    def async_connect(cls, v: str | None, values: ValidationInfo):
        if isinstance(v, str):
            return v
        
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_SERVER"),
            path=values.data.get("POSTGRES_DB")
        ).unicode_string()
    

@dataclass
class JWTConfig:
    secret: str
    algorithm: str
    access_token_ttl: timedelta = None
    refresh_token_ttl: timedelta = None


settings = Settings()


jwt_config = JWTConfig(
    secret=settings.JWT_SECRET_KEY,
    algorithm=settings.ALGORITHM,
    access_token_ttl=timedelta(seconds=settings.ACCESS_TOKEN_TTL),
    refresh_token_ttl=timedelta(seconds=settings.REFRESH_TOKEN_TTL),
)