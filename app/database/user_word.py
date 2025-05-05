from typing import Optional

from sqlalchemy import (
    DateTime,
    func,
    Enum,
    ForeignKey,
    UniqueConstraint,
)
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .status import Status


class UserWord(Base):
    # TODO: Сейчас возможно создавать UserWord для несуществующего User и Несуществующего Word
    __table_args__ = (UniqueConstraint("user_id", "word_id", name="user_word"),)

    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.new)
    t_stamp: Mapped[Optional[datetime]] = mapped_column(
        DateTime, server_default=func.now()
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
    )
    word_id: Mapped[int] = mapped_column(ForeignKey("word.id", ondelete="CASCADE"))

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) (user: {self.user_id}, word: {self.word_id!r})"

    def __repr__(self):
        return str(self)
