import re
from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    ConfigDict,
    Field,
    field_validator,
)


class UserSchema(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    password: Optional[str] = None
    google_access_token: Optional[str] = None
    is_active: bool = False

    model_config = ConfigDict(from_attributes=True)


class UserCreateSchema(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=20,
        examples=["your_username"],
    )
    email: EmailStr = Field(
        default=None,
        examples=["user@example.com"],
        description="Must be valid email format",
    )
    password: str = Field(
        min_length=6,
        max_length=20,
        description="6-20 chars, 1 uppercase, 1 lowercase and 1 digit",
    )

    @field_validator("username")
    def validate_username(cls, value: str) -> str:
        restricted = ["admin", "root", "moderator", "system"]
        if value.lower() in restricted:
            raise ValueError(f"Username '{value}' is restricted")

        if "__" in value:
            raise ValueError("Username cannot contain consecutive underscores")

        return value

    @field_validator("password")
    def validate_password(cls, value: str) -> str:
        if len(value) < 6 or len(value) > 20:
            raise ValueError("Password must be 6-20 characters long")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least 1 lowercase letter")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least 1 uppercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least 1 digit")
        return value


class UpdateUserSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    password: Optional[str] = None
    google_access_token: Optional[str] = None
