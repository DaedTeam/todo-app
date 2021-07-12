from typing import Optional

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Header
from starlette import status

from app.api.v1.functions import PagingResponse, ResponseData, swagger_response
from app.api.v1.schemas.label import LabelMongoSchema, LabelCreate, LabelUpdate
from app.api.v1.services.label_service import LabelService
from app.containers import Container
from app.utils.auth_util import AuthUtil

router = APIRouter()


@router.get(
    path="/",
    description="example list",
    responses=swagger_response(
        response_model=PagingResponse[LabelMongoSchema],
        success_status_code=status.HTTP_200_OK
    )
)
@inject
async def get_list(
        page_num: int = 1,
        page_limit: int = 100,
        authorization: Optional[str] = Header(None),
        service: LabelService = Depends(Provide[Container.label_service])
):
    # token = AuthUtil.decode_token(authorization)
    token = "token"
    labels = await service.mg_get_all(token, page_num, page_limit)
    return PagingResponse[LabelMongoSchema](**labels)


@router.get(
    path="/{label_id}",
    responses=swagger_response(
        response_model=ResponseData[LabelMongoSchema],
        success_status_code=status.HTTP_200_OK
    )
)
@inject
async def get_label_by_id(
        label_id: str,
        service: LabelService = Depends(Provide[Container.label_service])
):
    label = await service.mg_get_by_id(label_id)
    return ResponseData[LabelMongoSchema](**label)


@router.post(
    path="/",
    responses=swagger_response(
        response_model=ResponseData[LabelMongoSchema]
    )
)
@inject
async def create(
        label_create: LabelCreate,
        service: LabelService = Depends(Provide[Container.label_service])
):
    create_label = await service.mg_create(label_create)
    return ResponseData[LabelMongoSchema](**create_label)


@router.put(
    path="/{label_id}",
    responses=swagger_response(
        response_model=ResponseData
    )
)
@inject
async def update(
        label_update: LabelUpdate,
        label_id: str,
        service: LabelService = Depends(Provide[Container.label_service])
):
    return await service.mg_update(label_update, label_id)


@router.delete(
    path="/{label_id}",
    responses=swagger_response(
        response_model=ResponseData,
        fail_status_code=status.HTTP_404_NOT_FOUND,
        success_status_code=status.HTTP_200_OK
    )
)
@inject
async def delete(
        label_id=str,
        service: LabelService = Depends(Provide[Container.label_service])
):
    deleted_data = await service.mg_delete(label_id)
    return ResponseData(**deleted_data)
