from sqlalchemy.orm import Mapped

from .base import Base


class Word(Base):
    wrd: Mapped[str]
    translation: Mapped[str]
    # transcription: Mapped[str]
    # description: Mapped[str]
