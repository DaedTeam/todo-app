import math
from typing import List

from starlette import status

from app.api.v1.schemas.base import BaseEnhancedModel
from app.api.v1.status.exceptions import ExceptionHandle
from app.api.v1.status.messages import INVALID_OBJECT_ID, MESSAGE_STATUS
from app.repositories.base import BaseRepository


class RaiseError(BaseEnhancedModel):
    loc: str = None
    msg: str = None
    detail: str = None


class ServiceBase:

    def __init__(self, repos: BaseRepository = None, paging=None):
        self._repos = repos
        self.paging = paging
        self.errors = []

    async def mg_get_all(self, token: str, page_num=1, page_limit: int = 100):
        skip = (page_num - 1) * page_limit
        objects = await self._repos.mg_find_all(skip, page_limit)
        total_items = await self._repos.mg_count()
        total_page = math.ceil(total_items / page_limit)
        current_page = page_num
        return self.response_paging(objects, total_items=total_items, total_page=total_page, current_page=current_page)

    async def mg_get_by_id(self, obj_id):
        obj = await self._repos.mg_find_by_id(obj_id)
        return self.response(obj)

    async def mg_create(self, obj: BaseEnhancedModel):
        created_issue = await self._repos.mg_insert(obj)
        return self.response(created_issue)

    async def mg_update(self, obj: BaseEnhancedModel, obj_id):
        updated_obj = await self._repos.mg_update(obj, obj_id)
        return self.response(updated_obj)

    async def mg_delete(self, obj_id):
        delete_rs = await self._repos.mg_delete(obj_id)
        if not delete_rs:
            self.exception(MESSAGE_STATUS.get(INVALID_OBJECT_ID))
        return self.response(None, error_status_code=status.HTTP_404_NOT_FOUND)

    def exception(self, msg: str, loc: str = None, detail: str = ""):
        self.errors.append(RaiseError(msg=msg, detail=detail, loc=loc))

    def raise_exception(self, error_status_code=status.HTTP_400_BAD_REQUEST):
        errors = []
        for temp in self.errors:
            errors.append(temp.dict())
        raise ExceptionHandle(errors=errors, status_code=error_status_code)

    def response(self, data, error_status_code=status.HTTP_400_BAD_REQUEST):
        if self.errors:
            self.raise_exception(error_status_code=error_status_code)
        else:
            return {
                "data": data,
                "errors": self.errors,
            }

    def response_paging(
            self,
            data: List,
            total_items,
            total_page,
            current_page,
            error_status_code=status.HTTP_400_BAD_REQUEST,
    ):
        if self.errors:
            self.raise_exception(error_status_code=error_status_code)
        else:
            return {
                "data": data,
                "errors": self.errors,
                "total_items": total_items,
                "total_page": total_page,
                "current_page": current_page
            }
