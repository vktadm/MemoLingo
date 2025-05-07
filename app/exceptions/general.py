from app.exceptions.base import MainException


class NotFound(MainException):
    detail = "There are no records yet."
    status_code = 404


class ContentConflict(MainException):
    detail = "Data integrity violation."
    status_code = 409


class ConstraintViolationError(MainException):
    detail = "Content already exists."
    status_code = 400


class RepositoryError(MainException):
    detail = "Database operation failed."
    status_code = 500


class DatabaseError(MainException):
    detail = "Unexpected error during."
    status_code = 500
