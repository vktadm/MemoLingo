from app.exceptions.base import MainException


class ExternalServiceError(MainException):
    detail = "External service error."
    status_code = 500


class TimeoutError(MainException):
    detail = "External service timeout."
    status_code = 504


class RequestError(MainException):
    detail = "Service unavailable."
    status_code = 503
