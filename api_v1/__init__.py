from fastapi import APIRouter

# Базовые
from .word.views import router as wrd_router
from .learn_words.views import router as learn_router

# from .category.views import router as cat_router
# from .user.views import router as us_router
# from .user_progress.views import router as us_pr_router

# Авторизация
# from .demo_auth.views import router as demo_auth_router
# from .auth.demo_jwt_auth import router as jwt_router

router = APIRouter()

# Базовые
router.include_router(router=wrd_router, prefix="/word")
router.include_router(router=learn_router, prefix="/learn_router")
# router.include_router(router=us_router, prefix="/user")
# router.include_router(router=us_pr_router, prefix="/user_progress")

# router.include_router(router=cat_router, prefix="/category")

# Авторизация
# router.include_router(router=jwt_router, prefix="")
# router.include_router(router=demo_auth_router, prefix="")
