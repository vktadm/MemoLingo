from pydantic import BaseModel
from database.status import Status


class UserWordSchema(BaseModel):
    """"""

    id: int | None = None
    user_id: int
    word_id: int
    status: Status | None


class CreateUserWordSchema(BaseModel):
    """"""

    user_id: int
    word_id: int
    status: Status
