from sqlalchemy import (
    DateTime,
    func,
    Enum,
    ForeignKey,
    UniqueConstraint,
)
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .status import Status


class UserWord(Base):
    # TODO: Сейчас возможно создавать UserWord для несуществующего User и Несуществующего Word
    __table_args__ = (UniqueConstraint("user_id", "word_id", name="user_word"),)

    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.new)
    t_stamp: Mapped[datetime | None] = mapped_column(
        DateTime, server_default=func.now()
    )
    # repetition: Mapped[str | None]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
    )
    word_id: Mapped[int] = mapped_column(ForeignKey("word.id", ondelete="CASCADE"))
