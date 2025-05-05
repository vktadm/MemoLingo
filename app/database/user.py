from typing import TYPE_CHECKING, Optional

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import expression

from .base import Base

if TYPE_CHECKING:
    from .word import Word


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    password: Mapped[str] = mapped_column(String(120), nullable=True)
    google_access_token: Mapped[Optional[str]] = mapped_column(nullable=True)
    # TODO: сделать обязательным
    email: Mapped[Optional[str]] = mapped_column(nullable=True, unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default=expression.false(),
        nullable=False,
    )

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) (username={self.username!r})"

    def __repr__(self):
        return str(self)
