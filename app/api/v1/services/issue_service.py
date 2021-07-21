import math

from app.api.v1.services.base import ServiceBase


class IssueService(ServiceBase):

    async def mg_get_all(self, token: str, page_num=1, page_limit: int = 100):
        skip = (page_num - 1) * page_limit
        objects = await self._repos.mg_find_all(skip, page_limit)
        total_items = await self._repos.mg_count()
        total_page = math.ceil(total_items / page_limit)
        current_page = page_num
        return self.response_paging(objects, total_items=total_items, total_page=total_page, current_page=current_page)
