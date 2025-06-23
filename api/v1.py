from fastapi import APIRouter

from api.endpoints import fire_detect

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(fire_detect.router, tags=["opeanai interface"])
