from pydantic import BaseModel, ConfigDict


class WordBase(BaseModel):
    wrd: str
    translation: str
    # transcription: str | None
    # description: str | None


class WordCreate(WordBase):
    pass


class WordUpdate(WordCreate):
    wrd: str | None = None
    translation: str | None = None


class WordUpdatePartial(WordCreate):
    pass


class Word(WordBase):
    model_config = ConfigDict(from_attributes=True)  # берем только атрибуты
    id: int
