from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .word import Word


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    password: Mapped[str | None] = mapped_column(default="", server_default="")
    email: Mapped[str | None] = mapped_column(default="", server_default="")

    # words: Mapped[List["Word"]] = relationship(
    #     secondary="userprogress", back_populates="users"
    # )

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) (username={self.username!r})"

    def __repr__(self):
        return str(self)
