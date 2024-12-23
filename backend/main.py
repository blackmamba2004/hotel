from fastapi import FastAPI, Depends

from backend.api import api_router


app = FastAPI()


app.include_router(api_router)
