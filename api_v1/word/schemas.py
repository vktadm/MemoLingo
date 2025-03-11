from pydantic import BaseModel, ConfigDict


class WordBase(BaseModel):
    wrd: str
    translation: str

    # transcription: str | None
    # description: str | None
    # img: str | None


class WordCreate(WordBase):
    pass


class WordUpdate(WordBase):
    wrd: str | None
    translation: str | None


class Word(WordBase):
    model_config = ConfigDict(from_attributes=True)  # берем только атрибуты
    id: int
