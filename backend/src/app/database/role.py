from enum import Enum


class UserRole(str, Enum):
    USER = "user"  # Обычный авторизованный
    ADMIN = "admin"  # Администратор
