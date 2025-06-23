from api.v1 import v1_router
from fastapi import APIRouter


router = APIRouter()
# API路由
router.include_router(v1_router)