from sqlalchemy import ForeignKey, UniqueConstraint, Table, Column, Integer

# from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .category import Category
from .word import Word


category_word_association = Table(
    "category_word_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("category_id", ForeignKey("category.id"), nullable=False),
    Column("word_id", ForeignKey("word.id"), nullable=False),
    UniqueConstraint("category_id", "word_id", name="category_word"),
)
# class CategoryWord(Base):
#     alt_translation: Mapped[str | None]
#
#     category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
#     word_id: Mapped[int] = mapped_column(ForeignKey("word.id"))
#
#     category: Mapped["Category"] = relationship(
#         back_populates="words",
#     )
#     word: Mapped["Word"] = relationship(back_populates="categories")
#
#     __table_args__ = (UniqueConstraint("category_id", "word_id", name="category_word"),)
