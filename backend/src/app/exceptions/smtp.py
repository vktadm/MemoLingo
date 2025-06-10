from .base import APIException


class SMTPException(APIException):
    def __init__(self):
        super().__init__(
            status_code=500,
            detail="Couldn't send message.",
        )


class SMTPTokenException(APIException):
    def __init__(self):
        super().__init__(
            status_code=401, detail="Invalid token or token's lifetime has expired."
        )


class SMTPCooldownException(APIException):
    def __init__(self):
        super().__init__(
            status_code=500,
            detail="Cooldown time has not expired.",
        )
