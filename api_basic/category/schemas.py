from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    title: str
    # description: str | None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryCreate):
    title: str | None = None


class CategoryUpdatePartial(CategoryCreate):
    pass


class Category(CategoryBase):
    model_config = ConfigDict(from_attributes=True)  # берем только атрибуты
    id: int
