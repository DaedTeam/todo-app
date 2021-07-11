from fastapi import FastAPI

from app.api.v1.routers import issue_router as issue_router
from app.api.v1.routers import routers
from app.api.v1.routers import user_router as user_router
from app.containers import Container


def create_app():
    container = Container()
    container.config.from_yaml('config.yml')
    container.wire(modules=[routers, user_router, issue_router])
    # container.wire(modules=[sys.modules[__name__]])
    ''' Connect db '''
    container.postpres_db()
    container.mongodb()
    # db = container.db()
    # db.create_database()
    app = FastAPI(
        docs_url="/"
    )
    app.container = container
    app.include_router(routers.router)
    return app


if __name__ == '__main__':
    create_app()
