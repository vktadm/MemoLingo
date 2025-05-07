from app.exceptions.base import MainException


class NotFound(MainException):
    detail: str = "There are no records yet."
    status_code: int = 404
