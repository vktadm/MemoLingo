class MainException(Exception):
    detail: str = "Server error!"
    status_code: int = 500

    @property
    def to_dict(self):
        return {
            "detail": self.detail,
            "status_code": self.status_code,
        }


class UserAlreadyExists(MainException):
    detail = "User already exists! Create new username."
    status_code = 404


class UserNotFound(MainException):
    detail = "User not found!"
    status_code = 404


class UserIncorrectPassword(MainException):
    detail: str = "Incorrect password! Try again."
    status_code: int = 401
