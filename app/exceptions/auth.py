from app.exceptions.base import MainException


class TokenException(MainException):
    detail = "Invalid token."
    status_code = 401


class TokenExpired(TokenException):
    detail = "The token's lifetime has expired!"
