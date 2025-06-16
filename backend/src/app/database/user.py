from datetime import datetime
from typing import Optional

from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import expression

from .base import Base
from .role import UserRole


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    password: Mapped[str] = mapped_column(String(120), nullable=True)
    google_access_token: Mapped[Optional[str]] = mapped_column(nullable=True)
    email: Mapped[Optional[str]] = mapped_column(nullable=True, unique=True)
    user_role: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default=UserRole.USER,
        server_default=UserRole.USER,
    )
    join_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_date(),
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default=expression.false(),
        nullable=False,
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, email={self.email!r})"

    def __repr__(self):
        return (
            f"<User(id={self.id}, username={self.username!r}, "
            f"email={self.email!r}, is_active={self.is_active})>"
        )
