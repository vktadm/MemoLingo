from enum import Enum


class Status(Enum):
    NotStudy = "Новое слово"
    OnStudy = "Слово на изучении"
    EndStudy = "Заученное слово"
