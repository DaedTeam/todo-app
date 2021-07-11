from fastapi import APIRouter

from . import issue_router, user_router

router = APIRouter()
router.include_router(router=user_router.router, prefix="/users", tags=["User"])
router.include_router(router=issue_router.router, prefix="/issues", tags=["Issue"])
