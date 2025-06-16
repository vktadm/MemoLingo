from .base import APIException


class UserNotFoundException(APIException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="User not found. Try again!",
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


class UserForbiddenException(APIException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail="Forbidden resource.",
        )
