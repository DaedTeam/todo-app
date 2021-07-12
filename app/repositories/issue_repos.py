from typing import List

from bson import ObjectId
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncResult

from app.api.v1.schemas.base import BaseEnhancedModel
from app.db.mongo.collections import COLLECTION_TASK
from app.db.postpres.base import Issue
from app.repositories.base import BaseRepository


class IssueRepository(BaseRepository):

    async def find_all(self):
        async with self._db.session_scope() as session:
            stmt = select(Issue)
            rs: AsyncResult = await session.execute(stmt)
            return rs.scalars()

    async def find_by_id(self, user_id: int):
        async with self._db.session_scope() as session:
            stmt = select(Issue).where(Issue.id == user_id)
            rs: AsyncResult = await session.execute(stmt)
            user = rs.fetchone()
            return user

    async def insert(self, user: Issue):
        async with self._db.session_scope() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def update(self, issue_id: int, **kwargs) -> None:
        async with self._db.session_scope() as session:
            stmt = (
                update(Issue).where(Issue.id == issue_id).values(**kwargs).execution_options(synchronize_session="fetch")
            )
            await session.execute(stmt)
            await session.commit()

    async def delete_by_id(self, issue_id: int) -> None:
        async with self._db.session_scope() as session:
            stmt = (
                delete(Issue).where(Issue.c.id == issue_id)
            )
            await session.execute(stmt)
            await session.commit()

    async def mg_find_all(self, skip: int = 0, limit: int = 100) -> List[BaseEnhancedModel]:
        pipeline = [
            {"$skip": skip},
            {"$limit": limit},
            {
                "$lookup":
                    {
                        "from": COLLECTION_TASK,
                        "localField": "_id",
                        "foreignField": "issue_id",
                        "as": "tasks"
                    }
            }
        ]
        print(pipeline)
        return await self._mg_find(pipeline=pipeline)
