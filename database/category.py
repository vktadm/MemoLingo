from typing import List, TYPE_CHECKING
from sqlalchemy import String

from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base


if TYPE_CHECKING:
    from .word import Word


class Category(Base):
    title: Mapped[str] = mapped_column(String(), unique=True)
    translation: Mapped[str]
    description: Mapped[str | None] = mapped_column(default="", server_default="")
    # words: Mapped[List["Word"]] = relationship(
    #     secondary="category_word_association", back_populates="categories"
    # )

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) (title={self.title!r})"

    def __repr__(self):
        return str(self)
