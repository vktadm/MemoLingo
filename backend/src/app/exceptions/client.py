from .base import APIException


class ExternalServiceException(APIException):
    def __init__(self):
        super().__init__(
            status_code=500,
            detail="External service error.",
        )


class TimeoutException(APIException):
    def __init__(self):
        super().__init__(
            status_code=504,
            detail="External service timeout.",
        )


class RequestException(APIException):
    def __init__(self):
        super().__init__(
            status_code=503,
            detail="Service unavailable.",
        )
