from typing import List

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncResult

from app.db.postpres.base import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):

    async def find_all(self, page_index: int, page_limit: int) -> List[User]:
        async with self._db.session_scope() as session:
            stmt = select(User).offset(page_index * page_limit).limit(page_limit)
            rs: AsyncResult = await session.execute(stmt)
            return rs.scalars()

    async def find_by_id(self, user_id: int):
        async with self._db.session_scope() as session:
            stmt = select(User).where(User.id == user_id)
            rs: AsyncResult = await session.execute(stmt)
            user = rs.fetchone()
            return user

    async def insert(self, user: User) -> User:
        async with self._db.session_scope() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def update(self, user_id: int, update_user: User):
        async with self._db.session_scope() as session:
            stmt = select(User).where(User.id == user_id)
            rs: AsyncResult = await session.execute(stmt)
            user_from_db = rs.scalar_one()
            user_from_db.fullname = update_user.fullname
            user_from_db.username = update_user.username
            user_from_db.email = update_user.email
            user_from_db.phone = update_user.phone
            user_from_db.date_of_birth = update_user.date_of_birth
            user_from_db.gender = update_user.gender
            user_from_db.bio = update_user.bio
            await session.commit()
            return user_from_db

    async def delete_by_id(self, user_id: int) -> None:
        async with self._db.session_scope() as session:
            stmt = (
                delete(User).where(User.c.id == user_id)
            )
            await session.execute(stmt)
            await session.commit()
