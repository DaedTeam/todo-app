from enum import Enum
from typing import Dict, Generic, List, TypeVar, Union

from fastapi import status
from pydantic import Field
from pydantic.generics import GenericModel
from pydantic.main import BaseModel


class OrderBy(str, Enum):
    asc = "asc"
    desc = "desc"


class Paging(BaseModel):
    order_by: OrderBy = "asc"
    limit: int = Field(20, gt=0)
    page: int = Field(1, gt=0)


TypeX = TypeVar("TypeX")


class Error(BaseModel):
    loc: str = None
    mgs: str = None
    detail: str = None


class PagingResponse(GenericModel, Generic[TypeX]):
    data: List[TypeX]
    errors: List[Error] = []
    total_items = 0
    total_page = 0
    current_page = 0


class ResponseData(GenericModel, Generic[TypeX]):
    data: TypeX = None
    errors: List[Error] = []


class ResponseError(BaseModel):
    data: Union[Dict, List] = None
    errors: List[Error]


def swagger_response(
        response_model,
        success_status_code=status.HTTP_200_OK,
        success_description=None,
        fail_status_code=status.HTTP_400_BAD_REQUEST,
        fail_description=None,
):
    result = {}

    # success
    result.update(
        {
            success_status_code: {
                "model": response_model,
                "description": success_description,
            }
        }
    )

    # fail
    result.update(
        {fail_status_code: {"model": ResponseError, "description": fail_description}}
    )

    # fail
    result.update(
        {
            status.HTTP_422_UNPROCESSABLE_ENTITY: {
                "model": ResponseError,
                "description": fail_description,
            }
        }
    )
    return result
