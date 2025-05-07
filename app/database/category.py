from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Category(Base):
    title: Mapped[str] = mapped_column(unique=True)
    translation: Mapped[Optional[str]] = mapped_column(nullable=True)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    icon: Mapped[Optional[str]] = mapped_column(nullable=True)

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) (title={self.title!r})"

    def __repr__(self):
        return str(self)
