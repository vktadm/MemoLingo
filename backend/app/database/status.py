from enum import Enum


class Status(Enum):
    new = "new"  # Новое слово
    known = "know"  # На этапе "learn" пользователь пропустил
    revise = "revise"  # Изучает слово
    end = "master"  # Заучил слово в приложении
