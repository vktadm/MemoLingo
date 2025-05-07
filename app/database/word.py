from typing import Optional
from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Word(Base):
    wrd: Mapped[str] = mapped_column(unique=True)
    translation: Mapped[str]
    transcription: Mapped[Optional[str]] = mapped_column(nullable=True)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    img: Mapped[Optional[str]] = mapped_column(nullable=True)

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) ({self.wrd} - {self.translation!r})"

    def __repr__(self):
        return str(self)
