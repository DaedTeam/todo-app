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
    object_id: str
    user_id: str
