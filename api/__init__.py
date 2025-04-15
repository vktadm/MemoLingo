from fastapi import APIRouter

from api.handlers import routers


router = APIRouter()

# Подключаем API hendlers
for itm in routers:
    router.include_router(router=itm)

# Авторизация
# router.include_router(router=auth_router, prefix="/auth")
