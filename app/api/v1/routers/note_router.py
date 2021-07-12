from typing import Optional

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Header
from starlette import status

from app.api.v1.functions import PagingResponse, ResponseData, swagger_response
from app.api.v1.schemas.note import NoteCreate, NoteMongoSchema, NoteUpdate
from app.api.v1.services.note_service import NoteService
from app.containers import Container

router = APIRouter()


@router.get(
    path="/",
    description="example list",
    responses=swagger_response(
        response_model=PagingResponse[NoteMongoSchema],
        success_status_code=status.HTTP_200_OK
    )
)
@inject
async def get_list(
        page_num: int = 1,
        page_limit: int = 100,
        authorization: Optional[str] = Header(None),
        service: NoteService = Depends(Provide[Container.label_service])
):
    # token = AuthUtil.decode_token(authorization)
    token = "token"
    notes = await service.mg_get_all(token, page_num, page_limit)
    return PagingResponse[NoteMongoSchema](**notes)


@router.get(
    path="/{note_id}",
    responses=swagger_response(
        response_model=ResponseData[NoteMongoSchema],
        success_status_code=status.HTTP_200_OK
    )
)
@inject
async def get_by_id(
        note_id: str,
        service: NoteService = Depends(Provide[Container.note_service])
):
    note = await service.mg_get_by_id(note_id)
    return ResponseData[NoteMongoSchema](**note)


@router.post(
    path="/",
    responses=swagger_response(
        response_model=ResponseData[NoteMongoSchema]
    )
)
@inject
async def create(
        note_create: NoteCreate,
        service: NoteService = Depends(Provide[Container.note_service])
):
    created_note = await service.mg_create(note_create)
    return ResponseData[NoteMongoSchema](**created_note)


@router.put(
    path="/{note_id}",
    responses=swagger_response(
        response_model=ResponseData
    )
)
@inject
async def update(
        note_update: NoteUpdate,
        note_id: str,
        service: NoteService = Depends(Provide[Container.note_service])
):
    return await service.mg_update(note_update, note_id)


@router.delete(
    path="/{note_id}",
    responses=swagger_response(
        response_model=ResponseData,
        fail_status_code=status.HTTP_404_NOT_FOUND,
        success_status_code=status.HTTP_200_OK
    )
)
@inject
async def delete(
        note_id=str,
        service: NoteService = Depends(Provide[Container.note_service])
):
    deleted_data = await service.mg_delete(note_id)
    return ResponseData(**deleted_data)
