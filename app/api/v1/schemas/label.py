from uuid import UUID

from bson import ObjectId

from app.api.v1.schemas.base import BaseEnhancedModel


class LabelBase(BaseEnhancedModel):
    name: str
    color: str


class LabelCreate(LabelBase):
    user_id: int


class LabelUpdate(LabelBase):
    pass


class LabelSchema(LabelBase):
    id: int


class LabelMongoSchema(LabelBase):
    _id: ObjectId
    object_id: UUID
    user_id: str
