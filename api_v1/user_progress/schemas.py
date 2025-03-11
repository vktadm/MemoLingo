from pydantic import BaseModel, ConfigDict
from core.models.status import Status


class UserWordBase(BaseModel):
    status: Status


class UserWord(UserWordBase):
    model_config = ConfigDict(from_attributes=True)  # берем только атрибуты
    user_id: int
    word_id: int
