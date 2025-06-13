from typing import Optional

from pydantic import BaseModel


class UserLoginFormSchema(BaseModel):
    username: str
    password: str


class GoogleUserDataSchema(BaseModel):
    username: str
    google_access_token: str
    email: str
    name: Optional[str]
    # google_id: int
    # verified_email: bool # TODO сохранять в БД


class UserLoginSchema(BaseModel):
    id: Optional[int] = None
    access_token: str
