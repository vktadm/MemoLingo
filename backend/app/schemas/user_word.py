from pydantic import BaseModel
from backend.app.database.status import Status


class UserWordSchema(BaseModel):
    id: int
    status: Status


class CreateUserWordSchema(BaseModel):
    word_id: int
    status: Status
