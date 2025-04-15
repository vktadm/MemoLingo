from api.handlers.learn import router as learn_router
from api.handlers.revise import router as revise_router
from api.handlers.user import router as user_router
from api.handlers.auth import router as auth_router

routers = [
    # learn_router,
    # revise_router,
    user_router,
    auth_router,
]
