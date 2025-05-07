from typing import Optional
from pydantic import BaseModel


class BaseWordSchema(BaseModel):
    wrd: str
    translation: str
    transcription: Optional[str]
    description: Optional[str]
    img: Optional[str]


class CreateWordSchema(BaseWordSchema):
    transcription: Optional[str] = None
    description: Optional[str] = None
    img: Optional[str] = None


class UpdateWordSchema(CreateWordSchema):
    wrd: Optional[str] = None
    translation: Optional[str] = None


class WordSchema(BaseWordSchema):
    id: int
