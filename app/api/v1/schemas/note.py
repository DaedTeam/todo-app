from datetime import datetime

from app.api.v1.schemas.baseenhancedmodel import BaseEnhancedModel


class NoteBase(BaseEnhancedModel):
    title: str
    details: str
    color: str
    create_date: datetime
    update_date: datetime


class NoteCreate(NoteBase):
    user_id: int


class NoteSchema(NoteBase):
    pass
