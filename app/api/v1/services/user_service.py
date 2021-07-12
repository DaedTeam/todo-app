from typing import Iterator

from app.api.v1.schemas.user import UserCreate, UserSchema, UserUpdate
from app.api.v1.services.base import ServiceBase
from app.db.postpres.base import User
from app.repositories.user_repos import UserRepository


class UserService(ServiceBase):
    pass
    # async def get_users(self, page_index: int, page_limit: int) -> Iterator[UserSchema]:
    #     users = await self._repository.find_all(page_index, page_limit)
    #     user_bases = [UserSchema.from_orm(user) for user in users]
    #     total_items = await self._repository.count(User)
    #     total_page = 1
    #     current_page = page_index
    #     return self.response_paging(user_bases, total_items=total_items, total_page=total_page, current_page=current_page)
    #
    # async def get_user_by_id(self, user_id: int) -> UserSchema:
    #     user = await self._repository.find_by_id(user_id)
    #     return self.response(user)
    #
    # async def create_user(self, user_create: UserCreate) -> UserSchema:
    #     user: User = User(**user_create.dict())
    #     created_user = await self._repository.insert(user)
    #     return self.response(created_user)
    #
    # async def update_user(self, user_update: UserUpdate):
    #     user_db = User(**user_update.dict())
    #     updated_user = await self._repository.update(user_update.id, user_db)
    #     return self.response(updated_user)
    #
    # async def delete_user_by_id(self, user_id: int) -> None:
    #     deleted_user = await self._repository.delete_by_id(user_id)
    #     return self.response(deleted_user)
