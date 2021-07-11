from app.api.v1.schemas.baseenhancedmodel import BaseEnhancedModel


class LabelBase(BaseEnhancedModel):
    name: str
    color: str


class LabelCreate(LabelBase):
    user_id: int


class LabelSchema(LabelBase):
    id: int
