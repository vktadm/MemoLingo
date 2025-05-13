from sqlalchemy import ForeignKey, UniqueConstraint, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import expression

from .base import Base


class UserCategory(Base):
    # TODO: Сейчас возможно создавать UserCategory для несуществующего User и Несуществующего Category
    __table_args__ = (UniqueConstraint("user_id", "category_id", name="user_category"),)

    is_creator: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default=expression.false(),
        nullable=False,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id", ondelete="CASCADE"),
    )

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}) (user: {self.user_id}, word: {self.category_id!r})"

    def __repr__(self):
        return str(self)
