import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.config import settings
from core.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def default_page():
    return {"message": "This is MemoLingo"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
