from pydantic import BaseModel


class Word(BaseModel):
    id: int
    wrd: str
    translation: str

    # transcription: str | None
    # description: str | None
    # img: str | None
