from typing import Optional, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Word(Base):
    wrd: Mapped[str] = mapped_column()
    translation: Mapped[str]
    transcription: Mapped[Optional[str]] = mapped_column(nullable=True)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    img: Mapped[Optional[str]] = mapped_column(nullable=True)
    categories: Mapped[List["Category"]] = relationship(
        "Category", secondary="categoryword", back_populates="words"
    )

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) ({self.wrd} - {self.translation!r})"

    def __repr__(self):
        return str(self)
