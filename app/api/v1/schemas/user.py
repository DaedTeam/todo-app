from datetime import datetime
from enum import Enum

from app.api.v1.schemas.baseenhancedmodel import BaseEnhancedModel


class EGender(str, Enum):
    male = "male"
    female = "female"


class UserBase(BaseEnhancedModel):
    fullname: str
    username: str
    email: str
    phone: str
    date_of_birth: datetime
    bio: str
    gender: EGender


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    id: int
    pass


class UserSchema(UserBase):
    id: int
