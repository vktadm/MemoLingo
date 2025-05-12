from .user import UserSchema
from .auth import UserLoginSchema, GoogleUserDataSchema
from .user_word import UserWordSchema, CreateUserWordSchema
from .word import WordSchema, CreateWordSchema, UpdateWordSchema
from .category import CategorySchema, CreateCategorySchema, UpdateCategorySchema
from .user_category import (
    UserCategorySchema,
    CreateUserCategorySchema,
    UpdateUserCategorySchema,
)
from .category_word import (
    CategoryWordsSchema,
    CreateCategoryWordsSchema,
    UpdateCategoryWordsSchema,
)

__all__ = [
    # Word
    "WordSchema",
    "CreateWordSchema",
    "UpdateWordSchema",
    # User
    "UserSchema",
    # Auth
    "UserLoginSchema",
    "GoogleUserDataSchema",
    # User-Word
    "UserWordSchema",
    "CreateUserWordSchema",
    # Category
    "CategorySchema",
    "CreateCategorySchema",
    "UpdateCategorySchema",
    # UserCategory
    "UserCategorySchema",
    "CreateUserCategorySchema",
    "UpdateUserCategorySchema",
    # CategoryWord
    "CategoryWordsSchema",
    "CreateCategoryWordsSchema",
    "UpdateCategoryWordsSchema",
]
