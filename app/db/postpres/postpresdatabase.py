from contextlib import AbstractAsyncContextManager

from sqlalchemy import orm
from sqlalchemy.ext.asyncio import (
    AsyncEngine, AsyncSession, create_async_engine
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PostpresDatabase:

    def __init__(self, db_url: str):
        self._db_url = db_url
        self._engine: AsyncEngine = create_async_engine(db_url, echo=True)
        self.session_factory = orm.sessionmaker(self._engine, expire_on_commit=False, class_=AsyncSession)

    @property
    def db_url(self):
        return self._db_url

    def session_scope(self):
        return self.SessionScope(self)

    class SessionScope(AbstractAsyncContextManager):
        def __init__(self, outer):
            self._session_factory = outer.session_factory
            self._session: AsyncSession = self._session_factory()

        async def __aenter__(self) -> AsyncSession:
            return self._session

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            if exc_val:
                await self._session.rollback()
            await self._session.close()
