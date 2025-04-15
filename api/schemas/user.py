from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    username: str
    # password: str
    # email: EmailStr | None = None


class UserLoginSchema(BaseModel):
    access_token: str
