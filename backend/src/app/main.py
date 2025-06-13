import uvicorn
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from backend.src.app.settings import settings
from backend.src.app.handlers import routers


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Контекст жизненного цикла приложения"""
    logger.info("Starting application...")
    try:
        yield
    finally:
        logger.info("Shutting down application...")


def create_app() -> FastAPI:
    """Фабрика для создания приложения FastAPI"""
    app = FastAPI(
        title="MemoLingo API",
        description="API for MemoLingo",
        version="1.0.0",
        lifespan=lifespan,
    )
    # Настройка CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    main_router = APIRouter(tags=["Main"])

    # Подключаем main handlers
    @app.get("/", response_class=JSONResponse)
    async def index():
        return {"message": "Hello! Welcome to MemoLingo!"}

    app.include_router(main_router)

    # Подключаем API handlers
    for itm in routers:
        app.include_router(
            prefix=settings.api_prefix,
            router=itm,
        )

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
