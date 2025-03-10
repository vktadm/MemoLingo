from fastapi import APIRouter

from .word.views import router as wrd_router
from .category.views import router as cat_router

# from .user.views import router as us_router

# from .user_progress import router as us_pr_router
# from .category_word import router as cat_wrd_router

# from .views import router as memolingo_router

# from .demo_auth.views import router as demo_auth_router

from .auth.demo_jwt_auth import router as jwt_router

router = APIRouter()
# router.include_router(router=memolingo_router, prefix="/memolingo")
router.include_router(router=wrd_router, prefix="/word")
router.include_router(router=cat_router, prefix="/category")
router.include_router(router=jwt_router, prefix="")
# router.include_router(router=demo_auth_router, prefix="")
