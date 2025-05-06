from pydantic import BaseModel, EmailStr, ConfigDict


class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr | None = None
    name: str | None = None
    model_config = ConfigDict(from_attributes=True)
