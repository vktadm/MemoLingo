from pydantic import BaseModel


class GoogleUserDataSchema(BaseModel):
    id: int
    email: str
    access_token: str
    verified_email: bool
    name: str
