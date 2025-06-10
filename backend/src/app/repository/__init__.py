from .user import UsersRepository
from .word import WordRepository
from .black_list import TokenBlackListRepository
from .category import CategoryRepository
from .category_word import CategoryWordRepository
from .smtp import SMTPRepository

__all__ = {
    "UsersRepository",
    "WordRepository",
    "TokenBlackListRepository",
    "CategoryRepository",
    "CategoryWordRepository",
    "SMTPRepository",
}
