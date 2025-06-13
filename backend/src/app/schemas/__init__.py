from .user import UserSchema, UserCreateSchema, UpdateUserSchema
from .auth import UserLoginSchema, GoogleUserDataSchema, UserLoginFormSchema
from .user_word import UserWordSchema, CreateUserWordSchema
from .word import WordSchema, CreateWordSchema, UpdateWordSchema
from .category import CategorySchema, CreateCategorySchema, UpdateCategorySchema
from .user_category import (
    UserCategorySchema,
    CreateUserCategorySchema,
    UpdateUserCategorySchema,
)
from .category_word import CategoryWordsSchema

__all__ = [
    # Word
    "WordSchema",
    "CreateWordSchema",
    "UpdateWordSchema",
    # User
    "UserSchema",
    "UserCreateSchema",
    "UpdateUserSchema",
    # Auth
    "UserLoginFormSchema",
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
]
