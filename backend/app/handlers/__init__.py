from .learn import router as learn_router
from .revise import router as revise_router
from .user import router as user_router
from .auth import router as auth_router
from .word import router as word_router
from .category import router as category_router
from .category_word import router as category_word_router

routers = [
    learn_router,
    revise_router,
    user_router,
    auth_router,
    word_router,
    category_router,
    category_word_router,
]
