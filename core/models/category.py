from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Category(Base):
    title: Mapped[str]
    description: Mapped[str | None]
