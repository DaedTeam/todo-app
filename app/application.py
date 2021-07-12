from fastapi import FastAPI
from pydantic import BaseSettings, Field

from app.api.v1.routers import (
    issue_router, label_router, note_router, routers, task_router, user_router
)
from app.containers import Container


class AppSettings(BaseSettings):
    mongo_url: str = Field(env="MONGODB_URL")
    mongo_db: str = Field(env="MONGODB_NAME")
    postpres_url: str = Field(env="POSTPRES_URL")


def create_app():
    container = Container()
    ''' Config pydantic model '''
    container.config.from_pydantic(AppSettings())
    ''' Config yaml '''
    # container.config.from_yaml('config.yml')
    ''' Config env '''
    # container.config.mongo.url.from_env("MONGODB_URL")
    # container.config.mongo.db_name.from_env("MONGODB_NAME")
    container.wire(modules=[routers, user_router, issue_router, note_router, label_router, task_router])
    ''' Connect db '''
    container.postpres_db()
    container.mongodb()
    app = FastAPI()
    app.container = container
    app.include_router(routers.router)
    return app


if __name__ == '__main__':
    create_app()
