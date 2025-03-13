from pydantic import BaseModel, ConfigDict
from core.models.status import Status


class UserWordBase(BaseModel):
    """Базовая схема для представления слова со статусом."""

    wrd: str
    translation: str
    status: Status


class UserWord(UserWordBase):
    """Схема для слова,
    которое есть в таблице UserProgress"""

    model_config = ConfigDict(from_attributes=True)  # берем только атрибуты
    user_id: int
    word_id: int
    id: int
