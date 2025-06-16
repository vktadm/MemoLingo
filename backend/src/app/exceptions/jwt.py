from .base import APIException


class TokenException(APIException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Invalid token or the token's lifetime has expired!",
        )
