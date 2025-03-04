from sqlalchemy import String, DateTime, func, Enum, ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .user import User
from .word import Word
from .status import Status


class UserProgress(Base):
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.NotStudy)
    t_stamp: Mapped[datetime | None] = mapped_column(
        DateTime, server_default=func.now()
    )
    # repetition: Mapped[str | None]
