from typing import TYPE_CHECKING, Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

if TYPE_CHECKING:
    from .word import Word


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    password: Mapped[str] = mapped_column(String(120), nullable=True)
    google_access_token: Mapped[Optional[str]] = mapped_column(nullable=True)
    email: Mapped[Optional[str]] = mapped_column(nullable=True)
    name: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) (username={self.username!r})"

    def __repr__(self):
        return str(self)
