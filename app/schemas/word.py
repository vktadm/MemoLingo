from typing import Optional
from pydantic import BaseModel, ConfigDict


class BaseWordSchema(BaseModel):
    wrd: str
    translation: str
    transcription: Optional[str]
    description: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class CreateWordSchema(BaseWordSchema):
    transcription: Optional[str] = None
    description: Optional[str] = None


class UpdateWordSchema(CreateWordSchema):
    wrd: Optional[str] = None
    translation: Optional[str] = None


class WordSchema(BaseWordSchema):
    id: int
    img: Optional[str]
