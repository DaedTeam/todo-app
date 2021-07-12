from typing import Optional, List, Any

from bson.objectid import ObjectId
from pymongo.results import DeleteResult, UpdateResult
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy.sql.functions import count

from app.api.v1.schemas.base import BaseEnhancedModel
from app.db.mongo.base import MongoDatabase
from app.db.postpres.postpresdatabase import PostpresDatabase


class BaseRepository:

    def __init__(self, db: PostpresDatabase, mongodb: MongoDatabase = None, collection_name: str = None):
        self._db = db
        self._mongodb = mongodb
        self._collection = self._mongodb.get_collection(collection_name)

    async def count(self, Type):
        async with self._db.session_scope() as session:
            stmt = select(count("*")).select_from(Type)
            total_user: AsyncResult = await session.execute(stmt)
            return total_user.scalar()

    async def mg_count(self):
        n = await self._collection.count_documents({})
        return n

    async def mg_find_all(self, skip: int = 0, limit: int = 100) -> List[BaseEnhancedModel]:
        pipeline = [
            {"$skip": skip},
            {"$limit": limit}
        ]
        return await self._mg_find(pipeline=pipeline)

    async def mg_find_by_id(self, obj_id) -> Optional[BaseEnhancedModel]:
        found_dict = await self._collection.find_one({"_id": ObjectId(obj_id)})
        return BaseEnhancedModel.construct(**found_dict)

    async def _mg_find(self, **kwargs):
        pipeline = kwargs.get("pipeline")
        cursor = self._collection.aggregate(pipeline)
        db_models = await cursor.to_list(length=100)
        output_models = []
        # add mongo ObjectId
        for item in db_models:
            print(item)
            output_models.append(BaseEnhancedModel.construct(**item))
        return output_models

    async def mg_insert(self, obj: BaseEnhancedModel) -> Optional[BaseEnhancedModel]:
        rs = await self._collection.insert_one(obj.dict())
        try:
            inserted_item = await self._collection.find_one({"_id": ObjectId(rs.inserted_id)})
            return BaseEnhancedModel.construct(**inserted_item)
        except Exception:  # noqa
            return None

    async def mg_update(self, obj: BaseEnhancedModel, obj_id) -> Optional[BaseEnhancedModel]:
        _filter = {"_id": ObjectId(obj_id)}
        new_values = {"$set": obj.dict()}
        rs: UpdateResult = await self._collection.update_one(_filter, new_values)
        updated_obj = None
        if rs.modified_count != 0:
            updated_dict = await self._collection.find_one({"_id": ObjectId(obj_id)})
            updated_obj = BaseEnhancedModel.construct(**updated_dict)
        return updated_obj

    async def mg_delete(self, obj_id) -> bool:
        rs: DeleteResult = await self._collection.delete_one({"_id": ObjectId(obj_id)})
        return True if rs.deleted_count != 0 else False
