from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


class UserSchema(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    password: Optional[str] = None
    google_access_token: Optional[str] = None
    is_active: bool = False

    model_config = ConfigDict(from_attributes=True)
