from contextlib import asynccontextmanager
from fastapi import FastAPI

from config import settings
from api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router, prefix=settings.api_prefix)


@app.get("/")
def default_page():
    return {
        "message": "This is MemoLingo",
    }
