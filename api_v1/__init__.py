from fastapi import APIRouter

from .learn_words.views import router as learn_router
from .revise_words.views import router as revise_router

# Авторизация
# from .demo_auth.views import router as demo_auth_router
# from .auth.demo_jwt_auth import router as jwt_router


router = APIRouter()

router.include_router(router=learn_router, prefix="/learn")
router.include_router(router=revise_router, prefix="/revise")

# Авторизация
# router.include_router(router=jwt_router, prefix="")
# router.include_router(router=demo_auth_router, prefix="")
