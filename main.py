from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.engine import engine, Base
from routes import app_router
from settings.lifespan import init_db


def get_app() -> FastAPI:
    app = FastAPI(lifespan=init_db)
    app.include_router(app_router)
    return app


api = get_app()
