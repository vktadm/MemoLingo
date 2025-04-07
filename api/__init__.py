from fastapi import APIRouter

from api.handlers import routers

# Авторизация
from api.auth.endpoints import router as auth_router


router = APIRouter()

# Авторизация
for itm in routers:
    router.include_router(router=itm)

# Авторизация
router.include_router(router=auth_router, prefix="/auth")
