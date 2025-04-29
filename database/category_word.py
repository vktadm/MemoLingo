from sqlalchemy import ForeignKey, UniqueConstraint, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class CategoryWord(Base):
    __table_args__ = (UniqueConstraint("category_id", "word_id", name="category_word"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    word_id: Mapped[int] = mapped_column(ForeignKey("word.id"))

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) (category: {self.category_id}, word: {self.word_id!r})"

    def __repr__(self):
        return str(self)
