from typing import Optional

from pydantic import BaseModel


class UserLoginFormSchema(BaseModel):
    username: str
    password: str


class GoogleUserDataSchema(BaseModel):
    username: str
    google_access_token: str
    email: str
    is_active: bool


class UserLoginSchema(BaseModel):
    id: Optional[int] = None
    access_token: str
    user_role: str
