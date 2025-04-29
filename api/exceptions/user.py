from api.exceptions.base import MainException


class UserAlreadyExists(MainException):
    detail = "User already exists! Create new username."
    status_code = 403


class UserNotFound(MainException):
    detail = "User not found!"
    status_code = 404


class UserIncorrectPassword(MainException):
    detail = "Incorrect password! Try again."
    status_code = 401


class UserNoCreate(MainException):
    detail = "Failed to create a user!"
    status_code = 401
