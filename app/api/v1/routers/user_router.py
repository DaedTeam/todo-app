from typing import Optional

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query
from starlette import status

from app.api.v1.functions import PagingResponse, swagger_response
from app.api.v1.schemas.user import UserCreate, UserUpdate, UserMongoSchema
from app.api.v1.services.user_service import UserService
from app.containers import Container

router = APIRouter()


@router.get(
    path='/',
    responses=swagger_response(
        response_model=PagingResponse[UserMongoSchema],
        success_status_code=status.HTTP_200_OK
    )
)
@inject
async def get_list(
        page_num: Optional[int] = Query(1, gt=0),
        page_limit: Optional[int] = Query(100, gt=0),
        user_service: UserService = Depends(Provide[Container.user_service])
):
    token = "token"
    users = await user_service.mg_get_all(token, page_num, page_limit)
    return PagingResponse[UserMongoSchema](**users)


@router.get("/{user_id}")
@inject
async def get_user(
        user_id: str,
        user_service: UserService = Depends(Provide[Container.user_service])
):
    return await user_service.mg_get_by_id(user_id)


@router.post("/")
@inject
async def create_user(
        user_create: UserCreate,
        user_service: UserService = Depends(Provide[Container.user_service])
):
    return await user_service.mg_create(user_create)


@router.put("/")
@inject
async def update_user(
        user_update: UserUpdate,
        user_service: UserService = Depends(Provide[Container.user_service])
):
    return await user_service.mg_update(user_update)


@router.delete("/{user_id}")
@inject
async def delete(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service])
):
    return await user_service.mg_delete(user_id)
