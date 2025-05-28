from pydantic import BaseModel
from backend.src.app.database import Status


class UserWordSchema(BaseModel):
    id: int
    status: Status


class CreateUserWordSchema(BaseModel):
    word_id: int
    status: Status
