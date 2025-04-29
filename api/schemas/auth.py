from pydantic import BaseModel


class GoogleUserDataSchema(BaseModel):
    id: int
    access_token: str
    email: str
    verified_email: bool
    name: str


class UserLoginSchema(BaseModel):
    access_token: str
