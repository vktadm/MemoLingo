from typing import List, TYPE_CHECKING, Optional
from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


if TYPE_CHECKING:
    from .category import Category
    from .user import User


class Word(Base):
    wrd: Mapped[str] = mapped_column(String(), unique=True)
    translation: Mapped[str]

    transcription: Mapped[Optional[str]] = mapped_column(nullable=True)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    img: Mapped[Optional[str]] = mapped_column(nullable=True)

    # categories: Mapped[List["Category"]] = relationship(
    #     secondary="category_word_association", back_populates="words"
    # )
    # users: Mapped[List["User"]] = relationship(
    #     secondary="userprogress",
    #     back_populates="words",
    # )

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) ({self.wrd} - {self.translation!r})"

    def __repr__(self):
        return str(self)
