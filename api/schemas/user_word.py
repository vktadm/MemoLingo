from pydantic import BaseModel
from database.status import Status


class UserWord(BaseModel):
    """"""

    id: int | None = None
    user_id: int
    word_id: int
    status: Status | None


class CreateUserWord(BaseModel):
    """"""

    user_id: int
    word_id: int
    status: Status
