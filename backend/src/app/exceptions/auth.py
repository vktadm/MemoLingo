from .base import APIException


class TokenException(APIException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Invalid token.",
        )


class TokenExpiredException(APIException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="The token's lifetime has expired!",
        )


class UserAlreadyExistsException(APIException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail="User already exists! Create new username.",
        )


class UserIncorrectPasswordException(APIException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Incorrect password! Try again.",
        )


class UserAlreadyConfirmException(APIException):
    def __init__(self):
        super().__init__(
            status_code=200,
            detail="The user has already been activated.",
        )
