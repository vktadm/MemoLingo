from sqlalchemy import (
    String,
    DateTime,
    func,
    Enum,
    ForeignKey,
    UniqueConstraint,
    Integer,
)
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .status import Status


class UserProgress(Base):
    # TODO: Сейчас возможно создавать UserProgres для несуществующего User
    __table_args__ = (UniqueConstraint("user_id", "word_id", name="user_word"),)

    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.NotStudy)
    t_stamp: Mapped[datetime | None] = mapped_column(
        DateTime, server_default=func.now()
    )
    # repetition: Mapped[str | None]

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    word_id: Mapped[int] = mapped_column(ForeignKey("word.id"))
