from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .category import Category


class Word(Base):
    wrd: Mapped[str]
    translation: Mapped[str]
    transcription: Mapped[str | None]
    description: Mapped[str | None]
    img: Mapped[str | None]

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) ({self.wrd} -> {self.transcription!r})"

    def __repr__(self):
        return str(self)
