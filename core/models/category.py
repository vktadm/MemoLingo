from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base import Base


if TYPE_CHECKING:
    from .word import Word


class Category(Base):
    title: Mapped[str]
    translation: Mapped[str]
    description: Mapped[str | None]

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) (title={self.title!r})"

    def __repr__(self):
        return str(self)
