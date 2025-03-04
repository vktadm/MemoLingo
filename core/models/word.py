from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Word(Base):
    wrd: Mapped[str]
    translation: Mapped[str]
    transcription: Mapped[str | None]
    description: Mapped[str | None]
