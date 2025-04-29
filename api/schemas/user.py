from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    username: str
    password: str | None
    google_access_token: str | None
    email: EmailStr | None
    name: str | None


class UserCreateSchema(BaseModel):
    username: str | None = None
    password: str | None = None
    google_access_token: str | None = None
    email: EmailStr | None = None
    name: str | None = None
