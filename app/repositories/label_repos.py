from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncResult

from app.db.postpres.base import Label
from app.repositories.base import BaseRepository


class LabelRepository(BaseRepository):
    async def find_all(self):
        async with self._db.session_scope() as session:
            stmt = select(Label)
            rs: AsyncResult = await session.execute(stmt)
            return rs.scalars()

    async def find_by_id(self, user_id: int):
        async with self._db.session_scope() as session:
            stmt = select(Label).where(Label.id == user_id)
            rs: AsyncResult = await session.execute(stmt)
            user = rs.fetchone()
            return user

    async def insert(self, user: Label):
        async with self._db.session_scope() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def update(self, label_id: int, **kwargs) -> None:
        async with self._db.session_scope() as session:
            stmt = (
                update(Label).where(Label.id == label_id).values(**kwargs).execution_options(synchronize_session="fetch")
            )
            await session.execute(stmt)
            await session.commit()

    async def delete_by_id(self, label_id: int) -> None:
        async with self._db.session_scope() as session:
            stmt = (
                delete(Label).where(Label.c.id == label_id)
            )
            await session.execute(stmt)
            await session.commit()
