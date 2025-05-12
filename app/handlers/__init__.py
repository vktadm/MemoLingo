from app.handlers.learn import router as learn_router
from app.handlers.revise import router as revise_router
from app.handlers.user import router as user_router
from app.handlers.auth import router as auth_router
from app.handlers.word import router as word_router
from app.handlers.category import router as category_router
from app.handlers.category_word import router as category_word_router

routers = [
    learn_router,
    revise_router,
    user_router,
    auth_router,
    word_router,
    category_router,
    category_word_router,
]
