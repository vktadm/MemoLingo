import uvicorn
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse

from backend.src.app.settings import settings
from backend.src.app.handlers import routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Здесь можно добавить код инициализации при запуске
    yield
    # Здесь можно добавить код очистки при завершении


def create_app() -> FastAPI:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    app = FastAPI(lifespan=lifespan)
    main_router = APIRouter(tags=["Main"])

    # Подключаем main handlers
    @app.get("/", response_class=JSONResponse)
    async def index():
        return {"message": "Hello! Welcome to MemoLingo!"}

    app.include_router(main_router)

    # Подключаем API handlers
    for itm in routers:
        app.include_router(prefix=settings.api_prefix, router=itm)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
