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
    status_code = 403


class UserNotFound(MainException):
    detail = "User not found!"
    status_code = 404


class UserIncorrectPassword(MainException):
    detail = "Incorrect password! Try again."
    status_code = 401


class TokenException(MainException):
    detail = "Invalid token."
    status_code = 401


class TokenExpired(TokenException):
    detail = "The token's lifetime has expired!"
