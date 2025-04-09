from sqlalchemy import ForeignKey, UniqueConstraint, Table, Column, Integer

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class CategoryWordAssociation(Base):
    __tablename__ = "category_word_association"
    __table_args__ = (UniqueConstraint("category_id", "word_id", name="category_word"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    word_id: Mapped[int] = mapped_column(ForeignKey("word.id"))


# category_word_association = Table(
#     "category_word_association",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("category_id", ForeignKey("category.id"), nullable=False),
#     Column("word_id", ForeignKey("word.id"), nullable=False),
#     UniqueConstraint("category_id", "word_id", name="category_word"),
# )
