from enum import Enum


class Status(Enum):
    new = "new"
    known = "know"
    revise = "revise"
    end = "end"
