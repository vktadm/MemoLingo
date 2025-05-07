from .user import UserSchema
from .auth import UserLoginSchema, GoogleUserDataSchema
from .user_word import UserWordSchema, CreateUserWordSchema
from .word import WordSchema, CreateWordSchema, UpdateWordSchema

__all__ = {
    "WordSchema",
    "CreateWordSchema",
    "UpdateWordSchema",
    "UserSchema",
    "UserLoginSchema",
    "GoogleUserDataSchema",
    "UserWordSchema",
    "CreateUserWordSchema",
}
