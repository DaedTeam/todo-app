from motor.core import AgnosticCollection
from motor.motor_asyncio import AsyncIOMotorClient


class MongoDatabase:

    def __init__(self, db_url: str, db_name: str):
        self._db_url = db_url
        self._client = AsyncIOMotorClient(self._db_url)
        self._db = self._client[db_name]

    def get_collection(self, collection_name: str) -> AgnosticCollection:
        return self._db[collection_name]
