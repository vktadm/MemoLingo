from typing import Optional
from pydantic import BaseModel, ConfigDict


class BaseUserCategorySchema(BaseModel):
    is_creator: bool
    user_id: int
    category_id: int


class CreateUserCategorySchema(BaseUserCategorySchema):
    is_creator: bool
    user_id: int
    category_id: int


class UpdateUserCategorySchema(BaseUserCategorySchema):
    is_creator: Optional[bool] = None
    user_id: Optional[int] = None
    category_id: Optional[int] = None


class UserCategorySchema(BaseUserCategorySchema):
    model_config = ConfigDict(from_attributes=True)
    id: int
