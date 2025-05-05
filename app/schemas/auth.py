from typing import Optional

from pydantic import BaseModel


class GoogleUserDataSchema(BaseModel):
    username: str
    google_access_token: str
    email: str
    name: Optional[str]
    # google_id: int
    # verified_email: bool


class UserLoginSchema(BaseModel):
    access_token: str
