from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api import api_router
from backend.deps import get_db

def setup_ioc_container(
    app: FastAPI,
) -> FastAPI:
    app.dependency_overrides.update({
        AsyncSession: get_db,
    })

    return app

app = setup_ioc_container(FastAPI())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # разрешаем доступ с любого источника
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

app.mount("/static", StaticFiles(directory="static"), name="static")
