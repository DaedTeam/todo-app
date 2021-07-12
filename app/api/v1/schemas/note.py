from datetime import datetime

from app.api.v1.schemas.base import BaseEnhancedModel


class NoteBase(BaseEnhancedModel):
    title: str
    detail: str
    color: str
    create_date: datetime
    update_date: datetime


class NoteCreate(NoteBase):
    user_id: str


class NoteUpdate(NoteBase):
    pass


class NoteSchema(NoteBase):
    id: int


class NoteMongoSchema(NoteBase):
    object_id: str
    user_id: str
