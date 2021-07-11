from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.api.v1.schemas.user import UserCreate, UserUpdate
from app.api.v1.services.user_service import UserService
from app.containers import Container

router = APIRouter()


@router.get('/')
@inject
async def get_list(
        page_index: int = 0,
        page_limit: int = 100,
        user_service=Depends(Provide[Container.user_service])
):
    return await user_service.get_users(page_index, page_limit)


@router.get("/{user_id}")
@inject
async def get_user(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service])
):
    return await user_service.get_user_by_id(user_id)


@router.post("/")
@inject
async def create_user(
        user_create: UserCreate,
        user_service: UserService = Depends(Provide[Container.user_service])
):
    return await user_service.create_user(user_create)


@router.put("/")
@inject
async def update_user(
        user_update: UserUpdate,
        user_service: UserService = Depends(Provide[Container.user_service])
):
    return await user_service.update_user(user_update)


@router.delete("/{user_id}")
@inject
async def delete(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service])
):
    return await user_service.delete_user_by_id(user_id)
