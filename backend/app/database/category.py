from typing import Optional, List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Category(Base):
    title: Mapped[str] = mapped_column(unique=True)
    translation: Mapped[Optional[str]] = mapped_column(nullable=True)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    icon: Mapped[Optional[str]] = mapped_column(nullable=True)
    words: Mapped[List["Word"]] = relationship(
        "Word", secondary="categoryword", back_populates="categories"
    )

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) (title={self.title!r})"

    def __repr__(self):
        return str(self)
