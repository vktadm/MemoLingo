from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, ConfigDict


class BaseUser(BaseModel):
    username: str


class CreateUser(BaseUser):
    username: Annotated[str, MinLen(3), MaxLen(30)]  # TODO: lower()
    # email: EmailStr


class User(BaseUser):
    model_config = ConfigDict(strict=True)
    id: int
