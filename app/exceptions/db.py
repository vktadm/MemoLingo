from app.exceptions.base import APIException


class NotFoundException(APIException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="No content found.",
        )


class ContentConflictException(APIException):
    def __init__(self):
        super().__init__(
            status_code=409,
            detail="Data integrity violation.",
        )


class ConstraintViolationException(APIException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Content already exists.",
        )


class RepositoryException(APIException):
    def __init__(self):
        super().__init__(
            status_code=500,
            detail="Database operation failed.",
        )


class DatabaseException(APIException):
    def __init__(self):
        super().__init__(
            status_code=500,
            detail="Unexpected error during.",
        )
