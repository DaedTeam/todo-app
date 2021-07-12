from typing import Optional

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Header
from starlette import status

from app.api.v1.functions import PagingResponse, ResponseData, swagger_response
from app.api.v1.schemas.task import TaskCreate, TaskMongoSchema, TaskUpdate
from app.api.v1.services.task_service import TaskService
from app.containers import Container

router = APIRouter()


@router.get(
    path="/",
    description="example list",
    responses=swagger_response(
        response_model=PagingResponse[TaskMongoSchema],
        success_status_code=status.HTTP_200_OK
    )
)
@inject
async def get_list(
        page_num: int = 1,
        page_limit: int = 100,
        authorization: Optional[str] = Header(None),
        service: TaskService = Depends(Provide[Container.task_service])
):
    # token = AuthUtil.decode_token(authorization)
    token = "token"
    issues = await service.mg_get_all(token, page_num, page_limit)
    return PagingResponse[TaskMongoSchema](**issues)


@router.get(
    path="/{issue_id}",
    responses=swagger_response(
        response_model=ResponseData[TaskMongoSchema],
        success_status_code=status.HTTP_200_OK
    )
)
@inject
async def get_issue_by_id(
        issue_id: str,
        service: TaskService = Depends(Provide[Container.task_service])
):
    issue = await service.mg_get_by_id(issue_id)
    return ResponseData[TaskMongoSchema](**issue)


@router.post(
    path="/",
    responses=swagger_response(
        response_model=ResponseData[TaskMongoSchema]
    )
)
@inject
async def create_issue(
        issue_create: TaskCreate,
        service: TaskService = Depends(Provide[Container.task_service])
):
    created_issue = await service.mg_create(issue_create)
    return ResponseData[TaskMongoSchema](**created_issue)


@router.put(
    path="/{issue_id}",
    responses=swagger_response(
        response_model=ResponseData
    )
)
@inject
async def update_issue(
        issue_update: TaskUpdate,
        issue_id: str,
        service: TaskService = Depends(Provide[Container.task_service])
):
    return await service.mg_update(issue_update, issue_id)


@router.delete(
    path="/{issue_id}",
    responses=swagger_response(
        response_model=ResponseData,
        fail_status_code=status.HTTP_404_NOT_FOUND,
        success_status_code=status.HTTP_200_OK
    )
)
@inject
async def delete_issue(
        issue_id=str,
        service: TaskService = Depends(Provide[Container.task_service])
):
    deleted_data = await service.mg_delete(issue_id)
    return ResponseData(**deleted_data)
