from sqlalchemy.orm import Mapped

from .base import Base


class Category(Base):
    title: Mapped[str]
    # description: Mapped[str]
