from typing import Optional
from pydantic import BaseModel, ConfigDict


class BaseWordSchema(BaseModel):
    wrd: str
    translation: str
    transcription: Optional[str]
    description: Optional[str]
    img: Optional[str]


class CreateWordSchema(BaseWordSchema):
    wrd: str
    translation: str
    transcription: Optional[str] = None
    description: Optional[str] = None
    img: Optional[str] = None


class UpdateWordSchema(CreateWordSchema):
    id: Optional[int] = None
    wrd: Optional[str] = None
    translation: Optional[str] = None


class WordSchema(BaseWordSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int
