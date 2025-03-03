from fastapi import APIRouter
from .word.views import router as word_router
from .category.views import router as category_router


router = APIRouter()
router.include_router(router=word_router, prefix="/word")
router.include_router(router=category_router, prefix="/category")
