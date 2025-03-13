from pydantic import BaseModel, ConfigDict
from core.models.status import Status


class UserWordBase(BaseModel):
    """Базовая схема для представления слова со статусом."""

    status: Status


class NewUserWord(UserWordBase):
    """Схема для нового слова для пользователя,
    которого еще нет в таблице UserProgress"""

    id: int
    wrd: str
    translation: str
    status: Status = Status.NotStudy  # выставляем всем словам статус "Новое слово"


class UserWord(UserWordBase):
    """Схема для слова,
    которое есть в таблице UserProgress"""

    model_config = ConfigDict(from_attributes=True)  # берем только атрибуты
    user_id: int
    id: int
