from pydantic import BaseModel, ConfigDict
from core.models.status import Status


class UserWordBase(BaseModel):
    wrd: str
    translation: str
    status: Status


class NewUserWord(UserWordBase):
    word_id: int
    status: Status = Status.NotStudy


class UserWord(UserWordBase):
    model_config = ConfigDict(from_attributes=True)  # берем только атрибуты
    user_id: int
    word_id: int
    us_wrd_id: int
