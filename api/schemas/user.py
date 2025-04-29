from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    password: str | None = None
    google_access_token: str | None = None
    email: EmailStr | None = None
    name: str | None = None


class UserLoginSchema(BaseModel):
    access_token: str
