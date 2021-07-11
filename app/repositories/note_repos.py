from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncResult

from app.db.postpres.base import Note
from app.repositories.base import BaseRepository


class NoteRepository(BaseRepository):
    async def find_all(self):
        async with self._db.session_scope() as session:
            stmt = select(Note)
            rs: AsyncResult = await session.execute(stmt)
            return rs.scalars()

    async def find_by_id(self, user_id: int):
        async with self._db.session_scope() as session:
            stmt = select(Note).where(Note.id == user_id)
            rs: AsyncResult = await session.execute(stmt)
            user = rs.fetchone()
            return user

    async def insert(self, user: Note):
        async with self._db.session_scope() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def update(self, note_id: int, **kwargs) -> None:
        async with self._db.session_scope() as session:
            stmt = (
                update(Note).where(Note.id == note_id).values(**kwargs).execution_options(synchronize_session="fetch")
            )
            await session.execute(stmt)
            await session.commit()

    async def delete_by_id(self, note_id: int) -> None:
        async with self._db.session_scope() as session:
            stmt = (
                delete(Note).where(Note.c.id == note_id)
            )
            await session.execute(stmt)
            await session.commit()
