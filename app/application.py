from fastapi import FastAPI

from app.api.v1.routers import routers, note_router, label_router, user_router, issue_router, task_router
from app.containers import Container


def create_app():
    container = Container()
    container.config.from_yaml('config.yml')
    container.wire(modules=[routers, user_router, issue_router, note_router, label_router, task_router])
    # container.wire(modules=[sys.modules[__name__]])
    ''' Connect db '''
    container.postpres_db()
    container.mongodb()
    # db = container.db()
    # db.create_database()
    app = FastAPI()
    app.container = container
    app.include_router(routers.router)
    return app


if __name__ == '__main__':
    create_app()
