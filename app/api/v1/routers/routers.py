from fastapi import APIRouter

from . import issue_router, user_router, task_router, label_router, note_router

router = APIRouter()
router.include_router(router=user_router.router, prefix="/users", tags=["User"])
router.include_router(router=issue_router.router, prefix="/issues", tags=["Issue"])
router.include_router(router=task_router.router, prefix="/tasks", tags=["Task"])
router.include_router(router=label_router.router, prefix="/labels", tags=["Label"])
router.include_router(router=note_router.router, prefix="/notes", tags=["Note"])
