from .user import UserSchema, UserCreateSchema
from .auth import UserLoginSchema, GoogleUserDataSchema
from .user_word import UserWordSchema, CreateUserWordSchema
from .word import WordSchema

__all__ = {
    "WordSchema",
    "UserSchema",
    "UserCreateSchema",
    "UserLoginSchema",
    "GoogleUserDataSchema",
    "UserWordSchema",
    "CreateUserWordSchema",
}
