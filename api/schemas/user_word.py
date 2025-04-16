from pydantic import BaseModel
from database.status import Status


class UserWordSchema(BaseModel):
    id: int
    status: Status


class CreateUserWordSchema(BaseModel):
    word_id: int
    status: Status
