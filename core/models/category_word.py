from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .category import Category
from .word import Word


class CategoryWord(Base):
    alt_translation: Mapped[str | None]
