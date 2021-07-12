import os

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

from app.api.v1.routers import routers, note_router, label_router, user_router, issue_router, task_router
from app.containers import Container


def create_app():
    test_mongodb()
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


def test_mongodb():
    url = os.getenv("MONGODB", "mongodb+srv://tik:123@cluster0.bh9kt.mongodb.net/cube_engine?retryWrites=true&w=majority")
    db_name = os.getenv("MONGODB", "cube_engine")
    client = MongoClient(url)
    db = client[db_name]
    collection_name = "users"
    collection = db[collection_name]
    d = collection.find_one()
    print('\t ------- Test mongo db ----------')
    print(d)


if __name__ == '__main__':
    create_app()
